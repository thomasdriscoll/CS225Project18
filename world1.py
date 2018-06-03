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
import pygame, random
#Optional: Sets up constants and functions in global namespace
from pygame.locals import *

def main():
    pygame.init()
    screen = pygame.display.set_mode((400, 500))
    #fills in background
    background = pygame.Surface(screen.get_size())
    background = background.convert()
    background.fill((250, 250, 250))
    #Display the Background While Setup Finishes
    screen.blit(background, (0,0))
    pygame.display.flip()
    #OBJECTS GO HERE


    #create game clock
    clock = pygame.time.Clock()
    #Game loop
    done = False
    while not done:
        #increment clock
        clock.tick(60)
        #update screen
        weaselbots.update()
        #Check if collision will occur
        #updates screen image (redraws screen everytime)
        screen.blit(background, (0, 0))
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                done = True
                break;

    pygame.quit()

if __name__ == '__main__':
        main()
