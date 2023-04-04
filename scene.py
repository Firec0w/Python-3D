import pygame as pg
from objects import Object
from components import CameraComponent

from exceptions import NoCameraError

class Scene:
    """
    The scene object contains every Object objects on the scene,
    and updates them
    """
    def __init__(self, objects: Object = []):
        self.objects = objects
    
    def update(self):
        for obj in self.objects:
            obj.update()
    
    def draw(self, surface: pg.Surface):
        #Takes the first active camera as the render camera

        cameras = [c for c in self.objects if (CameraComponent in c and c.get_component(CameraComponent).active)]
        if not len(cameras):
            raise NoCameraError("The scene has no active camera !")
        
        camera = cameras[0]
        camera.get_component(CameraComponent).draw(camera, self, surface)