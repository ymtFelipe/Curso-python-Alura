import forca
import adivinhacao

def choice_game():
    print("*********************************")
    print("*******Choice your game!*******")
    print("*********************************")

    print("(1) Hangman (2) Guessing")

    game = int(input("Which game? "))

    if(game == 1):
        print("Playing hangman.")
        forca.play()
    elif(game == 2):
        print("Playing guessing")
        adivinhacao.play()

if(__name__ == "__main__"):
    choice_game()
