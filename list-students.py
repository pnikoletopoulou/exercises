
students = ['John Green', 'Alex Tomas', 'Mary Green', 'Anna Smith', 
            'Mike Tomas', 'Andrew Green']

fullnames = []

for student in students:
    first, last = student.split(' ')
    fullname = first[0].lower() + last.lower()

    counter = 0

    while fullname in fullnames:
       fullname = fullname + counter
       counter += 1

    fullnames.append(fullname)

print(fullnames)
