from PIL import Image, ImageFilter

image = Image.open(r"image path")

image = image.filter(ImageFilter.GaussianBlur)

image.show()
