from pytube import YouTube
from pytube import Playlist
print("1-download with link \n2-download a playlist \n")
choseSection = input("Pls Enter read the sections and choese right sections : (1,2,..n)\n")

if choseSection=="1":
	mylink = input("Pls Enter Your Link (https://www.youtube.com/watch?v=-QNYom5cJJs):\n")
	mylink = YouTube(mylink)
	print('title : ' + mylink.title)
	print("view count : {}".format(mylink.views))
	print("Yes / NO")
	condition = input("Pls Enter Y or N :")
	if condition == "Y" or condition =="y" :
		print("Downloading ......")
		stream = mylink.streams.get_highest_resolution()
		stream.download("/Users/Amirabbas/Desktop")

	elif condition == "N" or condition == "n" :
		exit()

if choseSection == "2":
	myPlaylistlink = input("Pls Enter ur playlist Link : \n")
	p = Playlist(myPlaylistlink)
	print(f'Downloading: {p.title}')
	print("view count : {}".format(p.views))
	print("Yes / NO")
	condition = input("Pls Enter Y or N :")
	if condition == "Y" or condition =="y" :
		print("Downloading ......")
		for video in p.videos:
			video.streams.get_highest_resolution().download("/Users/Amirabbas/Desktop")
	elif condition == "N" or condition == "n" :
		exit()
