
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
