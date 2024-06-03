

import pygame
import random
from settings import SQUARE_WIDTH, PIXEL_WIDTH, SCREEN, CLOCK, FPS, SNAKE_INITIAL_LENGTH
from board import initialize_screen, draw_snake, draw_target, update_display, display_main_menu, display_pause_menu, display_game_over

def generate_starting_position(snake):
    position_range = (PIXEL_WIDTH // 2, SQUARE_WIDTH - PIXEL_WIDTH // 2, PIXEL_WIDTH)
    while True:
        pos = [random.randrange(*position_range), random.randrange(*position_range)]
        snake_rects = [pygame.rect.Rect(snake_part) for snake_part in snake]
        new_rect = pygame.rect.Rect([pos[0], pos[1], PIXEL_WIDTH - 2, PIXEL_WIDTH - 2])
        if all(not new_rect.colliderect(snake_part) for snake_part in snake_rects):
            return pos

def reset(target, snake_pixel, snake):
    target.center = generate_starting_position(snake)
    snake_pixel.center = generate_starting_position([])
    return snake_pixel.copy()

def is_out_of_bounds(snake, snake_pixel):
    return any(part.colliderect(snake_pixel) for part in snake[1:])

def run_game():
    def restart_game():
        nonlocal snake_pixel, snake, snake_direction, snake_length, target, game_over, paused, in_main_menu
        snake_pixel = pygame.rect.Rect([0, 0, PIXEL_WIDTH - 2, PIXEL_WIDTH - 2])
        snake_pixel.center = generate_starting_position([])
        snake = [snake_pixel.copy()]
        snake_direction = (0, 0)
        snake_length = SNAKE_INITIAL_LENGTH

        target = pygame.rect.Rect([0, 0, PIXEL_WIDTH - 2, PIXEL_WIDTH - 2])
        target.center = generate_starting_position(snake)

        game_over = False
        paused = False
        in_main_menu = False

    running = True
    in_main_menu = True
    paused = False
    game_over = False

    snake_pixel = pygame.rect.Rect([0, 0, PIXEL_WIDTH - 2, PIXEL_WIDTH - 2])
    snake_pixel.center = generate_starting_position([])
    snake = [snake_pixel.copy()]
    snake_direction = (0, 0)
    snake_length = SNAKE_INITIAL_LENGTH

    target = pygame.rect.Rect([0, 0, PIXEL_WIDTH - 2, PIXEL_WIDTH - 2])
    target.center = generate_starting_position(snake)

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    running = False
                elif in_main_menu:
                    if event.key == pygame.K_s:
                        in_main_menu = False
                elif game_over:
                    if event.key == pygame.K_c:
                        restart_game()
                    elif event.key == pygame.K_q:
                        running = False
                elif paused:
                    if event.key == pygame.K_r:
                        restart_game()
                    elif event.key == pygame.K_q:
                        running = False
                    elif event.key == pygame.K_SPACE:
                        paused = False
                elif event.key == pygame.K_SPACE:
                    paused = True

        initialize_screen()

        if in_main_menu:
            display_main_menu()
        elif game_over:
            display_game_over()
        elif paused:
            display_pause_menu()
        else:
            if snake_pixel.colliderect(target):
                target.center = generate_starting_position(snake)
                snake_length += 1
                snake.append(snake_pixel.copy())

            keys = pygame.key.get_pressed()
            if keys[pygame.K_w]:
                snake_direction = (0, -PIXEL_WIDTH)
            if keys[pygame.K_s]:
                snake_direction = (0, PIXEL_WIDTH)
            if keys[pygame.K_a]:
                snake_direction = (-PIXEL_WIDTH, 0)
            if keys[pygame.K_d]:
                snake_direction = (PIXEL_WIDTH, 0)

            if snake_direction != (0, 0):
                snake_pixel.move_ip(snake_direction)

                if snake_pixel.left > SQUARE_WIDTH - PIXEL_WIDTH // 2:
                    snake_pixel.right = 0
                elif snake_pixel.right < PIXEL_WIDTH // 2:
                    snake_pixel.left = SQUARE_WIDTH
                elif snake_pixel.top > SQUARE_WIDTH - PIXEL_WIDTH // 2:
                    snake_pixel.bottom = 0
                elif snake_pixel.bottom < PIXEL_WIDTH // 2:
                    snake_pixel.top = SQUARE_WIDTH

                if is_out_of_bounds(snake, snake_pixel):
                    game_over = True

                snake.append(snake_pixel.copy())
                snake = snake[-snake_length:]

            draw_snake(snake)
            draw_target(target)

        update_display()
        CLOCK.tick(FPS)

    pygame.quit()

if __name__ == "__main__":
    run_game()
