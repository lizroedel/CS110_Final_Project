import pygame
import sys
import ghost
import wall

class Block(pygame.sprite.Sprite):
    def __init__(self, color, width, height):
        '''
        This is the Constructor function __init__
        param list: (tuple, int, int) self, color, width, height: Pass in the color of the block, and its x and y position
        return: (tuple, int, int) returns surface of image, color, height, and width
        '''
        pygame.sprite.Sprite.__init__(self)
        
        # Creates image and fills with color
        self.image = pygame.Surface([width, height])
        pygame.draw.ellipse(self.image,color,[0,0,width,height])

        self.rect = self.image.get_rect()
