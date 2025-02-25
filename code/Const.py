# C
import pygame

COLOR_ORANGE = (255, 128, 0)
COLOR_WHITE = (255, 255, 255)
COLOR_YELLOW = (255, 255, 0)

# E
EVENT_ENEMY = pygame.USEREVENT + 1
ENTITY_SPEED = {
    'level1bg0': 0,  # Fundo distante, move muito devagar
    'level1bg1': 1,  # Camada mais próxima, move devagar
    'level1bg2': 2,  # Camada intermediária, move um pouco mais rápido
    'level1bg3': 3,  # Camada intermediária mais rápida
    'level1bg4': 4,  # Camada mais rápida
    'level1bg5': 5,  # Camada mais próxima e mais rápida
    'Player1': 3,  # Velocidade Player 1
    'Player2': 3,  # Velocidade Player 2
    'jinn1' :  2,
    'Dragon':  1,
    'Demon' :  1,
    'Medusa':  1,
}


# M
MENU_OPTION = ('NEW GAME 1P',
               'NEW GAME 2P - COOPERATIVE',
               'NEW GAME 2P - COMPETITIVE',
               'SCORE',
               'EXIT')


# P
PLAYER_KEY_UP = {'Player1': pygame.K_UP,
                 'Player2': pygame.K_w}
PLAYER_KEY_DOWN = {'Player1': pygame.K_DOWN,
                 'Player2': pygame.K_s}
PLAYER_KEY_LEFT = {'Player1': pygame.K_LEFT,
                 'Player2': pygame.K_a}
PLAYER_KEY_RIGHT = {'Player1': pygame.K_RIGHT,
                 'Player2': pygame.K_d}
PLAYER_KEY_SHOOT = {'Player1': pygame.K_RCTRL,
                 'Player2': pygame.K_LCTRL}

# S

SPAW_TIME = 4000





# W
WIN_WIDTH = 576
WIN_HEIGHT = 324
