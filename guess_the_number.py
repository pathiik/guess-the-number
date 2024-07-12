import random

# Getting the user's choice of mode
def choice_input() -> int:
    try:
        choice = input("\nChoose a mode:\n1. Human Guess (H)\n2. Compute Guess (C)\n-> ")
        if choice == '1' or choice.lower() == 'h':
            return 1
        elif choice == '2' or choice.lower() == 'c':
            return 2
        else:
            print("Invalid input. Please enter 'H' or '1' for Human and 'C' or '2' for Computer")
            return choice_input()
    except Exception as e:
        print(f"An Error Occured {e}")
        return choice_input()
        
# Getting the range of numbers to guess from
def range_input() -> int:
    try:
        lowerLimit = int(input("\nEnter the lower limit: "))
        upperLimit = int(input("Enter the upper limit: "))

        if lowerLimit > upperLimit:
            print("Lower range must be less than upper range")
            return range_input()
        elif lowerLimit == upperLimit:
            print("Lower range and upper range cannot be the same")
            return range_input()
    except ValueError:
        print("Range must be an integer")
        return range_input()
    except Exception as e:
        print(f"An Error Occured {e}")
        return range_input()
    else:
        return lowerLimit, upperLimit

# Human Guess mode 
def human_guess():
    lowerLimit, upperLimit = range_input()
    random_number = random.randint(lowerLimit, upperLimit)
    print(random_number)
    guess = None
    count = 0
    
    while guess != random_number:
        try:
            guess = int(input("\nEnter your guess: "))
            count += 1
            closeGuessLow = random_number - 10
            closeGuessHigh = random_number + 10
            if guess < random_number:
                if guess >= closeGuessLow:
                    print("Close! Guess a little higher")
                else:
                    print("Your guess is too low")
            elif guess > random_number:
                if guess <= closeGuessHigh:
                    print("Close! Guess a little lower")
                else:
                    print("Your guess is too high")
            else:
                print(f"\nCongratulations! You guessed the number in {count} tries")
                break
        except ValueError:
            print("Guess must be an integer\nRestarting...")
            human_guess()
        except Exception as e:
            print(f"An Error Occured {e}\nRestarting...")
            human_guess()
        else:
            continue

# Computer Guess mode
def computer_guess():
    lowerLimit, upperLimit = range_input()
    guess = random.randint(lowerLimit, upperLimit)
    count = 0
    status = ''
    
    while status != 'c':
        print(f"\nIs {guess} your number?")
        status = input("Enter 'h' if it's too high, 'l' if it's too low, 'c' if it's correct: ").lower()
        count += 1
        if status == 'h':
            upperLimit = guess
            guess = random.randint(lowerLimit, upperLimit)
        elif status == 'l':
            lowerLimit = guess
            guess = random.randint(lowerLimit, upperLimit)
        elif status == 'c':
            print(f"\nCongratulations! The computer guessed the number in {count} tries")
        else:
            print("Invalid input. Please enter 'h', 'l' or 'c'")
            count -= 1
        
# Main function
def main():
    choice = choice_input()
    match choice:
        case 1:
            human_guess()
        case 2:
            computer_guess()
        case _:
            print("ERROR!")
    
    playAgain = input("\nDo you want to play again? (Y/N): ").lower()
    if playAgain == 'y':
        main()
    else:
        print("Goodbye!")
        exit()

if __name__ == "__main__":
    main()
