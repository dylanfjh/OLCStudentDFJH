### EXAMPLE DICTIONARY
# A dictionary variable holds a key and value pair
example = {
  'key1': 'value1',
  'key2': 'value2',
  'key3': 'value3',
  'key4': 'value4'
}


'''
################ Define a dictionary ###############
Define a dictionary named menu which will store a food item and price of food

'hamburger' costs 10
'pizza' costs 18.5
'lasagne' costs 25.70
'fries' costs 5
'''
# # write and test your code here 
menu = {
    'hamburger' : 10,
    'pizza' : 18.5,
    'lasagne' : 25.70,
    'fries' : 5}

# '''
# ################ Retrieve values from a dictionary ###############
# Print out the price of Lasagne only
# Print out the price of Fries only
# '''
# # write and test your code here 
# food1 = menu["fries"]
# print(food1)
# '''
# ########### Change the value of a dictionary key ###############
# Change the price of hamburger to 20
# Change the price of Fries to 3
# '''
# write and test your code here 
# print(menu)
# menu["hamburger"] = 20
# print(menu)
# menu["fries"] = 3
# print(menu)
# '''
# ############ Increase the value of a dictionary key ############
# Increase the price of Lasagne by 5
# Decrease the price of Pizza by 3
# '''
# # write and test your code here 
# menu["lasagne"] = menu["lasagne"] + 5
# #menu["lasagne"] = food2
# print(menu)
# menu["pizza"] -= 3
# print(menu)

# '''
# ############### Add a new key/ Value to the dictionary #####################
# Add a new menu item => Pasta which cost 15
# Add a new menu item => Sandwich which cost 6
# '''
# # write and test your code here 
# menu["pasta"] = 15
# menu["sandwich"] = 6
# print(menu)
# '''
# ############### Add a new key/ Value to the dictionary #####################
# Delete menu item Pasta
# '''
# # write and test your code here 
# del(menu["pasta"])
# print(menu)

# '''
# ########### Loop through to Retrieve Keys ##################
# # Write a for loop, and only display the name of food item that you sell
# # only display the keys
# '''
# for i in menu:
#     print(i)

# '''
# ########### Loop through to Retrieve Values ##################
# Write a for loop, and only print out the price
# '''
# # write and test your code here 
# for i in menu:
#     print(menu[i])

# '''
# ########### Loop through to Retrieve Key and Values ##################
# Write a for loop, and print out the menu key and values
# e.g.
# Hamburger costs $10.00
# Pizza costs $18.50
# '''
# # write and test your code here 
# for i in menu:
#     print(f"{i} costs ${menu[i]}. ")

'''
#################### Challenge 1 ######################################
Write a program to calculate how much money you need to buy all the items in the menu.
'''
# write and test your code here 
# sum = 0
# for food in menu:
#     food_price = menu[food] # retrieves the prices
#     sum = sum + food_price
# sum = 0
# for i in menu:
#     sum = sum + menu[i]
# print(sum)
    
'''
############### Challenge 2 ##########################################
Write a program to determine the most expensive item in the menu
'''

# list1 = [2944, 5490, 2357, 2619, 1177, 451, 8299, 2533, 4682, 6040,
#          5972, 7532, 4382, 8311, 6664, 4918, 3656, 3769, 6179, 7720,
#          5671, 537, 9777, 9421, 5455, 1241, 990, 3745, 8443, 4213,
#          4183, 2463, 9562, 8137, 5101, 397, 6966, 9927, 7473, 4105]
# max = 0 
# for i in list1:
#     if i > max:
#         max = i
# print(max)
# maximum number use a variable
# write and test your code here 
#for i in menu:
# max = 0
# maxitem = ""
# for i in menu:
#     if menu[i] > max:
#         max = menu[i]
#         maxitem = i
# print(max)
# print(maxitem)

'''
################ Challenge 3 ########################################
#### Due to inflation, prices have increased. Update all the prices by 10%
'''
# # write and test your code here 
# for i in menu:
#     menu[i] = round(menu[i] * 1.10, 2)
# print(menu)
    # how to print the whole dictionary out

'''
################ Challenge 4 ########################################
Upgrade this system where you ask customers what they want, and display the price 
# you can check if a key exists in a dicionaty, by using the 'in' keyword
# for example: if 'hamburger' in menu: will return true if hamburger exists 

Example:

Hello, What is your name? John
>>> Hi John, what would you like to eat? Laksa
>>> I'm sorry John, we don't sell Laksa. 

Hi John, what would you like to eat? Hamburger
>>> Great choice! Please pay $10.00. Your order will be delivered soon!
Hi John, what would you like to eat? Exit

Ok, bye!
### CHALLENGE: implement a wallet feature, so you have limited money to buy the item
Keep asking until no more money to buy
'''
# write and test your code here 
# name = input("what is your name? ")
# order = input(f"Hi, {name}. what do you want to eat? Here is our menu: {menu}")
# if order in menu: #in is how to chk for existence.
#     print(f"good. it is {menu[order]}.")
# else:
#     print(f"we do not have {order}")
# def showmenu():
#     print("-"*29)
#     for food in menu:
#         print("|{:^15} : {:^8} |".format(food, menu[food]))
#         #print(f"{food} : ${menu[food]}")
#     print("-"*29)
    
# budget = int(input("what is your budget? "))
# while True:
#     if budget > 0:
#         name = input("what is your name? ")
#         print("Here is our menu.")
#         showmenu()
#         order = input(f"Hi, {name}. what do you want to eat? ")
#         if order in menu:
#             mon_left = budget - menu[order]
#             # print(f"you hv ordered {order}, and have ${mon_left}. anymore?" ) 
#             # print("Here is our menu.")
#             # showmenu()
#             if mon_left <= 0:
#                 print("no money left.")
#                 break
#             else:
#                 order = input(f"Hi, {name}. what do you want to eat? ")
#                 if order in menu:
#                     mon_left = budget - menu[order]
#                     print(f" you hv ordered {order}, and have {mon_left}. anymore?" )
#     else:
#         break

    
    


'''
Q2
You are given a list of computing paper 1 marks and paper 2 marks

paper1 = {"Ken": 80, "Mike": 84, "Ash": 55, "Zee": 65}
paper2 = {"Ken": 88, "Mike": 64, "Ash": 65, "Zee": 85}

Design a program to

1a.  update Ken's computing mark to 83 for paper 1 

1b.  update Mike's computing mark to 58 for paper 2 

2.  show the average of paper 1 marks and average of paper 2 marks

3.  ask user to enter a person and the paper he wants to search. 
If the person is in the list, show the respective mark.
Otherwise shows that the person cannot be found
'''

paper1 = {"Ken": 80, "Mike": 84, "Ash": 55, "Zee": 65}
paper2 = {"Ken": 88, "Mike": 64, "Ash": 65, "Zee": 85}

# 1a
paper1["Ken"] = 83
print(paper1)
# 1b
paper2["Mike"] = 58
print(paper2)

#2
def count(ppr):
    for i in ppr:
        print(i + "/")
        sum = 0
        sum = sum + int(ppr[i])
        print(sum)
    return ppr

count(paper1)

#3

      