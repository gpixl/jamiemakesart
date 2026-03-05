import os
from datetime import datetime

questions = os.listdir("responses")
os.chdir("responses/")
questions.sort(key=os.path.getctime)


class question:
    lines = []
    date = ""

def sortByDate(e):
  return e.date


questionobjects = []

allquestions = ""
for i in questions:


    lines = open(i).readlines()

    date = lines[0].split("\"")[5].replace("\n", "")
    date = float(date)
    

    q = question()
    q.lines = lines
    q.date = date

    questionobjects.append(q)


questionobjects.sort(key=sortByDate)

for i in questionobjects:
    lines = i.lines

    print("gonna print date")
    print(i.date)
    realdate = datetime.fromtimestamp(i.date/1000)
    datestring = realdate.strftime('%B %d, %Y')

    final = ""
    for l in range(len(lines)):
        if l > 0:
            lines[l] = "<p>" + lines[l] + "</p>"
        final += lines[l]
    final = "<div class=\"askquestion\">" + final.replace("\n","") + "<p class=\"date\">" + datestring + "</p></div>"
    allquestions = final + "\n\n" + allquestions


os.chdir("../")

crunchdeclined = ""
declined = open("declined.txt").readlines()
for i in declined:
    hash = ""
    if "\"" in i:
        hash = i.split("\"")[3]
    else:
        hash = i
    crunchdeclined += hash.replace("\n","") + "\n"
    allquestions += "<i class=\"question\" style=\"display:none\" hash=\"" + hash.replace("\n","") + "\"></i>"

with open("declined.txt", "w") as d:
  d.write(crunchdeclined)

askpage = open("template.html").read()
askpage = askpage.replace("<!-- QUESTIONS GO HERE -->", allquestions)

with open("index.html", "w") as f:
  f.write(askpage)