#!/usr/bin/python
# -*- coding: utf-8 -*-
from lib2to3.pytree import convert

import pygame.image
from pygame import Surface, Rect
from pygame.font import Font

from code.Const import WIN_WIDTH, COLOR_ORANGE, MENU_OPTION, COLOR_WHITE


class Menu:
    def __init__(self, window):
        self.window = window
        self.surf = pygame.image.load('./assets/menuBg.png')
        self.rect = self.surf.get_rect(left=0, top=0)

    def run(self, ):
        pygame.mixer_music.load('./assets/menuSound.mp3')
        pygame.mixer_music.play(-1)
        while True:
            self.window.blit(source=self.surf, dest=self.rect)
            self.menu_text(50, 'CITY', COLOR_WHITE,( (WIN_WIDTH/ 2), 70 ))
            self.menu_text(50, 'INVASION', COLOR_WHITE, ((WIN_WIDTH / 2), 120))

            for i in range(len(MENU_OPTION)):
                self.menu_text(20, MENU_OPTION[i], COLOR_WHITE, ((WIN_WIDTH / 2), 200 + 20 * i))




            pygame.display.flip()

           # Check for all events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()  # close window
                    quit()  # end pygame


    def menu_text(self, text_size: int, text: str, text_color: tuple, text_center_pos: tuple):
        # Criar a fonte
        text_font: Font = pygame.font.SysFont(name= 'Lucida Sans Typewriter', size=text_size)
        # Renderizar o texto
        text_surf = text_font.render(text, True, text_color).convert_alpha()
        # Obter o retângulo para centralizar o texto
        text_rect: Rect = text_surf.get_rect(center=text_center_pos)
        # Exibir o texto na tela
        self.window.blit(source=text_surf, dest=text_rect)

