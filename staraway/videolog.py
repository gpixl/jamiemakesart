from PIL import Image
from datetime import time
import datetime as dt
from datetime import datetime
import os
import subprocess
import math

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
    
def get_length(input_video):
    result = subprocess.run(['ffprobe', '-v', 'error', '-show_entries', 'format=duration', '-of', 'default=noprint_wrappers=1:nokey=1', input_video], stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    return float(result.stdout)

def sortByDate(e):
  return e.date.timestamp() * -1

def pretty_timedelta(td):
    if td.days >= 0:
        return str(td)
    return f'-({-td!s})'

videoobjects.sort(key=sortByDate)

oldtimestamp = 0

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


    timeelapsed = (oldtimestamp - i.date.timestamp())
    if timeelapsed < 0:
       timeelapsed = 0
    oldtimestamp = i.date.timestamp()

    length = get_length(i.source)

    minsec = divmod(length, 60)


    length = round(length*10)/10


    links += "<div class=\"v1\" style=\"height:" + str(timeelapsed / 80000) + "px;\"></div><div class=\"img-wrap\" onclick=\"setVideo('" + i.source + "')\"><img src=\"thumbnails/" + i.name + ".png\"><p class=\"img-text\">" + timecreated.strftime('%b %d, %Y') + "<br><br>" + str(round(minsec[0])) + "m " + str(round(minsec[1])) + "s</p></div>\n"
    if firstvideo == "":
       firstvideo = i.source

site = open("template.html").read()

newsite = site.replace("<!-- VIDEOS GO HERE -->", links)
newsite = newsite.replace("<!-- SOURCE GOES HERE -->", "<source id=\"source\" src=\"" + firstvideo + "\">")

with open("videos.html", "w") as f:
  f.write(newsite)