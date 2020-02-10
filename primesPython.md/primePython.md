def is_prime_v1(n):
    """Return 'True' if 'n' is a prime number. False if not"""
    if n == 1:
        return false # 1 is not prime

    for d in range(2, n):
        if n % d == 0:
            return False
        return True

    # TEST FUNCTION
    for n in range(1, 21):
        print(n, is_prime_v1(n))
        
        # TIME FUNCTION
    t0 = time.time()
    for n in range(1, 100000): 
        is_prime_v1()
    t1 = time.time()
    print("time required: ", t1 - t0)
