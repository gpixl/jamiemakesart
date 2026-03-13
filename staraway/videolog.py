from PIL import Image
import os


videos = os.listdir("video")
print(videos)

links = ""

for i in videos:


    os.system("ffmpeg -i video/" + i + " -vf \"select=eq(n\,0)\" -q:v 3 output_image.png")

    og = Image.open("output_image.png")


    uppercrop = (og.width - og.height) / 2

    if uppercrop > 0:
        resize = og.crop((uppercrop,0,og.height+uppercrop, og.height))
    else:
        resize = og.crop((0,uppercrop*-1,og.width, og.width-uppercrop))
    
    name = i.split(".")[0]

    thumbnail = resize.resize((256,256))
    cropSize = 256/2/2
    thumbnail = thumbnail.crop((cropSize,cropSize,256-cropSize,256-cropSize))

    thumbnail = thumbnail.convert("P")

    thumbnail.save("thumbnails/" + name + ".png")
    os.remove("output_image.png")
    links += "<div class=\"img-wrap\"><img src=\"thumbnails/" + name + ".png\"><a class=\"img-text\" href=\"video/" + i + "\">3-13-2026</a></div>"

site = open("template.html").read()
sections = site.split("<!-- VIDEOS GO HERE -->")

print(sections)

newsite = sections[0] + links + sections[1]

with open("videos.html", "w") as f:
  f.write(newsite)