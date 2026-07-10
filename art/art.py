import PIL
from PIL import Image, ImagePalette
import os
from datetime import datetime
import random


images = os.listdir("assets/")

works = open("artworks.txt").read()
allworks = works.split(";;")

allhtml = ""

class artwork:
	source = ""
	name = ""
	date = ""
	link=""
	description=""
	group=""

class group:
	name = ""
	lastdateadded = ""

artworks = []
groups = []


def timeInt(gettime):
	return datetime.strptime(gettime, "%B %Y").timestamp()

for i in allworks:
	worktags = i.split("\n")
	if len(worktags) > 1:
		if len(worktags[0]) > 1:
			#readimg = Image.open("assets/" + worktags[0].split(" - ")[0])
			#dimensions = str(readimg.width) + 'x' + str(readimg.height)
			
			newArtwork = artwork()

			newArtwork.name = worktags[0].split('.')[0]


			
			newArtwork.source = worktags[0].split(" - ")[0]
			groupname = "none"
			if len(worktags[0].split(" - ")) > 1:
				groupname = worktags[0].split(" - ")[1]
			newArtwork.group = groupname

			addedgroup = False
			for g in groups:
				if g.name == groupname:
					addedgroup = True
					if (timeInt(worktags[3]) > timeInt(g.lastdateadded)):
						g.lastdateadded = worktags[3]

					
			if not addedgroup:
				newGroup = group()
				newGroup.name = groupname
				newGroup.lastdateadded = worktags[3]
				groups.append(newGroup)

			newArtwork.link = worktags[1]
			newArtwork.description = worktags[2]
			newArtwork.date = worktags[3]


			artworks.append(newArtwork)
			#postedDate = datetime.strptime(worktags[3], "%B %Y")
			#htmlstring = '<div class="image-wrap"><img id="' + worktags[0].split('.')[0] + '" \nlink="' + worktags[1] + '"\ndisplay="assets/' + worktags[0].split(" - ")[0] + '"\nalt="' + worktags[2] + '"\ndimensions="' + dimensions + '"\ndate="' + worktags[3] + '">\n<p class="image-text">' + worktags[2] + '<br><br>' + postedDate.strftime("%b %Y") + '<br></p></div>'
			#allhtml = htmlstring + allhtml



for i in groups:
	print(i.name)
	print(i.lastdateadded)

def getGroup(a):
	selectedgroup = None
	for i in groups:
		if a.group == i.name:
			selectedgroup = i
	return selectedgroup

def sortByGroup(e):
  return -timeInt(getGroup(e).lastdateadded)

def sortByTime(e):
  return -timeInt(e.date)

artworks = sorted(artworks, key=lambda x:(sortByGroup(x), sortByTime(x)))

currentgroup = ""
oldgroup = "NULL"
prefix = ""

for i in artworks:
	readimg = Image.open("assets/" + i.source)
	dimensions = str(readimg.width) + 'x' + str(readimg.height)
	postedDate = datetime.strptime(i.date, "%B %Y")


	htmlstring = '<div class="image-wrap"><img id="' + i.name + '" \nlink="' + i.link + '"\ndisplay="assets/' + i.source + '"\nalt="' + i.description + '"\ndimensions="' + dimensions + '"\ndate="' + i.date + '">\n<p class="image-text">' + i.description + '<br><br>' + postedDate.strftime("%b %Y") + '<br></p></div>'
	
	currentgroup = i.group
	if oldgroup != currentgroup:
		print(htmlstring)
		htmlstring = prefix + '\n\n<div class="box"><p>' + currentgroup + '</p>' + htmlstring
		oldgroup = currentgroup
		prefix = "</div>"
		

	allhtml = allhtml + htmlstring


site = open("template.html").read()
sections = site.split("<!-- IMAGES -->")

newsite = sections[0] + "<!-- IMAGES -->\n" + allhtml + "<!-- IMAGES -->\n" + sections[2]

with open("index.html", "w") as f:
	f.write(newsite)


def is_valid_image_pillow(file_name):
	try:
		with Image.open(file_name) as img:
			img.verify()
			return True
	except (IOError, SyntaxError):
		return False

for i in images:

	if is_valid_image_pillow("assets/" + i):
		og = Image.open("assets/" + i)

		uppercrop = (og.width - og.height) / 2

		if uppercrop > 0:
			resize = og.crop((uppercrop,0,og.height+uppercrop, og.height))
		else:
			resize = og.crop((0,uppercrop*-1,og.width, og.width-uppercrop))
		resize = resize.resize((512, 512))
		resize = resize.convert("RGB")
		resize = resize.resize((128, 128))


		thumbnail = Image.new("RGB", (128,128))
		thumbnail.paste(resize, (0,0))

		thumbnail = thumbnail.convert("P")
		if not os.path.exists("assets/thumbnails"):
			os.mkdir("assets/thumbnails")
		i = i.replace(".jpg", ".png").replace(".gif", ".png")
		thumbnail.save("assets/thumbnails/" + i)