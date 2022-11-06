from math import floor

class LogoPosition:
    
    def __init__(self, position) -> None:
        self.positions = {
        "center": self.to_center,
        "top_left":self.to_top_left,
        "top_right":self.to_top_right,
        "bottom_left":self.to_bottom_left,
        "bottom_right":self.to_bottom_right
        }
        self.position_function = self.positions[position]
        
    def to_center(self, image_width: int, image_height:int, logo_width:int, 
                logo_height: int, x_offset: int = 0, y_offset: int = 0) -> tuple:
        x_position = floor(image_width/2 - logo_width/2) + x_offset
        y_position = floor(image_height/2 - logo_height/2) + y_offset
        return (x_position, y_position)
            

    def to_top_left(self, image_width: int, image_height:int, logo_width:int, 
                logo_height: int, x_offset: int = 0, y_offset: int = 0) -> tuple:
        x_position = x_offset
        y_position = y_offset
        return (x_position, y_position)

    def to_top_right(self, image_width: int, image_height:int, logo_width:int, 
                logo_height: int, x_offset: int = 0, y_offset: int = 0) -> tuple:
        x_position = image_width - logo_width + x_offset
        y_position = y_offset
        return (x_position, y_position)


    def to_bottom_left(self, image_width: int, image_height:int, logo_width:int, 
                logo_height: int, x_offset: int = 0, y_offset: int = 0) -> tuple:
        x_position = x_offset 
        y_position = image_height - logo_height + y_offset
        return (x_position, y_position)

    def to_bottom_right(self, image_width: int, image_height:int, logo_width:int, 
                logo_height: int, x_offset: int = 0, y_offset: int = 0) -> tuple:
        x_position = image_width - logo_width + x_offset
        y_position = image_height - logo_height + y_offset
        return (x_position, y_position)

    