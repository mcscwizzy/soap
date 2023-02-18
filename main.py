from modules.soap import start_soap
import argparse


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--pathToVideo", help="Path to video e.g. ~/Documents/Video/Video.mp4"
    )
    parser.add_argument(
        "--pathToSrt", help="Path to SRT e.g. ~/Documents/Video/Video.srt"
    )
    args = parser.parse_args()
    start_soap(videofilepath=args.pathToVideo, srtfilepath=args.pathToSrt)


if __name__ == "__main__":
    main()
