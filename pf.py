""" Written by Brian Hou for CSE571: Probabilistic Robotics (Winter 2019)
    Modified by Wentao Yuan for CSE571: Probabilistic Robotics (Spring 2022)
"""

import numpy as np

from utils import minimized_angle


class ParticleFilter:
    def __init__(self, mean, cov, num_particles, alphas, beta):
        self.alphas = alphas
        self.beta = beta

        self._init_mean = mean
        self._init_cov = cov
        self.num_particles = num_particles
        self.reset()

    def reset(self):
        self.particles = np.zeros((self.num_particles, 3))
        for i in range(self.num_particles):
            self.particles[i, :] = np.random.multivariate_normal(
                self._init_mean.ravel(), self._init_cov)
        self.weights = np.ones(self.num_particles) / self.num_particles

    def move_particles(self, env, u):
        """Update particles after taking an action

        u: action
        """
        new_particles = self.particles

        # YOUR IMPLEMENTATION HERE

        # Call sample noisy action and move particles with noisy action.
        for i in range(new_particles.shape[0]):
            new_particles[i] = env.forward(x=new_particles[i], u=env.sample_noisy_action(u=u)).reshape(3,)

        # print("particle size: ", new_particles.shape, new_particles)
        
        return new_particles

    def update(self, env, u, z, marker_id):
        """Update the state estimate after taking an action and receiving 
        a landmark observation.

        u: action
        z: landmark observation
        marker_id: landmark ID
        """
        particles = self.move_particles(env, u)

        # YOUR IMPLEMENTATION HERE

        # Call observe() to get bearing of each of the new particles.
        observations = np.ndarray(particles.shape[0])
        for i in range(particles.shape[0]):
            observations[i] = env.observe(particles[i], marker_id)
        
        # Get the likelihood of the particle being in that position given z.
        innovations = np.ndarray(particles.shape[0])
        for i in range(observations.shape[0]):
            innovations[i] = minimized_angle(z - observations[i])

        likelihood = env.likelihood(innovations.reshape(1, innovations.shape[0]), self.beta)
        # Gather weights from diagonal.
        weights = likelihood.diagonal()
        # print("observations: ", observations)
        # print("\n")
        # print("innovations: ", np.amin(np.abs(innovations)))
        # print("\n")
        # print("z: ", z)
        # print("\n")
        # print("weights: ", np.amax(weights))

        # Resample with new weight.
        self.particles = self.resample(particles=particles, weights=weights)

        mean, cov = self.mean_and_variance(self.particles)
        return mean, cov

    def resample(self, particles, weights):
        """Sample new particles and weights given current particles and weights. Be sure
        to use the low-variance sampler from class.

        particles: (n x 3) matrix of poses
        weights: (n,) array of weights
        """
        # YOUR IMPLEMENTATION HERE
        # chosen_particles = []
        new_particles = np.ndarray(shape=(particles.shape))
        num_particles = particles.shape[0]
        total_weight = np.sum(weights)
        ratio = total_weight / num_particles
        r = np.random.uniform(low=0, high=(ratio))
        # print("r: ", r)
        c = weights[0]
        i = 0
        j = 0
        for m in range(num_particles):
            u = r + (m) * (ratio)
            while u > c:
                i = i + 1
                c = c + weights[i]
                # print("u: ", u)
                # print("c: ", c)
            
            new_particles[m] = particles[i]

        # new_particles = np.ndarray(shape=(len(chosen_particles), 3))
        # for i in range(len(chosen_particles)):
        #     new_particles[i] = chosen_particles[i]
                
        return new_particles

    def mean_and_variance(self, particles):
        """Compute the mean and covariance matrix for a set of equally-weighted
        particles.

        particles: (n x 3) matrix of poses
        """
        mean = particles.mean(axis=0)
        mean[2] = np.arctan2(
            np.sin(particles[:, 2]).sum(),
            np.cos(particles[:, 2]).sum(),
        )

        zero_mean = particles - mean
        for i in range(zero_mean.shape[0]):
            zero_mean[i, 2] = minimized_angle(zero_mean[i, 2])
        cov = np.dot(zero_mean.T, zero_mean) / self.num_particles
        cov += np.eye(particles.shape[1]) * 1e-6  # Avoid bad conditioning 

        return mean.reshape((-1, 1)), cov
