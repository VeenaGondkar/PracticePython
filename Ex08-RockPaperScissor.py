'''
Make a two-player Rock-Paper-Scissors game. (Hint: Ask for player plays (using input), compare them, print out a message of congratulations to the winner, and ask if the players want to start a new game)

Remember the rules:

    Rock beats scissors
    Scissors beats paper
    Paper beats rock

    1 < 2 , player 1 is winner, else player 2 is winner
    2 < 3, player 1 is winner, else player 2 is winner
    3 < 1, player 1 is winner, else player 2 is winner

'''

# rock = 1
# scissor = 2
# paper = 3
#
#
# while (True):
#     print "Enter a number to Play Rock Paper Scissor"
#     print "Rock = 1 \nScissor = 2 \nPaper - 3"
#     player1 = input("Player 1 - Enter a number")
#     player2 = input("Player 2 - Enter a number")
#
    # if player1 == player2:
    #     print "both are winner"
    # elif (player1 == 1 and player1 < player2):
    #     print "player 1 is winner"
    # elif (player1 == 2 and player1 < player2):
    #     print "player 1 is winner"
    # elif (player1 == 3 and player1 < player2):
    #     print "player 1 is winner"
    # else:
    #     print "player 2 is winner"
    #

import random
def rand(argument):
    comp={0:'rock',1:'paper',2:'scissors'}
    return comp.get(argument, "nothing")

while 1:
    user=input('place your bet (rock paper or scissors)')
    x=rand(random.randint(0,2))
    print(f"you picked {user}")
    print("computer picked ", x)
    if user==x:
        print('------------draw------------')
    elif (user=='rock' and x=='scissors') or (user=='paper' and x=='rock') or (user == 'scissors' and x=='paper'):
        print('-------------you win------------')
    else:
        print('-----------you lose-----------')

    user=input('do you want to play again? Y/N')
    if user.lower() == 'y':
        pass
    else:
        break