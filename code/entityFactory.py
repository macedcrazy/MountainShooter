#!/usr/bin/python
# -*- coding: utf-8 -*-
import random

from code.Const import WIN_WIDTH, WIN_HEIGHT
from code.background import Background
from code.enemy import Enemy
from code.player import Player


class EntityFactory:

    @staticmethod
    def get_entity(entity_name: str):
        match entity_name:
            case 'level1bg':
                list_bg = []
                for i in range(5):
                    list_bg.append(Background(f'level1bg{i}', (0, 0)))
                    list_bg.append(Background(f'level1bg{i}', (WIN_WIDTH, 0)))
                return list_bg
            case 'Player1':
                return Player('Player1', (10, WIN_HEIGHT / 2 - 30))
            case 'Player2':
                return Player('Player2', (10, WIN_HEIGHT / 2 + 30))
            case 'jinn1':
                return Enemy('jinn1', (WIN_WIDTH + 10, random.randint(50, WIN_HEIGHT - 50)))
            case 'Dragon':
                return Enemy('Dragon', (WIN_WIDTH + 10, random.randint(50, WIN_HEIGHT - 50)))
            case 'Demon':
                return Enemy('Demon', (WIN_WIDTH + 10, random.randint(50, WIN_HEIGHT - 50)))
            case 'Medusa':
                return Enemy('Medusa', (WIN_WIDTH + 10, random.randint(50, WIN_HEIGHT - 50)))






