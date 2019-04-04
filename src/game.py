import pygame
from pygame.locals import *

SIZE = WIDTH, HEIGHT = 800, 600


class Player(pygame.sprite.Sprite):
    def __init__(self, position):
        pygame.sprite.Sprite.__init__(self)
        self.userPosition = user_position
        self.userImage = []

    def update(self):
        self.rect = self.image.get_rect()
        self.rect.center = self.user_position

    def load_image(self, file):
        idleSprite = ['idle-2-0' + str(i) + '.png' for i in range(4)]
        idleImage = [pygame.image.load(file + i for i in idle_sprite]
        self.user_image.append(idleImage)
