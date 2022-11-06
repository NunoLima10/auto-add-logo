from src.exceptions import InvalidLogoSize,InvalidLogoPosition,InvalidLogoAngle,InvalidOffset,InvalidConfig
from tkinter import messagebox

import json

def load_config(file_path: str) -> dict:
    with open(file_path) as file:
        data = json.load(file)
        try:
            config = data["logo_config"]
            valid_config(config)
            return config

        except InvalidLogoSize:
            messagebox.showerror("Error", InvalidLogoSize.message)

        except InvalidLogoPosition:
            messagebox.showerror("Error", InvalidLogoPosition.message)

        except InvalidLogoAngle:
            messagebox.showerror("Error", InvalidLogoAngle.message)

        except InvalidOffset:
            messagebox.showerror("Error", InvalidOffset.message)
        
        except KeyError:
            messagebox.showerror("Error",InvalidConfig.message)


def valid_config(config: dict) -> None:

    if type(config["x_offset"]) is not int or type(config["y_offset"]) is not int:
        raise InvalidOffset

    if type(config["logo_angle"]) is not float:
        raise InvalidLogoAngle

    if type(config["logo_size"]) is not int:
        raise InvalidLogoSize

    if config["logo_size"] <= 0 or config["logo_size"] > 100:
            raise InvalidLogoSize

    if config["logo_position"] not in ["center","top_left","top_right","bottom_left","bottom_right"]:
        raise InvalidLogoPosition

