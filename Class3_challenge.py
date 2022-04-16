from PIL import Image, ImageDraw, ImageFont

# create Image object
text1 = "create Feature Image"
text2 = "With Python"
img_name = "featured-image-creation-with-python.png"
color = "dark_blue"
font = "Roboto-Bold.ttf"

new_image = Image.new("RGB", (60, 30), color="red")
new_image.save("python_image.png")
# background = Image.open("default.png")
# foreground = Image.open("python-logo.png")

