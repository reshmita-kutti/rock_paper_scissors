import time
import random
from colorama import Fore
from visuals import choices_art


def display_choices(user_choice, comp_choice):
    print("You chose:                           Computer chose:")
    user_art_lines = choices_art[user_choice].split('\n')
    comp_art_lines = choices_art[comp_choice].split('\n')
    for ua, ca in zip(user_art_lines, comp_art_lines):
        print(f"{ua:35} {ca}")


def display_result(result):
    print(result)


def display_score(scores):
    print(f"\n{Fore.CYAN}Score: You {scores['user']} - {scores['computer']} Computer\n")


def play_rps(user_choice, scores):
    print("You chose:")
    print(choices_art[user_choice])
    time.sleep(1)

    comp_choice = random.randint(0, 2)
    display_choices(user_choice, comp_choice)

    if user_choice == comp_choice:
        result = f"{Fore.YELLOW}You've drawn."
    elif (user_choice - comp_choice) % 3 == 1:
        result = f"{Fore.GREEN}You've won!"
        scores['user'] += 1
    else:
        result = f"{Fore.RED}You've lost."
        scores['computer'] += 1

    display_result(result)
    display_score(scores)
    return scores
