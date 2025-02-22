#!/usr/bin/python
# -*- coding: utf-8 -*-
from lib2to3.pytree import convert

import pygame.image
from pygame import Surface, Rect
from pygame.font import Font

from code.Const import WIN_WIDTH, COLOR_ORANGE, MENU_OPTION, COLOR_WHITE, COLOR_YELLOW


class Menu:
    def __init__(self, window):
        self.window = window
        self.surf = pygame.image.load('./assets/menubg.png')
        self.rect = self.surf.get_rect(left=0, top=0)

    def run(self, ):
        menu_option = 0
        pygame.mixer_music.load('./assets/menuSound.mp3')
        pygame.mixer_music.play(-1)
        while True:
            #Draw Images
            self.window.blit(source=self.surf, dest=self.rect)
            self.menu_text(50, 'CITY', COLOR_ORANGE, ((WIN_WIDTH / 2), 70))
            self.menu_text(50, 'INVASION', COLOR_ORANGE, ((WIN_WIDTH / 2), 120))

            for i in range(len(MENU_OPTION)):
                if i == menu_option:
                    self.menu_text(20, MENU_OPTION[i], COLOR_YELLOW, ((WIN_WIDTH / 2), 200 + 20 * i))
                else:
                    self.menu_text(20, MENU_OPTION[i], COLOR_WHITE, ((WIN_WIDTH / 2), 200 + 20 * i))
            pygame.display.flip()

            # Check for all events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()  # close window
                    quit()  # end pygame
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_DOWN: # down key
                        if menu_option < len(MENU_OPTION) - 1:
                            menu_option += 1
                        else:
                            menu_option = 0
                    if event.key == pygame.K_UP: # up key
                        if menu_option > 0:
                            menu_option -= 1
                        else:
                            menu_option = len(MENU_OPTION) - 1
                    if event.key == pygame.K_RETURN:  # Enter
                        return MENU_OPTION[menu_option]





    def menu_text(self, text_size: int, text: str, text_color: tuple, text_center_pos: tuple):
        # Criar a fonte
        text_font: Font = pygame.font.SysFont(name='Lucida Sans Typewriter', size=text_size)
        # Renderizar o texto
        text_surf = text_font.render(text, True, text_color).convert_alpha()
        # Obter o retângulo para centralizar o texto
        text_rect: Rect = text_surf.get_rect(center=text_center_pos)
        # Exibir o texto na tela
        self.window.blit(source=text_surf, dest=text_rect)
