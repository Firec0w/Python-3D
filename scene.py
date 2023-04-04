import pygame as pg
from objects import Object
from components import CameraComponent

class Scene:
    def __init__(self, objects: Object = []):
        self.objects = objects
    
    def update(self):
        for obj in self.objects:
            obj.update()
    
    def draw(self, surface: pg.Surface):
        #Takes the first active camera as the render camera

        camera = [c for c in self.objects if CameraComponent in c][0]
        camera.get_component(CameraComponent).draw(camera, self, surface)