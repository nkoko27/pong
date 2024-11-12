import pygame
from ball import Ball
from paddle import Paddle

pygame.init()
screen = pygame.display.set_mode((1600,900))
clock = pygame.time.Clock()
running = True
dt = 0

ball_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)
player_one_pos_start = pygame.Vector2(screen.get_width() / 7, 300)
player_one_pos_end = pygame.Vector2(screen.get_width() / 7, 600)
player_two_pos_start = pygame.Vector2(screen.get_width() - (screen.get_width() / 7), 300)
player_two_pos_end = pygame.Vector2(screen.get_width() - (screen.get_width() / 7), 600)
top_border_start = pygame.Vector2(0, 0)
top_border_end = pygame.Vector2(screen.get_width(), 0)
bottom_border_start = pygame.Vector2(0, screen.get_height() - 1)
bottom_border_end = pygame.Vector2(screen.get_width(), screen.get_height() - 1)
direction = "right"
game_start = False
horizontal_movement = 600
vertical_movement = 0
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    first = "p_2"
    screen.fill("black")

    ball = Ball(screen, "white", ball_pos, 10, dt, vertical_movement, horizontal_movement)
    p_1 = Paddle(screen, "white", player_one_pos_start.xy, player_one_pos_end.xy, 1)
    p_2 = Paddle(screen, "white", player_two_pos_start.xy, player_two_pos_end.xy, 2)
    top_border = pygame.draw.line(screen, "white", top_border_start.xy, top_border_end.xy)
    bottom_border = pygame.draw.line(screen, "white", bottom_border_start.xy, bottom_border_end.xy)

    keys = pygame.key.get_pressed()
    if keys[pygame.K_SPACE] and first == "p_2" and not game_start:
        game_start = True
    if keys[pygame.K_w] and p_1.rect.top > 1:
        player_one_pos_start.y -= 300 * dt
        player_one_pos_end.y -= 300 * dt
    if keys[pygame.K_s] and p_1.rect.bottom < screen.get_height() - 1:
        player_one_pos_start.y += 300 * dt
        player_one_pos_end.y += 300 * dt
    if keys[pygame.K_UP] and p_2.rect.top > 1:
        player_two_pos_start.y -= 300 * dt
        player_two_pos_end.y -= 300 * dt
    if keys[pygame.K_DOWN] and p_2.rect.bottom < screen.get_height() - 1:
        player_two_pos_start.y += 300 * dt
        player_two_pos_end.y += 300 * dt

    if game_start: 
        ball.move(direction)

    if p_2.rect.colliderect(ball.rect):
        if keys[pygame.K_UP]:
            vertical_movement = -player_two_pos_start.y
        elif keys[pygame.K_DOWN]:
            vertical_movement = player_two_pos_start.y
        else:
            vertical_movement = -vertical_movement
        direction = "left"
    if p_1.rect.colliderect(ball.rect):
        if keys[pygame.K_w]:
            vertical_movement = player_one_pos_start.y
        elif keys[pygame.K_s]:
            vertical_movement = -player_one_pos_start.y
        else:
            vertical_movement = -vertical_movement
        direction = "right"
    if top_border.colliderect(ball.rect) or bottom_border.colliderect(ball.rect):
        vertical_movement = -vertical_movement 


    if ball.position.x >= 1600 or ball.position.x <= 0:
        game_start = False
        vertical_movement = 0
        ball.restart(ball_pos, direction)
        player_one_pos_start = pygame.Vector2(screen.get_width() / 6, 300)
        player_one_pos_end = pygame.Vector2(screen.get_width() / 6, 600)
        player_two_pos_start = pygame.Vector2(screen.get_width() - (screen.get_width() / 6), 300)
        player_two_pos_end = pygame.Vector2(screen.get_width() - (screen.get_width() / 6), 600)
        # p_1.restart()
        # p_2.restart()

    pygame.display.flip()


    dt = clock.tick(60) / 1000


pygame.quit()
