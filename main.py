from game import Game
from solver import Solver
import time
from random import choices

colors = ["red", "green", "blue", "yellow", "white", "black"]


def human():
    solution = colors[:4]
    game = Game(solution)
    while not game.is_solved():
        guess = [input(f"color {i + 1}: ") for i in range(len(solution))]
        print("you guessed:", guess)
        black, white = game.guess(guess)
        print("black:", black, "white:", white)
    print("you won!")


def bot():
    size = 4
    solution = choices(colors, k=size)
    print("solution:", solution)
    game = Game(solution)
    solver = Solver(game, colors, size=size, forced_guess = True)
    while not game.is_solved():
        guess, result = solver.guess()
        print("bot guessed:", guess, "and got:", result, "Remaining_options:", len(solver.remaining_combinations))
        # print("remaining:", solver.remaining_combinations)
        time.sleep(1)
    print("bot won!")


def bot_vs_human():
    size = 4
    print("COLORS ARE:", end=" ")
    for color in colors:
        print(color, end=" ")
    print()
    time.sleep(3)
    print("Enter your color code:")
    time.sleep(1)
    solution = [input(f"color {i + 1}: ") for i in range(size)]
    game = Game(solution)
    solver = Solver(game, colors, size=size)

    print("Thinking...")
    turns = 0
    while not game.is_solved():
        guess, result = solver.guess()
        print("bot guessed:", end=" ")
        for color in guess:
            print(color, end=" ")
        print()
        time.sleep(5)
        print("This gets:", result[0], "black pips and", result[1], "white pips")
        if not game.is_solved():
            prompt = "\t(press enter to continue)"
            input(prompt).lower()
        turns += 1
    print("the bot won in", turns, "turns!")


if __name__ == '__main__':
    bot_vs_human()
