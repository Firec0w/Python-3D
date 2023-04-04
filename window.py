import pygame as pg
from scene import Scene

class Window:
    def __init__(self, size: tuple[int, int], scene: Scene):
        self.size = size
        
        self.display = pg.display
        self.screen = self.display.set_mode(size)
        
        self.scene = scene
        self.clock = pg.time.Clock()
    
    def update(self):
        deltaTime = self.clock.tick()
        
        self.screen.fill((0,0,0))
        self.display.set_caption(f"{self.clock.get_fps()}")
        
        for event in pg.event.get():
            if event.type == pg.QUIT:
                quit()
        
        self.scene.update()
        self.scene.draw(self.screen)
        self.display.flip()