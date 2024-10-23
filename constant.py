#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 21 09:16:35 2024

@author: jackson-devworks
"""

experiment_config = {
    "mmfi_config": "/home/jackson-devworks/Desktop/ECCV_2024/dataset_lib/config.yaml",
    "dataset_root": "/home/jackson-devworks/Desktop/HPE/Dataset",
    "noise_level": [0.01, 0.02, 0.05, 0.1, 0.5, 1, 5, 10, 20],
    "mode": 2, # Mode 0: no denoiser layer, Mode 1: have AE denoiser layers, Mode 2: use traditional filter to denoise
    "epoch": 20,
    "checkpoint": "/home/jackson-devworks/Desktop/ECCV_2024/output/AWGN/MeanFilterDenoising"
}

denoiser_config = {
    "epoch": 20,
    "mode": 0, # Mode 0: 1 stage AE, Mode 1: stacked AE
    "previous_encoder": "/home/jackson-devworks/Desktop/ECCV_2024/output/FourLayerDenosing/Encoder-DecoderReconstructor",
    "checkpoint": "/home/jackson-devworks/Desktop/ECCV_2024/output/SPN/OneLayerDenosing/Encoder-DecoderReconstructor"
}