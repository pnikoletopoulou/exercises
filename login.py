'''
Use the users CSV data below and put them in a file users.csv.
Then, write a program to ask user for username and pin. If the username and pin are in the file,
respond with a welcome message, else display a user not found message.
Example 1:
Username: grey07
PIN: 9012
Sorry, user not found
Example 2:
Username: grey07
PIN: 2070
Welcome Laura
'''
def load_users():
    file = open('users.csv')
    lines = file.readlines()

    users = {}

    for line in lines:
        parts = line.strip().split(',')
        if parts[0] != 'username':
           users[parts[0]] = {'Pin': parts[1]}
    return users 

def login_prompt():
   username = input('Username: ')
   Pin = input('Pin: ')
   return username,Pin

username, Pin = login_prompt()
users = load_users()

if username in users and users[username]['Pin'] == Pin:
    print("Welcome", username)
else:
    print('User not found!')