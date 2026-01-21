import pygame
from sound_control import * 
from game_logic import * 
from game_logic import (choose_mystery_word,format_mystery_word,Checkinput,
    Gameturn_pygame,Upperletter,Lowerletter,Specials)

mute_icon, unmute_icon, sound_rect = load_sound_icons()
sound_mute_icon, sound_unmute_icon, sfx_rect = load_sfx_icons()

def load_hangman_images():
    images = {}
    for i in range(7):
        img = pygame.image.load(f"assets/images/{i}_lives.png")
        images[i] = pygame.transform.smoothscale(img, (200, 200))
    return images

hangman_imgs = load_hangman_images()

def draw_hangman(screen, lives, x, y):
    lives = max(0, min(6, lives))
    img = hangman_imgs[lives]
    screen.blit(img, (x, y))


def draw_back_button(screen, button_font):
    """Draws the back-to-menu button and returns its rect."""
    back_btn = pygame.Rect(600, 537, 300, 50)
    txt = button_font.render("Back to main menu", True, (0, 0, 0))
    screen.blit(txt, (back_btn.x + 100, back_btn.y + 5))
    return back_btn


def draw_wrong_letters(screen, font, wrong_letters, x, y):
    """Affiche les lettres incorrectes."""
    if wrong_letters:
        text = " ".join(wrong_letters)
    else:
        text = ""

    label = font.render(text, True, (255, 255, 255)) 
    screen.blit(label, (x, y))



def new_game_menu(screen, blackboard, button_font,
                  mute_icon, unmute_icon, sound_rect, is_muted, sound_muted, lives_remaining):

    # INITIALIZE GAME
    Word = choose_mystery_word()
    Guessing, Wordlist = format_mystery_word(Word, Specials)
    Foundletters = []
    Wrongletters = []

    in_game = True

    while in_game:
        screen.blit(blackboard, (0, 0))

        draw_sound_button(screen, is_muted, mute_icon, unmute_icon, sound_rect)
        draw_sfx_button(screen, sound_muted, sound_mute_icon, sound_unmute_icon, sfx_rect)

        back_btn = draw_back_button(screen, button_font)

        draw_hangman(screen, lives_remaining, 125, 80)

        wrong_label = button_font.render("letters not in word :", True, (255, 255, 255))
        screen.blit(wrong_label, (450, 300))
        draw_wrong_letters(screen, button_font, Wrongletters, 450, 330)

        # CURRENT WORD
        word_str = " ".join(Guessing)
        txt = button_font.render(word_str, True, (255, 255, 255))
        screen.blit(txt, (150, 350))

        pygame.display.flip()

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

            # KEYBOARD
            if event.type == pygame.KEYDOWN:
                result = Gameturn_pygame(event, Wordlist, Upperletter, Lowerletter, Foundletters)

                if result is None:
                    continue

                if result == [True]:
                    pass

                elif result[0] is False:
                    lives_remaining -= 1

                    wrong_letter = result[1][0]
                    if wrong_letter not in Wrongletters:
                        Wrongletters.append(wrong_letter)

                else:
                    Matchlist, Letter = result
                    Foundletters.append(Letter[0])
                    for pos in Matchlist:
                        Guessing[pos] = Wordlist[pos]

                # WIN
                if "_" not in Guessing:
                    in_game = False
                    Wrongletters = []
                # LOSS
                if lives_remaining <= 0:
                    in_game = False
                    Wrongletters = []

            # MOUSE
            if event.type == pygame.MOUSEBUTTONDOWN:

                handle_sound_click(event, sound_rect, is_muted)
                handle_sfx_click(event, sfx_rect, sound_muted)

                if back_btn.collidepoint(event.pos):
                    in_game = False

    return is_muted