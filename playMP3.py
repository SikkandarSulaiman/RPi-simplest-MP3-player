import os, random

path = '\home\pi\Music\\'
mp3files = []

for f in os.listdir(path):
    if f[len(f)-4:]=='.mp3':
        mp3files.append(f)


while True:
    os.system('omxplayer '+path+random.choice(mp3files))
