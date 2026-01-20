import pygame

def load_sound_icons():
    mute_icon = pygame.image.load("assets/images/music.png")
    unmute_icon = pygame.image.load("assets/images/music_off.png")

    mute_icon = pygame.transform.scale(mute_icon, (40, 40))
    unmute_icon = pygame.transform.scale(unmute_icon, (40, 40))

    rect = mute_icon.get_rect(topleft=(20, 545))  # bas-gauche

    return mute_icon, unmute_icon, rect


def draw_sound_button(screen, is_muted, mute_icon, unmute_icon, rect):
    """Draws the mute/unmute icon."""
    screen.blit(unmute_icon if is_muted else mute_icon, rect)


def handle_sound_click(event, rect, is_muted):
    """Handles click on the sound icon and returns updated mute state."""
    if rect.collidepoint(event.pos):
        is_muted = not is_muted
        if is_muted:
            pygame.mixer.music.pause()
        else:
            pygame.mixer.music.unpause()
    return is_muted