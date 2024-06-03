

import pygame
from settings import SCREEN, BACKGROUND_COLOR, SNAKE_COLOR, TARGET_COLOR

def initialize_screen():
    SCREEN.fill(BACKGROUND_COLOR)

def draw_snake(snake):
    for snake_part in snake:
        pygame.draw.rect(SCREEN, SNAKE_COLOR, snake_part)

def draw_target(target):
    pygame.draw.rect(SCREEN, TARGET_COLOR, target)

def update_display():
    pygame.display.flip()

def display_main_menu():
    font = pygame.font.Font(None, 36)
    title = font.render("Snake Game", True, (255, 255, 255))
    start_text = font.render("Press S to Start", True, (255, 255, 255))
    quit_text = font.render("Press Q to Quit", True, (255, 255, 255))
    SCREEN.blit(title, (100, 150))
    SCREEN.blit(start_text, (100, 200))
    SCREEN.blit(quit_text, (100, 250))

def display_pause_menu():
    font = pygame.font.Font(None, 36)
    paused_text = font.render("Paused", True, (255, 255, 255))
    resume_text = font.render("Press SPACE to Resume", True, (255, 255, 255))
    restart_text = font.render("Press R to Restart", True, (255, 255, 255))
    quit_text = font.render("Press Q to Quit", True, (255, 255, 255))
    SCREEN.blit(paused_text, (100, 150))
    SCREEN.blit(resume_text, (100, 200))
    SCREEN.blit(restart_text, (100, 250))
    SCREEN.blit(quit_text, (100, 300))

def display_game_over():
    font = pygame.font.Font(None, 36)
    game_over_text = font.render("Game Over! Press C to restart or Q to quit.", True, (255, 255, 255))
    SCREEN.blit(game_over_text, (100, 200))
