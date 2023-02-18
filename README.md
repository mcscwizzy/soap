# Soap 
Soap is a software that removes profanity/cussing from movies by using a subtitles file. It will replace any profanity in the subtitles with ******** and silence the audio in the movie. 

# THIS IS A WORK IN PROGRESS!!!
This is a work in progress and the first initial release. EXPECT BUGS!!! Project is extremely alpha. I have not tried anything other than MP4 for video. MKV may work, but I have not attempted. 

# Prereqs
1. Windows/Mac/Linux
1. Python 3.11
1. FFMPEG

If FFMPEG and Python 3.11 are not installed this program will not work!!!

# Lauching
On first launch install required python packages
```pip install -r requirements.txt```

After installing required python packages you can run the program
```python main.py --pathToVideo ~/Videos/mymovie.mp4 --pathToSrt ~/Videos/myvideosrt.srt```

# It will take a while
Python is not a compiled language. It is not as fast as its compiled counterparts. This process takes time. You are looking at an hour to two hours depending on your system. I will look into speeding this up at a later date, but as of right now it is functional and that is a step in the right direction.

# If words are missed...
There are tons of combinations in subtitles as far as swearing goes and I know I have not got all of them. If you discover a few that I missed you can add them to the profanity.txt file so it will pick them up. Create a new branch, add them, then put in pull request and I'll merge it in. 

# Known bug
Having some issues with timestamps and audio sync. Working on getting that fixed. 


