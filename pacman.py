import pygame
import sys
import ghost
import block
import player
import wall

class Controller:
    def __init__(self):
        #initializes pygame module
        pygame.init()
        
        #initializes pygame mixer with ogg file
        pygame.mixer.init()
        pygame.mixer.music.load('pacman.ogg')
        pygame.mixer.music.play()

        #creates a 660 (width) x 810 (height) screen
        self.sze = (660,810)
        self.screen = pygame.display.set_mode(self.sze)

        # Creates a surface to draw on and used for converting color maps
        self.surface = pygame.Surface(self.screen.get_size())
        self.background = self.surface.convert()
        
        # Sets the header of the window
        self.header = pygame.display.set_caption('Merry Christmas Pacman')

        #colors frequently used
        self.black = (0,0,0)
        self.white = (255,255,255)
        self.green = (0,255,0)
        self.red = (255,0,0)
        
        self.clock = pygame.time.Clock()
        
        #fonts
        self.score_font = pygame.font.Font("Munro.ttf", 30)
        self.font = pygame.font.Font("Munro.ttf", 36)

        #score count
        self.score = 0
        self.bll = 141
        self.text=self.score_font.render("Score: "+str(self.score)+"/"+str(self.bll), True, self.white)
        
        self.caption = self.font.render("Merry Christmas Pacman", True, self.white)
        
        self.pink_ghost_directions = [
                                      [0,15,0],
                                      [0,-30,4],
                                      [15,0,9],
                                      [0,15,11],
                                      [-15,0,23],
                                      [0,15,7],
                                      [15,0,3],
                                      [0,-15,3],
                                      [15,0,19],
                                      [0,15,3],
                                      [15,0,3],
                                      [0,15,3],
                                      [15,0,3],
                                      [0,-15,15],
                                      [-15,0,7],
                                      [0,15,3],
                                      [-15,0,19],
                                      [0,-15,11],
                                      [15,0,9]
                                      ]

        self.red_ghost_directions = [
                                     [0,-15,4],
                                     [15,0,9],
                                     [0,15,11],
                                     [15,0,3],
                                     [0,15,7],
                                     [-15,0,11],
                                     [0,15,3],
                                     [15,0,15],
                                     [0,-15,15],
                                     [15,0,3],
                                     [0,-15,11],
                                     [-15,0,3],
                                     [0,-15,11],
                                     [-15,0,3],
                                     [0,-15,3],
                                     [-15,0,7],
                                     [0,-15,3],
                                     [15,0,15],
                                     [0,15,15],
                                     [-15,0,3],
                                     [0,15,3],
                                     [-15,0,3],
                                     [0,-15,7],
                                     [-15,0,3],
                                     [0,15,7],
                                     [-15,0,11],
                                     [0,-15,7],
                                     [15,0,5]
                                     ]

        self.blue_ghost_directions = [
                                      [30,0,2],
                                      [0,-15,4],
                                      [15,0,10],
                                      [0,15,7],
                                      [15,0,3],
                                      [0,-15,3],
                                      [15,0,3],
                                      [0,-15,15],
                                      [-15,0,15],
                                      [0,15,3],
                                      [15,0,15],
                                      [0,15,11],
                                      [-15,0,3],
                                      [0,-15,7],
                                      [-15,0,11],
                                      [0,15,3],
                                      [-15,0,11],
                                      [0,15,7],
                                      [-15,0,3],
                                      [0,-15,3],
                                      [-15,0,3],
                                      [0,-15,15],
                                      [15,0,15],
                                      [0,15,3],
                                      [-15,0,15],
                                      [0,15,11],
                                      [15,0,3],
                                      [0,-15,11],
                                      [15,0,11],
                                      [0,15,3],
                                      [15,0,1],
                                      ]

        self.orange_ghost_directions = [
                                        [-30,0,2],
                                        [0,-15,4],
                                        [15,0,5],
                                        [0,15,7],
                                        [-15,0,11],
                                        [0,-15,7],
                                        [-15,0,3],
                                        [0,15,7],
                                        [-15,0,7],
                                        [0,15,15],
                                        [15,0,15],
                                        [0,-15,3],
                                        [-15,0,11],
                                        [0,-15,7],
                                        [15,0,3],
                                        [0,-15,11],
                                        [15,0,9],
                                        ]

        self.pl = len(self.pink_ghost_directions)-1
        self.bl = len(self.red_ghost_directions)-1
        self.il = len(self.blue_ghost_directions)-1
        self.cl = len(self.orange_ghost_directions)-1
        
        self.pacmanimage = pygame.image.load("pacman.png").convert()

        #default locations for Pacman and ghosts
        self.pacman_width = 320 #Pacman width
        self.pacman_height = 100 #Pacman height
        self.red_ghost_width = 300 #red ghost width
        self.red_ghost_height = 750 #red ghost height
        self.pink_ghost_width = 330 #pink ghost width
        self.pink_ghost_height = 750 #pink ghost height
        self.orange_ghost_width = 300 #orange ghost width
        self.orange_ghost_height = 720 #orange ghost height
        self.blue_ghost_width = 340 #blue ghost width
        self.blue_ghost_height = 720 #blue ghost height
    
    def startGame():
    '''
        Runs the game screen
        param list: (none)
        return: (none)
    '''
        all_sprites_list = pygame.sprite.RenderPlain()
    
        block_list = pygame.sprite.RenderPlain()
    
        monsta_list = pygame.sprite.RenderPlain()
    
        pacman_collide = pygame.sprite.RenderPlain()
    
        wall_list = setupRoomOne(all_sprites_list)
    
        gate = setupGate(all_sprites_list)
    
        p_turn = 0
        p_steps = 0
    
        b_turn = 0
        b_steps = 0
    
        i_turn = 0
        i_steps = 0
    
        c_turn = 0
        c_steps = 0
    
    
        # the pacman
        Pacman = Player( self.pacman_width, self.pacman_height )
        all_sprites_list.add(Pacman)
        pacman_collide.add(Pacman)
    
        # Create the player paddle object
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
    
    
        # Draw the pellets
        for row in range(26):
            for column in range(21):
                if (row == 24 and row== 25 and row ==26) and (column == 24 and column == 25):
                    continue
                else:
                    block = Block(self.red, 4, 4)
                
                    # Set a random location for the pellet
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
    
        done = False
    
        i = 0
    
        pygame.mouse.get_pressed()
    
        end_it=False
        while (end_it==False):
            startscreen = pygame.image.load("startscreen.png").convert()
        for event in pygame.event.get():
            if event.type==pygame.MOUSEBUTTONDOWN:
                end_it=True
        self.screen.blit(startscreen, [0,0])
        pygame.display.flip()

    ################################################
        while done == False:
            self.screen.fill(self.black)
        # ALL EVENT PROCESSING SHOULD GO BELOW THIS COMMENT
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    done=True
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_DOWN:
                        Pacman.changespeed(0,30)
                    if event.key == pygame.K_RIGHT:
                        Pacman.changespeed(30,0)
                    if event.key == pygame.K_LEFT:
                            Pacman.changespeed(-30,0)
                    if event.key == pygame.K_UP:
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
        # ALL CODE TO DRAW SHOULD GO BELOW THIS COMMENT
        self.screen.fill(self.black)
        wall_list.draw(self.screen)
        gate.draw(self.screen)
        all_sprites_list.draw(self.screen)
        monsta_list.draw(self.screen)
        
        
        # ALL EVENT PROCESSING SHOULD GO ABOVE THIS COMMENT
        
        # ALL GAME LOGIC SHOULD GO BELOW THIS COMMENT
        Pacman.update(wall_list,gate)
        returned = pink_ghost.changespeed(self.pink_ghost_directions,False,p_turn,p_steps,self.pl)
        p_turn = returned[0]
        p_steps = returned[1]
        pink_ghost.changespeed(self.pink_ghost_directions,False,p_turn,p_steps,self.pl)
        pink_ghost.update(wall_list,False)
        
        returned = red_ghost.changespeed(self.red_ghost_directions,False,b_turn,b_steps,self.bl)
        b_turn = returned[0]
        b_steps = returned[1]
        red_ghost.changespeed(self.red_ghost_directions,False,b_turn,b_steps,self.bl)
        red_ghost.update(wall_list,False)
        
        returned = blue_ghost.changespeed(self.blue_ghost_directions,False,i_turn,i_steps,self.self.il)
        i_turn = returned[0]
        i_steps = returned[1]
        blue_ghost.changespeed(self.blue_ghost_directions,False,i_turn,i_steps,self.il)
        blue_ghost.update(wall_list,False)
        
        returned = orange_ghost.changespeed(self.orange_ghost_directions,"orange_ghost",c_turn,c_steps,self.cl)
        c_turn = returned[0]
        c_steps = returned[1]
        orange_ghost.changespeed(self.orange_ghost_directions,"orange_ghost",c_turn,c_steps,self.cl)
        orange_ghost.update(wall_list,False)
        
        # See if the Pacman block has collided with anything.
        blocks_hit_list = pygame.sprite.spritecollide(Pacman, block_list, True)
        
        # Check the list of collisions.
        if len(blocks_hit_list) > 0:
            score +=len(blocks_hit_list)
        # ALL GAME LOGIC SHOULD GO ABOVE THIS COMMENT
        
        # ALL CODE TO DRAW SHOULD GO BELOW THIS COMMENT
        
        self.screen.fill(self.black)
        wall_list.draw(self.screen)
        gate.draw(self.screen)
        all_sprites_list.draw(self.screen)
        monsta_list.draw(self.screen)
        
        #these rectangles black out the pellets outside of the maze
        rect1 = pygame.Surface((300,150))   # the width and height tuple
        rect1.set_alpha(255)            # opaqueness level from 0-255 level
        rect1.fill(self.black)           # this fills the entire surface
        self.screen.blit(rect1,(0,0))    # (0,0) are the top-left coordinates
    
        rect2 = pygame.Surface((360,90))
        rect2.set_alpha(255)
        rect2.fill(self.black)
        self.screen.blit(rect2,(300,0))
    
        rect3 = pygame.Surface((300,60))
        rect3.set_alpha(255)
        rect3.fill(self.black)
        self.screen.blit(rect3,(375,90))
        
        rect4 = pygame.Surface((270,60))
        rect4.set_alpha(255)
        rect4.fill(self.black)
        self.screen.blit(rect4,(0,150))
    
        rect5 = pygame.Surface((210,60))
        rect5.set_alpha(255)
        rect5.fill(self.black)
        self.screen.blit(rect5,(0,210))
    
        rect6 = pygame.Surface((150,120))
        rect6.set_alpha(255)
        rect6.fill(self.black)
        self.screen.blit(rect6,(0,270))
        
        rect7 = pygame.Surface((90,120))
        rect7.set_alpha(255)
        rect7.fill(self.black)
        self.screen.blit(rect7,(0,390))
    
        rect8 = pygame.Surface((255,105))
        rect8.set_alpha(255)
        rect8.fill(self.black)
        self.screen.blit(rect8,(0,705))
        
        rect9 = pygame.Surface((255,60))
        rect9.set_alpha(255)
        rect9.fill(self.black)
        self.screen.blit(rect9, (405,150))
        
        rect10 = pygame.Surface((195,60))
        rect10.set_alpha(255)
        rect10.fill(self.black)
        self.screen.blit(rect10, (465,210))
        
        rect11 = pygame.Surface((135,120))
        rect11.set_alpha(255)
        rect11.fill(self.black)
        self.screen.blit(rect11, (525,270))
        
        rect12 = pygame.Surface((75,120))
        rect12.set_alpha(255)
        rect12.fill(self.black)
        self.screen.blit(rect12, (585,390))
        
        rect13 = pygame.Surface((255,120))
        rect13.set_alpha(255)
        rect13.fill(self.black)
        self.screen.blit(rect13, (405,705))
    
        #adds background snowflakes
        snowflake = pygame.image.load("snowflake.png").convert()
        self.screen.blit(snowflake, [100,100])
        self.screen.blit(snowflake, [125,130])
        self.screen.blit(snowflake, [30,30])
        self.screen.blit(snowflake, [20,150])
        self.screen.blit(snowflake, [25,360])
        self.screen.blit(snowflake, [30,470])
        self.screen.blit(snowflake, [45,250])
        self.screen.blit(snowflake, [100,325])
        self.screen.blit(snowflake, [110,200])
        self.screen.blit(snowflake, [200,150])
        self.screen.blit(snowflake, [200,150])
        self.screen.blit(snowflake, [210,20])
        self.screen.blit(snowflake, [400,125])
        self.screen.blit(snowflake, [550,360])
        self.screen.blit(snowflake, [475,60])
        self.screen.blit(snowflake, [500,200])
        self.screen.blit(snowflake, [580,30])
        self.screen.blit(snowflake, [600,450])
        self.screen.blit(snowflake, [589,275])
        self.screen.blit(snowflake, [525,225])
        self.screen.blit(snowflake, [600,150])
        self.screen.blit(snowflake, [575,100])
    
        #this places the two cube blocks in the maze
        cube = pygame.image.load("cube.png").convert()
        self.screen.blit(cube, [145,440])
        self.screen.blit(cube, [505,440])

        self.screen.blit(self.text, [75, 740])
        self.screen.blit(self.caption,[150,40])
        
        monsta_hit_list = pygame.sprite.spritecollide(Pacman,monsta_list,False)
        if score == bll:
            winner = pygame.image.load("winner.png").convert()
            self.screen.blit(winner, [0,0])
            pygame.display.flip()

        if monsta_hit_list:
            startscreen = pygame.image.load("gameover.png").convert()
            self.screen.blit(startscreen, [0,0])
            pygame.display.flip()
            doNext()

    # ALL CODE TO DRAW SHOULD GO ABOVE THIS COMMENT

        self.clock.tick(10)

        pygame.font.init()


    # Fill the screen with a black background
        self.background.fill(self.black)

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

# This creates all the walls in room 1
def setupRoomOne(all_sprites_list):
    '''
        This creates all the walls in room 1
        param list: (list) all_sprites_list: A list of every object is added to this list (block, ghost, pacman, etc.)
        return: (list) returns wall_list in the form [x, y, width, height]
        '''
    
    # Make the walls. (x_pos, y_pos, width, height)
    wall_list=pygame.sprite.RenderPlain()
    green =(0,255,0)
    
    # This is a list of walls. Each is in the form [x, y, width, height]
    walls = [ [300,90,60,6],
             [300,90,6,60],
             [270,150,36,6],
             [270,150,6,66],
             [210,210,60,6],
             [210,210,6,66],
             [150,270,60,6],
             [150,270,6,126],
             [90,390,60,6],
             [90,390,6,126],
             [30,510,60,6],
             [30,510,6,180],
             [30,690,240,6],
             [270,690,6,120],
             [270,800,120,6],
             [360,90,6,60],
             [360,150,30,6],
             [390,150,6,60],
             [390,210,60,6],
             [450,210,6,60],
             [450,270,60,6],
             [510,270,6,120],
             [510,390,60,6],
             [570,390,6,120],
             [570,510,60,6],
             [630,510,6,180],
             [390,690,246,6],
             [390,690,6,240],
             [330,210,4,60],
             [270,270,126,4],
             [210,330,246,4],
             [330,330,4,66],
             [210,390,66,4],
             [390,390,66,4],
             [210,450,4,60],
             [450,450,4,60],
             [270,450,126,4],
             [150,450,4,4],
             [330,450,4,66],
             [510,450,4,4],
             [150,510,126,4],
             [390,510,126,4],
             [90,570,66,4],
             [270,570,126,4],
             [510,570,66,4],
             [210,570,4,60],
             [450,570,4,60],
             [90,630,186,4],
             [390,630,186,4],
             [330,570,4,120],
             #[330,750,4,6],
             ]
        
        # Loop through the list. Create the wall, add it to the list
        for item in walls:
            wall=Wall(item[0],item[1],item[2],item[3],green)
            wall_list.add(wall)
            all_sprites_list.add(wall)

# return our new list
return wall_list

def setupGate(all_sprites_list):
'''
    A white line that only the ghosts can cross into
    param list: (list) all_sprites_list: A list of every object is added to this list (block, ghost, pacman, etc.)
    return: (group/class) returns gate
    '''
        gate = pygame.sprite.RenderPlain()
        gate.add(Wall(270,690,120,2,self.white))
        all_sprites_list.add(gate)
        return gate



def main():
    wn = Controller()
    Controller.startGame()
    pygame.quit()
main()

