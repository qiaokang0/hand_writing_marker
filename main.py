import PIL
from PIL import ImageFont
from PIL import Image
from PIL import ImageDraw
import numpy as np

font = ImageFont.truetype("D:\正楷字体.TTF", 34)
zt = Image.new("RGB", (400, 41), (255, 255, 255))
draw = ImageDraw.Draw(zt)
draw.text((0, 0), "不", (0, 0, 0), font=font)
draw = ImageDraw.Draw(zt)
def judge(x):
    return x>250
def border(ns,judge=judge,buffer=1):
    c=judge(ns[0])
    l,r=0,len(ns)-1
    while l<r and c==judge(ns[l]):
        l+=1
    while l<r and c==judge(ns[r]):
        r-=1
    return (max(0,l-buffer),min(r+buffer,len(ns)-1))
def crop(im):
    ima=np.asarray(im)
    hs=np.min(ima,(1,2))
    h=border(hs)
    ws=np.min(ima,(0,2))
    w=border(ws)
    return h,w
h,w=crop(zt)
zt=zt.crop((w[0],h[0],w[1],h[1]))

def pad(zt,z,rg=20,step=5):
    zta=255-np.asarray(zt)
    za=255-np.asarray(z)
    ii,jj,mx=0,0,0
    for r in range(0,rg+1,step):
        
    for i in range(-rg, rg, step):
        for j in range(-rg, rg, step):
            zta2 = np.pad(zta, ((max(0, i), max(0, -i)), (max(0, j), max(0, -j)), (0, 0)), 'constant', constant_values=0)
            zt2 = Image.fromarray(zta2).resize(z.size)
            zt2.show()
            # Image.fromarray(za).show()
            # quit()
            zta2 = np.asarray(zt2)
            s = np.sum(np.concatenate(zta2 * za))

            if s > mx:
                mx = s
                ii, jj = i, j
            print(s, i, j)
    return ii,jj

# zt.show()
z = Image.open("D:\\不.png").convert('RGB')

ii,jj=pad(zt,z)
print("answer:",ii,jj)



quit()

img = img.resize((1000, 1000))
img_a = np.asarray(img)
print(img_a.shape)

img.show()
# img.save("D:\\a_test.png")


zitie = 255 - img_a
zitie_img = Image.fromarray(np.uint8(zitie))
# zitie_img.show()
zi = 255 - np.asarray(im)[:, :, :3]
zi_img = Image.fromarray(np.uint8(zi))
# zi_img.show()

mx = 0
ii, jj = 0, 0
# print(zitie.shape)
rg = 20
for i in range(-rg, rg):
    for j in range(-rg, rg):
        zitie2 = np.pad(zitie, ((max(0, i), max(0, -i)), (max(0, j), max(0, -j)), (0, 0)), 'constant',
                        constant_values=0)
        #         zitie2.resize(zi.shape)
        #         print(zitie2.shape)
        zitie2_img = Image.fromarray(zitie2).resize(zi_img.size)
        #         print(zitie2_img.size)
        zitie2 = np.asarray(zitie2_img)
        #         print(i,j,mx)
        #         if i==0 and j==0:
        #             Image.fromarray(np.uint8(zitie2)).show()
        s = np.sum(np.concatenate(zitie2 * zi))
        # #         print(i,j,s)
        if s > mx:
            mx = s
            ii, jj = i, j
            print(mx, i, j)

# #         zitie2_img.show()

zitie2 = np.pad(zitie, ((max(0, ii), max(0, -ii)), (max(0, jj), max(0, -jj)), (0, 0)), 'constant', constant_values=0)
zitie2_img = Image.fromarray(zitie2).resize(zi_img.size)

Image.fromarray(np.uint8(zitie)).show()
Image.fromarray(np.uint8(zitie2)).show()
Image.fromarray(np.uint8(zi)).show()
