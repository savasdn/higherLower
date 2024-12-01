from game_data import data
import random
from art import logo, vs


def format_data(account):
    account_name = account["name"]
    account_descr = account["description"]
    account_country = account["country"]
    return f"{account_name}, a {account_descr}, from {account_country}"

def check_answer(user_guess, followers_a, followers_b):
    if followers_a > followers_b:             # if follower_a > follower_b:     Same result.
        if user_guess == "a":                   # return user_guess == "a"
            return True                       # else:
        else:                                   # return user_guess == "b"
            return False
    else:
        if user_guess == "b":
            return True
        else:
            return False

score = 0
game_should_continue = True
account_b = random.choice(data)

print(logo)

while game_should_continue:
    account_a = account_b
    account_b = random.choice(data)
    if account_a == account_b:
        account_b = random.choice(data)

    print(f"Compare A: {format_data(account_a)}")
    print(vs)
    print(f"Against B: {format_data(account_b)}")

    guess = input("Who has more followers? Type 'A' or 'B': ")
    print("\n" * 20)
    print(logo)

    followers_a_count = account_a["follower_count"]
    followers_b_count = account_b["follower_count"]
    is_correct = check_answer(guess, followers_a_count, followers_b_count)

    if is_correct:
        score += 1
        print(f"You are right! Current score: {score}")
    else:
        print(f"Sorry. That's wrong. Final score: {score}")
        game_should_continue = False