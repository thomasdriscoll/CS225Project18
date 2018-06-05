#WORLD 1 --- AVL trees
# Rationale: AVL trees are binary trees and test more overall knowlege. Plus, we can always remove AVL functionality and just have a binary tree
# Game:
# -Small bubbles that follow a line and hit the root node
# -Before they hit the root, node, you have to determine whether to go right or left
# -Continue doing so until the bubble is a leaf node and determine whether an AVL rotation should occur (timer or unlimited time TBD)
# -Get that done and add on functionality (baby steps are the first steps the Flash ever took)


#Current objectives:
# - Handle "infinite" bubble generation in game loop
# - Stopping position of the bubble

#Calls the pygame library
import pygame, random, os, sys
#Optional: Sets up constants and functions in global namespace
from pygame.locals import *
#Global Color
BLACK = (0, 0, 0)

def load_image(name, colorkey=None):
    #Creates a full path for name to the numbers folder from current folder position
    #Think usr/.../cs225game/numbers
    fullname = os.path.join('numbers', name)
    #try function attempts to load image to see if that works
    try:
        image = pygame.image.load(fullname)
    #If try function fails, exits system
    except pygame.error, message:
        print 'Cannot load image:', name
        raise SystemExit, message
    #Makes a new copy of a Surface and converts color format/depth for display
    image = image.convert()
    #Sets colorkey for image
    if colorkey is not None:
    #If colorkey is -1, color of image is set to topleft pixel color of Surface
        if colorkey is -1:
            colorkey = image.get_at((0,0))
        image.set_colorkey(colorkey, RLEACCEL)
    return image, image.get_rect()

def get_number():
    num = random.randint(0, 9)
    if num == 0:
        return 'real_zero.png'
    elif num == 1:
        return 'real_one.png'
    elif num == 2:
        return 'real_two.png'
    elif num == 3:
        return 'real_three.png'
    elif num == 4:
        return 'real_four.png'
    elif num == 5:
        return 'real_five.png'
    elif num == 6:
        return 'real_six.png'
    elif num == 7:
        return 'real_seven.png'
    elif num == 8:
        return 'real_eight.png'
    elif num == 9:
        return 'real_nine.png'

class NumberPNG(pygame.sprite.Sprite):
    def __init__(self, y, x, width, movex, movey, image):
        pygame.sprite.Sprite.__init__(self)
        self.image, self.rect = load_image(image, -1)
        self.movex = movex
        self.movey = movey
        self.rect.centerx = width/2 + x
        self.rect.centery = y
    def update(self):
        newpos = self.rect.move((self.movex), (self.movey))
        self.rect = newpos

class Line(pygame.sprite.Sprite):
    def __init__(self, start_pos):
        pygame.sprite.Sprite.__init__(self)
        #Determine position of Line

#BubbleNode is going to need to be able to take two NumberPNG objects
# as well as three Line objects
class BubbleNode():
    def __init__(self, width, height, num1, num2):
        self.x = width/2
        self.y = 30
        self.movex = 0
        self.movey = 3
        self._width = width
        self._height = height
        self.num1 = NumberPNG(self.y, -10, width, self.movex, self.movey, num1)
        self.num2 = NumberPNG(self.y, 10, width, self.movex, self.movey, num2)
        self.nodes_nums = pygame.sprite.RenderPlain((self.num1, self.num2))
        self.triggered = False
    def update(self):
        if not self.triggered:
            if self.y >= self._height or self.y <= 0:
                self.movey = -self.movey
                self.num1.movey = -self.num1.movey
                self.num2.movey = -self.num2.movey
            self.y = self.y + self.movey
            self.nodes_nums.update()

    def draw(self, screen):
        BLACK = (0, 0, 0)
        pygame.draw.circle(screen, BLACK, (self.x, self.y), 50, 1)
        self.nodes_nums.draw(screen)

class BubbleNodeGroup():
    def __init__(self):
        self.bubbles = []
    def append(self, bubbleNode):
        self.bubbles.append(bubbleNode)
    def update(self):
        for node in self.bubbles:
            node.update()
    def draw(self, screen):
        for node in self.bubbles:
            node.draw(screen)

def main():
    pygame.init()
    #Set this to fullscreen in later development
    screen = pygame.display.set_mode((1000, 1000))
    width, height = screen.get_size()
    #fills in background
    background = pygame.Surface(screen.get_size())
    background = background.convert()
    background.fill((255, 255, 255))
    #Display the Background While Setup Finishes
    screen.blit(background, (0,0))
    pygame.display.flip()

    #OBJECTS
    #Create numbers png
    num1 = get_number()
    num2 = get_number()
    #numbers_png.append(one)
    #root bubble
    bubbles = BubbleNodeGroup()
    root = BubbleNode(width, height, num1, num2)
    bubbles.append(root)


    #create game clock
    clock = pygame.time.Clock()
    #Game loop
    done = False
    while not done:
        #increment clock
        clock.tick(60)
        #Check if collision will occur
        bubbles.update()
        #updates screen image (redraws screen everytime)
        screen.blit(background, (0, 0))
        bubbles.draw(screen)

        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                done = True
                break;

    pygame.quit()

if __name__ == '__main__':
        main()
