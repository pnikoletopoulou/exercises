
import random

numbers = []

for i in range(20):
    value = random.randint(1, 100)
    numbers.append(value)
    
counter = 0 

for i in numbers:
    if i % 2 == 0:
        counter += 1

print(counter)
