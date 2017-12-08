import pygame
import sys
from block import Block
from ghost import Ghost
from player import Player
from wall import Wall

def setupGate(all_sprites_list):
    '''
    A white line that only the ghosts can cross into
    param list: (list) all_sprites_list: A list of every object is added to this list (block, ghost, pacman, etc.)
    return: (group/class) returns gate
    '''
    
    gate = pygame.sprite.RenderPlain()
    gate.add(Wall(270,690,120,2,(255,255,255)))
    all_sprites_list.add(gate)
    
    return gate

def doNext():
    '''
    Quits game
    param list: (none)
    return: (none)
    '''
    while True:
    # ALL EVENT PROCESSING SHOULD GO BELOW THIS COMMENT
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()

    self.clock.tick(10)

class Controller():
    def __init__(self, width=660, height=810):
        #sets up pygame window and variables needed
    
        #sets up pygame
        pygame.init()
        self.width = width
        self.height = height
        self.clock = pygame.time.Clock()
        
        #creates a 660 (width) x 810 (height) screen
        self.sze = (self.width,self.height)
        self.screen = pygame.display.set_mode(self.sze)
        
        # Sets the header of the window
        self.header = pygame.display.set_caption('Merry Christmas Pacman')
        
        # Creates a surface to draw on and used for converting color maps
        self.surface = pygame.Surface(self.screen.get_size())
        self.background = self.surface.convert()
        
        #score count
        self.score = 0
        self.bll = 141
        
        #initializes pygame mixer with ogg file
        pygame.mixer.init()
        pygame.mixer.music.load('pacman.ogg')
        pygame.mixer.music.play()
        
        #fonts used in GUI
        pygame.font.init()
        self.score_font = pygame.font.Font("Munro.ttf", 30)
        self.font = pygame.font.Font("Munro.ttf", 36)
        
        #texts that appear in game screen
        self.text=self.score_font.render("Score: "+str(self.score)+"/"+str(self.bll), True, (255,255,255))
        self.caption = self.font.render("Merry Christmas Pacman", True, (255,255,255))
        
        #sets up directions of ghosts
        self.pink_ghost_directions = [ [0,15,0],[0,-30,4],[15,0,9],[0,15,11],
                                      [-15,0,23],[0,15,7],[15,0,3],[0,-15,3],
                                      [15,0,19],[0,15,3],[15,0,3],[0,15,3],
                                      [15,0,3],[0,-15,15],[-15,0,7],[0,15,3],
                                      [-15,0,19],[0,-15,11],[15,0,9] ]
        
        self.red_ghost_directions = [ [0,-15,4],[15,0,9],[0,15,11],[15,0,3],
                                     [0,15,7],[-15,0,11],[0,15,3],[15,0,15],
                                     [0,-15,15],[15,0,3],[0,-15,11],[-15,0,3],
                                     [0,-15,11],[-15,0,3],[0,-15,3],[-15,0,7],
                                     [0,-15,3],[15,0,15],[0,15,15],[-15,0,3],
                                     [0,15,3],[-15,0,3],[0,-15,7],[-15,0,3],
                                     [0,15,7],[-15,0,11],[0,-15,7],[15,0,5]]
            
        self.blue_ghost_directions = [[30,0,2],[0,-15,4],[15,0,10],[0,15,7],
                                      [15,0,3],[0,-15,3],[15,0,3],[0,-15,15],
                                      [-15,0,15],[0,15,3],[15,0,15],[0,15,11],
                                      [-15,0,3],[0,-15,7],[-15,0,11],[0,15,3],
                                      [-15,0,11],[0,15,7],[-15,0,3],[0,-15,3],
                                      [-15,0,3],[0,-15,15],[15,0,15],[0,15,3],
                                      [-15,0,15],[0,15,11],[15,0,3],[0,-15,11],
                                      [15,0,11],[0,15,3],[15,0,1],]
                                     
        self.orange_ghost_directions = [[-30,0,2],[0,-15,4],[15,0,5],[0,15,7],
                                        [-15,0,11],[0,-15,7],[-15,0,3],[0,15,7],
                                        [-15,0,7],[0,15,15],[15,0,15],[0,-15,3],
                                        [-15,0,11],[0,-15,7],[15,0,3],[0,-15,11],[15,0,9]]
                                     
        self.pl = len(self.pink_ghost_directions)-1
        self.bl = len(self.red_ghost_directions)-1
        self.il = len(self.blue_ghost_directions)-1
        self.cl = len(self.orange_ghost_directions)-1
        
        self.p_turn = 0
        self.p_steps = 0
    
        self.b_turn = 0
        self.b_steps = 0
    
        self.i_turn = 0
        self.i_steps = 0
    
        self.c_turn = 0
        self.c_steps = 0
        
        #SET LOCATIONS FOR PACMAN AND GHOSTS
        self.pacman_width = 320 #Pacman x
        self.pacman_height = 100 #Pacman y
        self.red_ghost_width = 300 #red ghost x
        self.red_ghost_height = 750 #red ghost y
        self.pink_ghost_width = 330 #pink ghost x
        self.pink_ghost_height = 750 #pink ghost y
        self.orange_ghost_width = 300 #orange ghost x
        self.orange_ghost_height = 720 #orange ghost y
        self.blue_ghost_width = 340 #blue ghost x
        self.blue_ghost_height = 720 #blue ghost y
    
    def main_loop(self):
        '''
        Runs the Starting, Game, Game Over, and Winner Screens
        param list: (none)
        return: (none)
            '''
        
        all_sprites_list = pygame.sprite.RenderPlain()
        block_list = pygame.sprite.RenderPlain()
        monsta_list = pygame.sprite.RenderPlain()
        pacman_collide = pygame.sprite.RenderPlain()
        wall_list =Wall.set_maze(all_sprites_list)
        gate = setupGate(all_sprites_list)

        #SETS PACMAN
        Pacman = Player(self.pacman_width, self.pacman_height)
        all_sprites_list.add(Pacman)
        pacman_collide.add(Pacman)

        #SETS GHOSTS
        red_ghost = Ghost( self.red_ghost_width, self.red_ghost_height, "red_ghost.png" )
        monsta_list.add(red_ghost)
        all_sprites_list.add(red_ghost)

        pink_ghost = Ghost( self.pink_ghost_width, self.pink_ghost_height, "pink_ghost.png" )
        monsta_list.add(pink_ghost)
        all_sprites_list.add(pink_ghost)
        
        blue_ghost =Ghost( self.blue_ghost_width, self.blue_ghost_height, "blue_ghost.png" )
        monsta_list.add(blue_ghost)
        all_sprites_list.add(blue_ghost)
        
        orange_ghost =Ghost( self.orange_ghost_width, self.orange_ghost_height, "orange_ghost.png" )
        monsta_list.add(orange_ghost)
        all_sprites_list.add(orange_ghost)

        #DRAWS PELLETS THAT PACMAN EATS
        for row in range(26):
            for column in range(21):
                if (row == 24 and row== 25 and row ==26) and (column == 24 and column == 25):
                    continue
                else:
                    block = Block((255,0,0), 4, 4)
                    
                    #location for pellets
                    block.rect.x = (30*column+6)+27
                    block.rect.y = (30*row+6)+27
                    
                    b_collide = pygame.sprite.spritecollide(block, wall_list, False)
                    p_collide = pygame.sprite.spritecollide(block, pacman_collide, False)
                    if b_collide:
                        continue
                    elif p_collide:
                        continue
                    else:
                        # Add the block to the list of objects
                        block_list.add(block)
                        all_sprites_list.add(block)

        pygame.mouse.get_pressed()

        #starting menu

        start_game=False
        while (start_game==False):
            startscreen = pygame.image.load("startscreen.png").convert()
            for event in pygame.event.get():
                if event.type==pygame.MOUSEBUTTONDOWN:
                    start_game=True
            self.screen.blit(startscreen, [0,0])
            pygame.display.flip()

        self.screen.fill([0,0,0])
        wall_list.draw(self.screen)
        gate.draw(self.screen)
        all_sprites_list.draw(self.screen)
        monsta_list.draw(self.screen)
        pygame.display.flip()

        #EVENT PROCESSING
        done = False
        while done == False:
            self.screen.fill((0,0,0))
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    done=True
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_DOWN:
                        img = pygame.image.load("pacmandown.png")
                        Pacman.image = img
                        Pacman.changespeed(0,30)
                    if event.key == pygame.K_RIGHT:
                        img = pygame.image.load("pacmanright.png")
                        Pacman.image = img
                        Pacman.changespeed(30,0)
                    if event.key == pygame.K_LEFT:
                        img = pygame.image.load("pacmanleft.png")
                        Pacman.image = img
                        Pacman.changespeed(-30,0)
                    if event.key == pygame.K_UP:
                        img = pygame.image.load("pacmanup.png")
                        Pacman.image = img
                        Pacman.changespeed(0,-30)

                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_RIGHT:
                        Pacman.changespeed(-30,0)
                    if event.key == pygame.K_LEFT:
                        Pacman.changespeed(30,0)
                    if event.key == pygame.K_DOWN:
                        Pacman.changespeed(0,-30)
                    if event.key == pygame.K_UP:
                        Pacman.changespeed(0,30)
                
                if event.type==pygame.MOUSEBUTTONDOWN:
                    done=True
                    #DRAWS GUI SCREEN
                    self.screen.fill([0,0,0])
                    wall_list.draw(self.screen)
                    gate.draw(self.screen)
                    all_sprites_list.draw(self.screen)
                    monsta_list.draw(self.screen)
                    pygame.display.flip()

        #PACMAN LOGIC
        Pacman.update(wall_list,gate)
        returned = pink_ghost.changespeed(self.pink_ghost_directions,False,self.p_turn,self.p_steps,self.pl)
        p_turn = returned[0]
        p_steps = returned[1]
        pink_ghost.changespeed(self.pink_ghost_directions,False,p_turn,p_steps,self.pl)
        pink_ghost.update(wall_list,False)
            
        returned = red_ghost.changespeed(self.red_ghost_directions,False,self.b_turn,self.b_steps,self.bl)
        b_turn = returned[0]
        b_steps = returned[1]
        red_ghost.changespeed(self.red_ghost_directions,False,b_turn,b_steps,self.bl)
        red_ghost.update(wall_list,False)
            
        returned = blue_ghost.changespeed(self.blue_ghost_directions,False,self.i_turn,self.i_steps,self.self.il)
        i_turn = returned[0]
        i_steps = returned[1]
        blue_ghost.changespeed(self.blue_ghost_directions,False,i_turn,i_steps,self.il)
        blue_ghost.update(wall_list,False)
            
        returned = orange_ghost.changespeed(self.orange_ghost_directions,"orange_ghost",self.c_turn,self.c_steps,self.cl)
        c_turn = returned[0]
        c_steps = returned[1]
        orange_ghost.changespeed(self.orange_ghost_directions,"orange_ghost",c_turn,c_steps,self.cl)
        orange_ghost.update(wall_list,False)

        # CHECKS IF PELLETS ARE EATEN
        blocks_hit_list = pygame.sprite.spritecollide(Pacman, block_list, True)
    
        # CHECKS COLLISION
        if len(blocks_hit_list) > 0:
            score +=len(blocks_hit_list)

def main():
    main_window = Controller()
    main_window.main_loop()
main()





