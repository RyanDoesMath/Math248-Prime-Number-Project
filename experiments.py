import Sieves
import time

EratosthenesTimes = []
WheelTimes = []
SundramTimes = []
AtkinTimes = []

start_time = time.time()
Sieves.EratosthenesSieve(100000)
print(time.time() - start_time)

for i in range(10, 10000, 10):
    start_time = time.time()
    Sieves.EratosthenesSieve(i)
    EratosthenesTimes.append(time.time() - start_time)

f = open("Times_for_Eratosthenes_Sieve", "w+")
f.write('[')
f.write(''.join((str(e) + ',') for e in EratosthenesTimes))
f.write(']')
f.close()
print(EratosthenesTimes)

