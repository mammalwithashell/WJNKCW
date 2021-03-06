from dotsandboxesAI.BoardEnvironment import BoardEnvironment, select_difficulty
from dotsandboxesAI.Agent import Agent


def main():
    """Commandline run of dots and boxes game
    """
    
    board = BoardEnvironment()
    A = Agent(select_difficulty(), board)
    board.set_players(A)
    board.instructions()
    board.play_game()
    
if __name__ == "__main__":
    main()