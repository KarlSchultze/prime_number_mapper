from prime_number_calculator import PrimeNumberCalculator
import numpy as np
import matplotlib.pyplot as plt
from tqdm import tqdm


def generate_graph(P):
    numerator_domain = []
    denomiator_domain = []
    f = []

    horizontal_line_at_1 = []

    prime_numbers_domain = P[:len(P)]
    f_at_prime = []

    # even_numbers_domain = []
    # f_at_even = []

    # fibonnaci_numbers_domain = [1/2, 1, 2]
    # f_at_fibonnaci = [1, 1, 1]

    for i in range(P[-1]):
        numerator_domain.append(i+1)
        denomiator_domain.append(int(str(i+1)[::-1]))
        f.append(numerator_domain[i]**2/denomiator_domain[i]**2)
        if i+1 in P:
            f_at_prime.append(numerator_domain[i]**2/denomiator_domain[i]**2)
        # if i+1 % 2 is not 0:
        #     f_at_even.append(numerator_domain[i]**2/denomiator_domain[i]**2)
        #     even_numbers_domain.append(i)
        # if i == fibonnaci_numbers_domain[-1] + fibonnaci_numbers_domain[-2]:
        #     f_at_fibonnaci.append(numerator_domain[i]**2/denomiator_domain[i]**2)
        #     fibonnaci_numbers_domain.append(i)
        horizontal_line_at_1.append(1)
        # horizontal_line_at_pi.append(np.pi)

    fig = plt.figure()
    ax = plt.axes()
    ax.set()
    ax.scatter(numerator_domain, f, marker=',')
    ax.scatter(prime_numbers_domain[:len(f_at_prime)], f_at_prime, marker=',')
    # ax.scatter(even_numbers_domain, f_at_even, marker=',')
    # ax.scatter(fibonnaci_numbers_domain, f_at_fibonnaci, marker=',')
    ax.plot(numerator_domain, horizontal_line_at_1)

    plt.show()


def main():
    n = int(input('Please enter a natural number greater than or equal to one: '))
    pnc = PrimeNumberCalculator()
    P = pnc.calculate_prime_set(n)
    generate_graph(P)


if __name__ == '__main__':
    main()
