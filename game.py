import pygame
import sys
from scripts.entities import PhysicsEntity
from scripts.utils import load_image

class Game: 
    def __init__(self):  
        pygame.init()

        pygame.display.set_caption('ninja game')
        #This function will create our window
        #screen is our handle for a window so we can draw onto it
        self.screen = pygame.display.set_mode((640, 480))
        #instantiate a clock object
        self.clock = pygame.time.Clock()
       
        self.movement = [False, False]

        self.assets = {
            'player': load_image('entities/player.png')
        }

        self.player = PhysicsEntity(self, 'player', (50, 50), (8, 15))
    
    def run(self):        
        #our game's main loop
        while True:
            #filling the whole screen with a background color to also erase the previous render of the blit images onto the screen
            self.screen.fill((14, 219, 248))
           
            self.player.update((self.movement[1] - self.movement[0], 0))
            self.player.render(self.screen)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        self.movement[0] = True
                    if event.key == pygame.K_RIGHT:
                        self.movement[1] = True
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_LEFT:
                        self.movement[0] = False
                    if event.key == pygame.K_RIGHT:
                        self.movement[1] = False

            pygame.display.update()
            #force our game to run at 60 fps
            self.clock.tick(60)

Game().run()