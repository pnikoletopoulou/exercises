'''
Ask user for 3 numbers, a, b, and c. First number is the starting point, 
second number is the end point, and third number is the step. 
Then, print values from a to b, with a c step. If a is greater than b, then step down from a to b. Examples:
a: 3, b: 12, c: 3
Output: 3, 6, 9, 12
a: 20, b: 5, c: 4
Output: 20, 16, 12, 8
'''

print("Give three numbers!")

a = input("First number: ")
a = int(a)
b = input("Second number: ")
b = int(b)
c = input("Third number: ") 
c = int(c)

for i in range(a, b+1, c):
    print(i)

if a > b:
    for i in range(a, b-1, -c):
        print(i)

# DONE