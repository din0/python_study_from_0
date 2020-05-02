from PIL import Image, ImageFilter, ImageOps

import os

def Formula(x, y, alpha):
    """
    :param a: 
    :param b: 
    :param alpha: 
    :return: 
    """
    return min(int(x*255/(256-y*alpha)), 255)

def SketchDrawer(image,blur=6, alpha=1.0):
    """
    :param blur:
    :param alpha:
    :return:
    """
    image_name = os.path.splitext(image)[0]
    image = Image.open('hxt.jpg') # 加载图片
    luminance_image = image.convert('L') # 图片转换成灰度图
    luminance_img_copy = luminance_image.copy()
    inverted_image = ImageOps.invert(luminance_img_copy) # 反转颜色

    for i in range(blur): # 模糊度
        # ImageFilter.BLUR为模糊滤波,处理之后的图像会整体变得模糊
        inverted_image = inverted_image.filter(ImageFilter.BLUR)
    width, height = luminance_image.size

    for x in range(width):
        for y in range(height):
            # 返回给定位置的像素值。如果图像为多通道，则返回一个元组。
            pixel_luminance = luminance_image.getpixel((x, y))
            pixel_inverted = inverted_image.getpixel((x, y))
            luminance_image.putpixel((x, y), Formula(pixel_luminance, pixel_inverted, alpha))
    
    luminance_image.show() # 展示图片效果
    luminance_image.save('{0}_L.jpg'.format(image_name))
    
SketchDrawer('20190623191235.jpg')