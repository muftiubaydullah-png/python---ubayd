# str = "Haalllo"

# print(len(str))
# print(str[::-1])  # Output: 'olleH'
# print(str[0])
# print(str[-1])
# print(str.count("l"))

# text =str(input("enter a word:"))
# if (text[::-1])==text:
#     print("palindrom")
# else:
#     print("not a palindrom")
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