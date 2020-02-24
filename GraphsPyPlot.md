```.py
import matplotlib.pyplot as pyplot
import random

# create the values for the x variable from -10 to 10
x = [i for i in range(1, 1001)]
# define the parabola function
y = [i**2 for i in x]
# create graph
pyplot.plot(x, y)
# title for this graph
pyplot.xlabel('x')
pyplot.ylabel('y')
# show the graph
pyplot.show()
```
________________________________

1. Generate 1000 random numbers between 1 and 100
```.py 

import matplotlib.pyplot as pyplot
import random

# y = []
y = list()
for x in range(1, 1001):
    y.append(random.randint(1, 101))
    print(y)
x = [x]
y = [y]

pyplot.plot(x, y)

pyplot.xlabel('x')
pyplot.ylabel('y')
# show the graph
pyplot.show()
```
_______________________________
2.  Calculate the average of the 1000 random numbers in ① using a loop.
```.py 

import matplotlib.pyplot as pyplot
import random

# y = []
y = list()
for x in range(1, 1001):
    y.append(random.randint(1, 101))
    print(y)
calc = 0
for c in y:
    calc += c
print('Average is :', calc / len(y))

for i in range(1, 100):
    number = i
```
_______________________________
3. 
```.py 
import matplotlib.pyplot as pyplot
import random

# y = []
y = list()
for x in range(1, 1001):
    y.append(random.randint(1, 101))

calc = 0
for c in y:
    calc += c
print('Average is :', calc / len(y))

number =[]
for i in range(1, 1001):
    number.append(i)

z = [ p**2 for p in number]
# define the parabola function
# create graph
pyplot.plot(number,z)
# title for this graph
pyplot.xlabel('x')
pyplot.ylabel('$y= x^2$')
# show the graph
pyplot.show()
```
__________________
4.
```.py 
import matplotlib.pyplot as pyplot
import math

min_x = -10
max_x = 10
step = 0.1
num_points = int((max_x - min_x)/step)
x = list()
for k in range(num_points):
    x.append(min_x + step*k)

y = [math.sin(0.5 * n) for n in x]
# define the parabola function
z = [math.cos(0.5 * f) for f in x]
# create graph
pyplot.plot(y, z)
# title for this graph
pyplot.xlabel('y')
pyplot.ylabel('z')
# show the graph
pyplot.show()
```
________________
