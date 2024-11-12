import pygame

class Paddle:
    def __init__(self, screen, color, start, end, player):
        self.screen = screen
        self.color = color
        self.start = start
        self.end = end
        self.player = player
        self.rect = pygame.draw.line(screen, color, start, end)
    def restart(self):
        if self.player == 1:
            self.start = pygame.Vector2(self.screen.get_width() / 6, 300)
            self.end = pygame.Vector2(self.screen.get_width() / 6, 600)
        else:
            self.start = pygame.Vector2(self.screen.get_width() - self.screen.get_width() / 6, 300)
            self.end = pygame.Vector2(self.screen.get_width() - self.screen.get_width() / 6, 600)
        self.rect = pygame.draw.line(self.screen, self.color, self.start, self.end)