
count = 0
while True:
	num = int(input("Enter a number"))
	count += num
	if num == 0:
		break
print(count)


while True:
	num1 = int(input("Enter a number"))
	if num1 == 0:
		print("exit")
		break
	elif num1 % 3 == 0 and 1 < num1 <= 30:
		print(num1)



import random
n = random.randint(1, 100)

attempt = 7
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
	attempt -= 1
	if attempt == 0:
		print("you lost")
		break





