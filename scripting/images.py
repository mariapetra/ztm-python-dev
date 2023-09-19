from PIL import Image, ImageFilter

img = Image.open("./images/pikachu.jpg")
filtered_img = img.filter(ImageFilter.EMBOSS)

filtered_img = img.convert("L")
filtered_img.save("grey.png", "png")
filtered_img.show()
filtered_img.rotate(90)
resize = filtered_img.resize((300, 300))
resize.save("newsize.png", "png")

box = (100, 100, 400, 400)
region = filtered_img.crop(box)
region.save("crop.png", "png")

print(img.format)
print(img.size)
print(img.mode)

print(dir(img))
# will show all the things we can use

# resize astro image

astro = Image.open("./images/astro.jpg")
astro.thumbnail((300, 300))
astro.save("small_astro.png", "png")

print(astro.size)
# will keep aspect ratio
