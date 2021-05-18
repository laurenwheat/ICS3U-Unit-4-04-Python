#!/usr/bin/env python3

# Created by: Lauren Wheatley
# Created on: May 2021
# This program plays the number guessing game

import constants
import random


def main():

    loop_counter = 0
    randomnumber = random.randint(constants.minimum, constants.maximum)

    while True:
        user_guess = input("Enter a number 1-10: ")

        try:
            user_guess_int = int(user_guess)

            if user_guess_int >= 0 and user_guess_int <= 9:
                loop_counter = loop_counter + 1

                if user_guess_int == randomnumber:
                    break
                elif user_guess_int > randomnumber:
                    print("Too high")
                elif user_guess_int < randomnumber:
                    print("Too low")
                else:
                    print("I dont know!")
            else:
                print("Guess must be between 1 and 10")

        except Exception:
            print("That is not a valid input!!!!!")

    print("Correct! it took you {0} tries!".format(loop_counter))
    print("Thanks for playing <3")


if __name__ == "__main__":
    main()
