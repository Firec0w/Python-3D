from __future__ import annotations

from pygame.math import Vector3
from components import *

from exceptions import ComponentError
from enum import auto, Enum


class Object:
    def __init__(self, transform: Transform = None, name: str = ""):
        
        self.name = str(name)
        self.transform = transform
        
        if self.name == "":
            self.name = str(id(self))
        
        if self.transform is None:
            self.transform = Transform()
        
        self.components = {Transform.componentName: self.transform}
    
    def update(self) -> Object :
        """Ran once a frame"""
        for c in self.components.values():
            c.update(self)
            
        return self
    
    def __repr__(self):
        return f"{self.name} object at {hex(id(self))}. Components : {[c + ' at ' + hex(id(v)) for c, v in self.components.items()]}"
    
    def get_component(self, component_type: type) -> object:
        if component_type.componentName in self.components:
            return self.components[component_type.componentName]
            
        raise ComponentError("Component not in object")
    
    def get_component_from_name(self, component_name: str) -> object:
        if component_name in self.components:
            return self.components[component_name]
        
        raise ComponentError("Component not in object")
    
    def __contains__(self, component: type) -> bool:
        """Return whether or not the object has a component

        Args:
            component (object): Component

        Returns:
            bool: ...
        """

        return component.componentName in self.components

    def has_component(self, component: type) -> bool:
        return component in self
    
    def add_component(self, component: object) -> Object:
        if component in self:
            raise ComponentError("Component already in object")
            
        self.components[component.componentName] = component
        
        return self