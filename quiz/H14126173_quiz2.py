x = int(input("Enter the shopping amount: "))
membership = input("Enter the membership level (Regular or Gold): ")
result = x

#一般會員
if membership == "Regular":
	if x > 3000:
		result = 0.8 * x
	elif x > 2000:
		result = 0.85 * x
	elif x > 1000:
		result = 0.9 * x
	else:
		x = x
	
	print("Regular $" + str(result))

#黃金會員
elif membership == "Gold":
	if x > 3000:
		result = 0.75 * x
	elif x > 2000:
		result = 0.8 * x
	elif x > 1000:
		result = 0.85 * x
	else:
		x = x
	
	print("Gold $" + str(result))

#都不是
else:
	print("Invalid membership level. Please enter 'Regular' or 'Gold'.")