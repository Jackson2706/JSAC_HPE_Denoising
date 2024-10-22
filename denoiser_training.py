#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 21 13:28:23 2024

@author: jackson-devworks
"""
import yaml
import torch
from sklearn.model_selection import train_test_split
from torch import nn
import numpy as np
import os
from tqdm import tqdm
import torch.optim as optim
import torch


from constant import experiment_config, denoiser_config
from dataset_lib import make_dataset, make_dataloader
from model import OneStageAE, TwoStageAE, ThreeStageAE, FourStageAE
from utils import compute_pck_pckh, calulate_error, add_awgn

with open(experiment_config['mmfi_config'], 'r') as fd:  # change the .yaml file in your code.
    config = yaml.load(fd, Loader=yaml.FullLoader)
    
dataset_root = experiment_config['dataset_root']
train_dataset, test_dataset = make_dataset(dataset_root, config)
rng_generator = torch.manual_seed(config['init_rand_seed'])
train_loader = make_dataloader(train_dataset, is_training=True, generator=rng_generator, **config['train_loader'])
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")




# Training parameters
num_epochs = denoiser_config['epoch']  # Number of training epochs

# Training loop
for noise_lv in tqdm(experiment_config["noise_level"]):
    torch.cuda.empty_cache()
    previousAE = torch.load(os.path.join("/home/jackson-devworks/Desktop/ECCV_2024/output/ThreeLayerDenosing/Encoder-DecoderReconstructor", str(noise_lv), "last.pt"))
    checkpoint_path = os.path.join(denoiser_config['checkpoint'], str(noise_lv))
    os.makedirs(checkpoint_path, exist_ok=True)
    model = FourStageAE(previousAE.getEncoder()).to(device)
    criterion = nn.MSELoss().to(device)  # Mean Squared Error Loss for reconstruction
    optimizer = optim.Adam(model.parameters(), lr=0.001)  # Adam optimizer
    for epoch in tqdm(range(num_epochs)):
        model.train()  # Set the model to training mode
        running_loss = 0.0
        torch.cuda.empty_cache()
        for idx, data in enumerate(train_loader):
            csi_data = data['input_wifi-csi']

            # Get the input data
            if denoiser_config['mode'] == 1:
                csi_data = torch.tensor(csi_data).float().to(device)
                csi_data = model.getProcessingInput(csi_data)
                csi_data = csi_data.cpu().detach()
                
            csi_data = csi_data.numpy()
            csi_data = add_awgn(csi_data, noise_lv)
            # Convert to tensor if necessary
            csi_data = torch.tensor(csi_data).float()  # Ensure data type is float
            
            csi_data = csi_data.to(device)
            # Zero the parameter gradients
            optimizer.zero_grad()
    
            # Forward pass
            reconstructed = model(csi_data)
    
            # Compute the loss
            loss = criterion(reconstructed, csi_data)
    
            # Backward pass and optimize
            loss.backward()
            optimizer.step()
    
            # Accumulate the running loss
            running_loss += loss.item()
    
        # Print the average loss for this epoch
        avg_loss = running_loss / len(train_loader)
        
        print(f'Epoch [{epoch + 1}/{num_epochs}], Loss: {avg_loss:.4f}')
        torch.save(model, os.path.join(checkpoint_path, "last.pt"))

print('Training complete.')