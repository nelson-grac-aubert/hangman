import pygame
from sound_control import * 

mute_icon, unmute_icon, sound_rect = load_sound_icons()
sound_mute_icon, sound_unmute_icon, sfx_rect = load_sfx_icons()

def draw_back_button(screen, button_font):
    """Draws the back-to-menu button and returns its rect."""
    back_btn = pygame.Rect(600, 537, 300, 50)
    txt = button_font.render("Back to main menu", True, (0, 0, 0))
    screen.blit(txt, (back_btn.x + 100, back_btn.y + 5))
    return back_btn


def new_game_menu(screen, blackboard, button_font,
                  mute_icon, unmute_icon, sound_rect, is_muted, sound_muted):
    """Main loop for the New Game screen."""

    in_game = True
    while in_game:
        screen.blit(blackboard, (0, 0))

        draw_sound_button(screen, is_muted, mute_icon, unmute_icon, sound_rect)
        draw_sfx_button(screen, sound_muted, sound_mute_icon, sound_unmute_icon, sfx_rect)

        # Back button
        back_btn = draw_back_button(screen, button_font)

        pygame.display.flip()

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                
                handle_sound_click(event, sound_rect, is_muted)
                handle_sfx_click(event, sfx_rect, sound_muted)

                # Back button
                if back_btn.collidepoint(event.pos):
                    in_game = False

    return is_muted