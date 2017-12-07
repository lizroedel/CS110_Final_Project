import pygame
import sys

class player(pygame.sprite.Sprite):
    '''
    This is the Constructor function __init__
    param list: (int, int, str) x, y, filename: Set height and width and pass in filename of the pacman player image
    return (int, int, str) returns surface of image and x and y coords
    '''
    
    # Set speed vector
    change_x=0
    change_y=0
        
        # Constructor function
    def __init__(self,x,y):
    '''
    This is the Constructor function __init__
    param list: (int, int, str) x, y, filename: Set height and width and pass in filename of the pacman player image
    return (int, int, str) returns surface of image and x and y coords
    '''
        # Call the parent's constructor
        pygame.sprite.Sprite.__init__(self)
        
            # Make our top-left corner the passed-in location.
        self.rect = self.pacmanimage.get_rect()
        self.rect.top = y
        self.rect.left = x
        self.prev_x = x
        self.prev_y = y
        
        # Clear the speed of the player
    def prevdirection(self):
    '''
    This function clears the speed of the player
    param list: (object) self: refers to the object of this class, only needs self
    return: (none)
    '''
        self.prev_x = self.change_x
        self.prev_y = self.change_y
        
        # Change the speed of the player
    def changespeed(self,x,y):
    '''
    Changes the speed of the player
    param list: (int, int) x, y:
    return: (none)
    '''
        self.change_x+=x
        self.change_y+=y
        
        # Find a new position for pacmam
    def update(self,walls,gate):
        # Get the old position, in case we need to go back to it
            
        old_x=self.rect.left
        new_x=old_x+self.change_x
        prev_x=old_x+self.prev_x
        self.rect.left = new_x
            
        old_y=self.rect.top
        new_y=old_y+self.change_y
        prev_y=old_y+self.prev_y
            
            # Did this update cause us to hit a wall?
        x_collide = pygame.sprite.spritecollide(self, walls, False)
        if x_collide:
            # Whoops, hit a wall. Go back to the old position
            self.rect.left=old_x
        # self.rect.top=prev_y
        # y_collide = pygame.sprite.spritecollide(self, walls, False)
        # if y_collide:
            #     # Whoops, hit a wall. Go back to the old position
            #     self.rect.top=old_y
            #     print('a')
        else:
                
            self.rect.top = new_y
                
                # Did this update cause us to hit a wall?
            y_collide = pygame.sprite.spritecollide(self, walls, False)
            if y_collide:
                    # Whoops, hit a wall. Go back to the old position
                self.rect.top=old_y
            # self.rect.left=prev_x
            # x_collide = pygame.sprite.spritecollide(self, walls, False)
            # if x_collide:
            #     # Whoops, hit a wall. Go back to the old position
            #     self.rect.left=old_x
            #     print('b')
            
            if gate != False:
                gate_hit = pygame.sprite.spritecollide(self, gate, False)
                if gate_hit:
                    self.rect.left=old_x
                    self.rect.top=old_y
