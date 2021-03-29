import os
from PIL import Image

cdir = os.getcwd()
sdir = cdir + "\\Img"

w, h = 0, 0
imageList = []
for f in os.listdir(sdir):
    print(f)
    inputimg = Image.open(sdir + "\\" + f)
    w, h = inputimg.size
    img = inputimg.convert('RGB')
    imageList.append(img)
imageList.pop()
img.save(cdir + "\\mypdf.pdf", save_all=True, append_images=imageList)
