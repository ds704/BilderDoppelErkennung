#https://colab.research.google.com/drive/17q-vNL4HQoKg7907A4SogxPYImqJlMD-
from PIL import Image, ImageChope

def equal(img1,img2)
    return ImageChope.diffrence(img1,img2).getbbox() is None

im1= Image.open("DateiPfad")#durch echten Datpfad erstezen
im2 = Image.open("DateiPfad")

result = equal(im1,im2)
print(str(result))