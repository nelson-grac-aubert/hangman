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

# DIFFICULTY MANAGEMENT

difficulty_levels = ["Easy", "Medium", "Hard", "Impossible"]
difficulty_index = 1

def get_difficulty():
    return difficulty_levels[difficulty_index]

def set_difficulty(index):
    global difficulty_index
    difficulty_index = index % len(difficulty_levels)

def establish_difficulty_word_list(difficulty) : 
    """ Return different lists of words depending on difficulty """
    easy_list = []
    medium_list = []
    hard_list = []

    if difficulty == "Easy" : 
        for element in load_words() : 
            if len(element) <= 6 : 
                easy_list.append(element)
        return easy_list
    if difficulty == "Medium" : 
        for element in load_words() : 
            if 6 < len(element) <= 9 : 
                medium_list.append(element)
        return medium_list
    if difficulty == "Hard" or difficulty == "Impossible" : 
        for element in load_words() : 
            if 9 < len(element) <= 12 : 
                hard_list.append(element)
        return hard_list