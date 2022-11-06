from src.select_file import select_images,select_config,select_logo
from src.icon import decode_icon
from src.logo_adder import LogoAdder

from tkinter import Tk
import os

def main() -> None:
    root = Tk()
    icon = decode_icon()
    root.iconbitmap(icon)
    root.attributes('-alpha', 0)
    os.remove(icon)
    
    logo = select_logo()
    images = select_images()
    config = select_config()

    logo_adder = LogoAdder(logo, images, config)
    logo_adder.start()
    

if __name__== "__main__":
    main()