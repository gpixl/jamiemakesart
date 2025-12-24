import os
from bs4 import BeautifulSoup

writedir = "../blog/"

currentdir = "blogs/"
blogs = os.listdir(currentdir)
print(blogs)
entries = ""

template = open("template.html").read()

for b in blogs:
  

    blogfile = currentdir + b

    blog = open(blogfile).read()

    soup = BeautifulSoup(blog, "html.parser")
    title = soup.find(id="title").contents[0]
    date = soup.find(id="date").contents[0]

    entry = '<div class="entry"><a href="' + b + '">' + title + '</a> <i>' + date + '</i>'
    entries += entry + "\n"

    newblog = template.replace("<!-- TITLE -->", title)
    newblog = template.replace("<!-- CONTENT -->", blog)

    with open(writedir + b, "w") as f:
        f.write(newblog)


index = open("index.html").read()
index = index.replace("<!-- ENTRIES -->", entries)

print(entry)

with open(writedir + "index.html", "w") as f:
  f.write(index)