Upperletter = [["A","À","Â","Ä"],"B",["C","Ç"],"D",["E","É","È","Ê","Ë"],"F","G","H",["I","Î","Ï"],"J","K","L","M","N",["O","Ô","Ö"],"P","Q","R","S","T",["U","Ù","Û","Ü"],"V","W","X",["Y","Ÿ"],"Z"]
Lowerletter = ["a","à","â","ä"],"b",["c","ç"],"d",["e","é","è","ê","ë"],"f","g","h",["i","î","ï"],"j","k","l","m","n",["o","ô","ö"],"p","q","r","s","t",["u","ù","û","ü"],"v","w","x",["y","ÿ"],"z"
Specials = [" ",",",".","-","'"]

from txt_file_management import load_words, is_valid_word
import random

def choose_mystery_word(filepath="words.txt"):
    """Loads words.txt, gets a random valid word, format it"""
    words = load_words(filepath)

    valid_words = [w for w in words if is_valid_word(w)]

    if not valid_words:
        raise ValueError("Aucun mot valide trouvé dans words.txt")

    return random.choice(valid_words)

mot_a_tester = choose_mystery_word("words.txt")
print(mot_a_tester)

def format_mystery_word(word, specials):
    """Format the chosen mystery word into Guessing and Wordlist lists."""
    Guessing = []
    Wordlist = []

    for char in word:
        if char in specials:
            Guessing.append(char)
        else:
            Guessing.append("_")
        Wordlist.append(char)

    return Guessing, Wordlist

listes_formatees = format_mystery_word(mot_a_tester, Specials)
print(listes_formatees)



