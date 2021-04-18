
import random
import pyttsx3

speak= pyttsx3.init()
# speech = input("Enter text to speak >")

game = ["\U00002702 scissors" ,"\U0001F4C4 paper", "\U0001F9F1 rock" ]
speak.say("scissors paper rock")
speak.runAndWait()

keep_playing = "true"
while keep_playing == "true":
    cmove = random.choice(game)
    pmove = input("What is your game: scissors, paper or rock?")
    print("the computer choose", cmove)
    if cmove == pmove:
        print("Tie")
    elif pmove == "scissors" and cmove== "rock":
        print("players wins")
    elif pmove== "scissors" and cmove== "paper":
        print("computer wins")
    elif pmove== "papers" and  cmove== "rock":
        print("computer wins")
    elif pmove== "papers" and cmove== "scissors":
        print("computer wins")
    elif pmove== "rock" and cmove== "paper":
        print("players wins")
    elif pmove== "rock" and cmove== "rock":
        print("players wins")   


