from pygame.math import Vector3
from math import cos, sin

from projection import rotation_matrix

class Transform:
    componentName: str = "TransformComponent"
    
    @property
    def orientation(self):
        """
        Returns the orientation of the object,
        as a vector of magnitude 1
        """
        rotate = rotation_matrix(*self.rotation) 
        u = Vector3(1,0,0)
        
        o = Vector3(u.x * rotate[0].x + u.y * rotate[0].y + u.z * rotate[0].z,
                    u.x * rotate[1].x + u.y * rotate[1].y + u.z * rotate[1].z,
                    u.x * rotate[2].x + u.y * rotate[2].y + u.z * rotate[2].z)
        
        return o
    
    @orientation.setter
    def orientation(self, value: Vector3):
        ...
    
    def update(self, parent):
        ...
    
    def __init__(
        self,
        position: Vector3 = None,
        rotation: Vector3 = None,
        size: Vector3 = None
        ):
        """Transform object

        Args:
            position (Vector3, optional): X, Y, Z. Defaults to None.
            rotation (Vector3, optional): Roll, Pitch, Yaw. Defaults to None.
            size (Vector3, optional): Size coeficient. Defaults to None.
        """
        
        self.position = position
        self.rotation = rotation
        self.size = size
        
        if self.position is None:
            self.position = Vector3(0,0,0)
        
        if self.rotation is None:
            self.rotation = Vector3(0,0,0)
        
        if self.size is None:
            self.size = Vector3(1,1,1)