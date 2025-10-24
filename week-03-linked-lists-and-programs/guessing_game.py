from random import randint

def computer_guess(attempts, numrange):
    """
    A guessing game where the computer tries to guess
    a randomly chosen secret number using a binary search strategy.
    """
    
    # Step 1: The secret number is chosen randomly.
    number = randint(1, numrange)
    print("Welcome! The computer will try to guess the secret number.")
    print(f"The number is between 1 and {numrange}.")
    print(f"The computer has {attempts} guesses to find it.\n")
    
    # Step 2: Define the search range.
    low = 1
    high = numrange

    # Step 3: Loop for each attempt.
    while attempts > 0:
        # The computer guesses the midpoint.
        guess = (low + high) // 2
        print(f"Computer guesses: {guess}")
        
        # Step 4: Compare guess with the secret number.
        if guess == number:
            print("✅ Correct! The computer guessed the number!")
            print(f"Secret number was: {number}")
            print("GAME OVER: success!\n")
            return
        
        elif guess < number:
            print("Too low.")
            low = guess + 1  # Move the lower bound up.
            
        else:
            print("Too high.")
            high = guess - 1  # Move the upper bound down.
        
        # Step 5: Reduce remaining attempts.
        attempts -= 1
        print(f"Guesses remaining: {attempts}\n")
    
    # If loop finishes, computer ran out of attempts.
    print("❌ No more guesses — bad luck!")
    print(f"The secret number was {number}.")
    print("GAME OVER: thanks for playing.\n")
