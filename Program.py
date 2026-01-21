import random
Upperletter = [["A","À","Â","Ä"],"B",["C","Ç"],"D",["E","É","È","Ê","Ë"],"F","G","H",["I","Î","Ï"],"J","K","L","M","N",["O","Ô","Ö"],"P","Q","R","S","T",["U","Ù","Û","Ü"],"V","W","X",["Y","Ÿ"],"Z"]
Lowerletter = ["a","à","â","ä"],"b",["c","ç"],"d",["e","é","è","ê","ë"],"f","g","h",["i","î","ï"],"j","k","l","m","n",["o","ô","ö"],"p","q","r","s","t",["u","ù","û","ü"],"v","w","x",["y","ÿ"],"z"
Specials = [" ",",",".","-","'"]
Words = [["Bonjour","Yo"],["Fraulein","U"],["l'arc-en-ciel","hippie"],["Anticonstitutionnellement","Minecraft"]]


# Set the mystery word
def Settingguess(Word,Spec):
    Guessing = []
    Wordlist = []
    for i in Word:
        Checkspec = False
        for e in range(len(Spec)):
            if i == Spec[e]:
                Guessing += [Spec[e]]
                Checkspec = True
                break
        if Checkspec == False:
            Guessing += ["_"]
        Wordlist += [i]
    return [Guessing,Wordlist]

# Set difficulty of the game
def Setdifficultylevel(Difficulty,Words):
    if Difficulty == "1":
        return [random.choice(Words[0]),7]
    if Difficulty == "2":
        return [random.choice(Words[1]),7]
    if Difficulty == "3":
        return [random.choice(Words[2]),7]
    if Difficulty == "4":
        return [random.choice(Words[3]),1]

# Checks if input in a letter
def Checkinput(Guess,Upper,Lower):
    for i in range(26):
        if Guess in Upper[i] or Guess in Lower[i]:
            return i
    return False

# Handle game turns
def Gameturn(Word,Upper,Lower,Foundletters):
    Guess = input("Lettre : ")
    Checkresult = Checkinput(Guess,Upper,Lower)
    if isinstance(Checkresult,bool):
        print("Erreur, veuillez choisir une lettre")
        return Gameturn(Word,Upper,Lower)
    else:
        if Upper[Checkresult][0] in Foundletters:
            return [True]
        else:
            Matchlist = []
            for i in range(len(Word)):
                if Word[i] in Upper[Checkresult] or Word[i] in Lower[Checkresult]:
                    Matchlist += [i]
            if not Matchlist == []:
                return [Matchlist,[Upper[Checkresult][0]]]
            else:
                return [False,[Upper[Checkresult][0]]]

# Display updated mystery word
def Goodguess(Guessing,Word,Checkwin):
    for i in Checkwin:
        Guessing[i] = Word[i]
        Word[i] = " "
    return [Guessing,Word]

# Main branch of the game
def Game(Upper,Lower,Spec,Words):
    Difficulty = Setdifficultylevel(input("Choisissez votre difficulté : 1 2 3 4"),Words)
    Word = Difficulty[0]
    Lettersleft = len(Word)
    Turn = Difficulty[1]
    Set = Settingguess(Word,Spec)
    Guessing = Set[0]
    Wordlist = Set[1]
    Foundletters = []
    while not Turn == 0:
        print(Guessing)
        print(Wordlist)
        print(Foundletters)
        print("Chances restantes",Turn)
        print("Lettre restant à trouver",Lettersleft)
        Checkwin = Gameturn(Wordlist,Upper,Lower,Foundletters)
        if not isinstance(Checkwin[0],bool):
            Newstep = Goodguess(Guessing,Wordlist,Checkwin[0])
            Guessing = Newstep[0]
            Wordlist = Newstep[1]
            Foundletters += Checkwin[1]
            Lettersleft -= len(Checkwin[0])
            if Lettersleft == 0:
                return "Win"
        elif Checkwin[0] == True:
            print("Cette lettre à déjà été deviné.")
        else:
            Foundletters += Checkwin[1]
            Turn -= 1
    return "Perdu"
        
        

            




print(Game(Upperletter,Lowerletter,Specials,Words))

