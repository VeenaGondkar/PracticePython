import random
class Player(object):

    def __init__(self):
        self.hand = []

    def human_move(self):
        while True:
            print("rock (r), paper (p), scissors(s)")
            choice = input("Make Your Move: ")
            choice = choice.strip()
            if choice == "r" or choice == "rock":
                return 1
            if choice == "p" or choice == "paper":
                return 2
            if choice == "s" or choice == "scissors":
                return 3

    def computer_move(self):
        return random.randint(1,3)

class RPS():
    def __init__(self):
        self.cScore = 0  # computer score
        self.hScore = 0  # player score

    def decide_winner(self, m, p):
        """"
        rock breaks scissors
        paper covers rock
        scissors cuts paper
        """
        if (m, p) == (1, 3):
            print("rock breaks scissors")
            print("Computer Wins")
            self.cScore += 1
        elif (p, m) == (1, 3):
            print("rock breaks scissors")
            print("You Win")
            self.hScore += 1
        elif (m, p) == (2, 1):
            print("paper covers rock")
            print("Computer Wins")
            self.cScore += 1
        elif (p, m) == (2, 1):
            print("paper covers rock")
            print("You Win")
            self.hScore += 1
        elif (m, p) == (3, 2):
            print("scissors cuts paper")
            print("Computer Wins")
            self.cScore += 1
        elif (p, m) == (3, 2):
            print("scissors cuts paper")
            print("You Win")
            self.hScore += 1
        else:
            print("Tie!")

    def display_score(self):
        print("Score:")
        print("Computer: ", self.cScore, " You: ", self.hScore ,"\n")

    def playAgain(self):
        yn = input("Play Again? (y/n): ")
        yn = yn.strip()
        yn = yn.lower()
        if yn == "n" or yn == "no":
            print("Final Scores:")
            print("Computer: ", self.cScore, " You: ", self.hScore)
            if self.hScore > self.cScore:
                print("Congrats! You won the game")
            elif self.hScore == self.cScore:
                print("This was a tie")
            else:
                print("Sorry! Computer won the game")
            return False
        return True

    def gameLoop(self):
        while True:
            print("Welcome to Rock, Paper, Scissors game")
            print("-" * 26)

            player = Player()
            computer_move = player.computer_move()
            human_move = player.human_move()

            print("\nYou chose: ", human_move, " Computer chose: ", computer_move)
            self.decide_winner(computer_move, human_move)
            self.display_score()
            if self.playAgain() == False:
                return
            print("\n")

if __name__ == "__main__":
    game = RPS()
    game.gameLoop()