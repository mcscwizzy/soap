def load_srt(filepath: str) -> list:
    """Loads srt file and splits lines into list

    Args:
        filepath (str): filepath to srt

    Returns:
        list
    """

    subtitles = open(
        filepath,
        mode="r",
        encoding="utf-8-sig",
    )

    return subtitles.read().splitlines()


def map_srt_file(srt_file: list) -> list:
    """Maps srt file to a workable list of dictionaries

    Args:
        srt_raw_data (list): _description_

    Returns:
        list: _description_
    """
    srt_map = []
    srt_captions = {}

    for srt in srt_file:
        if srt == "":
            srt_map.append(srt_captions)
            srt_captions = {}
            continue
        if srt.isdigit():
            srt_captions["caption_index"] = srt
            continue
        if "-->" in srt:
            srt_captions["timestamp"] = srt
            continue
        else:
            if "captions" not in srt_captions:
                srt_captions["captions"] = [srt]
            else:
                srt_captions["captions"].append(srt)
    return srt_map


def convert_timestamp_to_seconds(timestamp: str) -> int:
    """Converts timestamp to seconds

    Args:
        timestamp (str):

    Returns:
        int:
    """
    if int(timestamp.split(":")[0]) == 00:
        timestamp = int(timestamp.split(":")[1]) * 60
    else:
        hour = int(str(timestamp.split(":")[0]).replace("0", "")) * 3600
        minute = int(timestamp.split(":")[1]) * 60
        timestamp = hour + minute
    return timestamp


def find_profanity_timestamps(srt_file: list) -> list:
    """Finds profanity at timestamps and adds to a list for muting

    Args:
        srt_file (list): _description_

    Returns:
        list: _description_
    """
    profanity_timestamps = []
    for srt in srt_file:
        for caption in srt["captions"]:
            if "********" in caption:
                timestamp_start = convert_timestamp_to_seconds(srt["timestamp"])
                timestamp_end = timestamp_start + 1
                profanity_timestamps.append((timestamp_start, timestamp_end))

    return profanity_timestamps


def write_srt_to_file(srt_map: list) -> None:
    """Writes new srt file based on the clean srt map

    Args:
        srt_map (list)
    """
    with open(
        "/Users/johnwalker/Downloads/planet-of-the-apes-clean.srt",
        "a",
        encoding="utf-8-sig",
    ) as file:
        for srt in srt_map:
            file.write(f"{srt['caption_index']}\n")
            file.write(f"{srt['timestamp']}\n")
            for caption in srt["captions"]:
                file.write(f"{caption}\n")

            file.write("\n")
