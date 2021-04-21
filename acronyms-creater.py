user_input = str(input("Enter The Phrase: "))
usrinpt = user_input.split()
self = " "
for i in usrinpt:
    self = self+str(i[0]).upper()
print(self)
