# Input the total number of students
n = int(input("Enter the total number of students: "))

# Initialize a list to represent students seated at the round table
students = list(range(1, n + 1))

# Initialize the index to start counting
index = 0

# Iterate until there is only one student left
while len(students) > 1:
    # Find the next student to report
    index = (index + 2) % len(students)
    # Remove the student who reports 3
    students.pop(index)

# Output the student ID who is the last one seating on the round table
print("The student ID of the last one remaining:", students[0])

#會計系 H14126173 賈閔之
