import time
import matplotlib.pyplot as plt


def sieve_of_eratosthenes(limit):
    primes = [True] * (limit + 1)
    primes[0] = primes[1] = False
    for num in range(2, int(limit**0.5) + 1):
        if primes[num]:
            for multiple in range(num * num, limit + 1, num):
                primes[multiple] = False
    return [num for num, is_prime in enumerate(primes) if is_prime]


def is_psp(num, base, prime):
    exp = num - 1
    while exp % prime != 0:
        exp += num - 1
    return pow(base, exp // prime, num) == 1


def pomerance_algorithm(limit):
    primes = sieve_of_eratosthenes(limit)
    result = []
    for num in range(2, limit):
        is_psp_2 = all(is_psp(num, 2, prime) for prime in primes)
        is_psp_3 = all(is_psp(num, 3, prime) for prime in primes)
        if is_psp_2 and is_psp_3:
            result.append(num)
    return result


limits = [10**6 ,10**8]  # Разные лимиты для анализа времени выполнения

for i in limits:
    psp_numbers = pomerance_algorithm(i)
    print(f"PSP numbers less than {i}: {psp_numbers}")
execution_times = []

for limit in limits:
    start_time = time.time()
    psp_numbers = pomerance_algorithm(limit)
    end_time = time.time()
    execution_times.append(end_time - start_time)
    print(f"PSP numbers less than {limit}: {len(psp_numbers)}")

# Построение графика времени выполнения
plt.figure(figsize=(8, 6))
plt.plot(limits, execution_times, marker='o', color='b', linestyle='-', linewidth=2, markersize=8)
plt.xlabel('Number Limit')
plt.ylabel('Execution Time (seconds)')
plt.title('Execution Time vs. Number Limit')
plt.grid(True)
plt.show()
