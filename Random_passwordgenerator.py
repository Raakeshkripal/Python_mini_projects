import string 
import random
character = list(string.ascii_letters+string.digits+"!@#$%^&*()")
def generate_password():
    length=int(input("enter the length:"))
    random.shuffle(character)
    password = []
    for i in range(length):
        password.append(random.choice(character))
    random.shuffle(password)
    print("".join(password))
generate_password()
