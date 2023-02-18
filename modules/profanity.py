def load_profanity() -> list:
    """Loads profanity file

    Returns:
        list
    """
    file = open("config/profanity.txt")
    file = file.read().splitlines()
    return file


def find_profanity_srt(captions: list) -> list:
    """Finds profanity on passed in caption and replaces with ****

    Args:
        caption (str): caption from srt

    Returns:
        bool
    """
    profanities = load_profanity()
    clean_captions = []

    for profanity in profanities:
        for caption in captions:
            if profanity in caption.lower():
                clean_captions.append(str(caption).replace(profanity, "****"))

    if len(clean_captions) == 0:
        clean_captions = captions

    return clean_captions
