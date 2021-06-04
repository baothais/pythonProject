def is_prime(prime):
    if prime < 2:
        return False
    return all(prime % i != 0 for i in range(2, int(pow(prime, 0.5)) + 1))

print(is_prime(6))


