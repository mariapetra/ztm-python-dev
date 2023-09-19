from PIL import Image, ImageFilter

img = Image.open("./images/pikachu.jpg")
filtered_img = img.filter(ImageFilter.EMBOSS)

filtered_img = img.convert("L")
filtered_img.save("grey.png", "png")

print(img.format)
print(img.size)
print(img.mode)

print(dir(img))
# will show all the things we can use
