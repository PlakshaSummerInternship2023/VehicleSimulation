import pygame

from utils import SimObject, testbanner
from constants import WINDOW_SIZE, FPS, BOAT_COLOR, WATER_COLOR
from constants import BOAT_EDGE_THICKNESS

class RenderEngine(SimObject):
    def __init__ (self,dimension: int):
        super().__init__(dimension)
        
        pygame.init()
        self.screen = pygame.display.set_mode(WINDOW_SIZE)
        self.background = WATER_COLOR

        self.clock = pygame.time.Clock()

        self.screen.fill(self.background)

    def __prerender__ (self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
        self.screen.fill(self.background)

    def __postrender__ (self):
        pygame.display.flip()
        pygame.display.update()
        self.clock.tick(FPS)

    def render (self, body):
        self.__prerender__()
        # -------------------
        
        for a,b in body.polygon_generator():
            pygame.draw.line(self.screen, BOAT_COLOR, a, b,BOAT_EDGE_THICKNESS)
            pygame.draw.circle(self.screen, BOAT_COLOR, a, BOAT_EDGE_THICKNESS)
            pygame.draw.circle(self.screen, BOAT_COLOR, b,BOAT_EDGE_THICKNESS)

        # -------------------
        self.__postrender__()


