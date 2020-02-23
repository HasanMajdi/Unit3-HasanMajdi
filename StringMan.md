# read a text in python
```.py
from functools import reduce

file = open("text.txt", "r")

extract = file.read()

words = extract.split()

print("number f words is {}".format(len(words)))
```
###
```.py
keywords = ['house', 'worker', 'master', 'hard']
for key in keywords:
    print("checking words " +key+ "in the text")
    print(key in words)
```

###

```.py
**( another way to print using f' )**
lenOfText = len(extract)
 num_letters=0
 for symbol in extract
     if symbol.isalpha():
         num_letters = num_letters + 1

print(f'there are {num_letters} out of {leghtOfText} total characthers')

print(extract.capitalize)
```
###

```.py
def checklen(x):
    if len(x)>5:
        return True
    else:
        return False

long_words = '#'.join(list(filter(lambda x: len(x) > 5, words)))

totalSumPythonic = reduce(lambda a,b : ord(a)+b, extract)
print(totalSumPythonic)
```
### 
```.py
totalSum = 0
for l in extract:
    totalSum += ord(l)
print(totalSum)
```
###
