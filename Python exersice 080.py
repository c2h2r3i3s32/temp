import random

total_flips = 0
time = 10

for _ in range(time):
    flips = 0
    consecutive = 0
    last_flip = ''
    outcomes = ''
    
    while consecutive < 3:
        if random.randint(0, 1) == 0:
            flip = 'H'
        else:
            flip = 'T'
        outcomes += flip
        flips += 1
        
        if flip == last_flip:
            consecutive += 1
        else:
            consecutive = 1
        last_flip = flip      
    
    print(outcomes)
    total_flips += flips
    print("flips", flips)

average_flips = total_flips / time
print('Average number of flips is', average_flips)