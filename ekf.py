""" Written by Brian Hou for CSE571: Probabilistic Robotics
"""

import numpy as np

from utils import minimized_angle


class ExtendedKalmanFilter:
    def __init__(self, mean, cov, alphas, beta):
        self.alphas = alphas
        self.beta = beta

        self._init_mean = mean
        self._init_cov = cov
        self.reset()

    def reset(self):
        self.mu = self._init_mean
        self.sigma = self._init_cov

    def update(self, env, u, z, marker_id):
        """Update the state estimate after taking an action and receiving a landmark
        observation.

        u: action
        z: landmark observation
        marker_id: landmark ID
        """
        # YOUR IMPLEMENTATION HERE
        # print("mu: ", self.mu)
        # print("sigma: ", self.sigma)
        # print("beta: ", self.beta)
        # print("alpha: ", self.alphas)
        # x = self.mu.reshape(3,)

        # Calculate dynamics.
        mu_pred, G = env.G(x=self.mu, u=u)
        V = env.V(x=self.mu, u=u)
        M = env.noise_from_motion(u, self.alphas)
        cov_pred = np.matmul(np.matmul(G, self.sigma), G.T) + np.matmul(np.matmul(V, M), V.T)

        # Calculate observations.
        H = env.H(x=mu_pred, marker_id=marker_id)
        # print("cov: ", cov_pred.shape, cov_pred)
        # print("H shape: ", H.shape, H)
        # K = Kalman Gain
        K = np.matmul(np.matmul(cov_pred, H.T), np.linalg.inv(np.matmul(np.matmul(H, cov_pred), H.T) + self.beta))
        mu_pred = mu_pred + np.matmul(K, minimized_angle(z - env.observe(x=mu_pred, marker_id=marker_id)))
        cov_pred = np.matmul((np.identity(n=cov_pred.shape[0]) - np.matmul(K, H)), cov_pred)

        self.mu = mu_pred
        self.sigma = cov_pred
        

        return self.mu, self.sigma
