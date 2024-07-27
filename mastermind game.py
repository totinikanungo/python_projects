def accept_num(player_id):
    while True:
        num = input(f"Enter the number, {player_id}: ")
        if num.isdigit() and len(num) >= 2:
            return num
        else:
            print("Invalid input.Please enter a valid number.")

def guessing_num(player_id , num):
    while True:
        guessed = input(f"Enter your guess, {player_id}: ")
        if guessed.isdigit() and len(guessed) >= 2 and len(num)==len(guessed):
            return guessed
        else:
            print("Invalid input.Please enter a valid guess.")

def hint_number(num, guess):
    hint = ""
    print("X means the element is present in the same index, O means the element is present but in a different index, - means the element is not present.")
    for i in range(len(num)):
        if num[i] == guess[i]:
            hint += "X"
        elif guess[i] in num:
            hint += "O"
        else:
            hint += "-"
    return hint

def gameplay(player1_id, player2_id):
    num1 = accept_num(player1_id)
    player2_guess = 0
    print(f"{player1_id} has entered the number.")
    
    
    while True:
        guess = guessing_num(player2_id , num1) 
        player2_guess += 1
        if num1 == guess:
            print("Congrats!! You have guessed the number.")
            break
        else:
            print("Hint:", hint_number(num1, guess))
    
    num2 = accept_num(player2_id)
    player1_guess = 0
    print(f"{player2_id} has entered the number.")
    
    while True:
        guess = guessing_num(player1_id , num2)
        player1_guess += 1
        if num2 == guess:
            print("Congrats!! You have guessed the number.")
            break
        else:
            print("Hint:", hint_number(num2, guess))

    if player1_guess < player2_guess:
        print(f"{player1_id} wins.")
    elif player2_guess < player1_guess:
        print(f"{player2_id} wins.")
    else:
        print("It's a tie!")

player1_id = input("Enter the name of player1: ")
player2_id = input("Enter the name of player2: ")
print(f"{player1_id} is setting the number and {player2_id} is guessing it")
gameplay(player1_id, player2_id)