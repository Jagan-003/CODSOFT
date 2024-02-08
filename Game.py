import random

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "tie"
    elif (user_choice == "rock" and computer_choice == "scissors") or \
         (user_choice == "scissors" and computer_choice == "paper") or \
         (user_choice == "paper" and computer_choice == "rock"):
        return "user"
    else:
        return "computer"

def display_result(user_choice, computer_choice, result):
    print("\nYour choice:", user_choice)
    print("Computer's choice:", computer_choice)
    if result == "user":
        print("You win! \N{grinning face}")
    elif result == "computer":
        print("Computer wins! \N{pensive face}")
    else:
        print("It's a tie! \N{neutral face}")

def play_game():
    user_score = 0
    computer_score = 0

    while True:
        print("\n" + "="*30)
        print("Welcome to Rock, Paper, Scissors!")
        print("="*30 + "\n")
        
        user_choice = input("Choose rock, paper, or scissors: ").lower()
        while user_choice not in ["rock", "paper", "scissors"]:
            print("Invalid choice. Please choose rock, paper, or scissors.")
            user_choice = input("Choose rock, paper, or scissors: ").lower()

        computer_choice = random.choice(["rock", "paper", "scissors"])
        
        result = determine_winner(user_choice, computer_choice)
        display_result(user_choice, computer_choice, result)

        if result == "user":
            user_score += 1
        elif result == "computer":
            computer_score += 1

        print("\nScores:")
        print("You:", user_score)
        print("Computer:", computer_score)

        play_again = input("\nDo you want to play again? (yes/no): ").lower()
        if play_again != "yes":
            print("\nFinal Scores:")
            print("You:", user_score)
            print("Computer:", computer_score)
            print("\nThanks for playing! See you next time!")
            break

if __name__ == "__main__":
    play_game()
