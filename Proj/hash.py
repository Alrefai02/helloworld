# hash table file

from node import Node

class hashTable:

    def __init__(self, size):
        self.size = size 
        self.list = size * [None]

    def hash1(self, key): # first hash function
        return (key % self.size)
    # time complexity O(1)

    def hash2(self, key): # second hash function
        return 5 - key % 5
    # time complexity O(1)

    def wordToText(self, word): # turns the word to a key
        counter = 0
        num = 0
        for i in word[::-1]:
            num += (ord(i)-96)*(27**counter)
            counter +=1
        return num
    # time complexity O(n), but since the words are very short it might as well be O(1)
    
    def insert(self, word): #inserts word in hash table
        key = self.wordToText(word)
        node = Node(word, key)
        index = self.hash1(key)
        step = self.hash2(key)
        
        if self.list[index] == None or self.list[index] == -1:
            self.list[index] = node
            return True
        
        while ((self.list[index] != None) and (self.list[index] != -1)):
            index += step
            index = index % self.size
        self.list[index] = node
    # time complexity O(1)

    def find(self, word): # searches for word in hash table
        key = self.wordToText(word)
        index = self.hash1(key)
        step = self.hash2(key)

        while ((self.list[index]) != None and (self.list[index] != -1)):
            if self.list[(index) % self.size].word == word:
                return True
            index += step
            index = index % self.size
        return False
    # time complexity O(1)

    def remove(self, word): # removes word from hash table
        key = self.wordToText(word)
        index = self.hash1(key)
        steps = self.hash2(key)
        
        while (self.list[index] != None):
            if(self.list[index].word == word):
                tmp = self.list[index]
                self.list[index] = -1
                return tmp
            index += steps
            index = index % self.size
        return None
    # time complexity O(1)

    def print(self): # prints all cells in hash table
        print("\nCell\tWord\t")
        for i in range(len(self.list)):
            if self.list[i] == None or self.list[i] == -1:
                print(f'{i} \t\t *')
            else:
                print(f'{i} \t\t {self.list[i].word}')
    # time complexity O(n), where n is the size of the hash tables 
    