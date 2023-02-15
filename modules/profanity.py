def load_profanity() -> list:
    """Loads profanity file

    Returns:
        list
    """
    file = open("config/profanity.txt")
    file = file.read().splitlines()
    return file


def find_profanity(caption: str) -> bool:
    """Finds profanity on passed in caption

    Args:
        caption (str): caption from srt

    Returns:
        bool
    """
    found_profanity = False
    profanities = load_profanity()

    for profanity in profanities:
        if profanity in caption.lower():
            found_profanity = True
            break

    return found_profanity
