import pygame
import sys
import ghost
import wall

class Player(pygame.sprite.Sprite):
    
    '''
    This is the Constructor function __init__
    param list: (int, int, str) x, y, filename: Set height and width and passes in filename of the pacman player image
    return (int, int, str) returns surface of image and x and y coords
    '''
    
    # SETS SPEED VECTORS
    change_x=0
    change_y=0
    
    def __init__(self,x,y):
    
        '''
        This is the Constructor function __init__
        param list: (int, int, str) x, y, filename: Set height and width and pass in filename of the pacman player image
        return (int, int, str) returns surface of image and x and y coords
        '''
        
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("pacman.png").convert()
        
        #MAKES TOP LEFT CORNER THE PASSED IN LOCATION
        self.rect = self.image.get_rect()
        self.rect.top = y
        self.rect.left = x
        self.prev_x = x
        self.prev_y = y
        
    #CLEARS SPEED OF PACMAN
    def prevdirection(self):

        '''
        This function clears the speed of the player
        param list: (object) self: refers to the object of this class, only needs self
        return: (none)
            '''
        self.prev_x = self.change_x
        self.prev_y = self.change_y
        
    #CHANGES SPEED OF PACMAN
    def changespeed(self,x,y):

        '''
        Changes the speed of the player
        param list: (int, int) x, y:
        return: (none)
        '''
        
        self.change_x+=x
        self.change_y+=y
        
    #FINDS NEW POSITION OF PACMAN
    def update(self,walls,gate):
        '''
        Gets the old position of pacman
        and new position
        param list:
            
        '''
        old_x=self.rect.left
        new_x=old_x+self.change_x
        prev_x=old_x+self.prev_x
        self.rect.left = new_x
            
        old_y=self.rect.top
        new_y=old_y+self.change_y
        prev_y=old_y+self.prev_y
        
        x_collide = pygame.sprite.spritecollide(self, walls, False)
        if x_collide:
            self.rect.left=old_x
        else:
            self.rect.top = new_y
            y_collide = pygame.sprite.spritecollide(self, walls, False)
            if y_collide:
                self.rect.top=old_y
            if gate != False:
                gate_hit = pygame.sprite.spritecollide(self, gate, False)
                if gate_hit:
                    self.rect.left=old_x
                    self.rect.top=old_y
