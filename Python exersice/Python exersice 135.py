def are_anagrams(word1, word2):
    word1 = word1.replace(" ", "")
    word2 = word2.replace(" ", "")
    
    return sorted(word1) == sorted(word2)

word1 = input("Enter the first word: ").strip()
word2 = input("Enter the second word: ").strip()
    
if are_anagrams(word1, word2):
    print(f'"{word1}" and "{word2}" are anagrams.')
else:
    print(f'"{word1}" and "{word2}" are not anagrams.')


