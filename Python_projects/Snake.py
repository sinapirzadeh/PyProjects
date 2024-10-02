from tkinter import *
from random import randint
from sys import executable, argv
from os import execl


# ---------------------
WITHE = 800
HEIGHT = 800
SPACE_SIZE = 40
SLOWNESS = 300
BADY_SIZE = 2
SNAKE_COLOR = "yellow"
bg_color = "black"
score = 0
direction = "down"
FoodColor = 'red'
# ---------------------
# functions


class Snake:
    def __init__(self) -> None:
        self.body_size = BADY_SIZE
        self.coordinates = []
        self.squares = []
        for _ in range(0, self.body_size):
            self.coordinates.append([0, 0])

        for x, y in self.coordinates:
            square = canvas.create_rectangle(
                x, y, x+SPACE_SIZE, y+SPACE_SIZE, fill=SNAKE_COLOR, tags='snake')
            self.squares.append(square)


class Food:
    def __init__(self) -> None:
        x = randint(0, (WITHE // SPACE_SIZE) - 1) * SPACE_SIZE
        y = randint(0, (HEIGHT // SPACE_SIZE) - 1) * SPACE_SIZE
        self.coordinates = [x, y]
        canvas.create_oval(
            x, y, x+SPACE_SIZE, y+SPACE_SIZE, fill=FoodColor, tags='food')


def next_turn(snake, food):
    x, y = snake.coordinates[0]

    match direction:
        case "up":
            y -= SPACE_SIZE
        case "down":
            y += SPACE_SIZE
        case "left":
            x -= SPACE_SIZE
        case "right":
            x += SPACE_SIZE

    snake.coordinates.insert(0, [x, y])
    square = canvas.create_rectangle(
        x, y, x+SPACE_SIZE, y+SPACE_SIZE, fill=SNAKE_COLOR)
    snake.squares.insert(0, square)

    if x == food.coordinates[0] and y == food.coordinates[1]:
        global score
        score += 1
        label.config(text=f'Score: {score}')
        canvas.delete('food')
        food = Food()
    else:
        del snake.coordinates[-1]
        canvas.delete(snake.squares[-1])
        del snake.squares[-1]

    if check_game_over():
        game_over()
    else:
        window.after(SLOWNESS, next_turn, snake, food)


def check_game_over():
    x, y = snake.coordinates[0]

    if x < 0 or x > WITHE:
        return True
    elif y < 0 or y > HEIGHT:
        return True

    for sq in snake.coordinates[1:]:
        if x == sq[0] and y == sq[1]:
            return True

    return False


def game_over():
    canvas.delete(ALL)
    canvas.create_text(canvas.winfo_width() / 2, canvas.winfo_height() /
                       2, font=("system", 40), text='game over!', fill='#DF1A2F', tags='gameover')


def change_direction(new_dir):
    global direction

    if new_dir == 'left':
        if direction != 'right':
            direction = new_dir
    elif new_dir == 'right':
        if direction != 'left':
            direction = new_dir
    elif new_dir == 'up':
        if direction != 'down':
            direction = new_dir
    elif new_dir == 'down':
        if direction != 'up':
            direction = new_dir


def restartGame():
    path = executable
    execl(path, path, *argv)


# ---------------------
window = Tk()
window.title = 'بازی مار'
window.resizable(False, False)

label = Label(window, text=f'Score:{score}', font=('system', 26))
label.pack()

canvas = Canvas(window, bg=bg_color, width=WITHE, height=HEIGHT)
canvas.pack()

restart = Button(window, text='بازی دوباره', fg='red', command=restartGame)
restart.pack()

window.bind("<Left>", lambda event: change_direction("left"))
window.bind("<Right>", lambda event: change_direction("right"))
window.bind("<Up>", lambda event: change_direction("up"))
window.bind("<Down>", lambda event: change_direction("down"))

snake = Snake()
food = Food()
next_turn(snake, food)

window.update()
window.mainloop()
