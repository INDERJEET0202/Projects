import random

def password_generator(length, special_chars, numbers):
    password_list = []
    for i in range(length):
        if i % 2 == 0:
            password_list.append(random.choice(special_chars))
        else:
            password_list.append(random.choice(numbers))
    password = ''.join(password_list)
    return password

l = 8
s = ['!', '@', '#', '$', '%', '^', '&', '*', '?']
n = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
new_password = password_generator(l, s, n)
print(new_password)