import PIL
from PIL import ImageFont
from PIL import Image
from PIL import ImageDraw

font = ImageFont.truetype("正楷字体.TTF",34)

img=Image.new("RGBA", (500,250),(255,255,255))
draw = ImageDraw.Draw(img)
draw.text((0, 0),"测试",(0,0,0),font=font)
draw = ImageDraw.Draw(img)

img.save(".\a_test.png")
