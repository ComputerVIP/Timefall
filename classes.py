import pygame
from math import atan2, degrees

class Base:
    def __init__(self, x, y, state = 0):
        self.x = x
        self.y = y
        self.state = state
        self.img = None

    def get_rect(self):
        if self.img:
            rect = self.img.get_rect(center=(self.x, self.y))
            return rect
        return pygame.Rect(self.x, self.y, 0, 0)

    def draw(self, surface):
        if self.img:
            rect = self.get_rect()
            surface.blit(self.img, rect)

class Player(Base):
    def __init__(self, x, y, state = 2):
        super().__init__(x, y, state)  # Initialize Base
        self.speed = 5

        # Load original only once
        self.original_img = pygame.image.load('Resources\\ply_test.png')
        self.img = self.original_img  # Set the img for Base class

    def draw(self, surface, colour):
        # Mouse angle
        mx, my = pygame.mouse.get_pos()
        rect = self.get_rect()  # Get current positioned rect
        dx = mx - rect.centerx
        dy = my - rect.centery

        angle = degrees(atan2(-dy, dx))

        # Rotate from ORIGINAL only
        self.original_img.fill(colour)
        self.img = pygame.transform.rotate(self.original_img, angle)

        # Get new rect for rotated image
        new_rect = self.img.get_rect(center=(self.x, self.y))

        # Draw
        surface.blit(self.img, new_rect)

    def move(self, box, keys, walls):
        # Compute desired move
        dx, dy = 0, 0
        if keys[pygame.K_w]:
            dy -= self.speed
        if keys[pygame.K_s]:
            dy += self.speed
        if keys[pygame.K_a]:
            dx -= self.speed
        if keys[pygame.K_d]:
            dx += self.speed

        # Move X first and handle collision/pushing
        if dx != 0:
            self.x += dx
            if self.get_rect().colliderect(box.get_rect()):
                # try to push box horizontally; if can't, revert player
                if not box.move(dx, 0):
                    self.x -= dx

        # Move Y next and handle collision/pushing
        if dy != 0:
            self.y += dy
            if self.get_rect().colliderect(box.get_rect()):
                # try to push box vertically; if can't, revert player
                if not box.move(0, dy):
                    self.y -= dy

        # Keep player on-screen (clamp)
        if self.x < 0:
            self.x = 0 + 32
        if self.x > 800:
            self.x = 800 - 32
        if self.y < 0:
            self.y = 0 + 32
        if self.y > 600:
            self.y = 600 - 32
        
        for i in walls:
            if self.get_rect().colliderect(i.rect):
                # Calculate overlap on each side
                player_rect = self.get_rect()
                overlap_left = player_rect.right - i.rect.left
                overlap_right = i.rect.right - player_rect.left
                overlap_top = player_rect.bottom - i.rect.top
                overlap_bottom = i.rect.bottom - player_rect.top
                
                # Find the minimum overlap (closest edge)
                min_overlap = min(overlap_left, overlap_right, overlap_top, overlap_bottom)
                
                # Push player out from the closest edge
                if min_overlap == overlap_left and dx > 0:
                    self.x = i.rect.left - self.get_rect().width / 2
                elif min_overlap == overlap_right and dx < 0:
                    self.x = i.rect.right + self.get_rect().width / 2
                elif min_overlap == overlap_top and dy > 0:
                    self.y = i.rect.top - self.get_rect().height / 2
                elif min_overlap == overlap_bottom and dy < 0:
                    self.y = i.rect.bottom + self.get_rect().height / 2


class Box(Base):
    def __init__(self, x, y, state):
        super().__init__(x, y, state)
        self.img = pygame.Surface((30, 30))
        self.img.fill((255, 0, 0))  # Set color once in __init__
        # Don't create separate rect

    def draw(self, surface):
        rect = self.get_rect()  # This now returns properly positioned rect
        surface.blit(self.img, rect)

    def move(self, dx, dy):
        """
        Move box by dx, dy if there's room. Returns True if box moved, False otherwise.
        This lets the player attempt to push the box and only move into it if the box can be pushed.
        """
        moved = False

        # Attempt horizontal move if requested
        if dx != 0:
            new_x = self.x + dx
            if 32 <= new_x <= 800 - 32:
                self.x = new_x
                moved = True

        # Attempt vertical move if requested
        if dy != 0:
            new_y = self.y + dy
            if 32 <= new_y <= 600 - 32:
                self.y = new_y
                moved = True

        return moved
    
class End(Base):
    def __init__(self, x, y, state, active = False):
        super().__init__(x, y, state)
        self.active = active
        self.img = pygame.Surface((30, 30))
        self.img.fill((0, 255, 0))

    def next_level(self, player):
        # Only trigger if colliding, active and the states match (or this end is 'both' state==2)
        if self.get_rect().colliderect(player.get_rect()) and self.active and (self.state == player.state or self.state == 2):
            # placeholder: mark reached or print (implement level switching elsewhere)
            print("End reached for player state", player.state)

class Button(Base):
    def __init__(self, x, y, state):
        super().__init__(x, y, state)
        self.img = pygame.Surface((20, 10))
        self.img.fill((0, 0, 255))  # Set color once in __init__

    def activate(self, box, end):
        if self.get_rect().colliderect(box.get_rect()) and self.state == box.state:
            end.active = True

class Wall:
    def __init__(self, x, y, width, height):
        self.rect = pygame.Rect(x, y, width, height)

    def draw(self, surface, colour):
        pygame.draw.rect(surface, colour, self.rect)