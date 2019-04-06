import pygame
import Player
from pygame.locals import *


class Game:
    def __init__(self):
        self.size = 800, 600
        self.screen = pygame.display.set_mode(self.size)
        self.clock = pygame.time.Clock()

    def main(self):
        frame = [0]
        pygame.init()
        pygame.display.set_caption("Test")

        rect = self.screen.get_rect()
        player = Player.Player("res/Char/", rect.center, frame)

        while True:
            time = self.clock.tick(60)
            frame[0] += 1
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
