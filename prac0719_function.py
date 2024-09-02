### Basic 1: Functions with no parameters, no return value
'''
# Question 1: Declare a function that prints "Hello, World!" 
# and call the function.
# Example input: 
# Expected output: Hello, World!
'''
# Write your code here
# defining the function
# def hello():
#     print("Hello, world")

# # calling the function
# hello()


### Basic 2: Functions with 1 or more parameters
'''
# Question 2: Declare a function greet that takes a 
# name as a parameter and prints a greeting message.
# Example input: name = 'John'
# Expected output: 'Hello, John!'
'''
# Write your code here

# def hello(name):
#     print(f"Hello, {name}")
    
# name2 = input("what is your name? ")
# hello(name2)

############## EXPLANATION ON WHY WE NEED TO RETURN ###################
# if you return a value, it allows you to use it for different scenarios
#### define a function to calculate the area of triangles
# def areatriangle(base, height):
#     area = 0.5 * base * height
#     return area

# # 3 triangles
# t1 = areatriangle(45, 98)
# t2 = areatriangle(123, 4334546)
# t3 = areatriangle(123, 23423423)

# print(t1 + t2 + t3) # total area of 3 triangles
# ############## EXPLANATION ON WHY WE NEED TO RETURN ###################

'''
# Question 3: Declare a function greet that takes yourname and myname
# as parameters and prints a introduction message.
# Example input: yourname = 'John', myname="Marcus"
# Expected output: 'Hello, John! I'm Marchus, nice to meet you!'
'''
# Write your code here
# def greetings(yourname , myname):
#     print(f" Hello, {yourname}! I'm {myname}, nice to meet you.")

# yourname = input("what is your friends name? ")
# myname = input("what is your name? ")
# greetings(yourname , myname)
    

### Basic 3: Functions with parameters and return value

'''
# Question 4: Declare a function that takes two numbers 
# as parameters and returns their sum.
# Example input: a = 5, b = 3
# Expected output: 8
'''
# Write your code here
# def addition(a , b):
#     num = int(a) + int(b)
#     print(str(num))
# ### the a abv and btm is a diff variable. it will be confusing ###
# a = input("what is the first number? ")
# b = input("what is your second number? ")
# addition(a,b)

# def sum(a , b):
#     return(a + b)

# num1 = int(input("what is the first number? "))
# num2 = int(input("what is the second number? "))
# sum (num1 , num2)
# print(sum(num1, num2))


#print(addition(5, 3)) #this code will test your function

'''
# Question 5: Declare a function that takes a number as a parameter 
# and returns True if the number is even, otherwise False.
# Example input: number = 4
# Expected output: True
'''
# Write and test your code here
# def evenodd(num):
#     if int((num)) % 2 == 0:
#         return True
#     else:
#         return False

# # num1 = input("what is the num you want to check? ")
# # print(evenodd(num1))

# for i in range(1, 101):
#     print(f'Number {i} is even = {evenodd(i)}')

sentence = input("what do you want to write? ")
sym = input("what symbol do you want to add? ")
def print_signage(msg, symbol):
    middle = symbol + "" + msg + "" + symbol
    len_sentence = len(middle)
    start = symbol * len_sentence
    print(start)
    print(middle)
    end = symbol * len_sentence
    print(end)
    return (msg, symbol)

print_signage(sentence, sym)
    
    
    
        
    
    