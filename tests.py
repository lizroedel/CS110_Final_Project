import pygame
class Maze(pygame.sprite.Sprite):
    def __init__(self, height, width, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.height = height
        self.width = width
        self.wall = pygame.Surface([width, height])
        self.wall.fill = "blue"
        self.rect = self.wall.get_rect()
        self.rect.x = x
        self.rect.y = y
   def setMaze()
        walls = []   #list of tuples of walls in the form (height, width, x, y)
        
class Pacman:
    def __init__(self, pacImage):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(pacImage).convert_alpha()
        self.x = 0
        self.y = 0
        self.speed = 4
        self.health = 3
    def moveRight(self):
        self.x += self.speed
    def moveLeft(self):
        self.x -= self.speed
    def moveUp(self):
        self.y += self.speed
    def moveDown(self):
        self.y -= self.speed
    def
class Ghost:
    def __init__(self, start:tuple):
        self.x = start[0]
        self.y = start[1]
class Food:
    def __init__(self, locate:tuple, foodImage):
        self.x = locate[0]
        self.y = locate[1]
        self.radius = 2
        self.color = "orange"
def main():
    print("#### Testing pacman model ####")
    test_pacman = pacman.Pacman()

    print("=====Standard Input Test=====")
    test_pacman.moveRight(5)
    assert test_pacman.getCoordinates() == (5,0)

    print("=====Zero Input Test=====")
    test_pacman.moveRight(0)
    asset test_pacman.getCoordinates() == (5,0)

    print("=====Negative Input Test=====")
    test_pacman.moveRight(-1)
    assert test_pacman.getCoordinates() == (4,0)

    print("=====Standard Input Test=====")
    test_pacman.moveLeft(5)
    assert test_pacman.getCoordinates() == (5,0)

    print("=====Zero Input Test=====")
    test_pacman.moveLeft(0)
    asset test_pacman.getCoordinates() == (5,0)

    print("=====Negative Input Test=====")
    test_pacman.moveLeft(-1)
    assert test_pacman.getCoordinates() == (4,0)

    print("=====Standard Input Test=====")
    test_pacman.moveUp(5)
    assert test_pacman.getCoordinates() == (5,0)

    print("=====Zero Input Test=====")
    test_pacman.moveUp(0)
    asset test_pacman.getCoordinates() == (5,0)

    print("=====Negative Input Test=====")
    test_pacman.moveUp(-1)
    assert test_pacman.getCoordinates() == (4,0)

    print("=====Standard Input Test=====")
    test_pacman.moveDown(5)
    assert test_pacman.getCoordinates() == (5,0)

    print("=====Zero Input Test=====")
    test_pacman.moveDown(0)
    asset test_pacman.getCoordinates() == (5,0)

    print("=====Negative Input Test=====")
    test_pacman.moveDown(-1)
    assert test_pacman.getCoordinates() == (4,0)


main()
