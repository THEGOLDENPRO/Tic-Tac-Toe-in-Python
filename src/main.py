import time
import pygame, sys, numpy
import settings

from game import board, render
from audio import sound

pygame.init()

screen = pygame.display.set_mode((settings.SCREEN_RES))
pygame.display.set_caption("Tic Tac Toe")

game_board = board(rows=settings.board.rows, cols=settings.board.cols, screen=screen)
player = 1
game_over = False

def restart(): # Restart the game.
    global game_board, player, game_over
    sound.play("restart.mp3", vol=1.0)
    screen.fill(settings.UMBER)
    render.draw_table(screen, colour=settings.lines.colour, width=settings.lines.width)

    game_board = board(rows=settings.board.rows, cols=settings.board.cols, screen=screen)
    player = 1
    game_over = False

# Start Game
screen.fill(settings.UMBER)
render.draw_table(screen, colour=settings.lines.colour, width=settings.lines.width)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        if event.type == pygame.MOUSEBUTTONDOWN: #Runs when mouse is clicked.
            x_cods = event.pos[0]
            y_cods = event.pos[1]

            clicked_row = int(y_cods // 200)
            clicked_col = int(x_cods // 200)

            if game_board.square.is_available(clicked_row, clicked_col) and game_over == False:
                if player == 1:
                    game_board.square.mark(clicked_row, clicked_col, player=1)
                    sound.play("1st_player_place.mp3")
                    if game_board.check_win(player):
                        audio = sound.play("win_place_effect.mp3")
                        time.sleep(audio.get_length())
                        game_over = True
                    player = 2

                elif player == 2:
                    game_board.square.mark(clicked_row, clicked_col, player=2)
                    sound.play("2nd_player_place.mp3")
                    if game_board.check_win(player):
                        audio = sound.play("win_place_effect.mp3")
                        time.sleep(audio.get_length())
                        game_over = True
                    player = 1

                render.draw_figures(screen, board=game_board)
                game_board.print()

        # Runs when game is over.
        if game_over == True:
            game_over = None

            sound.play("win_sound.mp3")

            
        if event.type == pygame.KEYDOWN: # When "R" key is pressed the game restarts.
            if event.key == pygame.K_r:
                restart()

    pygame.display.update()