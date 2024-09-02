# ord() to find the decimal value in ascii
# print(ord('A'))

# # chr() to find the character
# print(chr(65))

'''
# Exercise 1: Sum of ASCII Values
# Write a Python program that calculates the sum of the ASCII values of 

all characters in a given string.
# Example input: text = "hello"
# Expected output: 532
'''
# Solution for Exercise 1
# word = "hello"
# sum = 0
# for i in word:
#     totalOrd = ord(i)
#     sum = sum + totalOrd
# print(sum)

'''
# Exercise 2: Character from ASCII Value
# Write a Python program that takes an ASCII value as input and prints 
the corresponding character.
# Example input: ascii_value = 97
# Expected output: 'a'
'''
# choose_acsii = int(input("what is the Ascii number? "))
# alphabet = chr(choose_acsii)
# print(alphabet)



'''
# Exercise 3: Uppercase to Lowercase Conversion
# Write a Python program that converts an uppercase letter to its lowercase 
equivalent using ASCII values.
# Example input: letter = 'A'
# Expected output: 'a'
'''
# prompt = input("choose a letter in caps. ")
# num_char = ord(prompt)
# char_char = chr(num_char +32 )
# print(char_char)

'''
# Exercise 4: Lowercase to Uppercase Conversion
# Write a Python program that converts a lowercase letter to its 
uppercase equivalent using ASCII values.
# Example input: letter = 'b'
# Expected output: 'B'
'''
# prompt = input("choose a letter in lower caps. ")
# num_char = ord(prompt)
# char_char = chr(num_char - 32 )
# print(char_char)

'''
# Exercise 5: ASCII Value Difference
# Write a Python program that calculates the difference between the 
ASCII values of two characters.
# Example input: char1 = 'a', char2 = 'd'
# Expected output: 3
'''
prompt1 = input("choose a letter. ")
prompt2 = input("choose another letter. ")
prompt1_char = ord(prompt1)
prompt2_char = ord(prompt2)
diff_charint = prompt1_char - prompt2_char
print(abs(diff_charint))

'''
# Exercise 6: Alphabetical Sequence
# Write a Python program that prints the next 5 characters in the ASCII 
sequence from a given character.
# Example input: start_char = 'x'
# Expected output: 'y', 'z', '{', '|', '}'
'''
# choose = input("choose a random character. ")
# asciinum = ord(choose)
# print(asciinum)
# for i in range(1,6):
#     print(chr(asciinum + i))


'''
# Exercise 7: Sum of ASCII Values of Digits
# Write a Python program that calculates the sum of the ASCII values of all 
digit characters in a given string.
# Example input: text = "a1b2c3"
# Expected output: 150

to check if the character is a number >> .isdigit()
'''
# choose = input("choose random character(s). ")
# sum = 0
# for c in choose:
#     if c.isdigit():
#         decinum = ord(c)
#         sum = sum + decinum
# print(sum)

# sum = 0
# for i in choose:
#     # print(i)
#     decinum = ord(i)
#     # print(decinum)
#     sum = sum + decinum
# print(sum)



'''
# Exercise 8: Replace Characters with ASCII Sum
# Write a Python program that replaces each character in a string with the 
sum of its ASCII value and a given integer.
# Example input: text = "abc", increment = 1
# Expected output: 'b', 'c', 'd'
'''


'''
# Exercise 1: Generate a Simple Password
# Write a Python program that generates a random password of a given length 
    using ASCII printable characters.
# Example input: length = 8
# Expected output: A random password of 8 characters, e.g., 'aB3#xG2!'
# HINT: ASCII printable characters range from 33 to 126
'''
# import random
# len_pass = int(input("choose the amt of numbers you wan in your pw. "))
# pw = ""
# for i in range(len_pass):
#     ran_num = random.randint(33, 126)
#     ran_char = chr(ran_num)
#     pw = pw + ran_char
    # print(ran_char)

# print(pw)


'''
# Exercise 2: Generate a Password with Specific Character Types
# Write a Python program that generates a random password of a given length, 
ensuring it includes at least one uppercase letter, one lowercase letter, 
and one digit.
# Example input: length = 8
# Expected output: A random password of 8 characters, including at least 
one uppercase, one lowercase, and one digit, e.g., 'aB3xG2#1'
ASCII between 65 - 90     # Uppercase letter
ASCII between 97 - 122    # Lowercase letter
ASCII between 48 - 57     # Digit
'''
'''
import random
len_pass = int(input("choose the amt of numbers you wan in your pw. "))
pw = ""
for i in range(1):
    ran_num = random.randint(65,90)
    ran_char = chr(ran_num)
    pw = pw + ran_char
    print(ran_char)
print(pw)

for i in range (1):
    ran_num = random.randint(97,122)
    ran_char = chr(ran_num)
    pw = pw + ran_char
    print(ran_char)
print(pw)

for i in range(1):
    ran_num = random.randint(48,57)
    ran_char = chr(ran_num)
    pw = pw + ran_char
    print(ran_char)
print(pw)
    
for i in range(len_pass - 3):
    ran_num = random.randint(33,126)
    ran_char = chr(ran_num)
    pw = pw + ran_char
    print(ran_char)
print(pw)
'''

import random
len_pass = int(input("choose the amt of numbers you wan in your pw. "))
pw = ""
for i in range(len_pass):
    ran_num = random.randint(33,126)
    ran_char = chr(ran_num)
    pw = pw + ran_char
    print(ran_char)
pw_str = str(pw)
print(pw)
for i in range(len_pass):
    if i.isupper():
        break
for i in range(len_pass):
    if i.islower():
        break
print(pw)



# # while true for validation
# while True:
#     prompt = input("Enter a number: ")
#     if prompt.isdigit():
#         break # break out of the loop
#     else:
#         print("You must enter a number. ")
