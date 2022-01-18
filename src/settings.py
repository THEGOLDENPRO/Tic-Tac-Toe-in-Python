# Screen Res
WIDTH = 600
HEIGHT = 600
SCREEN_RES = (WIDTH, HEIGHT)

# Colours: RGB
RED = (255, 0, 0)

# Theme Colours
UMBER = (101, 82, 77) #Background
RYTHUM = (129, 126, 159) #Lines
ETON_BLUE = (127, 194, 155) #Cross: X
YELLOW_GREEN_CRAYOLA = (181, 239, 138) #Not: O
MINDARO = (215, 241, 113) #Win Line

# Line Settings
class lines:
    width = 15
    colour = RYTHUM

# Board Settings
class board:
    rows = 3
    cols = 3

# Circle Settings
class circle:
    radius = 60
    width = 15

# Cross Settings
class cross:
    width = 25
    space = 55

# Win Line Settings
class win_line:
    width = 15