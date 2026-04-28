def primes(limit):
    if limit < 2:
        return []

    # Step 1: Create a list to track prime status
    sieve = [True] * (limit + 1)
    sieve[0] = sieve[1] = False  # 0 and 1 are not prime

    # Step 2: Apply the sieve
    for num in range(2, int(limit ** 0.5) + 1):
        if sieve[num]:
            # Mark multiples of num as not prime
            for multiple in range(num * num, limit + 1, num):
                sieve[multiple] = False

    # Step 3: Collect all prime numbers
    return [num for num, is_prime in enumerate(sieve) if is_prime]