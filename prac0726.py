#### SIMPLE ADDITION PROGRAM
# ask for 2 numbers using input
# add up and print out the answer

# num1 = input("what is the number 1? ")
# num2 = input("what is the number 2? ")
# add = int(num1) + int(num2)
# # print(add)

# # 100 + 200 = 300
# # print(num1 + " + " + num2 + " = " + str(add))
# print( num1, "+", num2, "=", add) ##easier way to do it

# #print 10 hello
# for i in range(10):
#     print("hello")

# # print number 0 - 10
# for i in range(11):
#     print (i)

# for i in range (3):
#     print("a")
#     for i in range(3):
#         print("c")
#     print(" ")


# option 2: range(start, stop) ## 21 - 30
# for i in range(21, 31):
#     print(i)

##### 46 - 98
# for i in range(46, 99):
#     print(i)

# # option 3 - range(start, stop, step) 
# for i in range(3, 37, 3):
#     print(i)

# # print multiples of 7 from 7 to 84
# for i in range(7,85,7):
#     print(i)



'''
# Question 1: Print numbers from 0 to a given number (exclusive)
# Test case 1: example input: 5, example output: 0 1 2 3 4
# Test case 2: example input: 3, example output: 0 1 2
'''
## Write and test your code here
# num = int(input("choose a number that is more than 0? "))
# for i in range(0, num):
#     print(i)
        

# '''
# # Question 2: Print numbers from a given start number 
# # to a given stop number (exclusive)
# # Test case 1: example input: 3 8, example output: 3 4 5 6 7
# # Test case 2: example input: 1 5, example output: 1 2 3 4
# '''
# ## Write and test your code here
# num1 = int(input("choose a number that is more than 0? "))
# num2 = int(input("choose another number that is more than the first number? "))
# for i in range(num1, num2):
#     print(i)

'''
# Question 3: Print even numbers from 0 to a given number (exclusive)
# Test case 1: example input: 10, example output: 0 2 4 6 8
# Test case 2: example input: 7, example output: 0 2 4 6
'''
# Write and test your code here
# num = int(input("choose a number that is more than 0? "))
# for i in range(0, num, 2):
#     print(i)

'''
# Question 4: Print numbers from a given start number 
# to a given stop number (exclusive) with a given step
# Test case 1: example input: 2 10 2, example output: 2 4 6 8
# Test case 2: example input: 1 10 3, example output: 1 4 7
'''
## Write and test your code here
# num1 = int(input("choose a number that is more than 0? "))
# num2 = int(input("choose another number that is more than the first number? "))
# jump = int(input("choose how much the number will jump by. "
# for i in range(num1, num2, jump):
#     print(i)

'''
# Question 5: Print the squares of numbers from 
# 0 to a given number (exclusive)
# Test case 1: example input: 5, example output: 0 1 4 9 16
# Test case 2: example input: 3, example output: 0 1 4
'''
## Write and test your code here
# num1 = int(input("choose a number that is more than 0? "))
# for i in range(0, num1 +1):
#     print(int(i)**2)

'''
# Question 6: Print the cubes of numbers from a 
# given start number to a given stop number (exclusive)
# Test case 1: example input: 1 5, example output: 1 8 27 64
# Test case 2: example input: 2 6, example output: 8 27 64 125
'''
## Write and test your code here
# num1 = int(input("choose a number that is more than 0? "))
# num2 = int(input("choose another number that is more than the first number? "))
# for i in range(num1, num2 +1):
#     print(int(i)**3)



'''
# Question 7: Print numbers in reverse from 
# a given start number to 0 (inclusive)
# Test case 1: example input: 5, example output: 5 4 3 2 1 0
# Test case 2: example input: 3, example output: 3 2 1 0
'''
## Write and test your code here


'''
# Question 8: Print the even numbers from a 
# given start number to a given stop number (exclusive)
# Test case 1: example input: 2 10, example output: 2 4 6 8
# Test case 2: example input: 1 7, example output: 2 4 6
'''
## Write and test your code here


'''
# Question 9: Print the odd numbers 
# from 0 to a given number (exclusive)
# Test case 1: example input: 10, example output: 1 3 5 7 9
# Test case 2: example input: 7, example output: 1 3 5
'''
## Write and test your code here


'''
# Question 10: Print the multiplication table 
# of a given number up to 10
# Test case 1: example input: 5, 
example output: 5 10 15 20 25 30 35 40 45 50

# Test case 2: example input: 3, 
example output: 3 6 9 12 15 18 21 24 27 30
'''
## Write and test your code here


'''
# Question 11: Print the first n numbers of the Fibonacci sequence
# Test case 1: example input: 5, example output: 0 1 1 2 3
# Test case 2: example input: 7, example output: 0 1 1 2 3 5 8
'''
## Write and test your code here


'''
Q2
You are given a list of computing paper 1 marks and paper 2 marks

paper1 = {"Ken": 80, "Mike": 84, "Ash": 55, "Zee": 65}
paper2 = {"Ken": 88, "Mike": 64, "Ash": 65, "Zee": 85}

Design a program to

1.  update Ken's mathematics mark to 83
2.  show the average of paper 1 marks and average of paper 2 marks
3.  ask user to enter a person and the paper he wants to search. 
If the person is in the list, show the respective mark.
Otherwise shows that the person cannot be found

Open the file computing.py and work on the program.  
Save your file as computing_yourname_class.py.
'''

# VARIABLE TYPE
# 

paper1 = {"Ken": 80, 
          "Mike": 84, 
          "Ash": 55, 
          "Zee": 65}

### TO CHANGE THE VALUE OF A KEY IN THE DICTIONARY
#print(paper1["Ken"]) # TO RETRUEVE A VALUE
paper1["Ken"] = 83 # 
# paper1["Mike"] = 83 # 
# paper1["Ash"] = 83 # 
# paper1["Zee"] = 83 # 
#print(paper1)


scores = [80,84,55,65] # BASED ON THE INDEX
scores[0] = 83 ## CHANGE IN A LIST


paper2 = {"Ken": 88, 
          "Mike": 64, 
          "Ash": 65, 
          "Zee": 85}

paper2["Ken"] = 83 


#############
# 2.  show the average of paper 1 marks and average of paper 2 marks
# loop through all the keys in dictionary
sum = 0
count = 0
for student in paper1:
    print(student) # printing out the key 
    #print(paper1[student]) # print out the value
    score = paper1[student]
    sum = sum + score
    count = count + 1

print(sum/ count)



#3.  ask user to enter a person and the paper he wants to search. 
name = input("Search for who? ")
papernum = input("What Paper? ")

if papernum == "1":
    # pass
    if name in paper1: # checks for existence of this value in dictionary
        score = paper1[name]
        print("{}'s score is {}".format(name, score))
    else:
        print("{} does not exist.".format(name))
    # search paper1 dictionary
elif papernum == "2":
    pass
    # search paper2 dictionary
else:
    print ("Invalid paper")

