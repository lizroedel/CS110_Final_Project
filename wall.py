import pygame
import sys
import ghost
import player

class Wall(pygame.sprite.Sprite):
    def __init__(self,x,y,width,height, color):
        pygame.sprite.Sprite.__init__(self)
        
        #MAKES MAZE
        self.image = pygame.Surface([width, height])
        self.image.fill(color)
        
        self.rect = self.image.get_rect()
        self.rect.top = y
        self.rect.left = x
    
    def set_maze(all_sprites_list):
        '''
        This creates all the walls in room 1
        param list: (list) all_sprites_list: A list of every object is added to this list (block, ghost, pacman, etc.)
        return: (list) returns wall_list in the form [x, y, width, height]
        '''
        
        wall_list = pygame.sprite.RenderPlain()
        green = (0,255,0)
    
        # LIST OF WALLS in [x, y, width, height] format
        walls = [ [300,90,60,6],[300,90,6,60],[270,150,36,6],[270,150,6,66],[210,210,60,6],
                 [210,210,6,66],[150,270,60,6],[150,270,6,126],[90,390,60,6],[90,390,6,126],
                 [30,510,60,6],[30,510,6,180],[30,690,240,6],[270,690,6,120],[270,800,120,6],
                 [360,90,6,60],[360,150,30,6],[390,150,6,60],[390,210,60,6],[450,210,6,60],
                 [450,270,60,6],[510,270,6,120],[510,390,60,6],[570,390,6,120],[570,510,60,6],
                 [630,510,6,180],[390,690,246,6],[390,690,6,240],[330,210,4,60],[270,270,126,4],
                 [210,330,246,4],[330,330,4,66],[210,390,66,4],[390,390,66,4],[210,450,4,60],
                 [450,450,4,60],[270,450,126,4],[150,450,4,4],[330,450,4,66],[510,450,4,4],
                 [150,510,126,4],[390,510,126,4],[90,570,66,4],[270,570,126,4],[510,570,66,4],
                 [210,570,4,60],[450,570,4,60],[90,630,186,4],[390,630,186,4],[330,570,4,120],]
        
        # LOOPS THRU LIST AND ADDS WALL TO LIST
        for item in walls:
            wall = Wall(item[0],item[1],item[2],item[3],green)
            wall_list.add(wall)
            all_sprites_list.add(wall)

        return wall_list
