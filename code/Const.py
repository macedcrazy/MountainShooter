# C
import pygame

C_ORANGE = (255, 128, 0)
C_WHITE = (255, 255, 255)
C_YELLOW = (255, 255, 0)
C_GREEN = (0, 128, 0)
C_CYAN = (0, 128, 128)


# E
ENTITY_DAMAGE = {
    'level1bg0': 0,
    'level1bg1': 0,
    'level1bg2': 0,
    'level1bg3': 0,
    'level1bg4': 0,
    'level1bg5': 0,
    'Player1': 1,
    'Player2': 1,
    'jinn1': 1,
    'Dragon': 1,
    'Demon': 1,
    'Medusa': 1,
    'Player1Shot': 25,
    'Player2Shot': 25,
    'jinn1Shot': 25,
    'DragonShot': 15,
    'DemonShot': 15,
    'MedusaShot': 25,

}
ENTITY_SCORE = {
    'level1bg0': 0,
    'level1bg1': 0,
    'level1bg2': 0,
    'level1bg3': 0,
    'level1bg4': 0,
    'level1bg5': 0,
    'Player1': 0,
    'Player2': 0,
    'jinn1': 100,
    'Dragon': 50,
    'Demon': 50,
    'Medusa': 100,
    'Player1Shot': 0,
    'Player2Shot': 0,
    'jinn1Shot': 0,
    'DragonShot': 0,
    'DemonShot': 0,
    'MedusaShot': 0,

}
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
    'jinn1': 1,
    'Dragon': 1,
    'Demon': 1,
    'Medusa': 1,
    'Player1Shot': 1,
    'Player2Shot': 1,
    'jinn1Shot': 5,
    'DragonShot': 2,
    'DemonShot': 2,
    'MedusaShot': 5,
}



ENTITY_HEALTH = {
    'level1bg0': 999,
    'level1bg1': 999,
    'level1bg2': 999,
    'level1bg3': 999,
    'level1bg4': 999,
    'level1bg5': 999,
    'Player1': 300,
    'Player2': 300,
    'jinn1': 50,
    'Dragon': 60,
    'Demon': 70,
    'Medusa': 100,
    'Player1Shot': 1,
    'Player2Shot': 1,
    'jinn1Shot': 2,
    'DragonShot': 1,
    'DemonShot': 1,
    'MedusaShot': 2,

}

ENTITY_SHOT_DELAY = {
    'Player1': 20,
    'Player2': 15,
    'jinn1': 100,
    'Dragon': 200,
    'Demon': 200,
    'Medusa': 100,

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
PLAYER_KEY_SHOOT = {'Player1': pygame.K_DELETE,
                    'Player2': pygame.K_LCTRL}

# S

SPAW_TIME = 4000

# W
WIN_WIDTH = 576
WIN_HEIGHT = 324
