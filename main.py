import pygame
import sys


def main():
    pygame.init()
    screen = pygame.display.set_mode((400, 200))
    pygame.display.set_caption("Hello")
    font = pygame.font.SysFont("Arial", 36)
    text = font.render("Hello, world!", True, (0, 0, 0))
    text_rect = text.get_rect(center=(200, 100))

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        screen.fill((255, 255, 255))
        screen.blit(text, text_rect)
        pygame.display.flip()


if __name__ == "__main__":
    main()
