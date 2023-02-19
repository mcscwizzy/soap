# Soap 
Soap is an open source software that removes profanity/cussing from movies by using an SRT subtitle file. It will replace profanity in the subtitles with ******** and silence the audio in the movie. Any additional profanity that you wish to be covered can be put in the ```config\profanity.txt``` file. 

This is a personal project that I started a few months ago because I was tired of all the swearing in movies. More and more good movies are completed ruined by language. There are a few paid services out there that do just that, but I wanted something I could run on my own network and save onto my Plex server. 

This is a labor of love. I will be maintaining this for as long as I can. I plan on expanding this into a web app for our terminal shy friends. 

# Compatibility
This is a crossplatform solution. I wrote this app on a Mac, and tested on Linux. Windows is next on the list, but it should work just fine. Just be aware if using Windows to please escape your backslashes when including filepaths. So for example: ```python main.py --pathToVideo "c:\\path\\to\\your\\video.mp4" --pathToSrt "c:\\path\\to\\your\\srtFile.srt"```


# How to install
```
# Install preReqs 
# WINDOWS
# See https://chocolatey.org/install how to install chocolatey
choco install ffmpeg
choco install python

# MAC
# See https://brew.sh how to install brew
brew install ffmpeg
brew install python

# Debian based distros
# For all other distros and OS's you just need python3.11 and FFMPEG
sudo apt update && sudo apt upgrade -y
sudo apt install ffmpeg
sudo apt install python3.11

# Clone the repo
git clone https://github.com/mcscwizzy/soap.git

# CD into directory
cd ./soap

# install required Python libraries
pip install -r requirements.txt

# Soap can now be run
python main.py --pathToVideo /path/to/your/video.mp4 --pathToSrt /path/to/your/srtFile.srt
```

# It will take a while
Python is not as fast as its compiled counterparts. This process takes time. You are looking at around two hours depending on your system. 

# If words are missed...
There are many different combinations of swear words in the English language. I have included the basic spelling and phrases of those
words in the ```config\profanity.txt``` file. If there are additional words that you wish to have bleeped out enter them into that text
file and the app will it pick up. It's just the opposite if you want some words to come through. Just take them out of the list in the config file.