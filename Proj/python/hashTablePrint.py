from hash import hashTable
file = open('Dictionary.txt', 'r') 
dictionary = hashTable(211)
[dictionary.insert(i.rstrip().lower()) for i in file]
file.close()
dictionary.print()
