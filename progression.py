import random
from engine import play_game


def generate_progression():
    length = random.randint(5, 10)
    start = random.randint(1, 10)
    ratio = random.randint(2, 5)
    progression = [start * (ratio ** i) for i in range(length)]
    hidden_index = random.randint(0, length - 1)
    correct_answer = progression[hidden_index]
    progression[hidden_index] = ".."
    return progression, correct_answer


def play_progression_game():
    play_game(game_logic=generate_progression, game_description="What number is missing in the progression?",
              max_rounds=3)


if __name__ == "__main__":
    play_progression_game()
