import pygame

class PhysicsEntity:
    def __init__(self, game, e_type, pos, size):
        self.game = game
        self.type = e_type
        #the list function will convert any iterable into a list
        self.pos = list(pos)
        self.size = size
        self.velocity = [0, 0]

    def update(self, movement = (0, 0)):
        #we are creating a vector that represents how much the entity should be moved in this frame
        #based on how much we want to force it to move in this particular frame
        # plus however much there already is in velocity
        frame_movement = (movement[0] + self.velocity[0], movement[1] + self.velocity[1])

        self.pos[0] += frame_movement[0]
        self.pos[1] += frame_movement[1]
    
    def render(self, surf):
        surf.blit(self.game.assets['player'], self.pos)