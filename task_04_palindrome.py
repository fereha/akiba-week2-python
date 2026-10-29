# Palindrome checker
word = input("Enter a word: ")
word = word.lower()
reversed_word = word[::-1]
if word == reversed_word:
    print("Yes, it is a palindrome.")
else:
    print("No, it is not a palindrome.")