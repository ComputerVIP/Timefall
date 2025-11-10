import pygame
from math import atan2, degrees

class Base:
    def __init__(self, x, y, rot):
        self.x = x
        self.y = y
        self.rot = rot
        self.img = None

    def get_rect(self):
        if self.img:
            rect = self.img.get_rect(center=(self.x, self.y))
            return rect
        return pygame.Rect(self.x, self.y, 0, 0)
    

    def move(self, dx, dy):
        self.x += dx
        self.y += dy

class Player(Base):
    def __init__(self, x, y, state):
        self.state = state
        self.x = x
        self.y = y
        self.speed = 5

        # Load original only once
        self.original_img = pygame.image.load('Resources\\ply_test.png')
        self.img = self.original_img

        self.rect = self.img.get_rect(center=(self.x, self.y))

    def draw(self, surface, x, y):
        # Update rect position based on x/y movement
        self.rect.center = (self.x, self.y)

        # Mouse angle
        mx, my = pygame.mouse.get_pos()
        dx = mx - self.rect.centerx
        dy = my - self.rect.centery

        angle = degrees(atan2(-dy, dx)) - 90

        # Rotate from ORIGINAL only
        self.img = pygame.transform.rotate(self.original_img, angle)

        # Keep corrected center
        self.rect = self.img.get_rect(center=self.rect.center)

        # Draw
        surface.blit(self.img, self.rect)

    def move(self, keys):
        if keys[pygame.K_w]:
            self.y -= self.speed
        if keys[pygame.K_s]:
            self.y += self.speed
        if keys[pygame.K_a]:
            self.x -= self.speed
        if keys[pygame.K_d]:
            self.x += self.speed


class Box(Base):
    def __init__(self, x, y):
        super().__init__(x, y, 0)
        self.img = pygame.Surface((30, 30))
        self.img.fill((255, 0, 0))
        self.rect = self.img.get_rect(center=(self.x, self.y))

    def draw(self, surface, x, y):
        surface.blit(self.img, (x, y))

    def move(self, player, keys):
        p_x, p_y = 0,0
        
        if keys[pygame.K_w]:
            p_y -= player.speed
        if keys[pygame.K_s]:
            p_y += player.speed
        if keys[pygame.K_a]:
            p_x -= player.speed
        if keys[pygame.K_d]:
            p_x += player.speed
        
        self.x += p_x
        self.y += p_y