import pygame
from pygame.locals import *
frame = 0


class Player(pygame.sprite.Sprite):
    def __init__(self, path, position):
        pygame.sprite.Sprite.__init__(self)
        self.user_position = [position[0], position[1]]
        self.user_image = []
        self.loadImage(path)

    def update(self, screen):
        global frame
        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_UP]:
            self.user_position[1] -= 3
        elif pressed[pygame.K_DOWN]:
            self.user_position[1] += 3
        elif pressed[pygame.K_LEFT]:
            self.user_position[0] -= 3
        elif pressed[pygame.K_RIGHT]:
            self.user_position[0] += 3

        frame += 1
        point = self.user_position
        screen.blit(self.user_image[0][frame % 4], self.user_position)

    def loadImage(self, path):
        idle_sprite = ['idle-2-0' + str(i) + '.png' for i in range(4)]
        idle_image = [pygame.image.load(path + i) for i in idle_sprite]
        self.user_image.append(idle_image)


class Game:
    def __init__(self):
        self.size = 800, 600
        self.screen = pygame.display.set_mode(self.size)
        self.clock = pygame.time.Clock()

    def main(self):
        pygame.init()
        pygame.display.set_caption("Test")

        rect = self.screen.get_rect()
        player = Player("res/Char/", rect.center)

        while True:
            time = self.clock.tick(15)

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
