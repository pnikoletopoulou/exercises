
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
