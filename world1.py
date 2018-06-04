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
def load_image(name):
    #Creates a full path for name to the data subdirectory
    #Think linux: /home/user/directory/subdirectory/etc./data
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
    #If colorkey is -1, color of image is set to topleft pixel color
        if colorkey is -1:
            colorkey = image.get_at((0,0))
        image.set_colorkey(colorkey, RLEACCEL)
    return image, image.get_rect()

class NumberPNG(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image, self.rect = load_image('real_zero', -1)
    def draw(self):

class BubbleNode():
    def __init__(self, width, height, screen):
        self.x = width/2
        self.y = height/3
        self.y_speed = 5
        self.screen = screen
        self._width = width
        self._height = height
    def update(self):
        if self.y >= self._height or self.y <= 0:
            self.y_speed = -self.y_speed
        self.y = self.y + self.y_speed
    def draw(self):
        BLACK = (0, 0, 0)
        pygame.draw.circle(self.screen, BLACK, (self.x, self.y), 50, 1)

def main():
    pygame.init()
    screen = pygame.display.set_mode((400, 500))
    width, height = screen.get_size()
    #fills in background
    background = pygame.Surface(screen.get_size())
    background = background.convert()
    background.fill((250, 250, 250))
    #Display the Background While Setup Finishes
    screen.blit(background, (0,0))
    pygame.display.flip()
    #OBJECTS GO HERE
    bubble1 = BubbleNode(width, height, screen)
    #Create numbers png

    #create game clock
    clock = pygame.time.Clock()
    #Game loop
    done = False
    while not done:
        #increment clock
        clock.tick(60)
        #update screen
        #bubble1.update()
        #Check if collision will occur
        #updates screen image (redraws screen everytime)
        screen.blit(background, (0, 0))
        bubble1.draw()
        number0.draw()
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                done = True
                break;

    pygame.quit()

if __name__ == '__main__':
        main()
