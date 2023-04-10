"""Define Pizza Class."""

class Pizza:

    # Attributes
    size: str #small or large
    toppings: int
    gluten_free: bool

    def __init__(self, size_input:str, toppings_input: int, gluten_free_input: str):
        self.size = size_input
        
