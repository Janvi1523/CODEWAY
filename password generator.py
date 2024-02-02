'''import string
import random

#characters that can be used in the password
all_characters = string.ascii_letters + string.digits + string.punctuation

#ask user for length of the password
length = int(input("Enter the length of the password: "))

# generate password
pwd = ''.join(random.choices(all_characters, k=length))

# display the generated password to the user
print("Your password is:", pwd)'''


import string
import random

#characters that can be used in the password
all_characters = string.ascii_letters + string.digits + string.punctuation

#ask user for length of the password
length = int(input("Enter the length of the password: "))

# generate password
pwd = ''.join(random.choices(all_characters, k=length))

# display the generated password to the user
print("Your password is:", pwd)

