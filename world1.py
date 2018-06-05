#WORLD 1 --- AVL trees
# Rationale: AVL trees are binary trees and test more overall knowlege. Plus, we can always remove AVL functionality and just have a binary tree
# Game:
# -Small bubbles that follow a line and hit the root node
# -Before they hit the root, node, you have to determine whether to go right or left
# -Continue doing so until the bubble is a leaf node and determine whether an AVL rotation should occur (timer or unlimited time TBD)
# -Get that done and add on functionality (baby steps are the first steps the Flash ever took)


#Current objectives:
# 1) Create the bubble object
# 2) Create the line object with positioning
# 3)

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

class NumberPNG(pygame.sprite.Sprite):
    def __init__(self, width, height, image):
        pygame.sprite.Sprite.__init__(self)
        self.image, self.rect = load_image(image, -1)
        self.movex = 0
        self.movey = 5
        self.rect.centery = height/3
    def update(self):
        newpos = self.rect.move((self.movex), (self.movey))
        self.rect = newpos

class Line(pygame.sprite.Sprite):
    def __init__(self, width, height, screen):
        pygame.sprite.Sprite.__init__(self)

#BubbleNode is going to need to be able to take two NumberPNG objects
# as well as three Line objects
class BubbleNode():
    def __init__(self, width, height, num1, num2):
        self.x = width/2
        self.y = height/3
        self.y_speed = 5
        self._width = width
        self._height = height
        self.num1 = NumberPNG(width, height, num1)
        self.num2 = NumberPNG(width, height, num2)
        self.num1.rect.centerx = width/2 - 10
        self.num2.rect.centerx = width/2 + 10
        self.num1.movey = 5
        self.num2.movey = 5
        self.nodes_nums = pygame.sprite.RenderPlain((self.num1, self.num2))
    def update(self):
        if self.y >= self._height or self.y <= 0:
            self.y_speed = -self.y_speed
            self.num1.movey = -self.num1.movey
            self.num2.movey = -self.num2.movey
        self.y = self.y + self.y_speed
        self.nodes_nums.update()
    def draw(self, screen):
        BLACK = (0, 0, 0)
        pygame.draw.circle(screen, BLACK, (self.x, self.y), 50, 1)
        self.nodes_nums.draw(screen)

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
    numbers_png = []
    num1 = 'real_zero.png'
    num2 = 'real_one.png'
    #numbers_png.append(one)
    #root bubble
    bubble1 = BubbleNode(width, height, num1, num2)


    #create game clock
    clock = pygame.time.Clock()
    #Game loop
    done = False
    while not done:
        #increment clock
        clock.tick(60)
        #Check if collision will occur
        bubble1.update()
        #updates screen image (redraws screen everytime)
        screen.blit(background, (0, 0))
        bubble1.draw(screen)

        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                done = True
                break;

    pygame.quit()

if __name__ == '__main__':
        main()
