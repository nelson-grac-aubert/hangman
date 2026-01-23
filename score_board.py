import pygame
from path_helper import resource_path
from sound_control import * 
from score_management import load_scores

# SOUND ICON
mute_icon, unmute_icon, sound_rect = load_sound_icons()
sound_mute_icon, sound_unmute_icon, sfx_rect = load_sfx_icons()

def draw_title(screen, width, text):
    """Draws a centered black title at the top."""
    title_font = pygame.font.Font(resource_path('assets/fonts/FrederickatheGreat-Regular.ttf'), 40)
    title_surface = title_font.render(text, True, (0, 0, 0))
    screen.blit(title_surface, (width//2 - title_surface.get_width()//2, 0))


def draw_back_button(screen, button_font):
    """Draws the back-to-menu button and returns its rect."""
    back_btn = pygame.Rect(600, 537, 300, 50)
    txt = button_font.render("Back to main menu", True, (0, 0, 0))
    screen.blit(txt, (back_btn.x + 100, back_btn.y + 5))
    return back_btn


def draw_scores(screen, scores):
    """Draws the list of scores (simple version, modifiable later)."""
    font = pygame.font.Font(resource_path('assets/fonts/FrederickatheGreat-Regular.ttf'), 33)

    start_y = 95
    spacing = 37

    top_scores = sorted(scores,
    key=lambda s: int(s.split(":")[1].strip()),reverse=True)[:10]

    for i, score in enumerate(top_scores):
        txt = font.render(f"{score}", True, (255, 255, 255))
        screen.blit(txt, (390, start_y + i * spacing))


def score_board_menu(screen, width, blackboard, button_font, is_muted, sound_muted):
    """Main loop for the score board screen."""

    score_screen = True

    while score_screen:
        screen.blit(blackboard, (0, 0))
        scores = load_scores() 

        draw_sound_button(screen, is_muted, mute_icon, unmute_icon, sound_rect)
        draw_sfx_button(screen, sound_muted, sound_mute_icon, sound_unmute_icon, sfx_rect)

        draw_title(screen, width, "Score Board")
        draw_scores(screen, scores)

        back_btn = draw_back_button(screen, button_font)

        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

            if event.type == pygame.MOUSEBUTTONDOWN:

                is_muted = handle_sound_click(event, sound_rect, is_muted)
                sound_muted = handle_sfx_click(event, sfx_rect, sound_muted)

                if back_btn.collidepoint(event.pos):
                    score_screen = False
