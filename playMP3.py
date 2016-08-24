import os, random

path = '/home/pi/Music/'
mp3files = []
played = []

for f in os.listdir(path):
    if f[len(f)-4:]=='.mp3':
        mp3files.append(f)

track=random.choice(mp3files)
os.system('omxplayer '+path+track)
played.append(track)
#Play a track,
#make sure that track is not repeated until all tracks are played atleast once
while True:
    track=random.choice(mp3files)
    if len(played) == len(mp3files):
        played = []
    try:
        played.index(track)
    except ValueError or IndexError:
        os.system('omxplayer '+path+track)
        played.append(track)
        continue

