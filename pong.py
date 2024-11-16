import pygame
import random
from ball import Ball
from paddle import Paddle

def check_win(p1, p2):
    return True if p1 == 3 or p2 == 3 else False

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
p1_score = 0
p2_score = 0
winner = ""
game_over = False
random_num = random.randint(0,1)
server = "p_2" if random_num == 1 else "p_1"
direction = "right" if server == "p_1" else "left"
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill("black")

    font = pygame.font.Font('freesansbold.ttf', 32)

    p1_text = font.render(f'P1 {p1_score}', True, "white", "black")
    p1_text_rect = p1_text.get_rect()
    p1_text_rect.center = (player_one_pos_start.x + 200, 100)

    p2_text = font.render(f'P2 {p2_score}', True, "white", "black")
    p2_text_rect = p1_text.get_rect()
    p2_text_rect.center = (player_two_pos_start.x - 200, 100)

    winner_text = font.render(f"{winner} wins!", True, "white", "black")
    winner_text_rect = winner_text.get_rect()
    winner_text_rect.center = (screen.get_width() / 2, screen.get_height() / 2 - 100)

    serve_text = font.render("SERVE", True, "white", "black")
    serve_text_rect = serve_text.get_rect()
    serve_text_rect.center = (screen.get_width() / 2, 100)

    arrow_text = font.render("-->", True, "white", "black")
    arrow_text_rect = arrow_text.get_rect()
    arrow_text_rect.center = (screen.get_width() / 2 - 200 if server == "p_1" else screen.get_width() / 2 + 200, 100)

    ball = Ball(screen, "white", ball_pos, 10, dt, vertical_movement, horizontal_movement)
    p_1 = Paddle(screen, "white", player_one_pos_start.xy, player_one_pos_end.xy, 1)
    p_2 = Paddle(screen, "white", player_two_pos_start.xy, player_two_pos_end.xy, 2)
    top_border = pygame.draw.line(screen, "white", top_border_start.xy, top_border_end.xy)
    bottom_border = pygame.draw.line(screen, "white", bottom_border_start.xy, bottom_border_end.xy)

    keys = pygame.key.get_pressed()
    if keys[pygame.K_SPACE] and not game_start:
        game_start = True
        game_over = False
    if keys[pygame.K_w] and p_1.rect.top > 1 and game_start:
        player_one_pos_start.y -= 300 * dt
        player_one_pos_end.y -= 300 * dt
    if keys[pygame.K_s] and p_1.rect.bottom < screen.get_height() - 1 and game_start:
        player_one_pos_start.y += 300 * dt
        player_one_pos_end.y += 300 * dt
    if keys[pygame.K_UP] and p_2.rect.top > 1 and game_start:
        player_two_pos_start.y -= 300 * dt
        player_two_pos_end.y -= 300 * dt
    if keys[pygame.K_DOWN] and p_2.rect.bottom < screen.get_height() - 1 and game_start:
        player_two_pos_start.y += 300 * dt
        player_two_pos_end.y += 300 * dt

    if game_start: 
        ball.move(direction)
    else:
        screen.blit(p1_text, p1_text_rect)
        screen.blit(p2_text, p2_text_rect)
        screen.blit(serve_text, serve_text_rect)
        screen.blit(arrow_text, arrow_text_rect)

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
        if ball.position.x >= 1600:
            p1_score += 1
            server = "p_2"
            direction = "left"
        else:
            p2_score += 1
            server = "p_1"
            direction = "right"
        game_start = False
        vertical_movement = 0
        ball_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)
        player_one_pos_start = pygame.Vector2(screen.get_width() / 6, 300)
        player_one_pos_end = pygame.Vector2(screen.get_width() / 6, 600)
        player_two_pos_start = pygame.Vector2(screen.get_width() - (screen.get_width() / 6), 300)
        player_two_pos_end = pygame.Vector2(screen.get_width() - (screen.get_width() / 6), 600) 
        if (check_win(p1_score, p2_score)):
            winner = "P1" if p1_score == 3 else "P2"
            game_over = True
    if game_over:
        screen.blit(winner_text, winner_text_rect)
        p1_score = 0
        p2_score = 0



    pygame.display.flip()
    pygame.display.set_caption("Ponged")


    dt = clock.tick(60) / 1000


pygame.quit()


