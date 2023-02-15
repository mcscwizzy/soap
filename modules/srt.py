def load_srt(filepath: str) -> list:
    """Loads srt file and splits lines into list

    Args:
        filepath (str): filepath to srt

    Returns:
        list
    """

    subtitles = open(filepath
        mode="r",
        encoding="utf-8-sig",
    )

    return subtitles.read().splitlines()


def map_srt_file(srt_raw_data: list) -> list:
    """Maps srt file to a workable list of dictionaries

    Args:
        srt_raw_data (list): _description_

    Returns:
        list: _description_
    """
    srt_map = []
    srt_captions = {}

    for srt in srt_raw_data:
        if srt == "":
            srt_map.append(srt_captions)
            srt_captions = {}
            continue
        if srt.isdigit():
            srt_captions["caption_index"] = srt
            continue
        if "-->" in srt:
            srt_captions["time_stamp"] = srt
            continue
        else:
            if "captions" not in srt_captions:
                srt_captions["captions"] = [srt]
            else:
                srt_captions["captions"].append(srt)
    return srt_map
