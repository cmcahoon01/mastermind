from game import Game


def main():
    solution = ["red", "green", "blue", "yellow"]
    game = Game(solution)
    while not game.is_solved():
        guess = [input(f"color {i+1}: ") for i in range(len(solution))]
        print("you guessed:", guess)
        black, white = game.guess(guess)
        print("black:", black, "white:", white)
    print("you won!")


if __name__ == '__main__':
    main()
