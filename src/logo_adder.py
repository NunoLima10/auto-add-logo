from src.color_printer import ColorPrinter
from src.exceptions import IsNotFolder,UnsupportedLogoType,InvalidLogoSize
from src.logo_position import LogoPosition
from PIL import Image
from pathlib import Path

import math 

class LogoAdder:
    def __init__(self, logo_path: str, image_folder_path: str, logo_position: str, 
                logo_size: float = 1) -> None:
        self.logo_path = logo_path
        self.image_folder_path = image_folder_path
        self.position_function = LogoPosition.positions[logo_position]
        self.logo_size = logo_size
        
        self.output_folder_name = "with_logo"
        self.output_folder = self.generate_output_folder()

    def generate_output_folder(self) -> Path:
        output_folder = Path(self.output_folder_name)
        if not output_folder.exists():
            output_folder.mkdir()
        return output_folder

    def validate_input(self) -> None:
        logo_file = Path(self.logo_path)
        if not logo_file.is_file() or logo_file.suffix not in [".jpg", ".png"]:
            raise UnsupportedLogoType
        
        folder_path = Path(self.image_folder_path)
        if not folder_path.is_dir():
            raise IsNotFolder
        
        if self.logo_size <= 0 or self.logo_size > 1:
            raise InvalidLogoSize
        
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

        return logo.resize((new_width,new_height))

    def add_logo(self, images_path: list, ) -> None:
        logo = self.setup_logo()
        logo_width, logo_height = logo.size

        for image_path in images_path:
            image = Image.open(image_path)
            image_width, image_height = image.size

            if logo_width > image_width or logo_height > image_height:
                continue

            position = self.position_function(image_width, image_height, logo_width, logo_height)
            image.paste(logo, position, logo)
            image.save(self.output_folder.joinpath(image_path.name))
    

    def start(self) -> None:
        try:
            self.validate_input()
            images = self.get_images()
            self.add_logo(images)

        except UnsupportedLogoType:
            ColorPrinter.show(
                text="Unsupported logo format, select jpg or png images",
                type="error",
                on_error_exit=True
                )
        except IsNotFolder:
            ColorPrinter.show(
                text="Select a folder with the images",
                type="error",
                on_error_exit=True
                ) 
        except InvalidLogoSize:
            ColorPrinter.show(
                text="Invalid image size, value must be in the range 0 to 1",
                type="error",
                on_error_exit=True
                )
