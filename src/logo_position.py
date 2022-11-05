from math import floor

class LogoPosition:
    @staticmethod
    def to_center(image_width: int, image_height:int, logo_width:int, 
                logo_height: int, x_offset: int = 0, y_offset: int = 0) -> tuple:
        x_position = floor(image_width/2 - logo_width/2) + x_offset
        y_position = floor(image_height/2 - logo_height/2) + y_offset
        return (x_position, y_position)
            
    @staticmethod
    def to_top_left(image_width: int, image_height:int, logo_width:int, 
                logo_height: int, x_offset: int = 0, y_offset: int = 0) -> tuple:
        x_position = x_offset
        y_position = y_offset
        return (x_position, y_position)

    @staticmethod
    def to_top_right(image_width: int, image_height:int, logo_width:int, 
                logo_height: int, x_offset: int = 0, y_offset: int = 0) -> tuple:
        x_position = image_width - logo_width + x_offset
        y_position = y_offset
        return (x_position, y_position)

    @staticmethod
    def to_bottom_left(image_width: int, image_height:int, logo_width:int, 
                logo_height: int, x_offset: int = 0, y_offset: int = 0) -> tuple:
        x_position = x_offset 
        y_position = image_height - logo_height + y_offset
        return (x_position, y_position)

    @staticmethod
    def to_bottom_right(image_width: int, image_height:int, logo_width:int, 
                logo_height: int, x_offset: int = 0, y_offset: int = 0) -> tuple:
        x_position = image_width - logo_width + x_offset
        y_position = image_height - logo_height + y_offset
        return (x_position, y_position)

    positions = {
        "center": to_center,
        "top_left":to_top_left,
        "top_right":to_top_right,
        "bottom_left":to_bottom_left,
        "bottom_right": to_bottom_right
    }