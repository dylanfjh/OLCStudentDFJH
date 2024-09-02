import random

'''
# Exercise 1: Boolean Assignment
# Assign a boolean value to a variable and print it.
# Example input: is_student = True
# Expected output: True
'''
# Write your code here
# is_student = True
# print(is_student)

'''
# Exercise 2: Simple if Statement
# Use an if statement to check if a number is positive.
# Example input: number = 5
# Expected output: 'The number is positive.'
'''
# Write your code here
# num = int(input("what is the number that you choose? "))
# if num >= 0:
#     print("the number is positive")
# else: 
#    print("the number is not positive") 
    

'''
# Exercise 3: if-else Statement
# Use an if-else statement to check if a number is positive or negative.
# Example input: number = -3
# Expected output: 'The number is negative.'
'''
# Write your code here
# num = int(input("what is the number that you choose? "))
# if num >= 0:
#     print("the number is positive")
# else: 
#    print("the number is not positive") 

'''
# Exercise 4: if-elif-else Statement
# Use an if-elif-else statement to check if a number is 
# positive, negative, or zero.
# Example input: number = 0
# Expected output: 'The number is zero.'
'''
# Write your code here
# num = int(input("what is the number that you choose? "))
# if num >= 0:
#     print("the number is positive")
# elif num == 0:
#     print("the number is zero")
# else: 
#    print("the number is not positive") 

'''
# Exercise 5: Boolean Comparison
# Assign values to two variables and use a boolean comparison to 
# check if they are equal.
# Example input: a = 10, b = 10
# Expected output: 'a and b are equal.'
'''
# Write your code here
# a = int(input("what is a number that you choose? "))
# b = int(input("what is a number that you choose? "))

# if a == b:
#     print("your both number are equal!" )
# else:
#     print("both your numbers are not equal!" )

'''
# Exercise 6: Check Even or Odd
# Use an if-else statement to check if a number is even or odd.
# Example input: number = 4
# Expected output: 'The number is even.'
# hint: use the mod %, any number divisible by 2 is even
'''
# Write your code here
# a = int(input("what is a number that you choose? "))
# if a % 2 == 0:
#     print("the number is even")
# else:
#     print("the number is odd")

'''
# Exercise 7: Age Group Classification
# Use if-elif-else statements to classify a person into age groups.
 < 13 = child
 < 20 = teenager
# Example input: age = 25
# Expected output: 'You are an adult.'
'''
# Write your code here


'''
# Exercise 8: Temperature Check
# Use if-elif-else statements to check if a temperature 
# is cold, warm, or hot.
# use your own values to determine what is cold, warm or hot.
# Example input: temperature = 30
# Expected output: 'It is warm.'
'''
# Write your code here


'''
# Exercise 9: Validating Age Input
# Use if-else statements to validate if the entered 
# age is a positive number.
# Example input: age = -5
# Expected output: 'Invalid age.'
'''
# Write your code here
# age = input("what is your age? ")
# if age < 0:
#     print("Invalid age. ")
# else:
#     print("thank you! ")

'''
# Exercise 10: Greeting Based on Time
# Use if-elif-else statements to print a greeting based 
# on the time of the day.
# Good morning, Good afternoon, Good evening, Good night
# assume time is based on 24 hour clock, i.e 13 is 1.00pm
# Example input: time = 15
# Expected output: 'Good afternoon.'
'''
# Write your code here
t = int(input("what is the time now? "))
if t > 21 and t <=24:
    pass
elif t > 19:
    pass

if t < 0:
elif t < 

'''
# Exercise 11: Grade Evaluation
# Use if-elif-else statements to evaluate a grade.
>= 90 = A*
>= 80 = A
>= 70 = B
>= 60 = C
anything lesser is a D
# Example input: grade = 85
# Expected output: 'You got an A.'
'''
# Write your code here


'''
# Exercise 12: Boolean Logic
# Assign boolean values to two variables and print the 
# result of their logical AND.
# Example input: is_sunny = True, has_umbrella = False
# Expected output: False
'''
# Write your code here
#HOW TO DO - WHAT IS THE QN ASKING
# is_sunny = True
# has_umbrella = False
# print(is_sunny and not has_umbrella)
### != 

'''
# Exercise 13: Voting Eligibility
# Use if-else statements to check if a person is eligible to vote.
# Example input: age = 17
# Expected output: 'You are not eligible to vote.'
'''
# Write your code here
# age = input("what is your age? ")
# if age < 17:
#     print("not allowed to vote. ")
# else:
#     print("please vote. ")

'''
# Exercise 15: Password Validation
# Use if-else statements to check if a password meets a 
# minimum length requirement (8)
# Example input: password = 'abc123'
# Expected output: 'Password is too short.'
'''
# Write your code here
# HOW TO DO
pw = "dkjfhsdkjfh"
passme = input("type in your password: ")
len(passme)
if len(pw) < 11:
    print("Password is too short!" )
else:
    print("Password is too long!" )

