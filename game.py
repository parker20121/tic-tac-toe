from board import Board
from random_player import RandomPlayer

import random


class Game:

    TOTAL_GAMES = 1000
    REWARD_WIN = 100
    REWARD_LOSS = -100
    REWARD_NONE = 0

    def __init__(self):
        return

    def play(self):

        playerX = RandomPlayer('x')
        playerO = RandomPlayer('o')

        games_played = 0
        games_tied = 0

        board = Board()
        players = [playerX, playerO]

        while games_played < Game.TOTAL_GAMES:

            playerX.reset()
            playerO.reset()
            board.reset()

            current_player = random.choice( players )

            while True:
                player = players[ current_player ]
                open_moves = board.empty_positions()

                if not open_moves:
                    games_tied += 1
                    playerO.tied_game()
                    playerO.learn( Game.REWARD_NONE )

                    playerX.tied_game()
                    playerX.learn( Game.REWARD_NONE )
                    break

                next_move = player.next_move( board )
                board.move( player, next_move )
                winner = board.has_winner()

                if winner:
                    player.won_game()
                    player.learn( Game.REWARD_WIN )

                    losing_player = players[ self.other_player(current_player) ]
                    losing_player.lost_game()
                    losing_player.learn( Game.REWARD_LOSS )

                    break

                current_player = self.other_player( current_player )

            games_played += 1

        print "Done.\n"

        print playerX.stats()
        print playerO.stats()

    def other_player(self, current_player):
        return (current_player + 1) % 2
