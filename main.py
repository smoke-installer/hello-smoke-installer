import pygame
import sys

pygame.init()

clock = pygame.time.Clock()
pygame.display.set_caption('Hello Smoke!')
screen = pygame.display.set_mode((1100, 600))

running = True


def main():
    while running:
        for event in pygame.event.get():
            if event == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit()

        screen.fill((52, 198, 235))

        arial_font = pygame.font.SysFont('Arial', 20)
        text = arial_font.render("Hello Smoke!", True, (255, 255, 255))
        screen.blit(text, (500, 300))

        clock.tick(60)
        pygame.display.flip()


if __name__ == '__main__':
    main()
