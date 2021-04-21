#To create acronyms using Python, you need to write a python program that generates a short form of a word from a given sentence.
#You can do this by splitting and indexing to get the first word and then combine it. 
#Let’s see how to create an acronym using Python:


user_input = str(input("Enter The Phrase: "))
usrinpt = user_input.split()
self = " "
for i in usrinpt:
    self = self+str(i[0]).upper()
print(self)
