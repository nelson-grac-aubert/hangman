import pygame
from txt_file_management import *
from sound_control import * 
from path_helper import resource_path

# SOUND ICON
mute_icon, unmute_icon, sound_rect = load_sound_icons()
sound_mute_icon, sound_unmute_icon, sfx_rect = load_sfx_icons()

def draw_error_message(screen, width, error_message, error_start_time):
    """Draws a fading error message and returns updated error_message."""
    if not error_message:
        return error_message

    elapsed = pygame.time.get_ticks() - error_start_time

    if elapsed < 3000:
        alpha = max(0, 255 - int((elapsed / 3000) * 255))

        err_font = pygame.font.Font(resource_path('assets/fonts/FrederickatheGreat-Regular.ttf'), 45)
        err_text = err_font.render(error_message, True, (255, 0, 0))
        err_text.set_alpha(alpha)

        screen.blit(
            err_text,
            (width//2 - err_text.get_width()//2, 330)
        )
    else:
        error_message = ""

    return error_message


def draw_word_list(screen, words, selected_index, words_font,
                   start_x, start_y, col_width, line_spacing,
                   visible_per_column, scroll_offset):

    max_visible = visible_per_column * 2

    visible_words = words[scroll_offset : scroll_offset + max_visible]

    for i, w in enumerate(visible_words):
        col = i // visible_per_column
        row = i % visible_per_column

        x = start_x + col * col_width
        y = start_y + row * line_spacing

        real_index = scroll_offset + i
        color = (144, 213, 255) if real_index == selected_index else (255, 255, 255)

        txt = words_font.render(w, True, color)
        screen.blit(txt, (x, y))

def word_list_menu(screen, width, blackboard, button_font,
                   mute_icon, unmute_icon, sound_rect, is_muted, sound_muted):

    """ Handles the menu to edit the hangman list of words """
    words = load_words()
    input_text = ""
    selected_index = None

    error_message = ""
    error_start_time = 0

    scroll_offset = 0
    visible_per_column = 10
    visible_total = visible_per_column * 2

    words_screen = True
    while words_screen:
        screen.blit(blackboard, (0, 0))

        draw_sound_button(screen, is_muted, mute_icon, unmute_icon, sound_rect)
        draw_sfx_button(screen, sound_muted, sound_mute_icon, sound_unmute_icon, sfx_rect)

        # Title
        title_font = pygame.font.Font(resource_path('assets/fonts/FrederickatheGreat-Regular.ttf'), 40)
        title = title_font.render("Word List", True, (0,0,0))
        screen.blit(title, (width//2 - title.get_width()//2, 0))

        # Display words
        words_font = pygame.font.Font(resource_path('assets/fonts/FrederickatheGreat-Regular.ttf'), 25)

        max_per_column = 10
        col_width = 250   
        start_x = 130
        start_y = 80
        line_spacing = 28

        draw_word_list(screen, words, selected_index, words_font,
        start_x, start_y, col_width, line_spacing,visible_per_column, scroll_offset)

        # Input box
        pygame.draw.rect(screen, (255,255,255), (550, 390, 300, 40), 2)
        txt = button_font.render(input_text, True, (255,255,255))
        screen.blit(txt, (560, 395))

        # Buttons
        add_btn = pygame.Rect(510, 440, 140, 40)
        del_btn = pygame.Rect(735, 440, 140, 40)
        back_btn = pygame.Rect(600, 537, 300, 50)

        screen.blit(button_font.render("Add", True, (255,255,255)), (add_btn.x+40, add_btn.y+5))
        screen.blit(button_font.render("Delete", True, (255,255,255)), (del_btn.x+25, del_btn.y+5))
        screen.blit(button_font.render("Back to main menu", True, (0,0,0)), (back_btn.x+100, back_btn.y+5))

        # Fading out error message
        error_message = draw_error_message(screen, width, error_message, error_start_time)

        pygame.display.flip()

        # Events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_BACKSPACE:
                    input_text = input_text[:-1]
                elif event.key == pygame.K_RETURN:
                    pass
                else:
                    if len(input_text) < 20:
                        input_text += event.unicode

            if event.type == pygame.MOUSEWHEEL:
                scroll_offset -= event.y  

                scroll_offset = max(0, min(scroll_offset, max(0, len(words) - visible_total)))

            if event.type == pygame.MOUSEBUTTONDOWN:
                
                is_muted = handle_sound_click(event, sound_rect, is_muted)
                sound_muted = handle_sfx_click(event, sfx_rect, sound_muted)

                if add_btn.collidepoint(event.pos):
                    new_word = input_text.strip()

                    if not new_word:
                        continue

                    if not is_valid_word(new_word):
                        error_message = "Unauthorized character"
                        error_start_time = pygame.time.get_ticks()
                        input_text = ""
                        continue

                    words.append(new_word)
                    save_words(words)
                    input_text = ""

                if del_btn.collidepoint(event.pos):
                    if selected_index is not None:
                        words.pop(selected_index)
                        save_words(words)
                        selected_index = None

                if back_btn.collidepoint(event.pos):
                    words_screen = False

                # Select word
                for i in range(visible_total):
                    real_index = scroll_offset + i
                    if real_index >= len(words):
                        break

                    col = i // visible_per_column
                    row = i % visible_per_column

                    x = start_x + col * col_width
                    y = start_y + row * line_spacing

                    rect = pygame.Rect(x, y, 300, line_spacing)
                    if rect.collidepoint(event.pos):
                        selected_index = real_index
