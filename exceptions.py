
class ComponentError(Exception):
    """Object component error"""
    
    def __init__(self, message: str):
        """Object component error"""
        
        self.message = message
        super().__init__(self.message)