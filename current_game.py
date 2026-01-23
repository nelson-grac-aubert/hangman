import pygame
from path_helper import resource_path
from sound_control import * 
from game_logic import * 
from game_logic import (choose_mystery_word,format_mystery_word,Checkinput,
    Gameturn_pygame,Upperletter,Lowerletter,Specials)
from score_management import ask_player_name, save_score, calculate_score

game_font = pygame.font.Font(resource_path('assets/fonts/FrederickatheGreat-Regular.ttf'), 45)

mute_icon, unmute_icon, sound_rect = load_sound_icons()
sound_mute_icon, sound_unmute_icon, sfx_rect = load_sfx_icons()

def load_hangman_images():
    images = {}
    for i in range(7):
        img = pygame.image.load(resource_path(f"assets/images/{i}_lives.png"))
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


def end_screen(screen, blackboard, button_font, win, word, lives):
    running = True

    play_btn = pygame.Rect(0, 0, 250, 60)
    menu_btn = pygame.Rect(0, 0, 250, 60)
    save_btn = pygame.Rect(0, 0, 250, 60)

    while running:
        screen.blit(blackboard, (0, 0))

        # Draw hangman
        draw_hangman(screen, lives, 125, 80)

        # WIN / GAME OVER message
        if win:
            msg = f"You win! The word was: {word}"
            score_msg = f"Your score is : {calculate_score(word, lives)}"
            save_btn.center = (screen.get_width() // 2, 400)
        else:
            msg = f"Game Over! The word was: {word}"
            score_msg = ""

        label = button_font.render(msg, True, (255,255,255))
        label_rect = label.get_rect(center=(screen.get_width() // 2, 305))
        screen.blit(label, label_rect)

        score_label = button_font.render(score_msg, True, (255,255,255))
        score_label_rect = score_label.get_rect(center=(screen.get_width() // 2, 353))
        screen.blit(score_label, score_label_rect)

        # Position buttons
        play_btn.center = (screen.get_width() // 2 - 200, 400)
        menu_btn.center = (screen.get_width() // 2 + 200, 400)

        # Draw buttons
        def draw_btn(rect, text):
            txt = button_font.render(text, True, (255,255,255))
            txt_rect = txt.get_rect(center=rect.center)
            screen.blit(txt, txt_rect)

        draw_btn(play_btn, "Play Again")
        draw_btn(save_btn, "Save Score")
        draw_btn(menu_btn, "Main Menu")

        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if play_btn.collidepoint(event.pos):
                    return "play"

                if menu_btn.collidepoint(event.pos):
                    return "menu"

                if win and save_btn.collidepoint(event.pos):
                    # Ask for name
                    player_name = ask_player_name(screen, blackboard, button_font)

                    # Save score
                    if player_name.strip():
                        save_score(player_name, word, lives)
                    return "menu"

                    # Return to victory screen (do NOT exit)
                    # Simply continue the loop


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
        screen.blit(wrong_label, (410, 95))
        draw_wrong_letters(screen, button_font, Wrongletters, 415, 130)

        # CURRENT WORD
        word_str = " ".join(Guessing)
        txt = game_font.render(word_str, True, (255, 255, 255))
        txt_rect = txt.get_rect(center=(screen.get_width() // 2, 350))
        screen.blit(txt, txt_rect)

        pygame.display.flip()

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

            # KEYBOARD
            if event.type == pygame.KEYDOWN:
                result = Gameturn_pygame(event, Wordlist, Upperletter, Lowerletter, Foundletters, Wrongletters)
                play_mouse_click(sound_muted)

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
                    choice = end_screen(screen, blackboard, button_font, True, Word, lives_remaining)
                    if choice == "play":
                        return "restart"
                    else:
                        return "menu"


                # LOSS
                if lives_remaining <= 0:
                    choice = end_screen(screen, blackboard, button_font, False, Word, lives_remaining)
                    if choice == "play":
                        return "restart"
                    else:
                        return "menu"


            # MOUSE
            if event.type == pygame.MOUSEBUTTONDOWN:

                handle_sound_click(event, sound_rect, is_muted)
                handle_sfx_click(event, sfx_rect, sound_muted)

                if back_btn.collidepoint(event.pos):
                    in_game = False

    return is_muted