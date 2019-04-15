import Sieves
import plotly.plotly as py
import plotly.graph_objs as go
import time

EratosthenesTimes = []
WheelTimes = []
SundramTimes = []
AtkinTimes = []

for i in range(100, 1000, 100):
    start_time = time.time()
    Sieves.EratosthenesSieve(i)
    EratosthenesTimes.append(time.time() - start_time)

yValues = []
for y in range(100, 10000, 100):
    yValues.append(y)
trace0 = go.Scatter(
    x = EratosthenesTimes,
    y = yValues
)
data = [trace0]
py.plot(data, filename = 'eratos-line', auto_open=True)
print(EratosthenesTimes)

