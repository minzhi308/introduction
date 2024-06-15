import json

def candyCrush(board):
    rows, cols = len(board), len(board[0])
    crushed = True  # Flag to indicate if any candies were crushed
    
    while crushed:
        crushed = False
        
        # Step 1: Mark candies to crush
        crush = [[False] * cols for _ in range(rows)]
        for r in range(rows):
            for c in range(cols - 2):
                if board[r][c] != 0 and abs(board[r][c]) == abs(board[r][c+1]) == abs(board[r][c+2]):
                    crush[r][c] = crush[r][c+1] = crush[r][c+2] = True
                    crushed = True
        
        for r in range(rows - 2):
            for c in range(cols):
                if board[r][c] != 0 and abs(board[r][c]) == abs(board[r+1][c]) == abs(board[r+2][c]):
                    crush[r][c] = crush[r+1][c] = crush[r+2][c] = True
                    crushed = True
        
        # Step 2: Crush marked candies
        for r in range(rows):
            for c in range(cols):
                if crush[r][c]:
                    board[r][c] = 0
        
        # Step 3: Drop candies
        for c in range(cols):
            for r in range(rows-1, 0, -1):
                if board[r][c] == 0:
                    for k in range(r-1, -1, -1):
                        if board[k][c] != 0:
                            board[r][c], board[k][c] = board[k][c], board[r][c]
                            break
        
    return board

# Read input from candy_input1.txt
with open('C:/Users/minzh/Downloads/test folder/sources/candy input1.txt', 'r') as file:
    # Read each line from the file
    lines = file.readlines()
    # Split each line by commas and convert strings to integers
    board = [list(map(int, line.strip().split(','))) for line in lines]

# Process the board until it becomes stable
result = candyCrush(board)

# Write output to candy_output1.txt
with open('C:/Users/minzh/Downloads/test folder/sources/candy output1.txt', 'w') as file:
    # Convert the result back to a string and write it to the file
    for row in result:
        file.write(','.join(map(str, row)) + '\n')
