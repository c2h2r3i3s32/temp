import random

def createDeck():
    suits = ['s', 'h', 'd', 'c']
    values = ['2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K', 'A']
    deck = [value + suit for suit in suits for value in values]
    return deck

def shuffle(deck):
    for i in range(len(deck)):
        swap_index = random.randint(0, len(deck) - 1)
        deck[i], deck[swap_index] = deck[swap_index], deck[i]

def main():
    deck = createDeck()
    print("Original deck:")
    print(deck)
    
    shuffle(deck)
    print("\nShuffled deck:")
    print(deck)

main()
