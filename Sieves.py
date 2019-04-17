import math

def EratosthenesHelper(maxNum, mostlyPrime):
    checkprimes = EratosthenesSieve(int(math.sqrt(mostlyPrime[-1])))
    for i in checkprimes:
        j = 1
        while i*j < mostlyPrime[-1]:
            if i*j in mostlyPrime:
                print(i * j, end = "\r") 
                mostlyPrime.remove(i*j)
            j += 1
    return checkprimes + mostlyPrime

def EratosthenesSieve(maxNum):
    primes = [True for i in range(maxNum+1)]
    returnPrimes = []
    p = 2
    while p*p <= maxNum:
        if primes[p] == True:
            for i in range(p*2, maxNum+1, p):
                primes[i] = False
        p += 1
    for i in range(1, len(primes)):
        if primes[i] == True:
            returnPrimes.append(i)
    returnPrimes.remove(1)
    return returnPrimes

def SundaramSieve(maxNum):
    m = int((maxNum - 2) / 2)
    primes = [0] * (m + 1)
    returnPrimes = []
    for i in range(1, m + 1):
        j = i
        while((i + j + 2*i*j) <= m):
            primes[i + j + 2*i*j] = 1
            j +=1
    for i in range(1, m + 1):
        if (primes[i] == 0):
            returnPrimes.append((2*i + 1))
    returnPrimes.append(2)
    returnPrimes.sort()
    return returnPrimes

def AtkinSieve(maxNum):
    primes = []
    sieve = [False] * maxNum
    for i in range(0, maxNum):
        sieve[i] = False
    n = 0
    x = 1
    while(x * x < maxNum):
        y = 1
        while(y * y < maxNum):
            n = (4 * x * x) + (y * y)
            if (n <= maxNum and (n % 12 == 1 or n % 12 == 5)):
                sieve[n] ^= True
            n = (3 * x * x) + (y * y)
            if (n <= maxNum and n % 12 == 7):
                sieve[n] ^= True
            n = (3 * x * x) - (y * y)
            if (x > y and n <= maxNum and n % 12 == 11):
                sieve[n] ^= True
            y += 1
        x += 1
    r = 5
    while(r * r < maxNum):
        if (sieve[r]) :
            for i in range(r * r, maxNum, r * r):
                sieve[i] = False
        r += 1
    for a in range(5, maxNum):
        if (sieve[a]):
            primes.append(a)
    primes.append(2)
    primes.append(3)
    primes.sort()
    return primes

