

import pygame

pygame.init()

SQUARE_WIDTH = 800
PIXEL_WIDTH = 20
SCREEN = pygame.display.set_mode((SQUARE_WIDTH, SQUARE_WIDTH))
CLOCK = pygame.time.Clock()
TARGET_COLOR = (255, 0, 0)
SNAKE_COLOR = (0, 255, 0)
BACKGROUND_COLOR = (0, 0, 0)
FPS = 10
SNAKE_INITIAL_LENGTH = 5
