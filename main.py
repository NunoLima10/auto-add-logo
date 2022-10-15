from PIL import Image
from pathlib import Path

def get_images(folder_path: str) -> list:
    images = []
    path = Path(folder_path)

    if not path.is_dir():
        return []

    for file in Path(folder_path).iterdir():
        if file.is_file() and file.suffix in [".jpg", ".png"]:
            images.append(file)

    return images

def main() -> None:
    files = get_images("photos")
    print(files)
    



if __name__== "__main__":
    main()