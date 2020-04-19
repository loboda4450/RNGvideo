import time
import numpy as np
from math import log, e


class RNGutils:
    def __init__(self):
        self.random_array = []
        self.entropy = 0.
        self.b0 = None
        self.d0 = None
        self.f0 = None
        self.l0 = None
        self.m = None

    def single_handler(self, lower_prime, higher_prime, rnd_range):
        try:
            self.m = lower_prime * higher_prime
            self.b0 = (lower_prime ** 2) % self.m
            self.d0 = (higher_prime ** 2) % self.m
            self.l0 = int(time.time()) * 1000
            self.f0 = self.b0 * self.d0 * self.l0 % rnd_range
        except Exception as exception:
            print(exception)

    def sequence_handler(self, primes, sequention_length, rnd_range):
        for i in range(int(sequention_length)):
            try:
                self.m = primes.lower_prime * primes.higher_prime
                self.b0 = (self.b0 ** 2) % self.m
                self.d0 = (self.d0 ** 2) % self.m
                self.l0 = (self.l0 * primes.lower_prime + primes.higher_prime) % self.m
                self.f0 = self.b0 * self.d0 * self.l0 % rnd_range
                self.random_array.append(self.f0)
            except Exception as excep:
                print(excep)

    def entropy_handler(self, base=None):
        n_labels = len(self.random_array)
        if n_labels <= 1:
            return 0

        value, counts = np.unique(self.random_array, return_counts=True)
        probs = counts / n_labels
        n_classes = np.count_nonzero(probs)
        if n_classes <= 1:
            return 0

        base = e if base is None else base
        for i in probs:
            self.entropy -= i * log(i, base)

    def single(self, primes, pixel_seed, rnd_range):
        primes.getFirstHigher(seed=pixel_seed)
        primes.getFirstLower(seed=pixel_seed)
        self.single_handler(lower_prime=primes.lower_prime, higher_prime=primes.higher_prime, rnd_range=rnd_range)
        return int(self.f0)

    def sequence(self, primes, pixel_seed, length, rnd_range):
        primes.getFirstHigher(seed=pixel_seed)
        primes.getFirstLower(seed=pixel_seed)
        self.single_handler(lower_prime=primes.lower_prime, higher_prime=primes.higher_prime, rnd_range=rnd_range)
        self.sequence_handler(primes=primes, sequention_length=length, rnd_range=rnd_range)
        self.entropy_handler(base=2)
        return self.random_array
