import random

class CandyCrushGame:
    def __init__(self, width, height, num_candy_types):
        self.width = width
        self.height = height
        self.num_candy_types = num_candy_types
        self.board = []
        self.score = 0
        self.initialize_board()
        
    def initialize_board(self):
        for _ in range(self.height):
            row = [random.randint(1, self.num_candy_types) for _ in range(self.width)]
            self.board.append(row)
            
    def print_board(self):
        for row in self.board:
            print(' '.join(map(str, row)))
        print(f"Score: {self.score}")
        
    def get_user_input(self):
        while True:
            try:
                row1, col1 = map(int, input("Enter the first candy position (row col): ").split())
                row2, col2 = map(int, input("Enter the adjacent candy position (row col): ").split())
                if self.is_valid_move(row1, col1, row2, col2):
                    return (row1, col1), (row2, col2)
                else:
                    print("Invalid move. Please enter adjacent positions.")
            except ValueError:
                print("Invalid input. Please enter integers separated by space.")
                
    def is_valid_move(self, row1, col1, row2, col2):
        return (abs(row1 - row2) == 1 and col1 == col2) or (abs(col1 - col2) == 1 and row1 == row2)
    
    def swap_candies(self, pos1, pos2):
        (row1, col1), (row2, col2) = pos1, pos2
        self.board[row1][col1], self.board[row2][col2] = self.board[row2][col2], self.board[row1][col1]
    
    def find_matches(self):
        matches = []
        for r in range(self.height):
            for c in range(self.width):
                if c < self.width - 2 and self.board[r][c] == self.board[r][c + 1] == self.board[r][c + 2]:
                    matches.append((r, c))
                    matches.append((r, c + 1))
                    matches.append((r, c + 2))
                if r < self.height - 2 and self.board[r][c] == self.board[r + 1][c] == self.board[r + 2][c]:
                    matches.append((r, c))
                    matches.append((r + 1, c))
                    matches.append((r + 2, c))
        return set(matches)
    
    def eliminate_candies(self, matches):
        for r, c in matches:
            self.board[r][c] = 0
        self.score += len(matches)
        
    def drop_candies(self):
        for c in range(self.width):
            empty_spots = 0
            for r in range(self.height - 1, -1, -1):
                if self.board[r][c] == 0:
                    empty_spots += 1
                elif empty_spots > 0:
                    self.board[r + empty_spots][c] = self.board[r][c]
                    self.board[r][c] = 0
            for r in range(empty_spots):
                self.board[r][c] = random.randint(1, self.num_candy_types)
                
    def play(self):
        while True:
            self.print_board()
            pos1, pos2 = self.get_user_input()
            self.swap_candies(pos1, pos2)
            while True:
                matches = self.find_matches()
                if matches:
                    self.eliminate_candies(matches)
                    self.drop_candies()
                else:
                    break
            if self.score >= 100:  # Arbitrary condition to end the game
                print("Game over! You've reached 100 points!")
                break

if __name__ == "__main__":
    width = int(input("Enter the width of the board: "))
    height = int(input("Enter the height of the board: "))
    num_candy_types = int(input("Enter the number of candy types: "))
    game = CandyCrushGame(width, height, num_candy_types)
    game.play()
#會計系 H14126173 賈閔之