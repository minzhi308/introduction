board = [
  [" ", " ", " ", " ", " ", " ", " "],
  [" ", " ", " ", " ", " ", " ", " "],
  [" ", " ", " ", " ", " ", " ", " "],
  [" ", " ", " ", " ", " ", " ", " "],
  [" ", " ", " ", " ", " ", " ", " "],
  [" ", " ", " ", " ", " ", " ", " "],
]

def print_board(board):
  for i in range(6):
      print("+---+---+---+---+---+---+---+")
      for j in range(7):
          print(f"| {board[i][j]} ", end="")
      print("|")
  print("+---+---+---+---+---+---+---+")
  print("  0   1   2   3   4   5   6  ")

print_board(board)

end_game = False

def check_draw(board):
  # Check if the board is full
  board_full = all(" " not in row for row in board)

  # Alternatively, you can use nested loops to achieve the same:
  board_full = True
  for row in board:
      for cell in row:
          if cell == " ":
              board_full = False
              break
      if not board_full:
          break

  if board_full:
      print("It's a draw!")
      end_game = True
      return True

while not end_game:
  # X玩家
  # 輸入驗證
  while True:
      column_X = input("Player X >> ")
      if column_X.isdigit():  # 檢查輸入是否為數字
          column_X = int(column_X)
          if 0 <= column_X <= 6:  # 確保輸入在 0 到 6 之間 
              break
      print("Invalid input. try again [0~6].")

  column_x = 5

  while board[column_x][column_X] != " ":
      column_x -= 1
      if column_x < 0:
          print("Column is full. Try again.")
          while True:
              column_X = input("Player X >> ")
              if column_X.isdigit():  # 檢查輸入是否為數字
                  column_X = int(column_X)
                  if 0 <= column_X <= 6:  # 確保輸入在 0 到 6 之間 
                      break
              print("Invalid input. try again [0~6].")
          column_x = 5

  board[column_x][column_X] = "X"
  print_board(board)

  # Check if the game is over
  # Check horizontal
  for i in range(6):
      for j in range(4):
          if board[i][j] == board[i][j + 1] == board[i][j + 2] == board[i][j + 3] != " ":
              print(f"Winner: {board[i][j]}")
              end_game = True
              break
      if end_game:
          break
  # Check vertical
  for i in range(3):
      for j in range(7):
          if board[i][j] == board[i + 1][j] == board[i + 2][j] == board[i + 3][j] != " ":
              print(f"Winner: {board[i][j]}")
              end_game = True
              break
      if end_game:
          break
  # Check diagonal
  for i in range(3):
      for j in range(4):
          if (
              board[i][j]
              == board[i + 1][j + 1]
              == board[i + 2][j + 2]
              == board[i + 3][j + 3]
              != " "
          ):
              print(f"Winner: {board[i][j]}")
              end_game = True
              break
      if end_game:
          break

  # 在 X 玩家的回合後加入檢查是否平手
  check_draw(board)

  if end_game:
      break

  # O玩家
  # 輸入驗證
  while True:
      column_O = input("Player O >> ")
      if column_O.isdigit():  # 檢查輸入是否為數字
          column_O = int(column_O)
          if 0 <= column_O <= 6:  # 確保輸入在 0 到 6 之間 
              break
      print("Invalid input. try again [0~6].")

  column_x = 5

  while board[column_x][column_O] != " ":
      column_x -= 1
      if column_x < 0:
          print("Column is full. Try again.")
          while True:
              column_O = input("Player O >> ")
              if column_O.isdigit():  # 檢查輸入是否為數字
                  column_O = int(column_O)
                  if 0 <= column_O <= 6:  # 確保輸入在 0 到 6 之間 
                      break
              print("Invalid input. try again [0~6].")
          column_x = 5

  board[column_x][column_O] = "O"
  print_board(board)

  # Check horizontal
  for i in range(6):
      for j in range(4):
          if board[i][j] == board[i][j + 1] == board[i][j + 2] == board[i][j + 3] != " ":
              print(f"Winner: {board[i][j]}")
              end_game = True
              break
      if end_game:
          break
  # Check vertical
  for i in range(3):
      for j in range(7):
          if board[i][j] == board[i + 1][j] == board[i + 2][j] == board[i + 3][j] != " ":
              print(f"Winner: {board[i][j]}")
              end_game = True
              break
      if end_game:
          break
  # Check diagonal
  for i in range(3):
      for j in range(4):
          if (
              board[i][j]
              == board[i + 1][j + 1]
              == board[i + 2][j + 2]
              == board[i + 3][j + 3]
              != " "
          ):
              print(f"Winner: {board[i][j]}")
              end_game = True
              break
      if end_game:
          break

  # 在 O 玩家的回合後加入檢查是否平手
  check_draw(board)
  if end_game:
    break

#會計系 H14126173 賈閔之