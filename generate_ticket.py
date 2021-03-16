from io import BytesIO

import requests
from PIL import Image, ImageFont, ImageDraw

TEMPLATE_PATH = 'files/ticket.png'
FONT_PATH = 'files/Roboto-Black.ttf'
FONT_SIZE = 20
BLACK = (0, 0, 0, 255)
NAME_OFFSET = (450, 415)
EMAIL_OFFSET = (450, 450)

AVATAR_OFFSET = (100, 200)


def generate_ticket(name, email):
    base = Image.open(TEMPLATE_PATH).convert('RGBA')
    font = ImageFont.truetype(FONT_PATH, FONT_SIZE)

    draw = ImageDraw.Draw(base)
    draw.text(NAME_OFFSET, name, font=font, fill=BLACK)
    draw.text(EMAIL_OFFSET, email, font=font, fill=BLACK)

    # response = requests.get(url=f'http://tinygraphs.com/spaceinvaders/{name}?theme=seascape&numcolors=4&size=220&fmt=svg')
    # avatar_file_like = BytesIO(response.content)
    # avatar = Image.open(avatar_file_like)

    # base.paste(avatar, AVATAR_OFFSET)
    temp_file = BytesIO()
    base.save(temp_file, 'png')
    temp_file.seek(0)

    return temp_file

