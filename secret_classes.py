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
        self.original_img = pygame.image.load('Resources\\norm_imgs\\norm.png')
        self.img = self.original_img  # Set the img for Base class

    def draw(self, surface):
        # Mouse angle
        mx, my = pygame.mouse.get_pos()
        rect = self.get_rect()  # Get current positioned rect
        dx = mx - rect.centerx
        dy = my - rect.centery

        angle = degrees(atan2(-dy, dx))

        # Rotate from ORIGINAL only
        self.img = pygame.transform.rotate(self.img, angle-90)

        # Get new rect for rotated image
        new_rect = self.img.get_rect(center=(self.x, self.y))

        # Draw
        surface.blit(self.img, new_rect)

    def move(self, keys, walls, enemy, dim='norm'):
        self.img = pygame.image.load('Resources\\norm_imgs\\norm.png') if dim=='norm' else pygame.image.load('Resources\\opp_imgs\\opp.png')

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
        
        # Apply movement
        if dx != 0:
            self.x += dx
        if dy != 0:
            self.y += dy

        # Keep player on-screen (clamp)
        if self.x < 0:
            self.x = 0 + 13
        if self.x > 800:
            self.x = 800 - 13
        if self.y < 0:
            self.y = 0 + 13
        if self.y > 600:
            self.y = 600 - 13
        
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
        
        if self.get_rect().colliderect(enemy.get_rect()):
            player_rect = self.get_rect()
            overlap_left = player_rect.right - enemy.get_rect().left
            overlap_right = enemy.get_rect().right - player_rect.left
            overlap_top = player_rect.bottom - enemy.get_rect().top
            overlap_bottom = enemy.get_rect().bottom - player_rect.top

            min_overlap = min(overlap_left, overlap_right, overlap_top, overlap_bottom)

            if min_overlap == overlap_left and dx > 0:
                self.x = enemy.get_rect().left - self.get_rect().width / 2
            elif min_overlap == overlap_right and dx < 0:
                self.x = enemy.get_rect().right + self.get_rect().width / 2
            elif min_overlap == overlap_top and dy > 0:
                self.y = enemy.get_rect().top - self.get_rect().height / 2
            elif min_overlap == overlap_bottom and dy < 0:
                self.y = enemy.get_rect().bottom + self.get_rect().height / 2


class Enemy(Base):
    def __init__(self, x, y, state = 2, flip = False):
        super().__init__(x, y, state)  # Initialize Base
        self.speed = 5
        self.flip = flip

        # Load original only once
        self.original_img = pygame.image.load('Resources\\opp_imgs\\opp.png')
        self.img = self.original_img  # Set the img for Base class

    def draw(self, surface):
        # Mouse angle
        mx, my = pygame.mouse.get_pos()
        rect = self.get_rect()  # Get current positioned rect
        dx = mx - rect.centerx
        dy = my - rect.centery

        angle = degrees(atan2(-dy, dx))

        # Rotate from ORIGINAL only
        self.img = pygame.transform.rotate(self.img, angle-90)

        # Get new rect for rotated image
        new_rect = self.img.get_rect(center=(self.x, self.y))

        # Draw
        surface.blit(self.img, new_rect)

    def move(self, keys, walls, player, dim='norm'):
        # keep image loading behavior (optional)
        try:
            self.img = pygame.image.load('Resources\\opp_imgs\\opp.png') if dim=='norm' else pygame.image.load('Resources\\norm_imgs\\norm.png')
        except Exception:
            pass

        # store original position for selective revert on collision
        orig_x, orig_y = self.x, self.y

        # Snap + axis-follow behavior:
        # - not flipped: snap Y to player.y, move X toward player.x
        # - flipped: snap X to player.x, move Y toward player.y
        if self.flip:
            # snap X immediately
            self.x = player.x
            # move Y toward player
            dy = 0
            if keys[pygame.K_w]:
                dy -= self.speed
            elif keys[pygame.K_s]:
                dy += self.speed
            if self.x >= player.x and dy < 0:
                dy = dy -10
            if dy != 0:
                self.y -= dy
        else:
            # snap Y immediately
            self.y = player.y
            # move X toward player
            dx = 0
            if keys[pygame.K_a]:
                dx -= self.speed
            elif keys[pygame.K_d]:
                dx += self.speed
            if dx != 0:
                self.x -= dx

        # Keep on-screen (clamp)
        if self.x < 0:
            self.x = 0 + 13
        if self.x > 800:
            self.x = 800 - 13
        if self.y < 0:
            self.y = 0 + 13
        if self.y > 600:
            self.y = 600 - 13

        # Collision resolution: revert only the axis that caused collision
        for i in walls:
            if self.get_rect().colliderect(i.rect):
                # check overlap per axis by testing moves separately
                # revert X if X movement caused collision
                self.x = orig_x
                if not self.get_rect().colliderect(i.rect):
                    # reverting X fixed it -> keep reverted X, restore Y
                    self.y = self.y  # nothing
                else:
                    # X revert didn't fix, revert Y instead
                    self.x = self.x  # already reverted then try reverting Y
                    self.y = orig_y
                    # if still colliding, fully revert
                    if self.get_rect().colliderect(i.rect):
                        self.x, self.y = orig_x, orig_y

        # collision with player: simple separation similar to before
        if self.get_rect().colliderect(player.get_rect()):
            enemy_rect = self.get_rect()
            overlap_left = enemy_rect.right - player.get_rect().left
            overlap_right = player.get_rect().right - enemy_rect.left
            overlap_top = enemy_rect.bottom - player.get_rect().top
            overlap_bottom = player.get_rect().bottom - enemy_rect.top

            min_overlap = min(overlap_left, overlap_right, overlap_top, overlap_bottom)

            # push out along the minimum overlap direction
            if min_overlap == overlap_left:
                self.x = player.get_rect().left - self.get_rect().width / 2
            elif min_overlap == overlap_right:
                self.x = player.get_rect().right + self.get_rect().width / 2
            elif min_overlap == overlap_top:
                self.y = player.get_rect().top - self.get_rect().height / 2
            elif min_overlap == overlap_bottom:
                self.y = player.get_rect().bottom + self.get_rect().height / 2


class End(Base):
    def __init__(self, x, y, state, active = False, level = 1, initialized=False, frame=0):
        super().__init__(x, y, state)
        self.active = active
        self.level = level
        self.initialized = initialized
        self.frame = frame
        self.img = pygame.Surface((30, 30))
        self.img.fill((0, 255, 0))

    def next_level(self, player):
        # Only trigger if colliding, active and the states match (or this end is 'both' state==2)
        if self.get_rect().colliderect(player.get_rect()) and self.active and (self.state == player.state or self.state == 2):
            self.level += 1
            self.initialized = False  # Reset for next level
            return True
        return False
    
    def draw(self, surface, change_frame=True):
        if change_frame:
            if self.active == True:
                if self.frame == 0:
                    self.img = pygame.image.load('Resources\\goal_imgs\\goal_active_1.png')
                    self.frame = 1
                elif self.frame == 1:
                    self.img = pygame.image.load('Resources\\goal_imgs\\goal_active_2.png')
                    self.frame = 2
                elif self.frame == 2:
                    self.img = pygame.image.load('Resources\\goal_imgs\\goal_active_3.png')
                    self.frame = 3
                elif self.frame == 3:
                    self.img = pygame.image.load('Resources\\goal_imgs\\goal_active_4.png')
                    self.frame = 0
            else:
                if self.frame == 0:
                    self.img = pygame.image.load('Resources\\goal_imgs\\goal_inactive_1.png')
                    self.frame = 1
                elif self.frame == 1:
                    self.img = pygame.image.load('Resources\\goal_imgs\\goal_inactive_2.png')
                    self.frame = 2
                elif self.frame == 2:
                    self.img = pygame.image.load('Resources\\goal_imgs\\goal_inactive_3.png')
                    self.frame = 3
                elif self.frame == 3:
                    self.img = pygame.image.load('Resources\\goal_imgs\\goal_inactive_4.png')
                    self.frame = 0
        else:
            if self.active == True:
                if self.frame == 0:
                    self.img = pygame.image.load('Resources\\goal_imgs\\goal_active_1.png')
                elif self.frame == 1:
                    self.img = pygame.image.load('Resources\\goal_imgs\\goal_active_2.png')
                elif self.frame == 2:
                    self.img = pygame.image.load('Resources\\goal_imgs\\goal_active_3.png')
                elif self.frame == 3:
                    self.img = pygame.image.load('Resources\\goal_imgs\\goal_active_4.png')
            else:
                if self.frame == 0:
                    self.img = pygame.image.load('Resources\\goal_imgs\\goal_inactive_1.png')
                elif self.frame == 1:
                    self.img = pygame.image.load('Resources\\goal_imgs\\goal_inactive_2.png')
                elif self.frame == 2:
                    self.img = pygame.image.load('Resources\\goal_imgs\\goal_inactive_3.png')
                elif self.frame == 3:
                    self.img = pygame.image.load('Resources\\goal_imgs\\goal_inactive_4.png')
        if self.img:
            rect = self.get_rect()
            surface.blit(self.img, rect)

class Flip():
    def __init__(self, x, y, width, height):
        self.rect = pygame.Rect(x, y, width, height)

    def activate(self, player, enemy):
        if self.rect.colliderect(player.get_rect()):
            enemy.flip = True
        else:
            enemy.flip = False
        
    def draw(self, surface, dim='norm'):
        if dim == 'norm':
            pygame.draw.rect(surface, (143, 63, 122), self.rect)
        else:
            pygame.draw.rect(surface, (106, 143, 63), self.rect)
            

class Wall:
    def __init__(self, x, y, width, height):
        self.rect = pygame.Rect(x, y, width, height)

    def draw(self, surface, colour):
        pygame.draw.rect(surface, colour, self.rect)