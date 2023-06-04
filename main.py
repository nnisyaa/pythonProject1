# number = 0
# while number < 30:
#  if number == 0:
#   continue
#  print (number)
#  number += 3
from random import random

# while True:
#     print("1. First Task")
#     task_n = int(input)
#     if task_n == 1:
#      print ("Task number 1")

# import random
# n = random.randint(10, 99)
# print(n)
# from random import randint
#
# while True:
#  n = randint(10, 99)
#  print(n)
#  flag = int(input())


# # task 1
# count = 0
# while True:
# 	num = int(input("Enter a number"))
# 	count += num
# 	if num == 0:
# 		break
# print(count)
#
# # task 2
# while True:
# 	num1 = int(input("Enter a number"))
# 	if num1 == 0:
# 		print("exit")
# 		break
# 	elif nu1m % 3 == 0 and 1 < num1 <= 30:
# 		print(num1)


# task 3
import random
n = random.randint(1, 100)
print(n)
attempt = 4
while True:
	num2 = int(input("Guess the number"))
	if num2 == n:
		print("You won!")
		break
	elif num2 == 0:
		print("exit")
		break
	elif n - 3 < num2 < n + 3:
		print("super hot")
	elif n-5 < num2 < n+5:
		print("hot")
	elif n-10 < num2 < n+10:
		print("hotter")
	elif n-50 < num2 < n+50:
		print("cold")
	elif n-99 < num2 < n+99:
		print("super cold")
	elif attempt -= 1:
		print("you lost")
		break



