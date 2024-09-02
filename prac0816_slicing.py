# # ### List Slicing or String Slicing
# # listnums = [1,2,3,4,5,6,7,8,9]

# # var1 = listnums[-1]
# # print(var1)

# # # [start: stop]
# # var2 = listnums[0:3]
# # print(var2)

# # var3 = listnums[1:4]
# # print(var3)

# # # [start: stop: step]
# # var4 = listnums[1::2]
# # print(var4)

# # word = "SINGAPORE"
# # var5 = word[:3]
# # print(var5)

# # var6 = word[3:6]
# # print(var6)

# # var7 = word[::2]
# # print(var7)

# # var8 = word[::-1]
# # print(var8)

# # temp = ""
# # for i in word:
# #     temp = i + temp
# # print(temp)


# # String and List Operators
# # Using + to Concatenate
# # List Slicing
# '''
# Question 1: Extract a portion of a list.
# Write a function that takes a list and returns a new list 
# that contains only the first three elements of the original list.
# Example Input: [1, 2, 3, 4, 5]
# Example Output: [1, 2, 3]
# '''
# ## Write and test your code here
# list1 = [34,54,564,563,534,467,345,457,5675,67,1,2,3,4,5]

# def outputlist(inlist):
#     var1 = inlist[0:3]
#     return var1
    
# answer = outputlist(list1)
# print(answer)

# '''
# Question 2: Get the last three items of a list.
# Ask the user for a list of numbers and print the last three items.
# Example Input: [10, 20, 30, 40, 50]
# Example Output: [30, 40, 50]
# '''
# ## Write and test your code here
# list2 = [10,20,30,40,50,435,436,234,235,345,47,5675,6756,756]

# def outlist(inlist):
#     var2 = inlist[-3:]
#     return var2

# print(outlist(list2))

# '''
# Question 3: Create a sub-list from a list using slicing.
# Given a list of elements, write a function that returns a 
# sublist from the second element to the second last element.
# Example Input: [0, 1, 2, 3, 4, 5]
# Example Output: [1, 2, 3, 4]
# '''
# ## Write and test your code here
# list3 = [0, 1, 2, 3, 4, 5]

# def outlist(inlist):
#     var3 = inlist[1:-1]
#     return var3

# print(outlist(list3))

# '''
# Question 4: Reverse a list using slicing.
# Write a function that takes a list and returns it reversed.
# Example Input: [1, 2, 3, 4, 5]
# Example Output: [5, 4, 3, 2, 1]
# '''
# ## Write and test your code here
# list4 = [1, 2, 3, 4, 5]

# def outlist(inlist):
#     var4 = inlist[::-1]
#     return var4

# print(outlist(list4))

# '''
# Question 5: Slice a list into halves.
# Divide a list into two equal halves and returns both halves.
# You may assume that the list has an even number of items
# Example Input: [1, 2, 3, 4, 5, 6]
# Example Output: [1, 2, 3]  [4, 5, 6]
# '''
# ## Write and test your code here
# list5 = [1, 2, 3, 4, 5, 6,7,8,9,10]
# print(int(len(list5) / 2))# 6

# def outlist(inlist):
#     var5 = inlist[0 : int(len(list5) /2)]
#     var6 = inlist[int(len(list5) /2) : ]
#     return var5, var6

# out1, out2 = outlist(list5)
# print(out1)
# print(out2)

# '''
# Question 6: Extract every second element from a list.
# Write a function that returns a list of every second element from the given list.
# Example Input: ['a', 'b', 'c', 'd', 'e', 'f']
# Example Output: ['b', 'd', 'f']
# '''
# ## Write and test your code here
# list6 = ['a', 'b', 'c', 'd', 'e', 'f']

# def outlist(inlist):
#     var7 = inlist[1::2]
#     return var7

# print(outlist(list6))

# '''
# Question 7: Remove the first and last elements of a list using slicing.
# Create a function that takes a list and returns it without 
# the first and last elements.
# Example Input: [0, 1, 2, 3, 4]
# Example Output: [1, 2, 3]
# '''
# ## Write and test your code here
# list7 = [0, 1, 2, 3, 4]

# def outlist(inlist):
#     var8 = inlist[1:-1]
#     return var8

# print(outlist(list7))

# '''
# Question 8: Create a function to reverse the order of elements in a 
# list only from the second to the last but one.
# Example Input: [1, 2, 3, 4, 5, 6]
# Example Output: [1, 5, 4, 3, 2, 6]
# '''
# ## Write and test your code here
# list8 = [1, 2, 3, 4, 5, 6]

# def outlist(inlist):
#     var9 = inlist[1:-1]
#     var10 = var9[::-1]
#     print(var10)
#     return var10

# print([list8[0]] + outlist(list8) + [list8[-1]]) ## add [] to make it a list

# '''
# # Question 9: Extract the first three characters from a string
# # Test case 1: example input: hello, example output: hel
# # Test case 2: example input: Python, example output: Pyt
# '''
# ## Write and test your code here
# word9 = "hello"
# var11 = word9[:3]
# print(var11)

# word9a = "Python"
# var12 = word9a[:3]
# print(var12)

# '''
# # Question 10: Extract the last three characters from a string
# # Test case 1: example input: hello, example output: llo
# # Test case 2: example input: Python, example output: hon
# '''
# ## Write and test your code here


# '''
# # Question 11: Extract a subset of a list from index 2 to 5
# # Test case 1: example input: 1 2 3 4 5 6 7, 
# example output: [3, 4, 5, 6]
# # Test case 2: example input: 10 20 30 40 50 60, 
# example output: [30, 40, 50]
# '''
# ## Write and test your code here


# '''
# # Question 12: Extract every second character from a string
# # Test case 1: example input: hello, example output: hlo
# # Test case 2: example input: Python, example output: Pto
# '''
# ## Write and test your code here


# '''
# # Question 13: Extract the middle three characters from a string
# # You may assume the number of characters is odd
# # Test case 1: example input: abcdefg, example output: cde
# # Test case 2: example input: helloworld, example output: low
# '''
# ## Write and test your code here
# word13 = input("word? ")
# lenword = len(word13)
# middlelet = lenword//2

# def outlist(inlist):
#     var13 = inlist[middlelet - 1 : middlelet + 2]
#     return var13

# print(outlist(word13))

# '''
# # Question 14: Extract the first half of a string
# # Test case 1: example input: hello, example output: hel
# # Test case 2: example input: Python, example output: Pyt
# '''
# ## Write and test your code here
# word14 = input("word? ")
# lenword = len(word14)
# middlelet = lenword//2

# def outlist(inlist):
#     var14 = inlist[:middlelet]
#     return var14

# print(outlist(word14))

# '''
# # Question 15: Extract the second half of a string
# # Test case 1: example input: hello, example output: llo
# # Test case 2: example input: Python, example output: hon
# '''
# ## Write and test your code here

# '''
# Question 16:
# Write a function to split a string into half
# and return the first half
# Your function must handle an odd or even number length of characters
# # If the length is odd, you will ignore the middle character
# Example Input: "SINGING" Example Output: SIN
# Example Input: "FLYING" Example Output: FLY
# '''
# word16 = input("word? ")
# lenword = len(word16)
# middlelet = lenword//2

# if lenword % 2 == 0:
#     var16 = word16[:middlelet]  
#     print(var16)
# else:
#     var16a = word16[:middlelet]
#     print(var16a)
    
# '''
# # Challenge 1:
# Write a function `validate_nric(nric) -> bool` to 
# validate if a given input is a valid Singapore NRIC number. 
# A valid NRIC must start with 'S', 'T', 'F', or 'G', followed by 7 digits, 
# and ends with an uppercase letter.

# * In this case, assume that as long as the last character 
# is an uppercase letter it is valid.

# Normal Test: Input: "S1234567D", Output: True
# Error Test: Input: "A1234567D", Output: False
# Boundary Test: Input: "S123456", Output: False
# '''
# nric1 = input("nric? ")

# '''
# .isdigit() checks for number
# "123".isdigit() -->> return True

# .isalpha() checks for alphabets

# .isupper() # check for upper case
# .islower() # check for lower case

# if "S" in "STFG" .. return true
# if "Z" in "STFG" .. return false
# '''
# ## nric = S1234567F

# def validate_nric(nric):
#     # bool1 = False
#     # flagdigit = False
#     # flaglastalpha = False

#     # if nric[0].isalpha() and nric[0] in "STFG":
#     #     flag1 = True
#     # if nric[-1].isalpha():
#     #     flaglastalpha = True
#     # if flag1 and flaglastalpha and flagdigit
    
#     if not nric[0].isalpha() and nric[0] not in "STFG":
#         return False
#     elif not nric[-1].isalpha():
#         return False
#     elif not nric[1:-1].isdigit() and len(nric[1:-1]) != 9:
#         return False
#     else:
#         return True

# print(validate_nric(nric1))

'''
# Challenge 2:
Write a function `is_valid_username(username: str) -> bool` to 
check if a username is correctly generated. A valid username 
should be at least 6 characters long, should not contain any spaces, 
and must start with an uppercase letter followed by lowercase letters.

Normal Test: Input: "Johndoe", Output: True
Error Test: Input: "johnDoe", Output: False
Boundary Test: Input: "John", Output: False
'''
##the number of letters for the name has to be longer than or equal to 6
##only have one possibility for his name
##Uppercase then lowercase (.isupper() and .islower())

user_n = input("username? ")
def is_valid_username(username):
    if not len(username) >= 6: 
    ##why i put dyl also can?
        return False
    elif not username[0].isupper():
        return False
    elif not username[1:].islower():
        return False
    ##how to do for spacing?
    else:
        return True

print(is_valid_username(user_n))

'''
# Challenge 3:
Write a function `validate_license_plate(plate: str) -> bool` 
to check if a vehicle license plate is valid. 
A valid plate starts with 3 uppercase letters, followed by 4 digits, 
and ends with an uppercase letter.

Normal Test: Input: "SAB1234Z", Output: True
Error Test: Input: "SA1234Z", Output: False
Boundary Test: Input: "SAB123Z", Output: False
'''
carplate = input("what is your license plate?" )

def validate_license_plate(plate):
    if not plate[0:3].isupper() and not plate[-1].isupper():
        return False
    elif not plate[3:-1].isdigit():
        return False
    elif not plate[0:3].isalpha() and not plate[-1].isalpha():
        return False
    elif not len(plate) == 8:
        return False
    else:
        return True

print(validate_license_plate(carplate))

'''
# Challenge 4:
Write a function `is_valid_postal_code(postal_code: str) -> bool` 
to validate a Singaporean postal code. A valid postal code consists 
of exactly 6 digits where the first digit must be between 1 and 7.

Normal Test: Input: "123456", Output: True
Error Test: Input: "823456", Output: False
Boundary Test: Input: "12345", Output: False
'''

'''
# Challenge 5:
Write a function `validate_date_format(date_str: str) -> bool` 
to check if a date string is in the format "DD/MM/YYYY" 
where DD, MM, and YYYY are valid digits. 

The function should ensure that DD is between 01 and 31, 
MM is between 01 and 12, and YYYY is a valid 4-digit positive integer.

Normal Test: Input: "29/02/2020", Output: True
Error Test: Input: "32/13/2020", Output: False
Boundary Test: Input: "01/01/0001", Output: True
'''