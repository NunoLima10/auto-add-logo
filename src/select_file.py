from tkinter import filedialog
from pathlib import Path
from src.config import load_config

import sys


def select_images() -> Path:
    path = filedialog.askdirectory(title='Chose images folder',initialdir=Path.cwd())
    if path is None:
        sys.exit()
    
    return path

def select_config() -> str:
    filetypes = (('Json', "*.json"),)
    config_path = filedialog.askopenfile(title='Chose config file',initialdir=Path.cwd(),filetypes=filetypes,)
    if config_path is None:
        sys.exit()

    return load_config(config_path.name)

def select_logo() -> str:
    filetypes = (('Images', ('*.png','*.jpg')),)
    logo_path = filedialog.askopenfile(title='Chose logo file',initialdir=Path.cwd(),filetypes=filetypes,)
    if logo_path is None:
        sys.exit()

    return logo_path.name
