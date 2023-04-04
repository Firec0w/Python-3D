
class ComponentError(Exception):
    """Object component error"""
    
    def __init__(self, message: str):
        """Object component error"""
        
        self.message = message
        super().__init__(self.message)
        
class NoCameraError(Exception):
    """Raised when a scene has no active camera"""
    
    def __init__(self, message: str):
        """Raised when a scene has no active camera"""
        self.message = message
        super().__init__(self.message)