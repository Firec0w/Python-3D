from __future__ import annotations

import pygame as pg
from pygame.math import Vector3

from math import cos, sin, pi

class FirstPersonController:
    componentName: str = 'FirstPersonController'
    
    def __init__(self):
        ...
    
    def update(self, parent: Object):
        keys = pg.key.get_pressed()
        
        if keys[pg.K_SPACE]:
            parent.transform.position.y -= .1

        if keys[pg.K_LSHIFT]:
            parent.transform.position.y += .1

        
        if keys[pg.K_d]:
            parent.transform.position.z -= .1

        if keys[pg.K_a]:
            parent.transform.position.z += .1
            
            
        if keys[pg.K_s]:
            parent.transform.position.x -= .1

        if keys[pg.K_w]:
            parent.transform.position.x += .1
