import random

def get_user_choice():
    choices = ['rock', 'paper', 'scissors']
    while True:
        user_input = input("Enter your choice (rock, paper, scissors): ").lower()
        if user_input in choices:
            return user_input
        else:
            print("Invalid choice. Please choose rock, paper, or scissors.")

def get_computer_choice():
    choices = ['rock', 'paper', 'scissors']
    return random.choice(choices)

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "tie"
    elif (user_choice == 'rock' and computer_choice == 'scissors') or \
         (user_choice == 'scissors' and computer_choice == 'paper') or \
         (user_choice == 'paper' and computer_choice == 'rock'):
        return "user"
    else:
        return "computer"

def main():
    user_score = 0
    computer_score = 0
    print("Welcome to Rock-Paper-Scissors Game!")
    while True:
        user_choice = get_user_choice()
        computer_choice = get_computer_choice()
        print(f"You chose: {user_choice}")
        print(f"Computer chose: {computer_choice}")

        winner = determine_winner(user_choice, computer_choice)
        if winner == "tie":
            print("It's a tie!")
        elif winner == "user":
            print("You win!")
            user_score += 1
        else:
            print("Computer wins!")
            computer_score += 1

        print(f"Score -> You: {user_score} | Computer: {computer_score}")

        play_again = input("Do you want to play another round? (yes/no): ").lower()
        if play_again != 'yes':
            print("Thanks for playing! Final Score:")
            print(f"You: {user_score} | Computer: {computer_score}")
            break

if __name__ == "__main__":
    main()
