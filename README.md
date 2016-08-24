# Raspberry-Pi-simplest-MP3-player

Make your Raspberry Pi as a portable headless MP3 player.
Just power it up and hear audio through the 3.5mm jack.

Given a Python code which plays MP3 files in a shuffled manner.

It uses omxplayer to play songs indefinitely. Any version of Raspberry Pi will adapt this code.

Dump all your MP3 files in the Music folder if using Raspbian Jessie, or create a folder named Music using the command sudo mkdir home/pi/Music if you're using some other os versions.

To make it play MP3 on boot up,
in the command line type,

sudo crontab -e

and add the following line at the end of crontab

@reboot python /path/to/playMP3.py &

#Note 1:
Since we're using omxplayer, the name of mp3 files should not contain any whitespace characters.
#Note 2:
#To stop playing,
use the commands
$ sudo pkill python
$ sudo pkill omxplayer
#To play next file
$ sudo pkill omxplayer
