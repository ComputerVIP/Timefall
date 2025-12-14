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

    def move(self, box, keys, walls, doors, dim='norm'):

        # Only interact with box if in compatible dimensions
        # Map dim to state: 'norm' = 0, 'opp' = 1; check if states are compatible
        dim_state = 0 if dim == 'norm' else 1
        box_compatible = (dim_state == box.state or dim_state == 2 or box.state == 2)
        
        if box_compatible and self.get_rect().colliderect(box.get_rect()):
            self.img = pygame.image.load('Resources\\norm_imgs\\box_up_norm.png') if dim=='norm' else pygame.image.load('Resources\\opp_imgs\\box_up_opp.png')
        else:
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

        # Move X first and handle collision/pushing
        if dx != 0:
            self.x += dx
            if box_compatible and self.get_rect().colliderect(box.get_rect()) and box.pushable:
                # try to push box horizontally; if can't, revert player
                if not box.move(dx, 0, walls):
                    self.x -= dx

        # Move Y next and handle collision/pushing
        if dy != 0:
            self.y += dy
            if box_compatible and self.get_rect().colliderect(box.get_rect()) and box.pushable:
                # try to push box vertically; if can't, revert player
                if not box.move(0, dy, walls):
                    self.y -= dy
        if box_compatible and self.get_rect().colliderect(box.get_rect()) and not box.pushable:
                # Calculate overlap on each side
                player_rect = self.get_rect()
                box_rect = box.get_rect()
                overlap_left = player_rect.right - box_rect.left
                overlap_right = box_rect.right - player_rect.left
                overlap_top = player_rect.bottom - box_rect.top
                overlap_bottom = box_rect.bottom - player_rect.top
                
                # Find the minimum overlap (closest edge)
                min_overlap = min(overlap_left, overlap_right, overlap_top, overlap_bottom)
                
                # Push player out from the closest edge with smaller offset for more forceful push (allows clipping)
                if min_overlap == overlap_left and dx > 0:
                    self.x = box_rect.left - 10
                elif min_overlap == overlap_right and dx < 0:
                    self.x = box_rect.right + 10
                elif min_overlap == overlap_top and dy > 0:
                    self.y = box_rect.top - 10
                elif min_overlap == overlap_bottom and dy < 0:
                    self.y = box_rect.bottom + 10

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

        for i in doors:
            if i.active is True:
                if self.get_rect().colliderect(i.rect):
                    # Calculate overlap on each side
                    player_rect = self.get_rect()
                    overlap_left = player_rect.right - i.rect.left
                    overlap_right = i.rect.right - player_rect.left
                    overlap_top = player_rect.bottom - i.rect.top
                    overlap_bottom = i.rect.bottom - player_rect.top
                    
                    # Find the minimum overlap (closest edge)
                    min_overlap = min(overlap_left, overlap_right, overlap_top, overlap_bottom)
                    
                    # Push player out from the closest edge with minimal offset
                    if min_overlap == overlap_left and dx > 0:
                        self.x = i.rect.left - 2
                    elif min_overlap == overlap_right and dx < 0:
                        self.x = i.rect.right + 2
                    elif min_overlap == overlap_top and dy > 0:
                        self.y = i.rect.top - 2
                    elif min_overlap == overlap_bottom and dy < 0:
                        self.y = i.rect.bottom + 2
            else:
                continue


class Box(Base):
    def __init__(self, x, y, state, pushable=True):
        super().__init__(x, y, state)
        self.pushable = pushable
        self.img = pygame.Surface((30, 30))
        self.img.fill((255, 0, 0))  # Set color once in __init__
        # Don't create separate rect

    def draw(self, surface, dim='norm'):
        rect = self.get_rect()  # This now returns properly positioned rect
        self.img = pygame.image.load('Resources\\norm_imgs\\box_norm.png') if dim=='norm' else pygame.image.load('Resources\\opp_imgs\\box_opp.png')
        surface.blit(self.img, rect)

    def move(self, dx, dy, walls=None):
        """
        Move box by dx, dy if there's room. Returns True if box moved, False otherwise.
        This lets the player attempt to push the box and only move into it if the box can be pushed.
        """
        moved = False
        if self.pushable:
            # Attempt horizontal move if requested
            if dx != 0:
                new_x = self.x + dx
                if 32 <= new_x <= 800 - 12:
                    # Check for wall collisions
                    self.x = new_x
                    collision = False
                    if walls:
                        for wall in walls:
                            if self.get_rect().colliderect(wall.rect):
                                collision = True
                                break
                    if collision:
                        self.x -= dx  # Revert if hit wall
                    else:
                        moved = True

            # Attempt vertical move if requested
            if dy != 0:
                new_y = self.y + dy
                if 32 <= new_y <= 600 - 12:
                    # Check for wall collisions
                    self.y = new_y
                    collision = False
                    if walls:
                        for wall in walls:
                            if self.get_rect().colliderect(wall.rect):
                                collision = True
                                break
                    if collision:
                        self.y -= dy  # Revert if hit wall
                    else:
                        moved = True
        

        return moved
    
    
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


class Button(Base):
    def __init__(self, x, y, state, active=False):
        super().__init__(x, y, state)
        self.img = pygame.Surface((20, 10))
        self.active = active

    def draw(self, surface, dim):
        rect = self.get_rect()  # This now returns properly positioned rect
        if dim == 'norm' and not self.active:
            self.img = pygame.image.load('Resources\\button\\button_norm_up.png')
        elif dim == 'norm' and self.active:
            self.img = pygame.image.load('Resources\\button\\button_norm_down.png')
        elif dim == 'opp' and not self.active:
            self.img = pygame.image.load('Resources\\button\\button_opp_up.png')
        elif dim == 'opp' and self.active:
            self.img = pygame.image.load('Resources\\button\\button_opp_down.png')
        surface.blit(self.img, rect)

    def activate(self, box, end, doors):
        if self.get_rect().colliderect(box.get_rect()):
            if (self.state == box.state) or box.state == 2:
                end.active = True
                for i in doors:
                    i.alpha=255
                    i.active = False
            self.active = True


class Wall:
    def __init__(self, x, y, width, height):
        self.rect = pygame.Rect(x, y, width, height)

    def draw(self, surface, colour):
        pygame.draw.rect(surface, colour, self.rect)

class Door:
    def __init__(self, x, y, width, height, active=True):
        self.active = active
        self.rect = pygame.Rect(x, y, width, height)

    def draw(self, surface, colour):
        if colour is None:
            return
        else:
            pygame.draw.rect(surface, colour, self.rect)

class Click:
    def __init__(self, x, y, width, height):
        self.rect = pygame.Rect(x, y, width, height)
    def is_clicked(self, mouse_pos):
        return self.rect.collidepoint(mouse_pos)
    
    def draw(self, surface, colour):
        pygame.draw.rect(surface, colour, self.rect)

class Img:
    def __init__(self, x, y, img_path):
        self.x = x
        self.y = y
        self.img_path = img_path
        self.img = pygame.image.load(img_path)

    def draw(self, surface):
        rect = self.img.get_rect(center=(self.x, self.y))
        surface.blit(self.img, rect)