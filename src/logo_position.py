from math import floor

class LogoPosition:
    center = "center"
    top_left = "top_left"
    top_right ="top_right"
    bottom_left = "bottom_left"
    bottom_right = "bottom_right"

    @staticmethod
    def to_center(image_width: int, image_height:int, logo_width:int, 
                logo_height: int, x_offset: int = 0, y_offset: int = 0) -> tuple:
        x_position = floor(image_width/2 - logo_width/2)
        y_position = floor(image_height/2 - logo_height/2)
        return (x_position, y_position)
            
    @staticmethod
    def to_top_left(image_width: int, image_height:int, logo_width:int, 
                logo_height: int, x_offset: int = 0, y_offset: int = 0) -> tuple:
        x_position = 0
        y_position = 0
        return (x_position, y_position)

    @staticmethod
    def to_top_right(image_width: int, image_height:int, logo_width:int, 
                logo_height: int, x_offset: int = 0, y_offset: int = 0) -> tuple:
        x_position = image_width - logo_width
        y_position = 0
        return (x_position, y_position)

    @staticmethod
    def to_bottom_left(image_width: int, image_height:int, logo_width:int, 
                logo_height: int, x_offset: int = 0, y_offset: int = 0) -> tuple:
        x_position = 0 
        y_position = image_height - logo_height
        return (x_position, y_position)

    @staticmethod
    def to_bottom_right(image_width: int, image_height:int, logo_width:int, 
                logo_height: int, x_offset: int = 0, y_offset: int = 0) -> tuple:
        x_position = image_width - logo_width
        y_position = image_height - logo_height
        return (x_position, y_position)

    positions = {
        "center": to_center,
        "top_left":to_top_left,
        "top_right":to_top_right,
        "bottom_left":to_bottom_left,
        "bottom_right": to_bottom_right
    }