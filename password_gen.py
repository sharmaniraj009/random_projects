import random
import string

special_chars = ['!','@','#','$','%','^','&','*','/']

letters = string.ascii_letters
special = random.choice(special_chars)
integers = str(random.randint(0,9))

pwd = letters + special + integers

final = ""
for i in range(12):
    final += random.choice(pwd)

print(final + random.choice(special_chars))