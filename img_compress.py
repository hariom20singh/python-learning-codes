from PIL import Image
file_path =  "python-learning-codes/uncompressed_img.jpg"
img = Image.open(file_path)
height, width = img.size
compressed = img.resize((height, width), Image.ANTIALIAS)
compressed.save("python-learning-codes/compressed_img.jpg", optimize=True,quality=9)