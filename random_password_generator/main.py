import random
import string

def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def main():
    length = int(input("Enter the password length : "))
    password = generate_password(length)
    print(password)

if __name__ == "__main__":
    main()
