import random as rand


def main():
    print'''Let's play a game; i will randomly choice a number from 1 to 100,
    and you try to guess it'''
    randomNumber = rand.randint(1, 100)
    gameOn = False
    while not gameOn:
        try:
            userNumber = input("Your guess is: ")
            if userNumber == randomNumber:
                print "You guessed correct, congrats!"
                contGame = raw_input("""That was fun, right?! Do you wanna play again?!
                y for Yes, any other key for No: """)
                if contGame == "y":
                    randomNumber = rand.randint(1, 100)
                    gameOn = False
                else:
                    gameOn = True
            elif userNumber > randomNumber:
                print "guess a little lower!"
            else:
                print "guess a little higher!"
        except(NameError, SyntaxError):
            print "Please enter a number!"
    print "Game Over"


if __name__ == "__main__":
    main()
