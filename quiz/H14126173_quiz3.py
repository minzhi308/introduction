print("Welcome to the simple calculator program!")

answer = "yes" or "no" 
while answer == "yes":
	first = input("Enter the first number: ")
	second = input("Enter the second number: ")

	first = float(first)
	second = float(second)

	operation = input("Select an arithmatic operation(+,-,*,/): ")
	if operation == "+":
		result = first + second
		print("Result:", result)
	elif operation == "-":
		result = first - second
		print("Result:", result)
	elif operation == "*":
		result = first * second
		print("Result:", result)		
	elif operation == "/":
		if second == 0:
			print("Error: Division by zero!")
			continue
		else:
			result = first / second
			print("Result:", result)

	answer = input("Do you want to perform another calculation? (yes or no): ")
			
print("Goodbye!")