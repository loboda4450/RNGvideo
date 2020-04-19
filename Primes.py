import time


def isPrime(value):
    if value > 1:  # every prime value is bigger than 1
        for divisor in range(2, value):  # every prime value is dividable by 1
            if value % divisor == 0:
                return True

        return False


def getRandomPrime(primes):
    return primes.getFirstLower(primes.getFirstHigher((int(time.time())) % 1000) *
                                primes.getFirstLower((int(time.time())) % 1000))


class Primes:
    def __init__(self):
        self.higher_prime = None
        self.lower_prime = None
        self.prime = None

    def getCalculatedPrimeValue(self, option):
        if option == 'higher':
            if self.higher_prime is not None:
                return int(self.higher_prime)
            else:
                return None
        elif option == 'lower':
            if self.lower_prime is not None:
                return int(self.lower_prime)
            else:
                return None
        else:
            if self.prime is not None:
                return int(self.prime)
            else:
                return None

    def getFirstHigher(self, seed):
        local_var = seed
        while isPrime(local_var) or local_var == seed:
            local_var = local_var + 1

        self.higher_prime = local_var
        return int(self.higher_prime)

    def getFirstLower(self, seed):
        local_var = seed
        while isPrime(local_var) or local_var == seed:
            local_var = local_var - 1

        self.lower_prime = local_var
        return int(self.lower_prime)
