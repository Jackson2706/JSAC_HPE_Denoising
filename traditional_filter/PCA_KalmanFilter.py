#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 22 23:55:38 2024

@author: jackson-devworks
"""

import numpy as np
from sklearn.decomposition import PCA

class KalmanFilter:
    def __init__(self, process_variance, measurement_variance, initial_estimate=0, initial_error=1):
        """
        Initialize the Kalman Filter parameters.

        Args:
            process_variance (float): The variance of the process noise (Q).
            measurement_variance (float): The variance of the measurement noise (R).
            initial_estimate (float): Initial estimate of the state (x).
            initial_error (float): Initial estimate of the error covariance (P).
        """
        self.process_variance = process_variance  # Q
        self.measurement_variance = measurement_variance  # R
        self.estimate = initial_estimate  # x
        self.error_covariance = initial_error  # P

    def update(self, measurement):
        """
        Update the Kalman Filter estimate based on the measurement.

        Args:
            measurement (float): The new measurement to update the estimate.

        Returns:
            float: The updated estimate after applying the Kalman Filter.
        """
        # Prediction step (no control input assumed)
        self.error_covariance += self.process_variance  # P = P + Q

        # Kalman Gain calculation
        kalman_gain = self.error_covariance / (self.error_covariance + self.measurement_variance)  # K = P / (P + R)

        # Update the estimate with the new measurement
        self.estimate += kalman_gain * (measurement - self.estimate)  # x = x + K * (z - x)

        # Update the error covariance
        self.error_covariance *= (1 - kalman_gain)  # P = (1 - K) * P

        return self.estimate

def apply_kalman_filter_1d(data, process_variance=1e-5, measurement_variance=1e-2):
    """
    Apply Kalman Filter to 1D data (time series).

    Args:
        data (numpy array): Input 1D data (time series).
        process_variance (float): Variance of the process noise (Q).
        measurement_variance (float): Variance of the measurement noise (R).

    Returns:
        numpy array: Denoised data after applying Kalman Filter.
    """
    kf = KalmanFilter(process_variance, measurement_variance, initial_estimate=data[0])

    denoised_data = np.zeros_like(data)
    for i, measurement in enumerate(data):
        denoised_data[i] = kf.update(measurement)

    return denoised_data


def apply_pca_kalman_filter(csi_data, n_components=10, process_variance=1e-5, measurement_variance=1e-2):
    """
    Apply PCA for dimensionality reduction followed by Kalman Filter for denoising.

    Args:
        csi_data (numpy array): Input 4D WiFi CSI data of shape (batch_size, transmitters_receivers, subcarriers, time_steps).
        n_components (int): Number of PCA components to retain.
        process_variance (float): Variance of the process noise (Q).
        measurement_variance (float): Variance of the measurement noise (R).

    Returns:
        numpy array: Denoised CSI data after applying PCA and Kalman Filter.
    """
    batch_size, num_channels, num_subcarriers, num_timesteps = csi_data.shape
    
    # Initialize PCA object to reduce the number of subcarriers
    pca = PCA(n_components=n_components)

    # Initialize the output denoised data
    denoised_csi_data = np.zeros_like(csi_data)

    for b in range(batch_size):
        for channel in range(num_channels):
            # Apply PCA to reduce subcarriers dimensionality for each channel and batch
            reduced_data = pca.fit_transform(csi_data[b, channel, :, :].T)  # Transpose to apply PCA on subcarriers
            
            # Apply Kalman Filter to the reduced time series data
            denoised_reduced_data = np.zeros_like(reduced_data)
            for pc in range(n_components):
                denoised_reduced_data[:, pc] = apply_kalman_filter_1d(reduced_data[:, pc], process_variance, measurement_variance)

            # Reconstruct the data from the reduced components back to the original subcarrier space
            reconstructed_data = pca.inverse_transform(denoised_reduced_data).T  # Inverse PCA transformation

            # Store the denoised, reconstructed data
            denoised_csi_data[b, channel, :, :] = reconstructed_data

    return denoised_csi_data