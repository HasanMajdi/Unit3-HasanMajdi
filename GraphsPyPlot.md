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
```.py 
_______________________________
3. 

