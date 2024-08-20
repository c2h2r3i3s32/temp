import random

def roll_dice():
    die1 = random.randint(1, 6)
    die2 = random.randint(1, 6)
    return die1 + die2

def main():
    num_rolls = 1000

    frequency = {total: 0 for total in range(2, 13)}

    for _ in range(num_rolls):
        total = roll_dice()
        frequency[total] += 1

    print(f"{'Total':>5} {'Count':>10} {'Frequency (%)':>15} {'Expected (%)':>15}")
    for total in range(2, 13):
        observed_frequency = frequency[total] / num_rolls * 100
        expected_frequency = probability_theory(total) * 100
        print(f"{total:>5} {frequency[total]:>10} {observed_frequency:>15.2f} {expected_frequency:>15.2f}")

def probability_theory(total):
    if total < 2 or total > 12:
        return 0
    probabilities = {
        2: 1/36,
        3: 2/36,
        4: 3/36,
        5: 4/36,
        6: 5/36,
        7: 6/36,
        8: 5/36,
        9: 4/36,
        10: 3/36,
        11: 2/36,
        12: 1/36
    }
    return probabilities[total]

main()
