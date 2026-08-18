str = input("Enter a string: ")

vowel = 0
consonant = 0
for ch in str:
    if ch in "aeiouAEIOU":
        vowel += 1
    elif ch.isalpha():
        consonant += 1
print("Number of vowels:", vowel)
print("Number of consonant:", consonant)