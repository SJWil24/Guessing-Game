# 1
import random
from analyticskit import *
while True:
    secret_number = random.randint(1,10)
    guess = single_input("Guess a number between 1 and 10.")
    if secret_number == guess:
        show_message("Winner!","You win! You guessed the correct number.")
    else:
        show_message("Loser :(",f"You lose. The correct number was {secret_number}.")
    play_again = single_input("Would you like to play again? Enter Y or N.")
    if play_again.strip().lower()[0] != "y":
        break