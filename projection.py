from math import cos, sin, pi
from pygame.math import Vector3, Vector2

def rotation_matrix(roll: float, pitch: float, yaw: float) -> tuple[Vector3]:
    """Returns a rotation matrix

    Args:
        pitch (float): rad
        roll (float): rad
        yaw (float): rad

    Returns:
        list[Vector3]: Rotation Matrix:
        |AX.X, AX.Y, AX.Z|
        |AY.X, AY.Y, AY.Z|
        |AZ.X, AZ.Y, AZ.Z|
    """
    #Cosine and sine calculation
    cosa, sina = cos(yaw), sin(yaw)
    cosb, sinb = cos(pitch), sin(pitch)
    cosc, sinc = cos(roll), sin(roll)
    
    AX = Vector3(
        cosa * cosb,
        cosa * sinb * sinc - sina * cosc,
        cosa * sinb * cosc + sina * sinc
    )
    
    AY = Vector3(
        sina * cosb,
        sina * sinb * sinc + cosa * cosc,
        sina * sinb * cosc - cosa * sinc
    )
    
    AZ = Vector3(
        -sinb,
        cosb * sinc,
        cosb * cosc
    )
    
    return (AX, AY, AZ)

def persepectiveProjection(point: Vector3, camera: object) -> Vector2:
    """_summary_

    Args:
        point (Vector3): 3D Point to be projected
        camera (object): Object containing a Camera and transform component

    Returns:
        Vector2: projected point
    """
    
    #https://en.wikipedia.org/wiki/3D_projection
    
    P = point - camera.transform.position
    
    #Cosine and Sine Calculations
    
    #X = Roll
    #Y = Pitch
    #Z = Yaw
    C = Vector3(cos(camera.transform.rotation.z), cos(camera.transform.rotation.y + pi / 2), cos(camera.transform.rotation.x))
    S = Vector3(sin(camera.transform.rotation.z), sin(camera.transform.rotation.y + pi / 2), sin(camera.transform.rotation.x))
    
    A = (S.z * P.y + C.z * P.x)
    B = (C.z * P.y - S.z * P.x)
    
    #Tranformed point
    D = Vector3(
        C.y * (S.z * P.y + C.z * P.x) - S.y * P.z,
        S.x * (C.y * P.z + S.y * A) + C.x * B,
        C.x * (C.y * P.z + S.y * A) - S.x * B
    )
    
    #Projection onto the 2D plane
    E = camera.get_component_from_name("CameraComponent").display_surface
    
    Projection = Vector2(
        (E.z / D.z) * D.x + E.x,
        (E.z / D.z) * D.y + E.y
    )
    
    return Projection
