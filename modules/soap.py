from modules.srt import *
from modules.profanity import *
from modules.audio_video import *


def start_soap(videofilepath: str, srtfilepath: str):
    print("Loading srt file")
    srt_file = load_srt(filepath=srtfilepath)

    print("Mapping srt file to object")
    srt_map = map_srt_file(srt_file=srt_file)

    print("Removing profanity from srt map")
    for srt in srt_map:
        srt["captions"] = find_profanity_srt(captions=srt["captions"])

    print("Extracting audio from video")
    extract_audio_from_video(videofilepath=videofilepath)

    print("Get timestamps of profanity from srt file")
    timestamps = find_profanity_timestamps(srt_file=srt_map)

    print("Removing profanity from audio")
    clean_audio(videofilepath=videofilepath, timestamps=timestamps)

    print("Remove audio from video")
    remove_audio_from_video(videofilepath=videofilepath)

    print("Adding clean audio to video")
    add_audio_to_video(videofilepath=videofilepath)

    print("Writing new srt file")
    write_srt_to_file(srt_map=srt_map, srtfilepath=srtfilepath)

    print("Removing temp files")
    remove_temp_files(videofilepath=videofilepath)

    print("Done!")
