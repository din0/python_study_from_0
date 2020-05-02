from PIL import Image
from PIL import ImageEnhance

im = Image.open('hxt.jpg').convert("RGB")
im.show()

enhancer = ImageEnhance.Color(im)

for i in range(1, 10000+100, 5000):
    factor = i/100
    print("color balance %f" % factor)
    enhancer.enhance(factor).show()