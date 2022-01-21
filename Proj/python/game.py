# main game file, inclueds search fuction and main game loop

import random
from hash import hashTable
import os 
# initializing all variables 
file = open('Dictionary.txt', 'r') 
dictionary = hashTable(211)
[dictionary.insert(i.rstrip().lower()) for i in file] # Insert all words from dictionary to hash table  time complexity (O(n)), where n is the number of words in dictionary
file.close()
letters = [(chr(random.randint(97, 122))) for i in range(12)] # assigns 12 random letters to a list
used = [0] * 12 # list used for counting used letters
correct = []

def check(word): # funcion to check if the word is correct time complexity O(m*k) where m=len of letter list and n = len of word
    if word.lower() in correct: # checks if word was already answered time complexity (O(n)), where n is the number of words in list
        print("You've already entered the word, no credit!")
        return False
    if dictionary.find(word.lower()): # checks if word is in the given dictionary time complexity (O(1))
        for i in word.lower(): # compares each letter of the word with the letter list time complexity (O(n^2)) but its closer to O(m*k) where m=len of letter list and n = len of word
            for j in range(len(letters)):
                if i == letters[j] and used[j] == 0:
                    used[j] = 1
                    break
            else:
                print('Incorrect use of letter') # if the letters dont match with the list it retuns a false statment and prints a message
                return False
    else:
        print('This word does not exist in the dictionary') # if the word is not in the dictionary returns false and prints a message
        return False
    return word

# main game loop time complexity (O(n*m*k)), where n = times the player guessed, m = len of letters in letter list (12), k = len of longest word entered

print('Create your words from the following letters:') 
[print(i, end =' '*4) for i in letters]
print()

while True:
    word = input('Please enter your word or -1 to end:\n')
    if word == '-1': break
    if check(word): #calls the function to check input
        correct.append(word) # if correct append word to list
        print('That is correct!')
    used = [0] * 12 # resets used list for every new word

# Printing results time complexity (O(n))
print(f"You've entered the following correct words:")
[print(i) for i in correct]
print(f"You've got {len(correct)} points. Well done!")

print('Press any key to quit')  # for the .exe build of the game (so you can see results of the game)
os.system("pause >nul")
