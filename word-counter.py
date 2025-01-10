'''
Ask user for a word and find how many times the word exists in the story.txt
file.
'''

file = open('story.txt', 'r')
lines = file.readlines()
word = input("Give a word: ").lower()

counter = 0

for line in lines:
   words = line.lower().split()
   counter += words.count(word)
   
print(counter)
