# '''
# Recap 1

# list1 = [2944, 5490, 2357, 2619, 1177, 451, 8299, 2533, 4682, 6040,
#          5972, 7532, 4382, 8311, 6664, 4918, 3656, 3769, 6179, 7720,
#          1777, 7149, 2175, 8665, 4586, 5208, 320, 1314, 8950, 4884
#          ]

# ## Question: Find the maximum & minimum number in this list
# ''' 
# list1 = [2944, 5490, 2357, 2619, 1177, 451, 8299, 2533, 4682, 6040,
#          5972, 7532, 4382, 8311, 6664, 4918, 3656, 3769, 6179, 7720,
#          1777, 7149, 2175, 8665, 4586, 5208, 320, 1314, 8950, 4884
#          ]
# ##max number
# max = 0
# for i in list1:
#     if i > max:
#         max = i
# print(max)

# min = list1[0]
# for i in list1:
#     if i < min:
#         min = i
# print(min)


###############################################################
##### DEBUGGING TECHNIQUES #####################################
'''
Mock Task 3 Question 1
A library program needs to keep track of books being borrowed and returned. 
Each book has a unique ID and a title. The program allows a user to 
input the book ID and whether the book is being borrowed or returned. 
The program updates the status of the book accordingly and displays a message. 
There are several syntax and logic errors in the program.
'''
### DO NOT CHANGE the first 3 lines of code.
# books = {"1": "AVAILABLE", "2": "AVAILABLE", "3": "AVAILABLE", "4":"BORROWED"}
# action = input("Enter 'B' to borrow a book or 'R' to return a book: ")
# book_id = input("Enter the book ID: ")
### Make your code fixes after this
###buggy code
# if action = "b" ### added an additional = and : ### lower case
#     if books[book_id] == "Available": ### not caps
#         books["B"] = "borrowed"### added an additional = ### not caps
#         print("You have borrowed the book.")
#     else:
#         print("The book is already borrowed.")
# elif action = "r": ### added an additional = ### lower case
#     if books[book_id] == "borrowed": ### not caps ###double equal sign
#         books("R") = "available" ### added an additional = ### not caps ###square bracket
#         print(You have returned the book.") ### added inverted commas
#     else: 
#     print("The book is already available.") ### lack indentation
#     else: ### else with indentation, which is wrong
#         print("Invalid action.) ### added inverted commas
### DO NOT CHANGE the first 3 lines of code.
books = {"1": "AVAILABLE", "2": "AVAILABLE", "3": "AVAILABLE", "4":"BORROWED"}
action = input("Enter 'B' to borrow a book or 'R' to return a book: ")
book_id = input("Enter the book ID: ")

## buggy code with corrections
if action.upper() == "B":
    if books[book_id] == "AVAILABLE":
        books[book_id] = "BORROWED"
        print("You have borrowed the book.")
    else:
        print("The book is already borrowed.")
elif action.upper() == "R": 
    if books[book_id] == "BORROWED":
        books[book_id] = "AVAILABLE"
        print("You have returned the book.") 
    else:
        print("The book is already available.")
else:
    print("Invalid action.") 
print(books)

'''
Open the file LIBRARY.py. Save the file as 
MYLIBRARY_<your name><center number><index number>.py.
Identify and correct the errors in the program so that it works according to 
the requirements given. Save your program.
[10 marks]
'''

###### ANSWER FOR DEBUGGING
'''
# == check for equality, single = is variable assignment
if action.upper() == "B": ## missing colon and == # change to uppercase
    if books[book_id] == "AVAILABLE": # change to upper case
        books[book_id] = "BORROWED" # change to uppercase, change to book_id
        print("You have borrowed the book.")
    else:
        print("The book is already borrowed.")
elif action.upper() == "R": # missing == # change to uppercase
    if books[book_id] == "BORROWED": # change to upper case
        books[book_id] = "AVAILABLE" # should be []
        print("You have returned the book.") # missing ""
    else:
        print("The book is already available.") # indentation error
else: # wrong indentation
    print("Invalid action.") # missing ""

print(books)
'''






######################################################
'''
Mock Task 3 Question 2
A program calculates the total cost of items bought by a customer in a 
grocery store. Each item has a price and quantity. The program should 
allow the user to input the price and quantity of each item, 
calculate the total cost, apply a discount if applicable, 
and display the final cost. 

A discount of 10% is applied if the total cost of the items is more than $100
A discount of 15% is applied if the total cost of the items is more than $200

There are several syntax, logic, and runtime errors in the program.
'''

total_cost = 0

while False:
    price == input("Enter the price of the item: ")
    quantity = input("Enter the quantity of the item: ")
    cost = price + total_cost
    
    more_items = input("Do you have more items? (Y/N): )
    
    if more_items = "n"
        continue

if total_cost > 100:
    total_cost = total_cost * 10%
print("A 10% discount has been applied.")
else:
    total_cost = total_cost * 20%
print("A 20% discount has been applied.")
    
print("The total cost is:" total_cost)

'''
Open the file GROCERY.py. Save the file as 
MYGROCERY_<your name><center number><index number>.py.
Identify and correct the errors in the program so that it 
works according to the requirements given. Save your program.
[10 marks]
'''