'''
Given a list of students, generate usernames for each one of them and put
them in another list. In case a username already exists, due to name similarity, use a counter to
add a number at the end and increase the counter.
Example:
students = [‘John Doe’, ‘Mary Smith’, ‘Andrew Green’, ‘Lisa Tomas’,
‘Mike Smith’, ‘Alex Green’]
result will be => [‘jdoe’, ‘msmith’, ‘agreen’, ‘ltomas’, ‘msmith1’,
‘agreen2’]
'''

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
   
   
     
