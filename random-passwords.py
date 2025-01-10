'''
Write a program to generate random passwords. A password must be 10
characters long and contain upper- and lower-case letters, digits 0-9, and special characters.
Suggestion: use four lists, lower_case_letters, upper_case_letters, digits, special_characters,
and randomly select a list and then randomly characters from the list.
'''
import random

lower_case_letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p',
                       'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y','z']
upper_case_letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K',
                       'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'X', 'Y', 'Z']
digits = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
special_characters = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '_', '=', '+', '/',
                       '[', ']', '{', '}', ';', ':', '/', '?', '.', '>', '<']  

all = lower_case_letters + upper_case_letters + digits + special_characters

for i in range(10):
    password = random.choice(all)
    print(password, end='')

