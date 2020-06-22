from pytube import YouTube
from pytube import Playlist

import sys
import argparse
dwnld_ndx = 1


def download(uri):
	global dwnld_ndx
	#print(uri)
	try:
		yt = YouTube(uri)
		print(dwnld_ndx, yt.title)
		st = yt.streams.get_highest_resolution()
		st.download('./tmp')
	except:
		print("unknown url: "+ uri)
	dwnld_ndx += 1
		
def download_playlist(url):
	#print(url)
	videos = Playlist(url)
	#print (videos)
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

    parser = argparse.ArgumentParser(description='Process some options.')

    parser.add_argument('-v', '--video', const=1, nargs='?', help='Specifies the url is a video(default')
    parser.add_argument('-l', '--list', const=1, nargs='?', help='Specities the usl is a video playlist')
    parser.add_argument('url')

    args = parser.parse_args()
    print(args.url)

    if (args.list != None):
        download_playlist(args.url)
    else :
        download(args.url)
	
	