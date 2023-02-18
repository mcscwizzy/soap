from modules.srt import *
from modules.profanity import *


def main():
    srt_filepath = "/Users/johnwalker/Downloads/planet-of-the-apes.srt"
    srt_file = load_srt(filepath=srt_filepath)
    srt_map = map_srt_file(srt_file=srt_file)

    for srt in srt_map:
        srt["captions"] = find_profanity_srt(captions=srt["captions"])

    print(srt_map)


if __name__ == "__main__":
    main()
