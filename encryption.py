import random
chars = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u",
         "v", "w", "x", "y", "z", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", " "]
while 1 > 0:
    cryptali = ""
    while cryptali != "ept" and cryptali != "dpt":
        print("Tell me to encrypt or decrypt your message>>>(enter 'ept' for encrypt or 'dpt' for decrypt)")
        cryptali = input("enter 'ept' or 'dpt' ")
    print("lowercase,uppercase,digits 0-9 and spaces are accepted by me")
    your_message = input("tell me your message")
    if cryptali == "ept":
        key = random.randint(100, 100000)
        print("Your key for your encrypted message  is: " + str(key))
        print("The key is required while decrypting the message")
        i = 0
        encryptalimsg = ""
        while i < len(your_message):
            fool = int(str(chars.index(your_message[i])))
            fool = fool * key
            fool = fool + key
            print(fool)
            encryptalimsg = encryptalimsg + str(fool)
            encryptalimsg = encryptalimsg + ";"
            i += 1
            print("encrypted message: " + encryptalimsg)
    if cryptali == "dpt":
        key = int(input("input your key"))
        encryptalimsg = your_message
        lolmsg = ""
        i = 0
        encryptalimsg = str(encryptalimsg)
        while i <= len(encryptalimsg)-1:
            digit = ""
            while encryptalimsg[i] != ";":
                digit = digit + encryptalimsg[i]
                i += 1
            digit = int(digit) - key
            digit = int(digit) / key
            lolmsg = lolmsg + chars[int(digit)]
            i += 1
        print("your message has been decrypted: " + lolmsg)

#        Enjoy

