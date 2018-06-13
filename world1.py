#WORLD 1 --- binary trees
# Rationale: binary trees are binary trees and test more overall knowlege. Plus, we can always remove AVL functionality and just have a binary tree
# Game:
# -Small bubbles that follow a line and hit the root node
# -Before they hit the root, node, you have to determine whether to go right or left
# -Continue doing so until the bubble is a leaf node
# -Get that done and add on functionality (baby steps are the first steps the Flash ever took)


#Current objectives:
# - Some collisions between separate branches that result in a child having the wrong parent
# - Ending conditions
# - There's a legimate question of whether this would be better as a learning tool or as a game -- I'm thinking learning tool

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

class Tree():
    def __init__(self, x, y, left, right):
        self.x = x
        self.y = y
        num1 = random.randint(0, 9)
        num2 = random.randint(0, 9)
        self.value = num1*10 + num2
        self.left = None
        self.right = None
        self.parent = None
        self.level = 1

class Professor(pygame.sprite.Sprite):
    def __init__ (self, width, height, prof):
        pygame.sprite.Sprite.__init__(self)
        self.image, self.rect = load_image(prof, -1)
        self.rect.centerx = self.rect.width/2
        self.rect.centery = height/8

    def update(self):
        self.rect = self.rect

# class SpeechBubble(pygame.sprite.Sprite):
#     def __init__ (self, width, height, prof_width, speech):
#         pygame.sprite.Sprite.__init__(self)
#         self.image, self.rect = load_image(speech, -1)
#         self.rect.centerx = prof_width + self.rect.width/2
#         self.rect.centery = height/8
#
#     def update(self):
#         self.rect = self.rect

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
        #Connects position in binary tree to BubbleNode object
        self.tree = Tree(self.x, self.y, None, None)
        #Get nodes numbers and set them up for updating
        self.num1 = NumberPNG(self.y, -10, width, self.movex, self.movey, get_numberimage(self.tree.value / 10))
        self.num2 = NumberPNG(self.y, 10, width, self.movex, self.movey, get_numberimage(self.tree.value % 10))
        self.nodes_nums = pygame.sprite.RenderPlain((self.num1, self.num2))
        #Parameter that holds whether collision has occured
        self.collision = False
        #Determines whether to go right or left down tree
        self.direction = 'None'
        self.finished = False
    #Updates the current position of the BubbleNode object and makes it bounce off walls if necessary
    def update(self):
        #four cases: initial, moving along tree, collision, stopped
        self.finished = self.is_finished()
        if self.finished:
            self.movex = 0
            self.movey = 0
            self.nodes_nums.update(self.movex, self.movey)
        elif self.collision:
            if self.direction == 'None':
                pass
                # print("Error, dumb dumb")
                # pygame.quit()
            elif self.direction == 'right':
                #Add value check to make sure this correct
                self.movex = 3
                self.movey = 2
                self.collision = False
                self.direction = 'None'
            elif self.direction == 'left':
                self.movex = -3
                self.movey = 2
                self.collision = False
                self.direction = 'None'
        else:
            self.y = self.y + self.movey
            self.x = self.x + self.movex
            self.tree.x = self.x
            self.tree.y = self.y
            self.nodes_nums.update(self.movex, self.movey)

    def is_finished(self):
        if self.finished == True:
            return True
        if self.tree.parent == None:
            return False
        if self.tree.parent.left == self.tree or self.tree.parent.right == self.tree:
            if self.tree.level * self._height / 6 <= self.y:
                return True
        else:
            return False
    #Draws Node and nodes numbers
    def draw(self, screen):
        BLACK = (0, 0, 0)
        if self.tree.parent != None:
            pygame.draw.line(screen, BLACK, (self.x, self.y), (self.tree.parent.x, self.tree.parent.y), 1)
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
        current = self.bubbles[len(self.bubbles) - 1]
        # LATER -- ADD END GAME CHECKING HERE
        #Check if there is a collision and where it collides
        #Must handle tree parents
        for i in range(0, len(self.bubbles)):
            node = self.bubbles[i]
            node.update()
            if self.bubbles[i] == current:
                continue
            dist = (current.y - node.y) * (current.y-node.y) + (current.x - node.x) * (current.x - node.x)
            if dist <= 50*50 and current.tree.parent != node.tree:
                current.collision = True
                current.tree.level = node.tree.level + 1
                if node.tree.left == None and node.tree.value > current.tree.value and current.direction == 'left':
                    node.tree.left = current.tree
                    current.tree.parent = node.tree
                elif node.tree.right == None and node.tree.value <= current.tree.value and current.direction == 'right':
                    node.tree.right = current.tree
                    current.tree.parent = node.tree
                elif node.tree.left != None and node.tree.value > current.tree.value and current.direction == 'left':
                    current.tree.parent = node.tree
                elif node.tree.right != None and node.tree.value <= current.tree.value and current.direction == 'right':
                    current.tree.parent = node.tree
                    #print("Autograder has deemed your knowledge... insufficient")
                #Later, include children
            #If no collision or not entering the tree, it keeps on keeping on
            #Update every node

    #Changes properties of the Node if a significant game event occurs  -- STILL BUILDING

    #Calls draw function for each objects
    def draw(self, screen):
        for node in self.bubbles:
            node.draw(screen)

def main():
    # ------ PYGAME SETUP --------------
    pygame.init()
    #Set this to fullscreen in later development
    screen = pygame.display.set_mode((1800, 1000))
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
    #Create professor guide
    wade = Professor(width, height, 'wade.png')
    #speech = SpeechBubble(width, height, wade.rect.width, 'speech_bubble.png')
    #professor = pygame.sprite.RenderPlain((wade, speech))
    professor = pygame.sprite.RenderPlain((wade))

    # ------ OBJECTS ------------
    #Makes group of Nodes to handle
    bubbles = BubbleNodeGroup()
    #Root bubble a
    #Since the root sets all starting conditions, must override its properties
    root = BubbleNode(width, height)
    root.movey = 0
    root.x = width/2
    root.y = height/6
    root.num1.movey = 0
    root.num2.movey = 0
    root.num1.rect.centery = height/6
    root.num2.rect.centery = height/6
    root.finished = True
    root.tree.parent = None
    root.tree.x = root.x
    root.tree.y = root.y
    #Add root to bubbles group
    bubbles.append(root)

    # ---------OBJECTS AND FUNCTIONS FOR TESTING --------------

    #Game loop
    main = True
    while main:
        #increment clock
        clock.tick(60)
        pygame.display.flip()

        # ----- EXIT HANDLING ---------
        #Checks if exit event occurs
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                main = False
                break;
        # --- GAME LOGIC ----
        current = bubbles.bubbles[len(bubbles.bubbles) - 1]
        #Checks if 'A''D' '<-'key or  '->'key are called
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT or event.key == ord('a'):
                current.direction = 'left'
            if event.key == pygame.K_RIGHT or event.key == ord('d'):
                current.direction = 'right'
        #End Game logic
        if current.y > height:
            print("You've won!")
            main = False
            continue
        #Bubble generation
        if current.finished == True:
            bubbles.append(BubbleNode(width, height))
        #Update all objects
        bubbles.update()
        professor.update()
        #updates screen image (redraws screen everytime)
        screen.blit(background, (0, 0))
        bubbles.draw(screen)
        professor.draw(screen)

    pygame.quit()

if __name__ == '__main__':
        main()
