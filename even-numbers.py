'''
Create a list and fill with 20 random numbers (1 – 100). Then count how many of them are even. 
'''

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

# DONE