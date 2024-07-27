import random

print("This is a ROCK-PAPER-SCISSOR game")
print("RULES:")
print("ROCK beats SCISSOR, SCISSOR beats PAPER, PAPER beats ROCK")
print("Enter 1 for ROCK, 2 for SCISSOR, 3 for PAPER")

choose_list = [1, 2, 3]
user_choice = int(input("Enter a choice: "))
machine_choice = random.choice(choose_list)

if user_choice not in choose_list:
    print("Wrong choice")
else:
    choices = {1: "ROCK", 2: "SCISSOR", 3: "PAPER"}
    print(f"You chose {choices[user_choice]}")
    print(f"The machine chose {choices[machine_choice]}")

    if machine_choice == user_choice:
        print("It's a tie!!")
    elif (machine_choice == 1 and user_choice == 2) or (machine_choice == 2 and user_choice == 3) or (machine_choice == 3 and user_choice == 1):
        print("The machine wins. You're a loser.")
    else:
        print("Congrats!! You win.")