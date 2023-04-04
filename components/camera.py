from projection import persepectiveProjection, rotation_matrix
from pygame.math import Vector3, Vector2
import pygame as pg

from components.mesh import Mesh

class CameraComponent:
    componentName: str = "CameraComponent"
    
    def __init__(self, display_surface: Vector3 = Vector3(500, 500, 400), active: bool = True):
        self.display_surface = display_surface
        self.active = active
    
    def update(self, parent):
        ...
    
    def outside_screen(self, point: Vector2, screen_size: tuple[int, int] = (1000, 1000), margin: int = 0) -> bool:
        return point.x < 0 - margin or point.x > screen_size[0] + margin or point.y < 0 - margin or point.y > screen_size[1] + margin
    
    def inside_screen(self, point: Vector2, screen_size: tuple[int, int] = (1000, 1000), margin: int = 0):
        return not self.outside_screen(point, screen_size, margin)
    
    def draw(self, parent: object, scene: "Scene", surface: pg.Surface) -> None:
        for obj in scene.objects:
            if Mesh in obj:    
                mesh: Mesh = obj.get_component(Mesh)
                mesh = mesh.transform(obj.transform)
                
                projeted = [persepectiveProjection(vertex, parent) for vertex in mesh.vertices]
                
                for i, triangle in enumerate(mesh.triangles):
                    
                    if mesh.normals[i].dot(parent.transform.orientation) >= 0: #Backface culling
                        continue
                    
                    if any(self.outside_screen(projeted[t], margin = 10) for t in triangle):
                        continue
                    # Draws triangle wireframe
                    pg.draw.lines(surface, (0, 0, 0), True, [projeted[t] for t in triangle], 2)
                    pg.draw.polygon(surface, (255, 255, 255), [projeted[t] for t in triangle])
                    
                    # Draws normal:
                    
                    #s = persepectiveProjection(mesh.triangle_center(triangle), parent)
                    #e = persepectiveProjection(mesh.triangle_center(triangle) + mesh.normals[i], parent)
                    
                    #pg.draw.line(surface, (255, 0, 0), s, e, 1)
                    
                    
                    #draws Orientation