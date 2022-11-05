class InvalidConfig(Exception):
    message = "Config file is invalid, try to use and modify the default config"
class InvalidLogoSize(Exception):
    message = "Logo size is invalid, must be a value between 0 to 100 percent"
class InvalidLogoPosition(Exception):
    message = "Logo position is invalid, see default config to check all positions"
class InvalidLogoAngle(Exception):
    message = "Logo angle is invalid, must be a floating value"
class InvalidOffset(Exception):
    message = "Logo offset is invalid , must be an integer value"