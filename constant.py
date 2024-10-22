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
    "mode": 1, # Mode 0: no denoiser layer, Mode 1: have denoiser layers
    "epoch": 20,
    "checkpoint": "/home/jackson-devworks/Desktop/ECCV_2024/output/FourLayerDenosing"
}

denoiser_config = {
    "epoch": 20,
    "mode": 1, # Mode 0: 1 stage AE, Mode 1: stacked AE
    "checkpoint": "/home/jackson-devworks/Desktop/ECCV_2024/output/FourLayerDenosing/Encoder-DecoderReconstructor"
}