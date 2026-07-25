
template = open("template.html").read().split("***")

built = ""
for i in template:
	if ".html" in i:
		insert = open(i).read()
		built += insert
	else:
		built += i

with open("index.html", "w") as f:
  f.write(built + "\n")