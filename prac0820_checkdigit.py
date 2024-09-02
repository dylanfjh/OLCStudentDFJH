# name = "123,Mary,98989922,1 Toa Payoh Central" # CSV
# name2 = "Mary Ong"
# name3 = "Ethan Chong"

# # .split() # splits a string to a list based on a separator
# tempname = name.split(",") ##separator value.
# print(tempname)
# # fname = tempname[0]
# # lname = tempname[1]
# # print(fname)
# # print(lname)

'''
Challenge 7:
A developer needs to extract specific characters from a 
given string to generate a user ID.

(a) Write a function generate_user_id(name, birthdate) 
    that takes a user's full name as a single string in the 
    format "First Last" and a birthdate in the format "YYYYMMDD". 
    The function should return a user ID consisting of:

    - The first three letters of the last name (in uppercase),
    - The last two digits of the year of birth,
    - The first letter of the first name (in lowercase).
For example:
generate_user_id("John Doe", "19901225") should return DOE90j.
[6 marks]
'''
# name1 = input("what is your name? ")
# date1 = input("when is your birthday? ")
# def generate_user_id(name, birthdate):
#     if len(birthdate) != 8:
#         print("input your birthday agn. ")
#         return False
#     name2 = name.split(" ")
#     # print(name2)
#     lname = name2[1]
#     fname = name2[0]
#     # print(lname)
#     # print(fname)
#     date2 = birthdate[2:4]
#     # print(date2)
#     fletter = fname[0].lower()
#     # print(fletter)
#     lcapsletter = lname[:3].upper()
#     # print(lcapsletter)
#     id =  lcapsletter + date2 + fletter
#     # print(id)
#     return id
# print(generate_user_id(name1, date1))

'''
(b) Write a main program that:

    - Takes as input a full name and birthdate,
    - Calls the generate_user_id() function,
    - Outputs the generated user ID.
Test cases:

generate_user_id("Alice Tan", "20030515") should return TAN03a.
generate_user_id("Michael Johnson", "19850911") should return JOH85m.
[4 marks]
'''

############################### Check Digit ######################
'''
Challenge 6:
A programmer is writing a program to calculate the 
check digit for a 12-digit integer.

The check digit is calculated by multiplying the digits 
in odd positions by 3 and the digits in even positions by 1. 
These values are added together to produce a total. 
The total is subtracted from the next multiple of 10 to 
give a final value. If the final value is 10, the check digit is X.

Example: 
12-digit integer = 1  0  3  4  5  6  2  7  1  0  1  3
Result           = 3  0  9  4  15 6  6  7  3  0  3  3
Total = 3 + 0 + 9 + 4 + 15 + 6 + 6 +7 + 3 + 0 + 3 + 3 = 59
The next multiple of 10 is 60 (*hint: nextnum = math.ceil(num/10) * 10)
So, check digit = 60 - 59 = 1

(a) The The program code function calculate() takes a 
    12-digit number as a parameter. It calculates the 
    check digit and returns the check digit.

    Write the code for the function calculate [6]
'''

import math
twelnums = (input("gimme 12 numbers. "))
def calculate(digit123):
    ## jump num and multiply [:::]
    sumodd = 0
    sumeven = 0
    for i in range(12):
        if i % 2 ==0:
            # print(f"this is slot number {i} the number is {digit123[i]}")
            tempeven = int(digit123[i]) * 3
            # print(tempeven)
            sumeven = sumeven + int(tempeven)
            # print(sumeven)
        else:
            # print(f"this is slot number {i} the number is {digit123[i]}")
            sumodd = sumodd + int(digit123[i]) 
            # print(sumodd)

    totalsum = sumodd + sumeven
    # print(totalsum)
    nextnum = math.ceil(totalsum/10) * 10
    chkdig = nextnum - totalsum
    return chkdig

print(calculate(twelnums))
      
'''
(b) The main program:
•	Takes as input a 12-digit number until a valid 
    12-digit integer is entered
•	Calls the function calculate() with the valid input 
    as a parameter
•	Outputs the number with the check digit as its 13th digit

Write the code for the main program. [5]

Test that:
103456271013 = 1
123456789012 = 0
135792468013 = 5
'''
## use the calculate() functiion 
## make True = whole number
## false = cannot return a whole number
tweldigi = input("what are your 12 numbers? ")
print(calculate(tweldigi))
print(f"{tweldigi} = {calculate(tweldigi)}")

    

