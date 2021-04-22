import random
print("CyFy")
password_length = int(input("enter the length of password"))
s = "abcdefghijklmnopqrstuvwxyz01234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()?"
p = "".join(random.sample(s, password_length))
print(p)
