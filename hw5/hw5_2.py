import random  # 導入random模組以生成隨機數


# 創建棋盤函數
def create_board(length):
    # 以0.3的機率將棋盤上的格子設為懲罰格(P)，否則設為安全格(_)
    return ["P" if random.random() < 0.5 else "_" for _ in range(length)]


# # 打印棋盤函數
# def print_board(board, player_pos, penalty, roll):
#     # 將懲罰格設為安全格以便打印，但保留實際棋盤狀態
#     display_board = ["_" if square == "P" else square for square in board]

#     # 將玩家位置顯示在棋盤上
#     pos_a = player_positions[0]
#     pos_b = player_positions[1]

#     if pos_a < len(board):
#         if board[pos_a] == "P":
#             display_board[pos_a] = "a"
#         else:
#             display_board[pos_a] = "A"

#     if pos_b < len(board):
#         if board[pos_b] == "P":
#             display_board[pos_b] = "b"
#         else:
#             display_board[pos_b] = "B"

#     # 標記重疊位置
#     for i in range(len(display_board)):
#         if i > 0 and (display_board[i] in "AB" and display_board[i - 1] in "AB"):
#             display_board[i] = "X"
#         elif i > 0 and (display_board[i] in "ab" and display_board[i - 1] in "ab"):
#             display_board[i] = "x"

#     # 將棋盤轉換為字符串並附上玩家擲骰子的結果
#     board_str = "".join(display_board)
#     rolls_str = f"(A: {rolls[0]}, B: {rolls[1]})"
#     print(board_str + " " + rolls_str)


def print_board(board, roll_A, player_A, penalty_A, roll_B, player_B, penalty_B):
    display_board = ["_" if square == "P" else square for square in board]

    if penalty_A == True or roll_A == 0:
        display_board[player_A] = "a"
    else:
        display_board[player_A] = "A"

    if penalty_B == True or roll_B == 0:
        display_board[player_B] = "b"
    else:
        display_board[player_B] = "B"

    board_str = "".join(display_board)  # _______________
    print(f"{board_str} A: {roll_A}, B: {roll_B}")  # _____A__b______ A: 3, B: 3


def print_same_place(board, roll, player_pos, penalty=False):
    display_board = ["_" if square == "P" else square for square in board]

    if penalty == True or roll == 0:
        display_board[player_pos] = "x"
    elif penalty == False:
        display_board[player_pos] = "X"

    board_str = "".join(display_board)  # ________x______
    print(f"{board_str} A: {roll}, B: {roll}")  # ________x______ A: 3, B: 3


def check_winner(player_A, player_B):
    if player_A == 29 and player_B == 29:
        print("Both Players win!")
        return True
    elif player_A == 29:
        print("Player A wins!")
        return True
    elif player_B == 29:
        print("Player B wins!")
        return True
    else:
        return False


# 擲骰子函數
def roll_dice():
    return random.randint(1, 6)  # 隨機生成1到6之間的整數


# 遊戲主函數
def game():
    board_length = 30  # 棋盤長度設為30
    board = create_board(board_length)  # 創建棋盤
    board_str = "".join(board)  # 將棋盤轉換為字符串
    print(board_str)  # 打印棋盤

    # player A information
    player_A = 0
    penalty_A = False
    rolls_A = 0
    # player B information
    player_B = 0
    penalty_B = False
    rolls_B = 0
    turn = 0  # 記錄回合數

    while True:
        # 玩家A行動
        if penalty_A == False:
            rolls_A = roll_dice()  # 擲骰子
            player_A += rolls_A
            player_A = 29 if player_A > 29 else player_A
        else:
            rolls_A = 0
            player_A = player_A
            penalty_A = False

        # 玩家B行動
        if penalty_B == False:
            rolls_B = roll_dice()  # 擲骰子
            player_B += rolls_B
            player_B = 29 if player_B > 29 else player_B
        else:
            rolls_B = 0
            player_B = player_B
            penalty_B = False

        # 玩家A是否踩到懲罰格
        if board[player_A] == "P" and rolls_A != 0:
            penalty_A = True
        else:
            penalty_A = False

        # 玩家B是否踩到懲罰格
        if board[player_B] == "P" and rolls_B != 0:
            penalty_B = True
        else:
            penalty_B = False

        # print(f"Player A: {player_A}, Player B: {player_B}")  # 打印玩家位置
        if player_A == player_B and penalty_A == penalty_B:
            print_same_place(board, rolls_A, player_A, penalty_A)
        else:
            print_board(board, rolls_A, player_A, penalty_A, rolls_B, player_B, penalty_B)

        if check_winner(player_A, player_B):
            break

    print(board_str)  # 打印棋盤


if __name__ == "__main__":
    game()  # 運行遊戲

#會計系 H14126173 賈閔之