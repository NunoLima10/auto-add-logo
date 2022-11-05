from src.select_file import select_images,select_config,select_logo
from src.logo_adder import LogoAdder

def main() -> None:
    
    logo = select_logo()
    images = select_images()
    config = select_config()

    logo_adder = LogoAdder(logo, images, config)
    logo_adder.start()

if __name__== "__main__":
    main()