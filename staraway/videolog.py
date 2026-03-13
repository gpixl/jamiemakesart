from PIL import Image
import os
from datetime import time
from datetime import datetime

videos = os.listdir("video")
print(videos)

links = ""
firstvideo = ""


class video:
    source = ""
    name = ""
    date = datetime


videoobjects = []

for i in videos:
    newVideo = video()
    name = i.split(".")[0]
    name = name.replace("\\u200", "")
    name = name.replace("\\u200e", "")
    newVideo.date = datetime.strptime(name, "%b-%d-%Y")
    newVideo.source = "video/" + i
    newVideo.name = name

    

    videoobjects.append(newVideo)
    

def sortByDate(e):
  return e.date.timestamp() * -1

videoobjects.sort(key=sortByDate)

for i in videoobjects:


    # os.system("ffmpeg -i " + i.source + " -vcodec mjpeg -vframes 1 -an -f rawvideo -ss `ffmpeg -i " + i.source + " 2>&1 | grep Duration | awk '{print $2}' | tr -d , | awk -F ':' '{print ($3+$2*60+$1*3600)/2}'` output_image.png")
    os.system("ffmpeg -i " + i.source + " -vf \"select=eq(n\,0)\" -q:v 3 output_image.png")

    og = Image.open("output_image.png")


    uppercrop = (og.width - og.height) / 2

    if uppercrop > 0:
        resize = og.crop((uppercrop,0,og.height+uppercrop, og.height))
    else:
        resize = og.crop((0,uppercrop*-1,og.width, og.width-uppercrop))
    
    name = i.name

    thumbnail = resize.resize((256,256))
    cropSize = 256/2/2
    thumbnail = thumbnail.crop((cropSize,cropSize,256-cropSize,256-cropSize))

    thumbnail = thumbnail.convert("P")

    thumbnail.save("thumbnails/" + i.name + ".png")
    os.remove("output_image.png")

    timecreated = i.date

    print(timecreated.strftime('%m/%d/%Y'))



    links += "<div class=\"img-wrap\" onclick=\"setVideo('" + i.source + "')\"><img src=\"thumbnails/" + i.name + ".png\"><p class=\"img-text\">" + timecreated.strftime('%b %d, %Y') + "</p></div>\n"
    if firstvideo == "":
       firstvideo = i.source

site = open("template.html").read()

newsite = site.replace("<!-- VIDEOS GO HERE -->", links)
newsite = newsite.replace("<!-- SOURCE GOES HERE -->", "<source id=\"source\" src=\"" + firstvideo + "\">")

with open("videos.html", "w") as f:
  f.write(newsite)