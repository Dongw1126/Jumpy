import pygame
from const import *
from pygame.locals import *
frame = 0


class Player(pygame.sprite.Sprite):
    def __init__(self, path, position):
        pygame.sprite.Sprite.__init__(self)
        self.user_position = [position[0], position[1]]
        self.user_image = []
        self.loadImage(path)
        self.vel_left = False
        self.event_list = [False for i in range(EVENT)]

    def update(self, screen):
        global frame
        self.EventHandler()
        if self.event_list[IDLERIGHT]:
            screen.blit(self.user_image[IDLERIGHT][int(frame/4) % 4],
                        self.user_position)
        elif self.event_list[IDLELEFT]:
            screen.blit(self.user_image[IDLELEFT][int(frame/4) % 4],
                        self.user_position)
        elif self.event_list[WALKRIGHT]:
            screen.blit(self.user_image[WALKRIGHT][int(frame/4) % 5],
                        self.user_position)
        elif self.event_list[WALKLEFT]:
            screen.blit(self.user_image[WALKLEFT][int(frame/4) % 5],
                        self.user_position)

    def loadImage(self, path):
        idle_sprite = ['idle-2-0' + str(i) + '.png' for i in range(4)]
        idle_right_image = [pygame.image.load(path + i).convert_alpha()
                            for i in idle_sprite]
        idle_left_image = [pygame.transform.flip(i, True, False)
                           for i in idle_right_image]

        walk_right_sprite = ['run-0' + str(i) + '.png' for i in range(5)]
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

        else:
            if self.vel_left:
                self.event_list[IDLELEFT] = True
                self.event_list[IDLERIGHT] = False
            else:
                self.event_list[IDLERIGHT] = True
                self.event_list[IDLELEFT] = False


class Game:
    def __init__(self):
        self.size = 800, 600
        self.screen = pygame.display.set_mode(self.size)
        self.clock = pygame.time.Clock()

    def main(self):
        global frame
        pygame.init()
        pygame.display.set_caption("Test")

        rect = self.screen.get_rect()
        player = Player("res/Char/", rect.center)

        while True:
            time = self.clock.tick(60)
            frame += 1
            self.screen.fill((0, 0, 0))

            player.update(self.screen)
            pygame.display.flip()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit(0)


if __name__ == "__main__":
    g = Game()
    g.main()
