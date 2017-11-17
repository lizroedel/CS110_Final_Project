class Maze:
    def __init__(self):
        self.color = "black"
        self.height = 300
        self.width = 300
class Pacman:
    def __init__(self):
        self.color = 'yellow"
        self.x = 0
        self.y = 0
    def moveRight(self, right):
        self.x += right
    def moveLeft(self, left):
        self.x += left
    def moveUp(self, up):
        self.y += up
    def moveDown(self, down):
        self.y += down
class Ghost:
    def __init__(self, start:tuple):
        self.x = start[0]
        self.y = start[1]
class Food:
    def __init__(self, locate:tuple):
        self.x = locate[0]
        self.y = locate[1]
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
