'''
THIS PROGRAM IS THE CLASSICAL ROCK-PAPER-SCISSOR GAME DEVELOPED BY- SIDDHARTHA MUKHREJEE
PROGRAMMING LANGUAGE USED IS - PYTHON 3.11.1
IMPORTED LIBRARY IS RANDOM
HOPE YOU LIKE THIS CODE
'''
import random
def game(user_input,computer_input):

    if user_input=='R':
        if computer_input=='P':
            return 0
        elif computer_input=='S':
            return 1
        else:
            return 2

    if user_input=='P':
        if computer_input=='R':
            return 1
        elif computer_input=='S':
            return 0
        else:
            return 2

    if user_input=='S':
        if computer_input=='R':
            return 0
        elif computer_input=='P':
            return 1
        else:
            return 2

print("Welcome to Rock Paper Scissors Game\n")
cont = 'Y'
while cont != 'N':

    user_input= input("User Input (R) Rock (P) Paper (S) Scissors- ")
    print("User Input is - ",user_input)

    computer_ch= random.randint(1,3)
    if computer_ch==1:
        computer_input='R'
    elif computer_ch==2:
        computer_input='P'
    elif computer_ch==3:
        computer_input='S'

    print("Computer Input is - ",computer_input)

    result= game(user_input,computer_input)
    if result==1:
        print("User wins!, computer choice was- ",computer_input)
    elif result==0:
        print("Computer wins!, computer choice was- ",computer_input)
    else:
        print("It's a Tie, computer choice was- ",computer_input)
    cont=  input("Do You Wish to Continue Y/N ?")
