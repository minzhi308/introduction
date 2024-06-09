# Minesweeper
import random
import time


# (a)
def display(board):
    print("     a   b   c   d   e   f   g   h   i")
    for i in range(9):
        print("   +---+---+---+---+---+---+---+---+---+")
        print(f"{i+1}  ", end="")
        for j in range(9):
            # dictionary
            print(f"| {board[(i, j)]} ", end="")
        print("|")
    print("   +---+---+---+---+---+---+---+---+---+")


# (b)
def generate_mines(board, mines_count, row, col):
    mines = []
    # dictionary
    mine_map = {}

    row = int(row) - 1
    col = ord(col) - ord("a")

    for i in range(9):
        for j in range(9):
            mine_map[(i, j)] = " "

    # generate mines
    print("Generating mines...")
    for i in range(mines_count):
        while True:
            row_gen = random.randint(0, 8)
            col_gen = random.randint(0, 8)

            if (row_gen == row and col_gen == col) or (abs(row - row_gen) < 2 and abs(col - col_gen) < 2) or (row_gen, col_gen) in mines:
                continue
            else:
                mines.append((row_gen, col_gen))
                mine_map[(row_gen, col_gen)] = "X"
                break

    for i in range(9):
        for j in range(9):
            if mine_map[(i, j)] == "X":
                continue
            count = 0
            for r in range(i - 1, i + 2):
                for c in range(j - 1, j + 2):
                    if 0 <= r <= 8 and 0 <= c <= 8 and mine_map[(r, c)] == "X":
                        count += 1
            mine_map[(i, j)] = str(count)

    display(mine_map)

    board[(row, col)] = "0"

    print("Unfolding cells that are connected to the selected cell...")
    queue = [(row, col)]
    unfolded_pos = []
    while queue:
        r, c = queue.pop(0)
        for i in range(r - 1, r + 2):
            for j in range(c - 1, c + 2):
                if 0 <= i <= 8 and 0 <= j <= 8 and mine_map[(i, j)] == "0" and board[(i, j)] == " ":
                    board[(i, j)] = "0"
                    queue.append((i, j))
                    unfolded_pos.append((i, j))
    display(board)

    print("Unfolded cells:")
    while unfolded_pos:
        r, c = unfolded_pos.pop(0)
        for i in range(r - 1, r + 2):
            for j in range(c - 1, c + 2):
                if 0 <= i <= 8 and 0 <= j <= 8 and mine_map[(i, j)] != "0":
                    board[(i, j)] = mine_map[(i, j)]
    display(board)

    return mine_map


# (c)
def show_help():
    display(board)
    help_message = "Enter the column followed by the row (ex: a5). To add or remove a flag, add 'f' to the cell (ex: a5f). Type 'help' to show this message again. Type 'quit' to exit the game."
    print(help_message)


# (d)
def add_or_remove_flag(board, row, col, mines_count):
    if board[(row, col)] == " ":
        board[(row, col)] = "F"
        mines_count -= 1
    elif board[(row, col)] == "F":
        board[(row, col)] = " "
        mines_count += 1
    else:
        print("Cannot put a flag there.")

    return mines_count


def check_valid_position(col, row):
    row = int(row) - 1
    col = ord(col) - ord("a")

    if 0 <= row <= 8 and 0 <= col <= 8:
        return True
    return False


def transform_position(row, col):
    row = int(row) - 1
    col = ord(col) - ord("a")
    return row, col


def unfold(board, row, col, mine_map):
    gameover = False
    if board[(row, col)] == "F":
        print("There is a flag there.")
    elif board[(row, col)] != " ":
        print("That cell is already shown.")
    elif mine_map[(row, col)] == "X":
        print("Game over.")
        gameover = True
    else:
        board[(row, col)] = mine_map[(row, col)]
    return gameover


def check_win(board):
    for row in range(9):
        for col in range(9):
            if board[(row, col)] == " ":
                return False
    return True


play_again = True
while play_again:
    start = time.time()
    # dictionary
    board = {}

    for i in range(9):
        for j in range(9):
            board[(i, j)] = " "

    display(board)

    mines_count = 10

    position = input(f"Enter the cell ({mines_count} mines left): ")
    col, row = position[0], position[1]

    mine_map = generate_mines(board, mines_count, row, col)

    while True:
        position = input(f"Enter the cell ({mines_count} mines left): ")
        gameover = False
        if position == "help":
            show_help()
            continue

        if not check_valid_position(position[0], position[1]):
            print("Invalid position. Try again.")
            continue

        if len(position) == 3:
            col, row, flag = position[0], position[1], position[2]
            row, col = transform_position(row, col)
            mines_count = add_or_remove_flag(board, row, col, mines_count)
        elif len(position) == 2:
            col, row = position[0], position[1]
            row, col = transform_position(row, col)
            gameover = unfold(board, row, col, mine_map)

        if gameover:
            display(mine_map)
            break
        if check_win(board):
            end = time.time()
            print(f"You win. It took you {end - start:.2f} seconds.")
            break

        display(board)

    play_again = input("Do you want to play again? (yes/no): ")
    if play_again == "no":
        play_again = False

#會計系 H14126173 賈閔之