word = input("Is this word a palindrome?:")
reversed_word = word[::-1].lower()
if word.lower() == reversed_word:
    print(word + " is a palindrome")
else:
    print(word + " is not a palindrome")