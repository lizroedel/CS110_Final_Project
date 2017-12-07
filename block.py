class Block(pygame.sprite.Sprite):
    # Constructor. Pass in the color of the block,
    # and its x and y position
    def __init__(self, color, width, height):
    '''
    This is the Constructor function __init__
    param list: (tuple, int, int) self, color, width, height: Pass in the color of the block, and its x and y position
    return: (tuple, int, int) returns surface of image, color, height, and width
    '''
        # Call the parent class (Sprite) constructor
        pygame.sprite.Sprite.__init__(self)
        
        # Create an image of the block, and fill it with a color.
        self.image = pygame.Surface([width, height])
            self.image.fill(self.self.white)
            self.image.set_colorkey(self.white)
            pygame.draw.ellipse(self.image,color,[0,0,width,height])
            
            # Fetch the rectangle object that has the dimensions of the image
            # image.
            # Update the position of this object by setting the values
            # of rect.x and rect.y
            self.rect = self.image.get_rect()
