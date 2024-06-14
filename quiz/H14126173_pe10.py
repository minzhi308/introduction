import curses
import random

# Initialize the screen and curses settings
stdscr = curses.initscr()
curses.curs_set(0)
sh, sw = stdscr.getmaxyx()
w = curses.newwin(sh, sw, 0, 0)
w.keypad(1)
w.timeout(100)

# Initialize the snake
snk_x = sw // 4
snk_y = sh // 2
snake = [
    [snk_y, snk_x],
    [snk_y, snk_x - 1],
    [snk_y, snk_x - 2]
]

# Initialize food
def place_food(obstacles):
    food = [random.randint(1, sh-2), random.randint(1, sw-2)]
    while food in snake or food in obstacles:
        food = [random.randint(1, sh-2), random.randint(1, sw-2)]
    return food

normal_food = place_food([])
special_food = place_food([])

# Initialize obstacles
obstacles = []
num_obstacles = (sh * sw) // 20
while len(obstacles) < num_obstacles:
    if random.choice([True, False]):
        start_x = random.randint(1, sw - 6)
        start_y = random.randint(1, sh - 2)
        for i in range(5):
            obstacles.append([start_y, start_x + i])
    else:
        start_x = random.randint(1, sw - 2)
        start_y = random.randint(1, sh - 6)
        for i in range(5):
            obstacles.append([start_y + i, start_x])

# Main game loop variables
key = curses.KEY_RIGHT
paused = False
normal_food_eaten = 0
special_food_eaten = 0

# Game loop
while True:
    next_key = w.getch()
    key = key if next_key == -1 else next_key

    if key == ord(' '):
        paused = not paused
        continue

    if paused:
        continue

    # Update snake direction
    if key == curses.KEY_DOWN:
        direction = [1, 0]
    elif key == curses.KEY_UP:
        direction = [-1, 0]
    elif key == curses.KEY_LEFT:
        direction = [0, -1]
    elif key == curses.KEY_RIGHT:
        direction = [0, 1]

    new_head = [snake[0][0] + direction[0], snake[0][1] + direction[1]]

    # Screen wrapping
    new_head[0] = (new_head[0] + sh) % sh
    new_head[1] = (new_head[1] + sw) % sw

    # Check collisions
    if new_head in snake or new_head in obstacles:
        break

    # Check food consumption
    if new_head == normal_food:
        normal_food_eaten += 1
        normal_food = place_food(obstacles)
    elif new_head == special_food:
        special_food_eaten += 1
        special_food = place_food(obstacles)
        if len(snake) > 1:
            snake.pop()
    else:
        snake.pop()

    snake.insert(0, new_head)

    # Draw everything
    w.clear()
    for y, x in snake:
        w.addch(y, x, curses.ACS_CKBOARD)
    w.addch(normal_food[0], normal_food[1], 'π')
    w.addch(special_food[0], special_food[1], 'X')
    for y, x in obstacles:
        w.addch(y, x, ' ', curses.A_REVERSE)

    w.refresh()

curses.endwin()
print(f"Game Over! Normal food eaten: {normal_food_eaten}, Special food eaten: {special_food_eaten}")
