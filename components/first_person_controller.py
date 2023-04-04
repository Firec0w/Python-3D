from __future__ import annotations

import pygame as pg
from pygame.math import Vector3, Vector2

from math import cos, sin, pi

class FirstPersonController:
    componentName: str = 'FirstPersonController'
    
    def __init__(self):
        self.velocity = Vector3(0,0,0)
        
        self.movement_speed = .1
    
    def update(self, parent: Object):
        
        keys = pg.key.get_pressed()
        mouse = Vector2(pg.mouse.get_pos()) / 100.0
        
        parent.transform.rotation = Vector3(0, mouse.x, -mouse.y)
        
        if keys[pg.K_SPACE]:
            self.velocity.y -= .1

        if keys[pg.K_LSHIFT]:
            self.velocity.y += .1

        
        if keys[pg.K_d]:
            self.velocity -= self.movement_speed * parent.transform.orientation.zyx

        if keys[pg.K_a]:
            self.velocity += self.movement_speed * parent.transform.orientation.zyx
            
            
        if keys[pg.K_s]:
            self.velocity -= self.movement_speed * parent.transform.orientation

        if keys[pg.K_w]:
            self.velocity += self.movement_speed * parent.transform.orientation

        parent.transform.position += self.velocity
        self.velocity /= 1.5