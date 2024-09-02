# #### COUNTER ALGORITHM ##########

# message = "aaabbbababababccccbabababccccababababababcccabbbccccababa"

# # count the number of a in this string
# # count the number of b in this string
# # count the number of c in this string

# counta = 0
# countb = 0
# countc = 0

# for i in message:
#     if i == "a":
#         counta = counta + 1
#         #counta += 1
#     if i == "b":
#         countb = countb + 1  
#     if i == "c":
#         countc = countc + 1

# # print("we have " + str(counta) + " number of As")
# # print("we have " + str(countb) + " number of Bs")
# # print("we have " + str(countc) + " number of Cs")

# print(f"We have {counta} number of As")
# print(f"We have {countb} number of Bs")
# print(f"We have {countc} number of Cs")

# print("We have {} number of As and {} number of Bs".format(counta, countb))


### MAX/ MIN
# # nums = [1,23,45,3564,65,67,68,556,4325,457,57,45,57,56,2432,2133734,6567,878,9,56,234,2346,90890,435,23,4]
# # # Find the maximum number and minimum number in this list of numbers
# # maxnum = 0
# # minnum = nums[0] or max(nums)
# # for i in nums:
# #     if i > maxnum:
# #         maxnum = i
# #     if i < minnum:
# #         minnum =i
# print(f"the max num is {maxnum}.")      
# print(f"the min num is {minnum}.")


### create a list of 100 random numbers
# each number is a range between 1 - 1000
# every number in this list must be unique

import random
# num2 = random.randint(1, 1000)
# .append(value)
# for i in range(100):
#     num = random.randint(1, 1000)
#     listnums.append(num)
# print(listnums)

listnums = []

while len(listnums) <100:
    num = random.randint(1, 1000)
    if num not in listnums:
        listnums.append(num)
print(len(listnums))
print(listnums)

# for i in listnum:
#     num = random.randint(1, 1000)
#     if i = num:
#     listnums.append(num)
# print(listnums)
    
    

# for i in range(100):
#     print(list)