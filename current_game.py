import pygame
from sound_control import * 

def draw_back_button(screen, button_font):
    """Draws the back-to-menu button and returns its rect."""
    back_btn = pygame.Rect(600, 537, 300, 50)
    txt = button_font.render("Back to main menu", True, (0, 0, 0))
    screen.blit(txt, (back_btn.x + 100, back_btn.y + 5))
    return back_btn


def new_game_menu(screen, width, blackboard, button_font,
                  mute_icon, unmute_icon, sound_rect, is_muted):
    """Main loop for the New Game screen."""

    running = True
    while running:
        screen.blit(blackboard, (0, 0))

        # Draw sound button (bottom-left)
        screen.blit(unmute_icon if is_muted else mute_icon, sound_rect)

        # Back button
        back_btn = draw_back_button(screen, button_font)

        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

            if event.type == pygame.MOUSEBUTTONDOWN:

                # Sound button
                if sound_rect.collidepoint(event.pos):
                    is_muted = not is_muted
                    if is_muted:
                        pygame.mixer.music.pause()
                    else:
                        pygame.mixer.music.unpause()

                # Back button
                if back_btn.collidepoint(event.pos):
                    running = False

    return is_muted