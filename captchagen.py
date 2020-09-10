from PIL import ImageDraw, Image, ImageFont, ImageFilter
import random
import os

# importing modules needed for this to work ^

def random_char(y):
    str1 = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890'
    return ''.join(random.choice(str1) for x in range(y))

# definining function random_char which generates a random string

def random_chars(y):
    str1 = 'a b c d e f g h i j k l m n o p q r s tuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890'
    return ''.join(random.choice(str1) for x in range(y))

# definining function random_char which generates a random string with a few spaces

def random_chars2(y):
    str1 = 'a b c d e f g h i j k l m n o p q r s t u v w x y z A B C D E F G H I J K L M N O P Q R S T U V W X Y Z 1 2 3 4 5 6 7 8 9 0'
    return ''.join(random.choice(str1) for x in range(y))

# definining function random_char which generates a random string with all spaces

input('this mass generates capcthas btw, u sure u want to run this?') #a warning if you cant read comments or smtin

fontsize = random.randint(7, 16) #defining fontsize var and setting its value to a random intiger between 7 and 16
c1 = True #assigning a true value to c1 incase you want a single captcha
while True: #while loop which mass generates captchas, if you dont want it to mass generate just make it a if statement
    # MASS GENERATES CAPTCHAS WARNING
    # MASS GENERATES CAPTCHAS WARNING
    # MASS GENERATES CAPTCHAS WARNING
    a = random_char(random.randint(4, 7)) #defining a var and setting its value to a random intiger between 4 and 7
    b = random_chars(random.randint(4, 8)) #defining b var and setting its value to a random intiger between 4 and 8
    c = random_chars2(random.randint(4, 7)) #defining c var and setting its value to a random intiger between 3 and 7
    img = Image.new('RGB', (100, 30), color=(31, 27, 27)) #setting color
    d = ImageDraw.Draw(img) #defining b
    arandint = random.randint(0, 5) #setting value to var
    arandintv2 = random.randint(0, 5) #setting value to var 
    if arandint == 1:
        #if statement ^
        d.line((0, 0) + img.size, fill=200)
        d.line((10, 0) + img.size, fill=200)
        d.line((20, 0) + img.size, fill=200)
        d.line((30, 0) + img.size, fill=89)
        d.line((45, 0) + img.size, fill=89)
        d.line((10, 0) + img.size, fill=200)
        d.line((27, 0) + img.size, fill=246)
        d.line((34, 0) + img.size, fill=44)
        d.line((67, 0) + img.size, fill=45)
        #bunch of lines^
    elif arandint == 2:
        #elif statement ^
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
        #bunch of lines^
    elif arandint == 3:
        #elif statement ^
        d.line((0, 0) + img.size, fill=2)
        d.line((10, 0) + img.size, fill=140)
        d.line((20, 0) + img.size, fill=99)
        d.line((10, 0) + img.size, fill=200)
        d.line((29, 0) + img.size, fill=200)
        d.line((36, 0) + img.size, fill=89)
        d.line((58, 0) + img.size, fill=89)
        #bunch of lines^
    elif arandint == 4:
        #elif statement ^
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
        #bunch of lines^
    elif arandint == 5:
        #elif statement ^
        d.line((0, 0) + img.size, fill=99)
        d.line((10, 0) + img.size, fill=57)
        d.line((6, 0) + img.size, fill=80)
        d.line((30, 0) + img.size, fill=240)
        d.line((37, 0) + img.size, fill=1)
        d.line((60, 0) + img.size, fill=53)
        #bunch of lines^
    if arandintv2 == 1:
        #if statement ^
        font1 = ImageFont.truetype("arial.ttf", 19) #setting font
        d.text((24, 5), f"{a}", fill=(random.randint(1, 255), random.randint(1, 255), 0), font=font1) #setting text color and stuff
        imgblur = img.filter(ImageFilter.GaussianBlur(1.5)) #adding blur
        imgblur.save(fr'yourpath\{a}.png') #saving
        img_folder_path = r'C:/Users/scorz/Desktop/fusionbot/captchas/' #assigning value
        dirListing = os.listdir(img_folder_path) #assigning value
        print(f'[{len(dirListing)}] Succesfully created a captcha named: {a}.') #some print shit to make it look good
    elif arandintv2 == 1:
        #elif statement ^
        font1 = ImageFont.truetype("calibri.ttf", 19)
        d.text((24, 5), f"{b}", fill=(random.randint(1, 255), random.randint(1, 255), 0), font=font1)
        imgblur = img.filter(ImageFilter.GaussianBlur(1.5))
        imgblur.save(fr'C:\Users\scorz\Desktop\fusionbot\captchas\{b}.png')
        img_folder_path = r'C:/Users/scorz/Desktop/fusionbot/captchas/'
        dirListing = os.listdir(img_folder_path)
        print(f'[{len(dirListing)}] Succesfully created a captcha named: {b}.')
        #same thing which i said in first if statement for arandintv2
    elif arandintv2 == 1:
        #elif statement ^
        font1 = ImageFont.truetype("gadugi.ttf", 19)
        d.text((24, 5), f"{c}", fill=(random.randint(1, 255), random.randint(1, 255), 0), font=font1)
        imgblur = img.filter(ImageFilter.GaussianBlur(1.5))
        imgblur.save(fr'C:\Users\scorz\Desktop\fusionbot\captchas\{c}.png')
        img_folder_path = r'C:/Users/scorz/Desktop/fusionbot/captchas/'
        dirListing = os.listdir(img_folder_path)
        print(f'[{len(dirListing)}] Succesfully created a captcha named: {c}.')
        #same thing which i said in first if statement for arandintv2

