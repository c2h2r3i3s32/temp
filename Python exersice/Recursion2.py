def consonants(s):
    vowels = "aeiou"
    consonant_count = 0
    
    for char in example:
        if char.isalpha() and char not in vowels:
            consonant_count += 1   
    return consonant_count

example = "abc de"
print("Total consonants:", consonants(example))
