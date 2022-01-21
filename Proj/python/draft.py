import random
import copy
from hash import hashTable

def check(word): # funcion to check if the word is correct time complexity (O(n^2))
    if word.lower() in correct: 
        print('word is already entered')
        return False
    if word.lower() in word_dict: # checks if word is in the given dictionary 
        for i in word.lower(): # compares each letter of the word with the letter list
            if i in temp_list:
                temp_list.remove(i) # removes the letters to make sure no one letter is used more than once
            else:
                print('word is not made up of the letters above') # if the letters dont match with the list it retuns a false statment and prints a message
                return False
    else:
        print('word not in dictionary') # if the word is not in the dictionary returns false and prints a message
        return False
    return word


# initializing all variables 
file = open('Dictionary.txt', 'r') # imports the dictionary file and assigns in to variable file
word_dict = [i.rstrip() for i in file] # appends all the words in the dictionary to a list (time complexity O(n))
letter_list = [chr(random.randint(97, 122)) for i in range(12)] # picks 12 random letters and appends them to a list
temp_list = copy.deepcopy(letter_list) # we make a copy of the list that way we can check for duplicate letters without loosing our original word list
correct = []

# running the game
# funcion to check if the word is correct time complexity (O(n^3))
print(letter_list) 
word = input()
while word != '-1':
    if check(word): #calls the function to check input
        correct.append(word) # if correct append word to list
        print('correct')
    temp_list = copy.deepcopy(letter_list) # reset the temp_list so it can check again for next run
    word = input()
    
print(f'You guessed {len(correct)} words correctly, \nthe correct guesses were: {correct}')
