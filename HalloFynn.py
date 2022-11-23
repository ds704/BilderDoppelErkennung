#https://colab.research.google.com/drive/17q-vNL4HQoKg7907A4SogxPYImqJlMD-
from PIL import Image, ImageChops

def equal(img1,img2):
    return ImageChops.difference(img1,img2).getbbox() is None

im1 = Image.open("/home/ds704/Downloads/Putin1.jpeg")#durch echten Datpfad erstezen
im2 = Image.open("/home/ds704/Downloads/Selensky.jpeg")
im3 = Image.open("/home/ds704/Downloads/Putin2.jpeg")

result = equal(im1,im2)
print("Sind Putin und Selensky gleich?")
print(str(result))
print("Sind Putin und Putin gleich?")
result = equal(im1,im3)
print(str(result))