import codecs


text = open("eviltext.html").read()


# swap = {
# 	"<p>": "PSTART",
# 	"</p>": "PEND",
# 	"<ul>": "LSTART",
# 	"</ul>": "LEND",
# 	"<li>": "ISTART",
# 	"</li>": "IEND",
# 	"<br>": "BREAK",
# 	"<b>": "BSTART"

# }


swap = {
	"<": "HSTART",
	"/": "SLASH",
	">": "HEND",
	"\n": "NEWLINE",
	"	": "TAB"
}

for x, y in swap.items():
	text = text.replace(x, y)

text = codecs.encode(text, 'rot_13')

print(text)

with open("goodtext.txt", "w") as f:
  f.write(text + "\n")