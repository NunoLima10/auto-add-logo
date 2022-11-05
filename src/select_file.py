from tkinter import filedialog
from pathlib import Path
from src.config import load_config

def select_images() -> Path:
    path = filedialog.askdirectory(title='Chose images folder',initialdir=Path.cwd())
    
    if path is None:
        exit()
    
    return path

def select_config() -> str:
    filetypes = (('Json', "*.json"),)
    config_path = filedialog.askopenfile(title='Chose logo',initialdir='/',filetypes=filetypes,)
    if config_path is None:
        exit()

    return load_config(config_path.name)

def select_logo() -> str:
    filetypes = (('Images', ('*.png','*.jpg')),)
    logo_path = filedialog.askopenfile(title='Chose logo',initialdir='/',filetypes=filetypes,)
    
    if logo_path is None:
        exit()

    return logo_path.name
