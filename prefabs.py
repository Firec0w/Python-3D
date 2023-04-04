from objects import *

#Pre-made objects

def importObj(path: str) -> object:
    """Create a 3D object from an obj file"""
    
    obj = Object().add_component(Mesh())
    obj.mesh = obj.get_component(Mesh)
    
    #Obj file parser
    lines = []
    with open(path, 'r') as fp:
        lines = fp.readlines()
    for line in lines:
        line = line.replace('\n', '')
        elements = line.split()
        if elements and elements[0] == 'v': #If vertice:
            obj.mesh.vertices.append(Vector3(*[list(map(float, elements[1:]))][0:3]))
        if elements and elements[0] == 'f': #if Triangles
            obj.mesh.triangles.append([int(e.split('/')[0]) - 1 for e in elements[1:]][:3])
    
    obj.mesh.normal_from_triangles()
    
    return obj

def cube() -> Object:
    obj = Object().add_component(
    Mesh(
        vertices = 
            [Vector3(-1, -1, -1),
            Vector3( 1, -1, -1),
            Vector3( 1,  1, -1),
            Vector3(-1,  1, -1),
            Vector3(-1, -1,  1),
            Vector3( 1, -1,  1),
            Vector3( 1,  1,  1),
            Vector3(-1,  1,  1),],
            
        triangles = 
            [[0, 1, 5],
            [5, 4, 0],
            [1, 2, 6],
            [6, 5, 1],
            [4, 5, 6],
            [6, 7, 4],
            [2, 1, 0],
            [0, 3, 2],
            [7, 3, 0],
            [0, 4, 7],
            [7, 6, 2],
            [3, 7, 2]]
    ).normal_from_triangles()
    )
    
    obj.mesh = obj.get_component(Mesh)
    
    return obj