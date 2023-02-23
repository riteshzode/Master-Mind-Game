import random

COLORS = list("ABCDEF")  # color = "RGBYWO" ir red green blue etc
TRIES = 10
CODE_LENGTH = 4


def generate_color():
    return [random.choice(COLORS) for _ in range(CODE_LENGTH)]


def guess():
    while True:
        user_input = input("Guess the correct position of colors: ").upper().split(" ")

        if len(user_input) == CODE_LENGTH:

            for word in user_input:
                if word not in COLORS:
                    print(f"Invalid {word}, Try again !")
                    break
            else:
                break
        else:

            print(f"The length of guess must be {CODE_LENGTH}")
            continue
    return user_input


def check_guess(user_guess, generated_color):
    color_dict = {}
    correct_pos = 0
    incorrect_pos = 0

    for color in generated_color:
        if color not in color_dict:
            color_dict[color] = 1
        else:
            color_dict[color] += 1

        # if color not in color_dict:
        #     color_dict[color] = 0
        # color_dict[color] += 1
     

    for i, j in zip(user_guess, generated_color):
        if i == j:
            color_dict[i] -= 1
            correct_pos += 1

    for i, j in zip(user_guess, generated_color):
        if i in generated_color and color_dict[i] > 0:
            color_dict[i] -= 1
            incorrect_pos += 1

    return correct_pos, incorrect_pos


def game():
    print(f"Welcome to the Master Mind Game You have {TRIES} to guess the code...")
    print(f"The Valid Colors are {COLORS}")
    print()

    colr = generate_color()
    print(f"The correct Answer : {colr}")

    for attempt in range(TRIES):
        print(f"No of attempt remaining: {TRIES - attempt}")
        user = guess()
        correct, incorrect = check_guess(user_guess=user, generated_color=colr)

        if correct == CODE_LENGTH:
            print(f"You guessed the code in {attempt + 1} tries!")
            break

        print(f"Correct position: {correct}, Incorrect position: {incorrect}")
    else:

        print(f"you run out of tries. The code was: {colr} ")


if __name__ == "__main__":
    game()
