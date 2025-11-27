from PIL import Image
import os


images = os.listdir("assets/")

works = open("artworks.txt").read()
allworks = works.split(";;")

allhtml = ""

for i in allworks:
    worktags = i.split("\n")
    if len(worktags) > 1:
        if len(worktags[0]) > 1:
            readimg = Image.open("assets/" + worktags[0])
            dimensions = str(readimg.width) + 'x' + str(readimg.height)
            htmlstring = '<div class="image-wrap"><img\nlink="' + worktags[1] + '"\ndisplay="assets/' + worktags[0] + '"\nalt="' + worktags[2] + '"\ndimensions="' + dimensions + '">\n<p class="image-text">' + worktags[2] + '<br><br>(Click to view)</p></div>'
            allhtml = allhtml + htmlstring

site = open("index copy.html").read()
sections = site.split("<!-- IMAGES -->")

newsite = sections[0] + "<!-- IMAGES -->\n" + allhtml + "<!-- IMAGES -->\n" + sections[2]
print(newsite)

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
        resize = resize.resize((128, 128))

        thumbnail = Image.new("RGBA", (128,128))
        thumbnail.paste(resize, (0,0))
        if not os.path.exists("assets/thumbnails"):
            os.mkdir("assets/thumbnails")
        i = i.replace(".jpg", ".png").replace(".gif", ".png")
        thumbnail.save("assets/thumbnails/" + i)