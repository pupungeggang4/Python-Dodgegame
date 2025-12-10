from game.gamehandler import GameHandler
from game.gamevar import GameVar

if __name__ == '__main__':
    game_var = GameVar()
    game_handler = GameHandler()
    game_handler.run(game_var)
