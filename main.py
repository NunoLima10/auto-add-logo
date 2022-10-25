from src.logo_adder import LogoAdder
from src.logo_position import LogoPosition
from tkinter import filedialog

def main() -> None:
    filetypes = (('Images', ('*.png','*.jpg')),)
    logo_path = filedialog.askopenfile(title='Chose logo',initialdir='/',filetypes=filetypes,).name
    images_folder = filedialog.askdirectory(title='Chose images',initialdir='/')

    logo_adder = LogoAdder(
        logo_path, 
        images_folder, 
        LogoPosition.bottom_right, 
        logo_size=0.5,
        logo_angle = 0,
        x_offset = -50,
        y_offset = -50
    )
    logo_adder.start()
    
if __name__== "__main__":
    main()