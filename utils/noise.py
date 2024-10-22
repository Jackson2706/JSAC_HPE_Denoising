#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 21 10:55:19 2024

@author: jackson-devworks
"""

import numpy as np

def add_awgn(signal, noise_level):
    """
    Add Additive White Gaussian Noise (AWGN) to a signal.

    :param signal: Input signal (numpy array).
    :param noise_level: Noise level defined as the standard deviation of the noise as a proportion of the signal's dynamic range.
    :return: Noisy signal with AWGN added.
    """
    # Calculate the standard deviation based on the signal's dynamic range
    std_dev = noise_level * (np.max(signal) - np.min(signal))

    # Generate Gaussian noise
    noise = np.random.normal(loc=0, scale=std_dev, size=signal.shape)
    
    # Add noise to the original signal
    noisy_signal = signal + noise
    
    return noisy_signal
