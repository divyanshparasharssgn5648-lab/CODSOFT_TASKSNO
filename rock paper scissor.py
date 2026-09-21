import random

def rps_game():
    print("-----------------------------------")
    print("     ROCK - PAPER - SCISSORS       ")
    print("-----------------------------------")
    
    choices = ["rock", "paper", "scissors"]
    user_score = 0
    computer_score = 0

    while True:
        user_choice = input("Choose rock, paper, or scissors (or type 'quit' to exit): ").lower()

        if user_choice == 'quit':
            print(f"\nFinal Scores -> You: {user_score} | Computer: {computer_score}")
            print("Thanks for playing!")
            break

        if user_choice not in choices:
            print("Invalid choice! Please choose rock, paper, or scissors.\n")
            continue

        computer_choice = random.choice(choices)

        print(f"Your choice: {user_choice}")
        print(f"Computer's choice: {computer_choice}")

        if user_choice == computer_choice:
            print("It's a tie!\n")
        elif (user_choice == "rock" and computer_choice == "scissors") or \
             (user_choice == "scissors" and computer_choice == "paper") or \
             (user_choice == "paper" and computer_choice == "rock"):
            print("You win this round!\n")
            user_score += 1
        else:
            print("Computer wins this round!\n")
            computer_score += 1

        print(f"Current Score -> You: {user_score} | Computer: {computer_score}\n")

if __name__ == "__main__":
    rps_game()