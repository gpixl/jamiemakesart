
import zipfile
from ppadb.client import Client as AdbClient
import os

client = AdbClient(host="127.0.0.1", port=5037)

print(client.version())
devices = client.devices()

savedimagespath = "savedimages/"

if not os.path.exists(savedimagespath):
	os.mkdir(savedimagespath)

copynote = ""
for device in devices:
	imagefiles = device.shell("ls /sdcard/android/data/com.kin.easynotes/files")
	imagefiles = imagefiles.replace("\n", "").split("  ")
	print(imagefiles)
	for i in imagefiles:
		device.pull("/sdcard/Android/data/com.kin.easynotes/files/" + i, savedimagespath + i)
	

	downloads = device.shell("ls /sdcard/Download")
	downloads = downloads.split("\n")
	for i in downloads:
		if "EasyNotes" in i:
			print(i)
			copynote = i
	device.pull("/sdcard/Download/" + copynote, "zipfolder/" + copynote)


with zipfile.ZipFile("zipfolder/" + copynote, "r") as unzip:
	unzip.extractall("")
