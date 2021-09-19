from wand.image import Image
from wand.color import Color


with Image(filename="C:/Users/Linux/Documents/pokespawn/all_starter.jpg") as img:
    img.format = 'png'
    with Color('#FDFDFD') as white:
        twenty_percent = int(65535 * 0.4)  # Note: percent must be calculated from Quantum
        img.transparent_color(white, alpha=0.0, fuzz=twenty_percent)
    img.save(filename="all_starter.png")