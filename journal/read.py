import sqlite3
from datetime import datetime
import random

c = sqlite3.connect("note-list.db")

cur = c.cursor()

tablelist = []

t = cur.execute('SELECT name FROM sqlite_master WHERE name="notes-table"')

def sortByDate(e):
  return e.date


chars = " ,abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ.!?-'()"
mixchars = "uMARjmKLTDphXws?voF -Gb,OEySdiJCqlgPce.nzYZxHV'tQIkfaBNWrU![]"



def mix(s):
	s = s[::-1]
	
	allchars = list(chars)

	fin = ""
	for i in range(len(s)):
		if s[i] in allchars:
			fin += mixchars[allchars.index(s[i])]
		else:
			fin += s[i]
	s = fin

	return s

def unmix(s):
	s = s[::-1]
	
	allchars = list(mixchars)

	fin = ""
	for i in range(len(s)):
		if s[i] in allchars:
			fin += chars[allchars.index(s[i])]
		else:
			fin += s[i]
	s = fin

	return s


class note:
	title = ""
	text = ""
	date = ""

notes = []


all = t.execute('SELECT * FROM "notes-table"')

savefile = ""

for i in all:
	thistitle = i[1]
	thistext = i[2]
	thistime = i[5]

	n = note()
	n.title = thistitle
	n.text = thistext
	n.date = thistime

	notes.append(n)

finalall = ""

# https://www.w3schools.com/python/python_datetime.asp

notes.sort(key=sortByDate)
notes.reverse()

random.seed(5)

for i in notes:

	imagerep = "!(/storage/emulated/0/Android/data/com.kin.easynotes/files/"

	t = i.text
	t = t.replace(".jpg)", '.png">')
	t = t.replace(imagerep, '<img src="image/')


	fin = t

	newdate = datetime.fromtimestamp(int(i.date / 1000))
	datestring = newdate.strftime("%b %d, %Y - %I:%M%p")

	print(datestring)

	id = str(random.randrange(100000, 999999))

	all = ""
	for l in t.split("\n"):
		if not "<img" in l:
			l = mix(l)
			l = "=s=" + l + "=s="
		print(l)
		all += l + "\n"

	all = '<p class="notecontents" id="' + id + '" style="display:none;">' + all + "</p>"
	t = all

	t = '<a class="journaldate" onclick="unscramble(' + "'" + id + "'" + ', this)">' + datestring + "</a>\n" + t

	t = t.replace("\n", "<br>")

	t = "<div><p>" + t + "</p></div>\n"
	finalall += t

template = open("template.html").read()


with open("index.html", "w") as w:
	w.write(template.replace("<!--NOTESHERE-->", finalall))