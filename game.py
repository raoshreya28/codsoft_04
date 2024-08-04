import random

def get_computer_choice():
    """Generate a random choice for the computer."""
    choices = ['rock', 'paper', 'scissors']
    return random.choice(choices)

def determine_winner(user_choice, computer_choice):
    """Determine the winner of the game based on user and computer choices."""
    if user_choice == computer_choice:
        return 'tie'
    elif (user_choice == 'rock' and computer_choice == 'scissors') or \
         (user_choice == 'scissors' and computer_choice == 'paper') or \
         (user_choice == 'paper' and computer_choice == 'rock'):
        return 'win'
    else:
        return 'lose'

def play_game():
    """Play a single round of Rock-Paper-Scissors."""
    # Get user's choice
    user_choice = input("Enter rock, paper, or scissors: ").lower()
    
    # Validate user choice
    if user_choice not in ['rock', 'paper', 'scissors']:
        print("Invalid choice. Please select rock, paper, or scissors.")
        return None, None
    
    # Get computer's choice
    computer_choice = get_computer_choice()
    
    # Determine the winner
    result = determine_winner(user_choice, computer_choice)
    
    # Display choices and result
    print(f"\nYour choice: {user_choice}")
    print(f"Computer's choice: {computer_choice}")
    
    if result == 'tie':
        print("It's a tie!")
    elif result == 'win':
        print("You win!")
    else:
        print("You lose!")
    
    return result

def main():
    user_score = 0
    computer_score = 0

    print("Welcome to Rock-Paper-Scissors!")

    while True:
        result = play_game()
        
        # Update scores based on the result
        if result == 'win':
            user_score += 1
        elif result == 'lose':
            computer_score += 1

        # Display the current scores
        print(f"\nScore - You: {user_score} | Computer: {computer_score}")

        # Ask if the user wants to play another round
        play_again = input("\nDo you want to play again? (yes/no): ").lower()
        if play_again != 'yes':
            print("Thanks for playing!")
            break

if __name__ == "__main__":
    main()
