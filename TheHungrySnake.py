import pygame
import random

pygame.init()

color1 = (168, 228, 10)   # color of the snake
color2 = (147, 100, 81)    # background color
color3 = (8, 8, 8)    # Text color
color4 = (92, 20, 36)    # Score Text color
color5 = (255, 255, 194)    # Food color

width, height = 600, 400    # dimensions of the display box

game_display = pygame.display.set_mode((width, height))
pygame.display.set_caption("The Hungry Snake")

clock = pygame.time.Clock()

snake_size = 10
snake_speed = 10

message_font = pygame.font.SysFont('Comic Sans MS', 25)
score_font = pygame.font.SysFont('Comic Sans MS', 20)


def show_score(score):
    text = score_font.render('Score : ' + str(score), True, color4)
    game_display.blit(text, [0, 0])


def draw_snake(snake_len, snake_pixels):
    for pixel in snake_pixels:
        pygame.draw.rect(game_display, color1, [pixel[0], pixel[1], snake_len, snake_len])


def run_game():
    game_over = False
    game_close = False

    x = width / 2
    y = height / 2

    x_speed = 0
    y_speed = 0

    snake_pixels = []
    snake_length = 1

    target_x = round(random.randrange(0, width - snake_size) / 10.0) * 10.0
    target_y = round(random.randrange(0, height - snake_size) / 10.0) * 10.0

    horizontal = 0
    vertical = 0

    speed_inc = 0

    while not game_over:

        while game_close:
            game_display.fill(color2)
            game_over_message1 = message_font.render("GAME OVER!", True, color3)
            game_display.blit(game_over_message1, [width / 3 + 10, height / 3], )
            game_over_message2 = message_font.render("Play Again?(Y/N)", True, color3)
            game_display.blit(game_over_message2, [width / 3 - 10, height / 3+30], )
            show_score(snake_length - 1)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_n:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_y:
                        run_game()
                if event.type == pygame.QUIT:
                    game_over = True
                    game_close = False

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    if horizontal != 2:
                        x_speed = -snake_size
                        y_speed = 0
                        horizontal = 1
                        vertical = 0
                if event.key == pygame.K_RIGHT:
                    if horizontal != 1:
                        x_speed = snake_size
                        y_speed = 0
                        horizontal = 2
                        vertical = 0
                if event.key == pygame.K_UP:
                    if vertical != 1:
                        x_speed = 0
                        y_speed = -snake_size
                        vertical = 2
                        horizontal = 0
                if event.key == pygame.K_DOWN:
                    if vertical != 2:
                        x_speed = 0
                        y_speed = snake_size
                        vertical = 1
                        horizontal = 0

        x = (x + x_speed + width) % width
        y = (y + y_speed + height) % height

        game_display.fill(color2)
        pygame.draw.rect(game_display, color5, [target_x, target_y, snake_size, snake_size])

        snake_pixels.append([x, y])

        if len(snake_pixels) > snake_length:
            del snake_pixels[0]

        for pixel in snake_pixels[:-1]:
            if pixel == [x, y]:
                game_close = True

        draw_snake(snake_size, snake_pixels)
        show_score(snake_length - 1)

        pygame.display.update()

        if x == target_x and y == target_y:
            target_x = round(random.randrange(0, width - snake_size) / 10.0) * 10.0
            target_y = round(random.randrange(0, height - snake_size) / 10.0) * 10.0
            snake_length += 1
            speed_inc += (snake_length % 10 == 0)

        clock.tick(snake_speed+speed_inc)

    pygame.quit()
    quit()


run_game()