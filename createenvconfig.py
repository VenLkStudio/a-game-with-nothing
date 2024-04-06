import configparser

config = configparser.ConfigParser()
config.read("config.ini")
# config.add_section("GraphicsSettings")
config.set("GraphicsSettings", "SCREEN_WIDTH", "800")
config.set("GraphicsSettings", "SCREEN_HEIGHT", "600")
config.set("GraphicsSettings", "FPS", "60")


with open('config.ini', 'w') as configfile:
    config.write(configfile)