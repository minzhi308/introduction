import random

def read_maze_file():
    while True:
        try:
            file_name = input("Enter file name: ")
            with open(file_name, 'r') as file:
                lines = file.readlines()
                maze = {}
                for i, line in enumerate(lines):
                    for j, char in enumerate(line.strip()):
                        if char == '0':
                            maze[(i, j)] = 0
                        elif char == '1':
                            maze[(i, j)] = 1
                        elif char == '+':
                            maze[(i, j)] = 2  # Assuming '+' indicates the path
                        else:
                            maze[(i, j)] = 0  # Treat any other character as an empty cell
                N = len(lines)
                M = len(lines[0].strip())
                return maze, N, M
        except FileNotFoundError:
            print("IOEError occurred in main function. File not found. Please enter a valid file name.")
        except ValueError as e:
            print(f"Error: {e}")

def generate_path(maze, N, M):
    # This function generates a random path through an NxM maze, represented as a dictionary. The keys are (i, j) tuples representing
    # coordinates of each cell in the maze and the values are integers: 0 for empty, 1 for obstacle, and 2 for path. The path starts 
    # from (0,0) and ends at (N-1,M-1), and the direction (right or down) at each step is chosen randomly.

    # your code here
    path = [(0, 0)]
    maze[(0, 0)] = 2
    current_pos = (0, 0)
    
    while current_pos != (N-1, M-1):
        x, y = current_pos
        possible_moves = []
        if x < N-1 and maze[(x+1, y)] == 0:
            possible_moves.append((x+1, y))
        if y < M-1 and maze[(x, y+1)] == 0:
            possible_moves.append((x, y+1))
        
        if possible_moves:
            current_pos = random.choice(possible_moves)
            maze[current_pos] = 2
            path.append(current_pos)
        else:
            path.pop()
            if not path:
                raise ValueError("No possible path from start to end")
            current_pos = path[-1]
    
    return maze, path

def add_obstacles(maze, min_obstacles, N, M):
    # This function randomly adds obstacles (represented as 1) to the empty cells (represented as 0) in the given maze until at least
    # min_obstacles have been added. If a KeyError occurs while trying to set an obstacle, it is caught and a message is printed.

    # your code here
    empty_cells = [(i, j) for i in range(N) for j in range(M) if maze[(i, j)] == 0]
    if len(empty_cells) < min_obstacles:
        raise ValueError("Not enough empty cells to add the required number of obstacles.")
    random.shuffle(empty_cells)
    for i in range(min_obstacles):
        maze[empty_cells[i]] = 1
    return maze

def set_obstacle(maze, N, M):
    # This function allows a user to manually set an obstacle in the maze. The user is prompted to input the coordinates of the cell
    # where they want to place the obstacle. If the cell is part of the path or an obstacle is already present, an error message is 
    # displayed. If the coordinates are out of bounds or not integers, a KeyError or ValueError is raised, respectively.

    # your code here
    try:
        x = int(input("Enter the row (0-indexed): "))
        y = int(input("Enter the column (0-indexed): "))
        if (x, y) in maze:
            if maze[(x, y)] == 2:
                print("Error: Cannot place obstacle on the path!")
            else:
                maze[(x, y)] = 1
        else:
            print("Error: Coordinates out of bounds!")
    except ValueError:
        print("Error: Invalid coordinates!")


def remove_obstacle(maze, N, M):
    # This function allows a user to manually remove an obstacle from the maze. The user is prompted to input the coordinates of the 
    # cell where they want to remove the obstacle. If the cell is part of the path or there's no obstacle at the given cell, an error 
    # message is displayed. If the coordinates are out of bounds or not integers, a KeyError or ValueError is raised, respectively.

    # your code here
    try:
        x = int(input("Enter the row (0-indexed): "))
        y = int(input("Enter the column (0-indexed): "))
        if (x, y) in maze:
            if maze[(x, y)] == 2:
                print("Error: Cannot remove path cell!")
            else:
                maze[(x, y)] = 0
        else:
            print("Error: Coordinates out of bounds!")
    except ValueError:
        print("Error: Invalid coordinates!")


def print_maze(maze, N, M):
    # This function prints the current state of the maze in a grid-like format. Each cell is represented by a 3-character string: 
    # '   ' for empty cells, ' X ' for obstacles, and ' O ' for path cells.

    # your code here
    for i in range(N):
        for j in range(M):
            if maze[(i, j)] == 0:
                print("   ", end="")
            elif maze[(i, j)] == 1:
                print(" X ", end="")
            elif maze[(i, j)] == 2:
                print(" O ", end="")
        print()


def main():
    # This function serves as the main driver of the program. It reads the maze dimensions from a file, asks the user for the minimum 
    # number of obstacles to be added, generates the path and adds the obstacles, and then enters a loop where the user can choose to 
    # set or remove obstacles, print the maze, or exit the program. Exceptions for ValueError, IOError, and NameError are handled.

    # your code here
    # load grid
    try:
        maze, N, M = read_maze_file()

        while True:
            try:
                min_obstacles = int(input("Enter the minimum number of obstacles (0-55): "))
                if min_obstacles < 0 or min_obstacles > 55 or min_obstacles.isdigit() == False:
                    raise ValueError("ValueError occurred in main function. Invalid number of obstacles.")
                break
            except ValueError as e:
                print(e)

        maze, path = generate_path(maze, N, M)
        maze = add_obstacles(maze, min_obstacles, N, M)
        print_maze(maze, N, M)
        
        while True:
            print("Menu:")
            print("1. Add an obstacle")
            print("2. Remove an obstacle")
            print("3. Display maze")
            print("4. Exit")

            choice = input("Enter your choice: ")
            if choice == '1':
                set_obstacle(maze, N, M)
            elif choice == '2':
                remove_obstacle(maze, N, M)
            elif choice == '3':
                print_maze(maze, N, M)
            elif choice == '4':
                break
            else:
                print("Invalid choice!")
    except ValueError as e:
        print(f"Error: {e}")
    except IOError as e:
        print(f"Error: {e}")
    except NameError as e:
        print(f"Error: {e}")

main()
