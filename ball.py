import pygame

class Ball:
    def __init__(self, screen, color, position, radius, dt, vertical_movement, horizontal_movement):
        self.screen = screen
        self.color = color
        self.position = position
        self.radius = radius
        self.speed = pygame.Vector2(horizontal_movement * dt, vertical_movement * dt)
        self.rect = pygame.draw.circle(screen, color, position, radius)
        self.dt = dt

    def move(self, direction):
        self.position.x += self.speed.x if direction == "right" else -self.speed.x
        self.position.y += -self.speed.y if direction == "right" else self.speed.y
        self.rect = pygame.draw.circle(self.screen, self.color, self.position, self.radius)
    def restart(self, pos, dir):
        self.position.x = pos.x - 800 if dir == "right" else pos.x + 800
        self.position.y = self.screen.get_height() / 2
    def set_speed(self, paddle):
        self.speed.y += paddle * self.dt