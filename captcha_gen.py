from PIL import ImageDraw, Image, ImageFont, ImageFilter
import os, json, secrets

def load_json():
    with open('./config.json', 'r') as f:
        data = json.load(f)
    return data

def random_char(y):
    str1 = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    return ''.join(secrets.choice(str1) for _ in range(y))

font = [
    ImageFont.truetype("./fonts/gadugi.ttf", 19),
    ImageFont.truetype("./fonts/arial.ttf", 15),
    ImageFont.truetype("./fonts/Chalkduster_400.ttf", 16),
    ImageFont.truetype("./fonts/Chalkduster_400.ttf", 16),
    ImageFont.truetype("./fonts/Chalkduster_400.ttf", 16)
]

curr_json = load_json()

for _ in range(0, curr_json["number_to_generate"]):
    fontsize = secrets.randbelow(30)
    img = Image.new('RGB', (100, 30), color=(secrets.randbelow(100), secrets.randbelow(100), secrets.randbelow(100)))
    d = ImageDraw.Draw(img)

    for _ in range(0, secrets.randbelow(30)):
        d.line((secrets.randbelow(100), secrets.randbelow(100)) + img.size, fill=secrets.randbelow(100))

    text = random_char(5)
    d.text((24, 5), f"{text}", fill=(secrets.randbelow(255), secrets.randbelow(255), 0), font=secrets.choice(font))
    imgblur = img.filter(ImageFilter.GaussianBlur(1.3))
    imgblur.save(fr'{curr_json["path"]}/{text}.png')

    dirListing = os.listdir(curr_json["path"])
    print(f'[{len(dirListing)}] Successfully created a captcha named: {text}.')
