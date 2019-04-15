import math

def WheelSieve(maxNum):
    basis = [2, 3, 5]
    spokes = []
    toRemove = []
    newWheel = []
    returnWheel = []
    h = 1
    n = 1
    x = 1
    for i in basis:
        n = n * i
    for j in range(1, n + 1):
        spokes.append([j])
    while x*n + h < maxNum:
        for j in spokes:
            if x*n + h < maxNum:
                j.append(x*n + h)
            h += 1
        x += 1
        h = 1
    for i in range (1, n + 1):
        for j in basis:
            if i % j == 0 and i not in toRemove:
                toRemove.append(i)
    for i in spokes:
        if i[0] not in toRemove:
            newWheel.append(i)
        if i[0] in basis:
            newWheel.append([i[0]])
    for i in newWheel:
        for j in i:
            returnWheel.append(j)
    returnWheel.remove(1)
    returnWheel.sort()
    return EratosthenesHelper(maxNum, returnWheel)

def EratosthenesHelper(maxNum, mostlyPrime):
    checkprimes = EratosthenesSieve(int(math.sqrt(maxNum)))
    for i in checkprimes:
        for j in mostlyPrime:
            if j % i == 0 and i != j:
                mostlyPrime.remove(j)
    return mostlyPrime

def EratosthenesSieve(maxNum):
    composites = []
    primes = []
    for i in range(2, int(math.sqrt(maxNum))):
        if i not in composites:
            for x in range(i * i, maxNum, i):
                composites.append(x)
    for i in range(2, maxNum):
        if i not in composites:
            primes.append(i)
    return primes

def SundaramSieve(maxNum):
    m = int((maxNum - 2) / 2)
    primes = []
    for i in range(2, m + 1):
        primes.append(i)
    for i in range(1, m + 1):
        for j in range(1, m + 1):
            if j >= i:
                if i + j + 2*i*j in primes:
                    primes.remove(i + j + 2*i*j)
    for i in range(len(primes)):
        primes[i] = primes[i] * 2 + 1
    primes.append(2)
    primes.append(3)
    primes.sort()
    return primes

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

print(WheelSieve(100))
print(EratosthenesSieve(100))
print(SundaramSieve(100))
print(AtkinSieve(100))
print(WheelSieve(100) == EratosthenesSieve(100) 
        == SundaramSieve(100) == AtkinSieve(100))

