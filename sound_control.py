import pygame

def load_sound_icons():
    mute_icon = pygame.image.load("assets/images/music.png")
    unmute_icon = pygame.image.load("assets/images/music_off.png")
    mute_icon = pygame.transform.scale(mute_icon, (40, 40))
    unmute_icon = pygame.transform.scale(unmute_icon, (40, 40))

    rect = mute_icon.get_rect(topleft=(20, 545)) 

    return mute_icon, unmute_icon, rect

def load_sfx_icons() : 
    sound_mute_icon = pygame.image.load("assets/images/sound_off.png")
    sound_unmute_icon = pygame.image.load("assets/images/sound_on.png")
    sound_mute_icon = pygame.transform.scale(sound_mute_icon, (40, 40))
    sound_unmute_icon = pygame.transform.scale(sound_unmute_icon, (40, 40))

    rect = sound_mute_icon.get_rect(topleft=(70, 545))

    return sound_mute_icon, sound_unmute_icon, rect

def draw_sound_button(screen, is_muted, mute_icon, unmute_icon, rect):
    """Draws the mute/unmute icon."""
    screen.blit(unmute_icon if is_muted else mute_icon, rect)

def draw_sfx_button(screen, sound_muted, sound_mute_icon, sound_unmute_icon, rect):
    """Draws the mute/unmute icon."""
    screen.blit(sound_unmute_icon if sound_muted else sound_mute_icon, rect)


def handle_sound_click(event, rect, is_muted):
    """Handles click on the sound icon and returns updated mute state."""
    if rect.collidepoint(event.pos):
        is_muted = not is_muted
        if is_muted:
            pygame.mixer.music.pause()
        else:
            pygame.mixer.music.unpause()
    return is_muted

def handle_sfx_click(event, rect, sound_muted):
    """Handles click on the sound icon and returns updated mute state."""
    if rect.collidepoint(event.pos):
        sound_muted = not sound_muted
    return sound_muted