import moviepy.editor as mp

# file locations
movie_clip = "/Users/johnwalker/Downloads/planet-of-the-apes.mp4"
audio_clip = "/Users/johnwalker/Downloads/planet-of-the-apes-audio.mp3"

# load video
my_clip = mp.VideoFileClip(movie_clip)

# extract audio file
my_clip.audio.write_audiofile(audio_clip)
