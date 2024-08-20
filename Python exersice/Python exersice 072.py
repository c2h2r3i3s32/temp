word = input()

start, end = 0, len(word) - 1
palindrome = True

while start < end:
    if word[start] != word[end]:
        palindrome = False
        break
    start += 1
    end -= 1

if palindrome:
    print(word, "is a palindrome.")
else:
    print(word, "is not a palindrome.")

        



