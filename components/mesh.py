from __future__ import annotations

from pygame.math import Vector3
from components.transform import Transform

from projection import rotation_matrix

from math import cos, sin

class Mesh:
    componentName: str = "MeshComponent"
    
    def __init__(self,     
                vertices: list[Vector3] = None, 
                triangles: list[int] = None,
                normals: list[Vector3] = None):
        
        self.vertices = vertices # Position of each vertex
        self.triangles = triangles # List of vertex index
        self.normals = normals # Triangle normals
        
        if self.vertices is None:
            self.vertices = []
        
        if self.triangles is None:
            self.triangles = []
        
        if self.normals is None:
            self.normals = []

    def update(self, parent):
        ...
    
    def triangle_center(self, triangle: list[int]) -> Vector3:
        """Returns the center position of a triangle"""
        p1, p2, p3 = [self.vertices[triangle[n]] for n in range(3)]
        
        return (p1 + p2 + p3) / 3
    
    @staticmethod
    def rotate(point: Vector3, rotation_matrix: tuple[Vector3]):
        return Vector3(rotation_matrix[0].x * point.x + rotation_matrix[0].y * point.y + rotation_matrix[0].z * point.z,
                        rotation_matrix[1].x * point.x + rotation_matrix[1].y * point.y + rotation_matrix[1].z * point.z,
                        rotation_matrix[2].x * point.x + rotation_matrix[2].y * point.y + rotation_matrix[2].z * point.z)
    
    def transform(self, transform: Transform) -> Mesh:
        """Returns transformed mesh, with scaled, rotated and moved vertices,
        usable by the camera"""
        
        #Rotation matrix
        rotation = rotation_matrix(transform.rotation.x, transform.rotation.y, transform.rotation.z)
        
        #resized vertices
        resized = [Vector3(
            vert.x * transform.size.x, 
            vert.y * transform.size.y, 
            vert.z * transform.size.z) for vert in self.vertices]
        
        #Rotated vertices
        rotated = [Mesh.rotate(v, rotation)
                   + transform.position
                   for v in resized]
        
        return Mesh(
            vertices = rotated, 
            triangles = self.triangles, 
            normals = [Mesh.rotate(p, rotation) for p in self.normals])
    
    def normal_from_triangles(self) -> object:
        """Computes the face normals from triangle data. Returns Self"""
        
        #https://www.khronos.org/opengl/wiki/Calculating_a_Surface_Normal
        self.normals = []
        
        for triangle in self.triangles:
            vertices = [self.vertices[triangle[n]] for n in range(3)]
            
            U = vertices[1] - vertices[0]
            V = vertices[2] - vertices[0]
            
            self.normals.append(U.cross(V).normalize())
        
        return self