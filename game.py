import pygame
import sys

class Game: 
    def __init__(self):  
        pygame.init()

        pygame.display.set_caption('ninja game')
        #This function will create our window
        #screen is our handle for a window so we can draw onto it
        self.screen = pygame.display.set_mode((640, 480))
        #instantiate a clock object
        self.clock = pygame.time.Clock()
        #load an image
        self.img = pygame.image.load('PyGame-ninja/data/images/clouds/cloud_1.png')
        #the color 0,0,0 will be removed with transparency
        self.img.set_colorkey((0, 0, 0))
        self.img_pos = [160, 260]

        self.movement = [False, False]
    def run(self):        
        #our game's main loop
        while True:
            #filling the whole screen with a background color to also erase the previous render of the blit images onto the screen
            self.screen.fill((14, 219, 248))
            #bool technically can be converted to integers implicitly
            #when self.movement[1] is True, self.movement[0] will be False and the image will move down
            #in the other case it will move up because will be 0 - 1 (False - True)
            self.img_pos[1] += (self.movement[1] - self.movement[0]) *5
            #This function will put our image on the screen
            #Top left is 0, 0 
            #blit is just kind of a memory copy
            #you're copying some ection of memory onto another surface
            #in pygame a surface is basically just an image (the window itself has a surface which is the main one you render)
            #you can blit any surface onto another surface at a given location
            self.screen.blit(self.img, self.img_pos)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        self.movement[0] = True
                    if event.key == pygame.K_DOWN:
                        self.movement[1] = True
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_UP:
                        self.movement[0] = False
                    if event.key == pygame.K_DOWN:
                        self.movement[1] = False

            pygame.display.update()
            #force our game to run at 60 fps
            self.clock.tick(60)

Game().run()