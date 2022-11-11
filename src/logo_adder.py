from src.logo_position import LogoPosition
from PIL import Image
from pathlib import Path

import math 

class LogoAdder:
    def __init__(self, logo_path: str, image_folder_path: str, config: dict) -> None:
        self.logo_path = logo_path
        self.image_folder_path = image_folder_path
        self.position_function = LogoPosition(config["logo_position"]).position_function
        
        self.logo_size = config["logo_size"] / 100
        self.logo_angle = config["logo_angle"]
        self.x_offset = config["x_offset"]
        self.y_offset = config["y_offset"]
        
        self.output_folder_name = "with_logo"
        self.output_folder = self.generate_output_folder()

    def generate_output_folder(self) -> Path:
        output_folder = Path(self.output_folder_name)
        if not output_folder.exists():
            output_folder.mkdir()
        return output_folder
        
    def get_images(self) -> list:
        path = Path(self.image_folder_path)
        images_path = []

        for file_path in path.iterdir():
            if file_path.is_file() and file_path.suffix in [".jpg", ".png"]:
                images_path.append(file_path)
        return images_path

    def setup_logo(self) -> Image:
        logo = Image.open(self.logo_path)
        logo_width, logo_height = logo.size

        new_width = math.floor(logo_width * self.logo_size)
        new_height =  math.floor(logo_height * self.logo_size)

        return logo.resize((new_width,new_height)).rotate(self.logo_angle)

    def add_logo(self, images_path: list) -> None:
        logo = self.setup_logo()
        logo_width, logo_height = logo.size

        for image_path in images_path:
            image = Image.open(image_path)
            image_width, image_height = image.size

            if logo_width > image_width or logo_height > image_height:
                continue

            position = self.position_function(image_width, image_height, logo_width, logo_height,
                    self.x_offset, self.y_offset)

            image.paste(logo, position, logo)
            image.save(self.output_folder.joinpath(image_path.name),quality=100, subsampling=0)
    
    def start(self) -> None:
        images = self.get_images()
        self.add_logo(images)


