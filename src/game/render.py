import pygame

import settings

def draw_table(screen, colour, width):
    #Horizontal Lines
    pygame.draw.line(screen, color=colour, start_pos=(0, 200), end_pos=(600, 200), width=width)
    pygame.draw.line(screen, color=colour, start_pos=(0, 400), end_pos=(600, 400), width=width)

    #Vertical Lines
    pygame.draw.line(screen, color=colour, start_pos=(200, 0), end_pos=(200, 600), width=width)
    pygame.draw.line(screen, color=colour, start_pos=(400, 0), end_pos=(400, 600), width=width)

def draw_figures(screen, board):
    for row in range(settings.board.rows):
        for col in range(settings.board.cols):
            if board.get()[row][col] == 1: #Draw Circle
                pygame.draw.circle(screen, color=settings.YELLOW_GREEN_CRAYOLA, center=(int(col * 200 + 100), int(row * 200 + 100)), radius=settings.circle.radius, width=settings.circle.width)

            elif board.get()[row][col] == 2: #Draw Cross
                #First Line
                pygame.draw.line(screen, color=settings.ETON_BLUE, 
                start_pos=(col * 200 + settings.cross.space, row * 200 + 200 - settings.cross.space), 
                end_pos=(col * 200 + 200 - settings.cross.space, row * 200 + settings.cross.space), 
                width=settings.cross.width)

                #Secound Line
                pygame.draw.line(screen, color=settings.ETON_BLUE, 
                start_pos=(col * 200 + settings.cross.space, row * 200 + settings.cross.space), 
                end_pos=(col * 200 + 200 - settings.cross.space, row * 200 + 200 - settings.cross.space), 
                width=settings.cross.width)

def draw_vertical_winning_line(screen, col, player):
    pos_x = col * 200 + 100

    if player == 1: colour = settings.ETON_BLUE
    elif player == 2: colour = settings.YELLOW_GREEN_CRAYOLA

    pygame.draw.line(screen, color=colour, start_pos=(pos_x, 15), end_pos=(pos_x, settings.HEIGHT - 15), width=settings.win_line.width)

def draw_horizontal_winning_line(screen, row, player):
    pos_y = row * 200 + 100

    if player == 1: colour = settings.ETON_BLUE
    elif player == 2: colour = settings.YELLOW_GREEN_CRAYOLA

    pygame.draw.line(screen, color=colour, start_pos=(15, pos_y), end_pos=(settings.WIDTH - 15, pos_y), width=settings.win_line.width)

def draw_asc_diagonal(screen, player):
    if player == 1: colour = settings.ETON_BLUE
    elif player == 2: colour = settings.YELLOW_GREEN_CRAYOLA

    pygame.draw.line(screen, color=colour, start_pos=(15, settings.HEIGHT - 15), end_pos=(settings.WIDTH - 15, 15), width=settings.win_line.width)

def draw_desc_diagonal(screen, player):
    if player == 1: colour = settings.ETON_BLUE
    elif player == 2: colour = settings.YELLOW_GREEN_CRAYOLA

    pygame.draw.line(screen, color=colour, start_pos=(15, 15), end_pos=(settings.WIDTH - 15, settings.HEIGHT - 15), width=settings.win_line.width)