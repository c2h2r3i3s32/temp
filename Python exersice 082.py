base = 4.00
cost = 0.25
kilometer = 1000
meter = 140

def taxi_fare(distance):
    distance_meters = distance * kilometer
    intervals = distance_meters // meter
    total_fare = base + intervals * cost

    return total_fare

distance = int(input("Enter the distance traveled in kilometers: "))
fare = taxi_fare(distance)
print("The total fare for", distance, "kilometers is", fare)