import pafy #needs youtube-dl
import time
import subprocess, threading



def download_song(url):
	song = pafy.new(url)
	path = "/Users/Sarthak/Downloads/" #Change it for windows, the path where you want the song to go
	audio = song.getbestaudio()
	audio.download(path)
	song_path = path+song.title+".webm"
	subprocess.call(["open",song_path])
	time.sleep(song.length)
	##subprocess.call([]) code to kill VLC

def get_link(mood):
	file = open("Database.txt","r")
	l = file.readlines()
	dic = {
		l[0][:-1]:l[1], 
		l[2][:-1]:l[3], 
		l[4][:-1]:l[5], 
		l[6][:-1]:l[7]
	 }
	link = ""
	for letter in dic[mood]:
		if letter==',':
			download_song(link)
			link = ""
		if letter!=',' and letter!='\n' and letter!=' ':
			link = link+letter


get_link("angry")




