import Sieves
import time

EratosthenesTimes = []
WheelTimes = []
SundramTimes = []
AtkinTimes = []

start_time = time.time()
Sieves.EratosthenesSieve(50000)
print(time.time() - start_time)
start_time = time.time()
Sieves.SundaramSieve(50000)
print(time.time() - start_time)
start_time = time.time()
Sieves.AtkinSieve(50000)
print(time.time() - start_time)

counter = 0

f = open("Times_for_Eratosthenes_Sieve", "w+")
f.write('[')
for i in range(1000, 1000000, 1000):
    start_time = time.time()
    Sieves.EratosthenesSieve(i) 
    f.write(str(time.time() - start_time))
    f.write(', ')
    counter += 1
    if i < 1000000:
        print(counter, end = "\r")
f.write(']')

counter = 0

g = open("Times_for_Sundaram", "w+")
g.write('[')
for j in range(1000, 1000000, 1000):
    start_time = time.time()
    Sieves.SundaramSieve(j)
    g.write(str(time.time() - start_time))
    g.write(', ')
    counter += 1
    if j < 1000000:
        print(counter, end = "\r")
g.write(']')

counter = 0

h = open("Times_for_Atkin", "w+")
h.write('[')
for k in range(1000, 1000000, 1000):
    start_time = time.time()
    Sieves.AtkinSieve(k)
    h.write(str(time.time() - start_time))
    h.write(', ')
    counter += 1
    if k < 1000000:
        print(counter, end = "\r")
h.write(']') 

