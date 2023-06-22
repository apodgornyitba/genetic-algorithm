from .config import Config

Config.load_from_json('config.json')

def proportion_to_rgb(proportion):
    # Initialize the RGB values for the new color
    new_red = 0
    new_green = 0
    new_blue = 0

    # Loop through each color in the palette and calculate its contribution to the new color
    for i in range(Config.get_palette_color_amount()):
        new_red += proportion[i] * Config.palette[i][0]
        new_green += proportion[i] * Config.palette[i][1]
        new_blue += proportion[i] * Config.palette[i][2]

    # Truncate the RGB values and create a tuple of the new RGB values
    return (int(new_red), int(new_green), int(new_blue))