from PIL import ImageDraw, Image, ImageFont, ImageFilter
import random, os, json

def load_json():
    with open('./config.json', 'r') as f:
        data = json.load(f)
    return data

def random_char(y):
    str1 = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    return ''.join(random.choice(str1) for _ in range(y))

font = [
    ImageFont.truetype("./fonts/gadugi.ttf", 19),
    ImageFont.truetype("./fonts/arial.ttf", 15),
    ImageFont.truetype("./fonts/Chalkduster_400.ttf", 16),
    ImageFont.truetype("./fonts/Chalkduster_400.ttf", 16),
    ImageFont.truetype("./fonts/Chalkduster_400.ttf", 16)
]

curr_json = load_json()

for _ in range(0, curr_json["number_to_generate"]):
    fontsize = random.randint(10, 20)
    img = Image.new('RGB', (100, 30), color=(random.randint(0, 100), random.randint(0, 100), random.randint(0, 100)))
    d = ImageDraw.Draw(img)

    for _ in range(0, random.randint(10, 30)):
        d.line((random.randint(0, 100), random.randint(0, 100)) + img.size, fill=random.randint(0, 100))

    text = random_char(5)
    d.text((24, 5), f"{text}", fill=(random.randint(1, 255), random.randint(1, 255), 0), font=random.choice(font))
    imgblur = img.filter(ImageFilter.GaussianBlur(1.4))
    imgblur.save(fr'{curr_json["path"]}/{text}.png')

    dirListing = os.listdir(curr_json["path"])
    print(f'[{len(dirListing)}] Successfully created a captcha named: {text}.')
