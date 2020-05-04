from pytube import YouTube
from pytube import Playlist

import sys
dwnld_ndx = 1


def download(uri):
	global dwnld_ndx
	print(uri)
	try:
		yt = YouTube(uri)
		print(dwnld_ndx, yt.title)
		st = yt.streams.get_highest_resolution()
		st.download('./tmp')
	except:
		print("unknown url: "+ uri)
	dwnld_ndx += 1
		
def download_playlist(url):
	print(url)
	videos = Playlist(url)
	print (videos)
	#print("Number of Videos: "+ str(videos.len()))
	for video in videos:
		download(video)

		
def open_file_urllist (filename):
	f = open(filename,"r")
	lines = f.readlines()
	for line in lines:
		line = line.rstrip('\r\n')
		l = '\"'+str(line)+'\"'
		download(l)

def open_Playlist ( filename ) :
	f = open(filename,"r")
	line = f.readline()
	#line = line.rstrip('\r\n')
	url = '\"'+str(line)+'\"'
	print(url)
	download_playlist(url)
	
if __name__ == "__main__":
	#open_Playlist(sys.argv[1])
	#print(sys.argv[1])
	#download_playlist(sys.argv[1])
	download(sys.argv[1])
	
	