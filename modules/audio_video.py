import moviepy.editor as mp
from moviepy.editor import VideoFileClip, AudioFileClip, CompositeAudioClip
from pydub import AudioSegment
import os


def no_ext(videofilepath: str) -> str:
    """Removes video filepath extension

    Args:
        videofilepath (str): path to video

    Returns:
        str: return filepath with video extension
    """
    videofilepath = videofilepath.replace(videofilepath.split(".")[-1], "")
    videofilepath = videofilepath.rstrip(videofilepath[-1])
    return videofilepath


def extract_audio_from_video(videofilepath: str) -> None:
    """Extracts audio from video and saves it to a separate file

    Args:
        videofilepath (str):
    """

    # file locations
    movie_clip = f"{videofilepath}"
    audio_clip = f"{no_ext(videofilepath=videofilepath)}.wav"

    # load video
    my_clip = mp.VideoFileClip(movie_clip)

    # extract audio file
    my_clip.audio.write_audiofile(audio_clip)


def add_audio_to_video(videofilepath: str):
    """Adds clean audio to video

    Args:
        videofilepath (str)
    """
    filepath_without_ext = no_ext(videofilepath=videofilepath)
    videoclip = VideoFileClip(f"{filepath_without_ext}2.mp4")
    audioclip = AudioFileClip(f"{filepath_without_ext}2.wav")
    new_audioclip = CompositeAudioClip([audioclip])
    videoclip.audio = new_audioclip
    videoclip.write_videofile(f"{filepath_without_ext}-clean.mp4")


def remove_audio_from_video(videofilepath: str):
    """Removes audio from video so the new audio can be imported

    Args:
        videofilepath (str)
    """
    filepath_without_ext = no_ext(videofilepath=videofilepath)
    videoclip = VideoFileClip(videofilepath)
    new_clip = videoclip.without_audio()
    new_clip.write_videofile(f"{filepath_without_ext}2.mp4")


def clean_audio(videofilepath: str, timestamps: list):
    """Silences audio based on timestamps passed in

    Args:
        timestamps (list): list of tuples [(1,1), (2,2)]
        filepath (str): filepath of audio file
    """
    filepath_without_ext = no_ext(videofilepath=videofilepath)
    audio_file = AudioSegment.from_wav(f"{filepath_without_ext}.wav")

    parts = []

    # start for audio
    begin = 0

    for start, end in timestamps:

        # keep sound before silence
        mute_audio = audio_file[begin * 1000 : start * 1000]
        parts.append(mute_audio)

        # create silence
        duration = (end - start) * 1000
        mute_audio = AudioSegment.silent(duration)
        parts.append(mute_audio)

        # value for next loop
        begin = end

    # keep part after last silence
    parts.append(audio_file[begin * 1000 :])

    # join all parts using standard `sum()` but it need `parts[0]` as start value
    clean_audio = sum(parts[1:], parts[0])

    # save it
    clean_audio.export(f"{filepath_without_ext}2.wav", format="wav")


def remove_temp_files(videofilepath: str) -> None:
    """Removes temp files from processing

    Args:
        videofilepath (str):
    """

    try:
        # os.remove(f"{no_ext(videofilepath)}.wav")
        # os.remove(f"{no_ext(videofilepath)}2.wav")
        # os.remove(f"{no_ext(videofilepath)}2.mp4")
        os.remove(f"{no_ext(videofilepath)}2.srt")
    except:
        pass
