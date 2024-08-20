note = {261.63: 'C4', 293.66: 'D4', 329.63: 'E4', 349.23: 'F4', 392.00: 'G4', 440.00: 'A4', 493.88: 'B4'}
frequency = int(input("Enter a frequency: "))
closest_key = min(note, key=lambda x: abs(x - frequency))
closest_note = note[closest_key]
print(closest_note)
   