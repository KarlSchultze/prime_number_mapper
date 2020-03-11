class PrimeNumberCalculator:
    def __init__(self):
        # Instance variables.
        self._P = []

    def get_P(self):
        return self._P

    def calculate_prime_set(self, N):
        '''
        Calculates the primes less than the upper bound.
        Input:  N, a natural number greater than one.
        Output: P, the set of prime numbers less than N.
        '''
        # Validates N.
        if not isinstance(N, int):
            raise ValueError('N is not a natural number greater than one.', N)
        self._P = [2]
        for n in range(3, N):
            # Assume n in P.
            n_is_prime = True
            # Grabs indicies for every p in P.
            for i in range(len(self._P)):
                # If p divides n, then n is not prime.
                if n % self._P[i] == 0:
                    n_is_prime = False
            # Extends set of P if n is still prime.
            if n_is_prime:
                self._P.append(n)
        return self._P

    def validate_natural_number(self, n):
        if n is not int or n < 1:
            raise ValueError('N is not a natural number.')
        return n
