def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def print_primes_less_than_20():
    print("Prime numbers less than 20:")
    for num in range(2, 20):
        if is_prime(num):
            print(num)

print_primes_less_than_20()
