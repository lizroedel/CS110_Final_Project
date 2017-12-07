import pygame
import sys

black = (0,0,0)
white = (255,255,255)
blue = (0,0,255)
green = (0,255,0)
red = (255,0,0)
yellow = (255, 255, 0)

pygame.init()
pygame.mixer.init()
pygame.mixer.music.load('pacman.ogg')
pygame.mixer.music.play()

# Create an 660 x 810 sized screen
sze = (660,810)
screen = pygame.display.set_mode(sze)
pygame.font.init()

# This is a list of 'sprites.' Each block in the program is
# added to this list. The list is managed by a class called 'RenderPlain.'

# Set the title of the window
pygame.display.set_caption('Merry Christmas Pacman')

# Create a surface we can draw on
background = pygame.Surface(screen.get_size())

# Used for converting color maps and such
background = background.convert()

# Fill the screen with a black background
background.fill(black)

clock = pygame.time.Clock()

# This class represents the bar at the bottom that the player controls
class Wall(pygame.sprite.Sprite):
    # Constructor function
    def __init__(self,x,y,width,height, color):
        # Call the parent's constructor
        pygame.sprite.Sprite.__init__(self)
        
        # Make a green wall, of the size specified in the parameters
        self.image = pygame.Surface([width, height])
        self.image.fill(color)
        
        # Make our top-left corner the passed-in location.
        self.rect = self.image.get_rect()
        self.rect.top = y
        self.rect.left = x

'''
This creates all the walls in room 1
param list: (list) all_sprites_list: A list of every object is added to this list (block, ghost, pacman, etc.)
return: (list) returns wall_list in the form [x, y, width, height]

'''
def setupRoomOne(all_sprites_list):
    # Make the walls. (x_pos, y_pos, width, height)
    wall_list=pygame.sprite.RenderPlain()
    
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
'''
A white line that only the ghosts can cross into
param list: (list) all_sprites_list: A list of every object is added to this list (block, ghost, pacman, etc.)
return: (group/class) returns gate
'''

def setupGate(all_sprites_list):
    gate = pygame.sprite.RenderPlain()
    gate.add(Wall(270,690,120,2,white))
    all_sprites_list.add(gate)
    return gate

# This class represents the pellets
# It derives from the "sprite" class in Pygame
class Block(pygame.sprite.Sprite):
    
'''
This is the Constructor function __init__
param list: (tuple, int, int) self, color, width, height: Pass in the color of the block, and its x and y position
return: (tuple, int, int) returns surface of image, color, height, and width
'''
    def __init__(self, color, width, height):
        # Call the parent class (Sprite) constructor
        pygame.sprite.Sprite.__init__(self)
        
        # Create an image of the block, and fill it with a color.
        self.image = pygame.Surface([width, height])
        self.image.fill(white)
        self.image.set_colorkey(white)
        pygame.draw.ellipse(self.image,color,[0,0,width,height])
        
        # Fetch the rectangle object that has the dimensions of the image
        # image.
        # Update the position of this object by setting the values
        # of rect.x and rect.y
        self.rect = self.image.get_rect()

# This class represents the bar at the bottom that the player controls
class Player(pygame.sprite.Sprite):
    
    # Set speed vector
    change_x=0
    change_y=0
    
    # Constructor function
'''
This is the Constructor function __init__
param list: (int, int, str) x, y, filename: Set height and width and pass in filename of the pacman player image
return (int, int, str) returns surface of image and x and y coords
'''
    def __init__(self,x,y, filename):
        # Call the parent's constructor
        pygame.sprite.Sprite.__init__(self)
        
        # Set height, width
        self.image = pygame.image.load(filename).convert()
        
        # Make our top-left corner the passed-in location.
        self.rect = self.image.get_rect()
        self.rect.top = y
        self.rect.left = x
        self.prev_x = x
        self.prev_y = y
    
'''
This function clears the speed of the player
param list: (object) self: refers to the object of this class, only needs self
return: (none)
'''
    def prevdirection(self):
        self.prev_x = self.change_x
        self.prev_y = self.change_y

'''
Changes the speed of the player
param list: (int, int) x, y:
return: (none)
'''
    def changespeed(self,x,y):
        self.change_x+=x
        self.change_y+=y
    
'''
Find a new position for pacman
param list: (list) walls, gate: if pacman hits a wall or the gate, he returns to old x position
return: (none)
'''
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

#Inheritime Player klassist
class Ghost(Player):

'''
Change the speed of the ghost
param list: (list, object, int, int) indexes the list in [turn, steps] form
return: (int, int) returns index of turn and steps
'''
    def changespeed(self,list,ghost,turn,steps,l):
        try:
            z=list[turn][2]
            if steps < z:
                self.change_x=list[turn][0]
                self.change_y=list[turn][1]
                steps+=1
            else:
                if turn < l:
                    turn+=1
                elif ghost == "orange_ghost":
                    turn = 2
                else:
                    turn = 0
                    self.change_x=list[turn][0]
                    self.change_y=list[turn][1]
                    steps = 0
            return [turn,steps]
        except IndexError:
            return [0,0]

pink_ghost_directions = [
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

red_ghost_directions = [
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

blue_ghost_directions = [
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

orange_ghost_directions = [
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

pl = len(pink_ghost_directions)-1
bl = len(red_ghost_directions)-1
il = len(blue_ghost_directions)-1
cl = len(orange_ghost_directions)-1

#default locations for Pacman and ghosts
pacman_width = 320 #Pacman width
pacman_height = 100 #Pacman height
red_ghost_width = 300 #red ghost width
red_ghost_height = 750 #red ghost height
pink_ghost_width = 330 #pink ghost width
pink_ghost_height = 750 #pink ghost height
orange_ghost_width = 300 #orange ghost width
orange_ghost_height = 720 #orange ghost height
blue_ghost_width = 340 #blue ghost width
blue_ghost_height = 720 #blue ghost height

'''
Runs the game screen
param list: (none)
return: (none)
'''

def startGame():
    
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
    
    
    # the right pacman
    Pacman = Player( pacman_width, pacman_height, "pacman.png" )
    all_sprites_list.add(Pacman)
    pacman_collide.add(Pacman)
    
    # Create the player paddle object
    red_ghost = Ghost( red_ghost_width, red_ghost_height, "red_ghost.png" )
    monsta_list.add(red_ghost)
    all_sprites_list.add(red_ghost)
                                            
    pink_ghost = Ghost( pink_ghost_width, pink_ghost_height, "pink_ghost.png" )
    monsta_list.add(pink_ghost)
    all_sprites_list.add(pink_ghost)
                                                
    blue_ghost =Ghost( blue_ghost_width, blue_ghost_height, "blue_ghost.png" )
    monsta_list.add(blue_ghost)
    all_sprites_list.add(blue_ghost)

    orange_ghost =Ghost( orange_ghost_width, orange_ghost_height, "orange_ghost.png" )
    monsta_list.add(orange_ghost)
    all_sprites_list.add(orange_ghost)
    
                                                        
    # Draw the pellets
    for row in range(26):
        for column in range(21):
            if (row == 24 and row== 25 and row ==26) and (column == 24 and column == 25):
                continue
            else:
                block = Block(red, 4, 4)
                    
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

#bll = len(block_list)

    score = 0
    
    bll = 141
                                                                                                                    
    done = False
                                                                                                                        
    i = 0
    
    pygame.mouse.get_pressed()

    end_it=False
    while (end_it==False):
        startscreen = pygame.image.load("startscreen.png").convert()
        for event in pygame.event.get():
            if event.type==pygame.MOUSEBUTTONDOWN:
                end_it=True
        screen.blit(startscreen, [0,0])
        pygame.display.flip()
    
    ################################################
    while done == False:
        screen.fill(black)
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
                screen.fill(black)
                wall_list.draw(screen)
                gate.draw(screen)
                all_sprites_list.draw(screen)
                monsta_list.draw(screen)


 # ALL EVENT PROCESSING SHOULD GO ABOVE THIS COMMENT
 
 # ALL GAME LOGIC SHOULD GO BELOW THIS COMMENT
        Pacman.update(wall_list,gate)
        returned = pink_ghost.changespeed(pink_ghost_directions,False,p_turn,p_steps,pl)
        p_turn = returned[0]
        p_steps = returned[1]
        pink_ghost.changespeed(pink_ghost_directions,False,p_turn,p_steps,pl)
        pink_ghost.update(wall_list,False)

        returned = red_ghost.changespeed(red_ghost_directions,False,b_turn,b_steps,bl)
        b_turn = returned[0]
        b_steps = returned[1]
        red_ghost.changespeed(red_ghost_directions,False,b_turn,b_steps,bl)
        red_ghost.update(wall_list,False)
                                                                                                                                                                                                                        
        returned = blue_ghost.changespeed(blue_ghost_directions,False,i_turn,i_steps,il)
        i_turn = returned[0]
        i_steps = returned[1]
        blue_ghost.changespeed(blue_ghost_directions,False,i_turn,i_steps,il)
        blue_ghost.update(wall_list,False)
                                                                                                                                                                                                                            
        returned = orange_ghost.changespeed(orange_ghost_directions,"orange_ghost",c_turn,c_steps,cl)
        c_turn = returned[0]
        c_steps = returned[1]
        orange_ghost.changespeed(orange_ghost_directions,"orange_ghost",c_turn,c_steps,cl)
        orange_ghost.update(wall_list,False)
        
        # See if the Pacman block has collided with anything.
        blocks_hit_list = pygame.sprite.spritecollide(Pacman, block_list, True)
        
        # Check the list of collisions.
        if len(blocks_hit_list) > 0:
             score +=len(blocks_hit_list)
# ALL GAME LOGIC SHOULD GO ABOVE THIS COMMENT

# ALL CODE TO DRAW SHOULD GO BELOW THIS COMMENT

        screen.fill(black)
        wall_list.draw(screen)
        gate.draw(screen)
        all_sprites_list.draw(screen)
        monsta_list.draw(screen)
       
       #these rectangles black out the pellets outside of the maze
        rect1 = pygame.Surface((300,150))   # the width and height tuple
        rect1.set_alpha(255)            # opaqueness level from 0-255 level
        rect1.fill(black)           # this fills the entire surface
        screen.blit(rect1,(0,0))    # (0,0) are the top-left coordinates

        rect2 = pygame.Surface((360,90))
        rect2.set_alpha(255)
        rect2.fill(black)
        screen.blit(rect2,(300,0))

        rect3 = pygame.Surface((300,60))
        rect3.set_alpha(255)
        rect3.fill(black)
        screen.blit(rect3,(375,90))

        rect4 = pygame.Surface((270,60))
        rect4.set_alpha(255)
        rect4.fill(black)
        screen.blit(rect4,(0,150))

        rect5 = pygame.Surface((210,60))
        rect5.set_alpha(255)
        rect5.fill(black)
        screen.blit(rect5,(0,210))
        
        rect6 = pygame.Surface((150,120))
        rect6.set_alpha(255)
        rect6.fill(black)
        screen.blit(rect6,(0,270))
        
        rect7 = pygame.Surface((90,120))
        rect7.set_alpha(255)
        rect7.fill(black)
        screen.blit(rect7,(0,390))
        
        rect8 = pygame.Surface((255,105))
        rect8.set_alpha(255)
        rect8.fill(black)
        screen.blit(rect8,(0,705))
        
        rect9 = pygame.Surface((255,60))
        rect9.set_alpha(255)
        rect9.fill(black)
        screen.blit(rect9, (405,150))
        
        rect10 = pygame.Surface((195,60))
        rect10.set_alpha(255)
        rect10.fill(black)
        screen.blit(rect10, (465,210))

        rect11 = pygame.Surface((135,120))
        rect11.set_alpha(255)
        rect11.fill(black)
        screen.blit(rect11, (525,270))

        rect12 = pygame.Surface((75,120))
        rect12.set_alpha(255)
        rect12.fill(black)
        screen.blit(rect12, (585,390))

        rect13 = pygame.Surface((255,120))
        rect13.set_alpha(255)
        rect13.fill(black)
        screen.blit(rect13, (405,705))

        score_font = pygame.font.Font("Munro.ttf", 30)
        font = pygame.font.Font("Munro.ttf", 36)

        #adds background snowflakes
        snowflake = pygame.image.load("snowflake.png").convert()
        screen.blit(snowflake, [100,100])
        screen.blit(snowflake, [125,130])
        screen.blit(snowflake, [30,30])
        screen.blit(snowflake, [20,150])
        screen.blit(snowflake, [25,360])
        screen.blit(snowflake, [30,470])
        screen.blit(snowflake, [45,250])
        screen.blit(snowflake, [100,325])
        screen.blit(snowflake, [110,200])
        screen.blit(snowflake, [200,150])
        screen.blit(snowflake, [200,150])
        screen.blit(snowflake, [210,20])
        screen.blit(snowflake, [400,125])
        screen.blit(snowflake, [550,360])
        screen.blit(snowflake, [475,60])
        screen.blit(snowflake, [500,200])
        screen.blit(snowflake, [580,30])
        screen.blit(snowflake, [600,450])
        screen.blit(snowflake, [589,275])
        screen.blit(snowflake, [525,225])
        screen.blit(snowflake, [600,150])
        screen.blit(snowflake, [575,100])
        
        #this places the two cube blocks in the maze
        cube = pygame.image.load("cube.png").convert()
        screen.blit(cube, [145,440])
        screen.blit(cube, [505,440])
        
        #score count
        text=score_font.render("Score: "+str(score)+"/"+str(bll), True, white)
        screen.blit(text, [75, 740])
        caption = font.render("Merry Christmas Pacman", True, white)
        screen.blit(caption,[150,40])

        monsta_hit_list = pygame.sprite.spritecollide(Pacman,monsta_list,False)
        if score == bll:
            #doNext("Congratulations, you won!", 145, all_sprites_list,block_list,monsta_list,pacman_collide,wall_list,gate)
            winner = pygame.image.load("winner.png").convert()
            screen.blit(winner, [0,0])
            pygame.display.flip()
                                                                                                                                                                                                                                                            
        if monsta_hit_list:
            startscreen = pygame.image.load("gameover.png").convert()
            screen.blit(startscreen, [0,0])
            pygame.display.flip()
            doNext()
                                                                                                                                                                                                                                                                        
# ALL CODE TO DRAW SHOULD GO ABOVE THIS COMMENT
                                                                                                                                                                                                                                                                        
        pygame.display.flip()
                                                                                                                                                                                                                                                                        
        clock.tick(10)
'''
Quits game
param list: (none)
return: (none)
'''
def doNext():
    while True:
        # ALL EVENT PROCESSING SHOULD GO BELOW THIS COMMENT
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                                                        
    clock.tick(10)

startGame()

pygame.quit()
