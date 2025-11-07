import pygame
import random
import math
from abc import ABC, abstractmethod

pygame.init()

screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Norm Dimensional Simulation")
clock = pygame.time.Clock()

class Bullet:
    def __init__(self, x, y, rot, speed=10):
        self.x = x
        self.y = y
        self.rot = rot
        self.speed = speed
        self.img = pygame.Surface((5, 5))
        self.img.fill((255, 0, 0))

    def move(self):
        rad = math.radians(self.rot)
        self.x += self.speed * math.cos(rad)
        self.y += self.speed * math.sin(rad)

class Base:
    def __init__(self, x, y, rot, life):
        self.x = x
        self.y = y
        self.rot = rot
        self.life = life
        self.img = None

    def bullet_collide(self, bullet):
        bullet_rect = bullet.img.get_rect(topleft=(bullet.x, bullet.y))

class Player:
