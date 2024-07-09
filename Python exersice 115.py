def translate(word):
    vowels = "aeiou"
    if word[0] in vowels:
        return word + "way"
    else:
        for i in range(len(word)):
            if word[i] in vowels:
                return word[i:] + word[:i] + "ay"
        return word + "ay"  

def main():
    text = input("Enter a line of text: ")
    words = text.split()
    
    pig_latin_words = [translate(word) for word in words]
    
    pig_latin_text = ' '.join(pig_latin_words)
    print("Pig Latin translation:", pig_latin_text)

main()




