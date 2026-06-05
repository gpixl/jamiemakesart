from PIL import Image, ImagePalette
import os


path = "savedimages/"

images = os.listdir(path)

savedimagespath = "image/"
if not os.path.exists(savedimagespath):
	os.mkdir(savedimagespath)

for i in images:
	new = Image.open(path + i)

	size = 256

	if new.height > new.width:
		ratio = (new.width / new.height) * size
		ratio = int(ratio)
		new = new.resize((ratio, size))
	else:
		ratio = (new.height / new.width) * size
		ratio = int(ratio)
		new = new.resize((size, ratio))


	newpath = (savedimagespath + i).replace(".jpg", ".png")
	new.save(newpath)
	palette = Image.open(newpath)
	palette = palette.convert("P", dither=Image.Dither.FLOYDSTEINBERG, colors=256)
	palette.save(newpath)