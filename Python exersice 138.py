import random

def create_bingo_card():
    ranges = {
        'B': range(1, 16),
        'I': range(16, 31),
        'N': range(31, 46),
        'G': range(46, 61),
        'O': range(61, 76)
    }
    
    bingo_card = {}
    for letter, number_range in ranges.items():
        bingo_card[letter] = random.sample(number_range, 5)

    return bingo_card

def display_bingo_card(bingo_card):
    print(" B  |  I  |  N  |  G  |  O ")
    
    for i in range(5):
        for letter in 'BINGO':
            value = bingo_card[letter][i]
            print(f"{value} |", end=" ")
        print()  

bingo_card = create_bingo_card()
display_bingo_card(bingo_card)


