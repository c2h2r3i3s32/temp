import random

def generate():
    letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    number = '0123456789'
    
    if random.choice([True, False]):
        plate = ''.join(random.choices(letters, k = 3)) + ''.join(random.choices(number, k = 3))
    else:
        plate= ''.join(random.choices(number, k=4)) + ''.join(random.choices(letters, k= 3))
    
    return plate

random_plate = generate()
print(f"Randomly generated license plate: {random_plate}")
