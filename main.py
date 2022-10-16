# Nuno Lima 2022
from PIL import Image
from pathlib import Path

def get_images(folder_path: str) -> list:
    images_path = []
    path = Path(folder_path)

    if not path.is_dir():
        return []

    for file_path in path.iterdir():
        if file_path.is_file() and file_path.suffix in [".jpg", ".png"]:
            images_path.append(file_path)
    return images_path

def generate_output_folder() -> Path:
    output_folder = Path("with_logo")
    if not output_folder.exists():
        output_folder.mkdir()
    return output_folder

def add_logo(images_path: list, logo_path: str)-> None:
    output_folder = generate_output_folder()

    offset = 50 
    logo = Image.open(logo_path)
    logo_width, logo_height = logo.size

    for image_path in images_path:
        image = Image.open(image_path)
        image_width, image_height = image.size

        if logo_width > image_width or logo_height > image_height:
            continue

        position = (image_width - logo_width - offset, image_height - logo_height - offset)
        image.paste(logo, position, logo)
        image.save(output_folder.joinpath(image_path.name))

def main() -> None:
    images_folder = ""
    logo_path = ""

    images = get_images(images_folder)
    add_logo(images, logo_path)
    
if __name__== "__main__":
    main()