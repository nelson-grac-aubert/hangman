Upperletter = [["A","À","Â","Ä"],"B",["C","Ç"],"D",["E","É","È","Ê","Ë"],"F","G","H",["I","Î","Ï"],"J","K","L","M","N",["O","Ô","Ö"],"P","Q","R","S","T",["U","Ù","Û","Ü"],"V","W","X",["Y","Ÿ"],"Z"]
Lowerletter = ["a","à","â","ä"],"b",["c","ç"],"d",["e","é","è","ê","ë"],"f","g","h",["i","î","ï"],"j","k","l","m","n",["o","ô","ö"],"p","q","r","s","t",["u","ù","û","ü"],"v","w","x",["y","ÿ"],"z"
Specials = [" ",",",".","-","'"]

from txt_file_management import load_words, is_valid_word
import pygame
import random

def choose_mystery_word(filepath="words.txt"):
    """Loads words.txt, gets a random valid word, format it"""
    words = load_words(filepath)

    valid_words = [w for w in words if is_valid_word(w)]

    if not valid_words:
        raise ValueError("Aucun mot valide trouvé dans words.txt")

    return random.choice(valid_words)


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


def Checkinput(Guess,Upper,Lower):
    """ Check if keyboard input is in the word """
    for i in range(26):
        if Guess in Upper[i] or Guess in Lower[i]:
            return i
    return False


def Gameturn_pygame(event, Word, Upper, Lower, Foundletters):
    """ Game turn handling with pygame keyboard input """

    if event.type != pygame.KEYDOWN:
        return None

    Guess = event.unicode
    if Guess == "":
        return None 

    Checkresult = Checkinput(Guess, Upper, Lower)
    if Checkresult is False:
        return None

    normalized_letter = Upper[Checkresult][0]

    if normalized_letter in Foundletters:
        return [True]

    Matchlist = []
    for i in range(len(Word)):
        if Word[i] in Upper[Checkresult] or Word[i] in Lower[Checkresult]:
            Matchlist.append(i)

    if Matchlist:
        return [Matchlist, [normalized_letter]]
    else:
        return [False, [normalized_letter]]


    