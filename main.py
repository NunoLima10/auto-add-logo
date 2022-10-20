from src.logo_adder import LogoAdder
from src.logo_position import LogoPosition

def main() -> None:
    logo_path = "dot.png"
    images_folder = "photos"

    logo_adder = LogoAdder(
        logo_path, 
        images_folder, 
        LogoPosition.center, 
        logo_size=0.5,
        logo_angle = 0
    )
    logo_adder.start()
    
if __name__== "__main__":
    main()