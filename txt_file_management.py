def is_valid_word(word: str) -> bool:
    """Return True if the word contains only allowed characters."""
    allowed_specials = set(" ,.-'") 

    for char in word:
        if char.isalpha():
            continue
        if char in allowed_specials:
            continue
        return False

    return True

def load_words(filepath: str = "words.txt") -> list[str]:
    """Reads the words.txt file and returns a list of words"""
    try:
        with open(filepath, "r", encoding="utf-8") as f:
            return [w.strip() for w in f.readlines()]
    except FileNotFoundError:
        # If the file doesn't exist, return an empty list
        return []

def save_words(words: list[str], filepath: str = "words.txt") -> None:
    """Writes the list of words into words.txt"""
    with open(filepath, "w", encoding="utf-8") as f:
        f.write("\n".join(words))