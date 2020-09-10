from PIL import ImageDraw, Image, ImageFont, ImageFilter
import random
import os

def random_char(y):
    str1 = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890'
    return ''.join(random.choice(str1) for x in range(y))

def random_chars(y):
    str1 = 'a b c d e f g h i j k l m n o p q r s tuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890'
    return ''.join(random.choice(str1) for x in range(y))

def random_chars2(y):
    str1 = 'a b c d e f g h i j k l m n o p q r s t u v w x y z A B C D E F G H I J K L M N O P Q R S T U V W X Y Z 1 2 3 4 5 6 7 8 9 0'
    return ''.join(random.choice(str1) for x in range(y))


fontsize = random.randint(7, 16)
c1 = True
while True:
    a = random_char(random.randint(4, 7))
    b = random_chars(random.randint(4, 8))
    c = random_chars2(random.randint(4, 7))
    img = Image.new('RGB', (100, 30), color=(31, 27, 27))
    d = ImageDraw.Draw(img)
    arandint = random.randint(0, 5)
    arandintv2 = random.randint(0, 5)
    if arandint == 1:
        d.line((0, 0) + img.size, fill=200)
        d.line((10, 0) + img.size, fill=200)
        d.line((20, 0) + img.size, fill=200)
        d.line((30, 0) + img.size, fill=89)
        d.line((45, 0) + img.size, fill=89)
        d.line((10, 0) + img.size, fill=200)
        d.line((27, 0) + img.size, fill=246)
        d.line((34, 0) + img.size, fill=44)
        d.line((67, 0) + img.size, fill=45)
    elif arandint == 2:
        d.line((0, 0) + img.size, fill=143)
        d.line((10, 0) + img.size, fill=140)
        d.line((20, 1) + img.size, fill=10)
        d.line((30, 0) + img.size, fill=9)
        d.line((40, 0) + img.size, fill=10)
        d.line((50, 0) + img.size, fill=30)
        d.line((66, 0) + img.size, fill=106)
        d.line((70, 0) + img.size, fill=20)
        d.line((15, 0) + img.size, fill=220)
        d.line((10, 0) + img.size, fill=260)
        d.line((33, 0) + img.size, fill=49)
        d.line((43, 0) + img.size, fill=87)
    elif arandint == 3:
        d.line((0, 0) + img.size, fill=2)
        d.line((10, 0) + img.size, fill=140)
        d.line((20, 0) + img.size, fill=99)
        d.line((10, 0) + img.size, fill=200)
        d.line((29, 0) + img.size, fill=200)
        d.line((36, 0) + img.size, fill=89)
        d.line((58, 0) + img.size, fill=89)
    elif arandint == 4:
        d.line((0, 0) + img.size, fill=17)
        d.line((10, 0) + img.size, fill=11)
        d.line((20, 0) + img.size, fill=88)
        d.line((5, 0) + img.size, fill=67)
        d.line((13, 0) + img.size, fill=102)
        d.line((48, 0) + img.size, fill=11)
        d.line((20, 0) + img.size, fill=232)
        d.line((20, 0) + img.size, fill=250)
        d.line((80, 0) + img.size, fill=49)
        d.line((90, 0) + img.size, fill=79)
    elif arandint == 5:
        d.line((0, 0) + img.size, fill=99)
        d.line((10, 0) + img.size, fill=57)
        d.line((6, 0) + img.size, fill=80)
        d.line((30, 0) + img.size, fill=240)
        d.line((37, 0) + img.size, fill=1)
        d.line((60, 0) + img.size, fill=53)
    if arandintv2 == 1:
        font1 = ImageFont.truetype("arial.ttf", 19)
        d.text((24, 5), f"{a}", fill=(random.randint(1, 255), random.randint(1, 255), 0), font=font1)
        imgblur = img.filter(ImageFilter.GaussianBlur(1.5))
        imgblur.save(fr'C:\Users\scorz\Desktop\fusionbot\captchas\{a}.png')
        img_folder_path = r'C:/Users/scorz/Desktop/fusionbot/captchas/'
        dirListing = os.listdir(img_folder_path)
        print(f'[{len(dirListing)}] Succesfully created a captcha named: {a}.')
    elif arandintv2 == 1:
        font1 = ImageFont.truetype("calibri.ttf", 19)
        d.text((24, 5), f"{b}", fill=(random.randint(1, 255), random.randint(1, 255), 0), font=font1)
        imgblur = img.filter(ImageFilter.GaussianBlur(1.5))
        imgblur.save(fr'C:\Users\scorz\Desktop\fusionbot\captchas\{b}.png')
        img_folder_path = r'C:/Users/scorz/Desktop/fusionbot/captchas/'
        dirListing = os.listdir(img_folder_path)
        print(f'[{len(dirListing)}] Succesfully created a captcha named: {b}.')
    elif arandintv2 == 1:
        font1 = ImageFont.truetype("gadugi.ttf", 19)
        d.text((24, 5), f"{c}", fill=(random.randint(1, 255), random.randint(1, 255), 0), font=font1)
        imgblur = img.filter(ImageFilter.GaussianBlur(1.5))
        imgblur.save(fr'C:\Users\scorz\Desktop\fusionbot\captchas\{c}.png')
        img_folder_path = r'C:/Users/scorz/Desktop/fusionbot/captchas/'
        dirListing = os.listdir(img_folder_path)
        print(f'[{len(dirListing)}] Succesfully created a captcha named: {c}.')

