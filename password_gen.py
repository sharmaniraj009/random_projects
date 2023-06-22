import random
import string

special_chars = ['!','@','#','$','%','^','&','*','/']

letters = string.ascii_letters
special = random.choice(special_chars)
integers = str(random.randint(0,9))

pwd = letters + special + integers

length = int(input("enter the length of the required password : "))

final = ""
for i in range(length):
    final += random.choice(pwd)

print(final + random.choice(special_chars))