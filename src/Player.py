import pygame
from Const import *
from pygame.locals import *


class Player:
    def __init__(self, path, position, frame):
        self.frame = frame
        self.user_position = [position[0], position[1]]
        self.user_image = []
        self.loadImage(path)
        self.vel_left = False
        self.event_list = [False for i in range(EVENT)]

    def update(self, screen):
        global frame
        self.EventHandler()
        if self.event_list[IDLERIGHT]:
            screen.blit(self.user_image[IDLERIGHT][int(self.frame[0]/4) % 4],
                        self.user_position)
        elif self.event_list[IDLELEFT]:
            screen.blit(self.user_image[IDLELEFT][int(self.frame[0]/4) % 4],
                        self.user_position)
        elif self.event_list[WALKRIGHT]:
            screen.blit(self.user_image[WALKRIGHT][int(self.frame[0]/4) % 6],
                        self.user_position)
        elif self.event_list[WALKLEFT]:
            screen.blit(self.user_image[WALKLEFT][int(self.frame[0]/4) % 6],
                        self.user_position)

    def loadImage(self, path):
        idle_sprite = ['idle-2-0' + str(i) + '.png' for i in range(4)]
        idle_right_image = [pygame.image.load(path + i).convert_alpha()
                            for i in idle_sprite]
        idle_left_image = [pygame.transform.flip(i, True, False)
                           for i in idle_right_image]

        walk_right_sprite = ['run-0' + str(i) + '.png' for i in range(6)]
        walk_right_image = [pygame.image.load(path + i).convert_alpha()
                            for i in walk_right_sprite]
        walk_left_image = [pygame.transform.flip(i, True, False)
                           for i in walk_right_image]

        # The append order is the same as the constant declaration!!
        self.user_image.append(idle_right_image)
        self.user_image.append(idle_left_image)
        self.user_image.append(walk_right_image)
        self.user_image.append(walk_left_image)

    def EventHandler(self):
        pressed = pygame.key.get_pressed()
        self.event_list = [False for i in range(EVENT)]

        if pressed[pygame.K_RIGHT]:
            self.user_position[0] += 3
            self.event_list[WALKRIGHT] = True
            self.vel_left = False

        elif pressed[pygame.K_LEFT]:
            self.user_position[0] -= 3
            self.event_list[WALKLEFT] = True
            self.vel_left = True

        elif pressed[pygame.K_UP]:
            self.event_list[JUMP] = True
            self.vel_left = True

        else:
            if self.vel_left:
                self.event_list[IDLELEFT] = True
                self.event_list[IDLERIGHT] = False
            else:
                self.event_list[IDLERIGHT] = True
                self.event_list[IDLELEFT] = False
