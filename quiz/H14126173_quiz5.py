n = int(input("Enter the size of the grid: "))

# create a matrix with n x n (2D-lst)
matrix = [["_" for i in range(n)] for j in range(n)]

# print the grid
for i in range(n):
  for j in range(n):
    print(matrix[i][j], end = " ")
  print()

cell_coordinates = ""
new_value = ""

# or while cell_coordinates != "done":
while True:
  cell_coordinates = input("Enter the cell coordinates to edit: ")
  # if user enter"done" -> break
  if cell_coordinates == "done":
    break
  
  # str -> row, col
  row,col = cell_coordinates.split(",") # ['0','0']
   # str -> int
  row, col = int(row), int(col)
  new_value = input("Enter the new value for the cell: ")
  # update the matrix
  matrix[row][col] = new_value

# display the grid
for i in range(n):
  print(" ".join(matrix[i]))
