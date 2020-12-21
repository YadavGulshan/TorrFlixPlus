# TorrFlixPlus :movie_camera:
A simple torrent streamer written in Python 3.
#### Tested on Windows 10 64bit system with Python 3.9.0

## Inspiration 😇
* [TorrFlix](https://github.com/cyberboysumanjay/TorrFlix) 🤗

### Newly Added Features :<br>
> 
*1. Movie Name Correction using IMDB API.*<br>
*2. Choose Quality between 720 and 1080. Default 720p* <br>
*3. Direct Streaming in VLC.*<br>
<br>

## Arguments 
> -1080 To Choose 1080p in Streaming
> -h for Hindi Audio

## How to use
TorrFlixPlus uses Webtorrent-CLI as stream handler.
For that we need to setup nodejs and npm.
#### Windows users can install nodejs from [here](https://nodejs.org/en/download/).

Quickly check the installed version through this command.

> nodejs -v

We're all set to install webtorrent-cli now.
#### Windows users run this command.

> npm install webtorrent-cli -g

Make sure you have Python3 and pip installed on your pc, if not run this:
#### Windows users head over here and [download](https://www.python.org/downloads/) Python3 64bit

Install all requirements at once using the command:

> pip3 install -r requirements.txt


TorrFlixPlus using VLC for streaming. Make sure it is installed in your PC. Read install instructions [here](https://www.videolan.org/vlc/)

 Let's start the script now!
 Run the script using the command
 > python3 torflixplus.py   

 Don't forget to star the repo if you like the work :)
 #### © Copyright  [Roshan](https://github.com/truroshan)
 All rights reserved.
