from window import Window
from pygame.math import Vector3
from objects import *
from components import *
import prefabs

from math import sin, cos, pi
from scene import Scene

"""
Everything is defined as an object.
For example, a cube is defined by an object with a mesh component, and a transform component
"""

def main():
    mainCamera = Object().add_component(CameraComponent(display_surface = Vector3(500, 500, 400))).add_component(FirstPersonController())
    mainCamera.transform.position = Vector3(-5, 0, 0)

    teapot = prefabs.importObj(r"E:\Programation\Python\3D\teapot.obj")
    #teapot = prefabs.cube()
    teapot.transform.rotation.x = pi
    teapot.transform.position.y = 0
      
    mainScene = Scene(
        [mainCamera, teapot])
    
    mainWindow = Window((1000, 1000), mainScene)

    i = 0
    
    print(mainCamera)
    while True:
        #mainCamera.transform.rotation.z += .001

        mainWindow.update()
    
if __name__ == "__main__":
    main()

