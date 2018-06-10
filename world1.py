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

#Given a number between 0-9, returns the associated image
def get_numberimage(num):
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

#Creates the Number object, which is basically a dependent of the BubbleNode
#Moves with its associated Node object
class NumberPNG(pygame.sprite.Sprite):
    def __init__(self, y, x, width, movex, movey, image):
        pygame.sprite.Sprite.__init__(self)
        self.image, self.rect = load_image(image, -1)
        self.rect.centerx = width/2 + x
        self.rect.centery = y
    #To make sure the numbers move with nodes, it takes their current speed as update parameters
    def update(self, movex, movey):
        self.rect = self.rect.move(movex, movey)

class BubbleNode():
    def __init__(self, width, height):
        #Starting coordinates, size and speed
        self.x = width/2
        self.y = 30
        self.movex = 0
        self.movey = 3
        self.radius = 35
        #Screen width and height so I don't have to think about adjustment later
        self._width = width
        self._height = height
        #Get nodes numbers and set them up for updating
        num1 = random.randint(0, 9)
        num2 = random.randint(0, 9)
        self.value = num1*10 + num2
        self.num1 = NumberPNG(self.y, -10, width, self.movex, self.movey, get_numberimage(num1))
        self.num2 = NumberPNG(self.y, 10, width, self.movex, self.movey, get_numberimage(num2))
        self.nodes_nums = pygame.sprite.RenderPlain((self.num1, self.num2))
        #Parameter that holds whether to go right or left down tree
        self.direction = None
    #Updates the current position of the BubbleNode object and makes it bounce off walls if necessary
    def update(self):
        if self.y >= self._height - self.radius or self.y <= 0:
            self.movey = -self.movey
        if self.x < self.radius or self.x > (self._width - self.radius):
            self.movex = -self.movex
        self.y = self.y + self.movey
        self.x = self.x + self.movex
        self.nodes_nums.update(self.movex, self.movey)
    #Draws Node and nodes numbers
    def draw(self, screen):
        BLACK = (0, 0, 0)
        pygame.draw.circle(screen, BLACK, (self.x, self.y), self.radius, 1)
        self.nodes_nums.draw(screen)

class BubbleNodeGroup():
    #List of the nodes on the screen
    def __init__(self):
        self.bubbles = []
    #Easy way to add nodes to the current node list
    def append(self, bubbleNode):
        self.bubbles.append(bubbleNode)
    #Checks for collision and then calls update function for each node
    def update(self):
        self.collision(0)
        for node in self.bubbles:
            node.update()
    #Changes properties of the Node if a significant game event occurs  -- STILL BUILDING
    def collision(self, i):
        i = 0 #Temporary
        current = self.bubbles[len(self.bubbles) - 1]
        root = self.bubbles[i]
        if root.y - current.y <= 50:
            current.movex = 1
            current.movey = 0
    #Calls draw function for each objects
    def draw(self, screen):
        for node in self.bubbles:
            node.draw(screen)

def main():
    # ------ PYGAME SETUP --------------
    pygame.init()
    #Set this to fullscreen in later development
    screen = pygame.display.set_mode((1000, 1000))
    width, height = screen.get_size()
    #fills in background
    background = pygame.Surface(screen.get_size())
    background = background.convert()
    #Color of background, potentially have pretty background later
    background.fill((255, 255, 255))
    #Display the Background While Setup Finishes
    screen.blit(background, (0,0))
    pygame.display.flip()
    #create game clock
    clock = pygame.time.Clock()

    # ------ OBJECTS ------------
    #Makes group of Nodes to handle
    bubbles = BubbleNodeGroup()
    #root bubble and overriding its properties
    root = BubbleNode(width, height)
    root.movey = 0
    root.x = width/2
    root.y = height/4
    root.num1.movey = 0
    root.num2.movey = 0
    root.num1.rect.centery = height/4
    root.num2.rect.centery = height/4
    #Add root to bubbles group
    bubbles.append(root)

    # ---------OBJECTS AND FUNCTIONS FOR TESTING --------------
    bubble1 = BubbleNode(width, height)
    bubbles.append(bubble1)
    #This serves to remind me of how to add infinite number of elements
    #By doing bubbles.append(BubbleNode(width, height)) in the main game loop, I should be
    #able to work around screen size / number of nodes issue
    # for i in range(1, 3):
    #     bubbles.append(BubbleNode(width,height))

    #Game loop
    main = True
    while main:
        #increment clock
        clock.tick(60)
        pygame.display.flip()

        # ----- EVENT HANDLING ---------
        #Checks if exit event occurs
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                main = False
                break;
        #Checks if 'A''D' '<-'key or  '->'key are called
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT or event.key == ord('a'):
                bubbles.bubbles[1].direction = 'left'
            if event.key == pygame.K_RIGHT or event.key == ord('d'):
                bubbles.bubbles[1].direction = 'right'

        #Update all objects
        bubbles.update()
        #updates screen image (redraws screen everytime)
        screen.blit(background, (0, 0))
        bubbles.draw(screen)

    pygame.quit()

if __name__ == '__main__':
        main()
