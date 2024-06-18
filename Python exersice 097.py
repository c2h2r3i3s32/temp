import random

def generate_random_password():
    length = random.randint(7, 10)
    password = ''.join(chr(random.randint(33, 126)) for _ in range(length))
    return password

def is_good_password(password):
    if len(password) < 8:
        return False

    has_upper = any(char.isupper() for char in password)
    has_lower = any(char.islower() for char in password)
    has_digit = any(char.isdigit() for char in password)

    return has_upper and has_lower and has_digit

if __name__ == "__main__":
    random_password = generate_random_password()
    password = random_password 
    print(f"Randomly generated password: {random_password}")
    
    if is_good_password(password):
        print("The password is good.")
    else:
        print("The password is not good.")




