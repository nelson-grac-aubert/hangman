import pygame
from path_helper import resource_path

pygame.mixer.init()

# LOAD SOUND ICONS
def load_sound_icons():
    mute_icon = pygame.image.load(resource_path("assets/images/music.png"))
    unmute_icon = pygame.image.load(resource_path("assets/images/music_off.png"))
    mute_icon = pygame.transform.scale(mute_icon, (40, 40))
    unmute_icon = pygame.transform.scale(unmute_icon, (40, 40))

    rect = mute_icon.get_rect(topleft=(20, 545)) 

    return mute_icon, unmute_icon, rect

def load_sfx_icons():
    sound_mute_icon = pygame.image.load(resource_path("assets/images/sound_off.png"))
    sound_unmute_icon = pygame.image.load(resource_path("assets/images/sound_on.png"))
    sound_mute_icon = pygame.transform.scale(sound_mute_icon, (40, 40))
    sound_unmute_icon = pygame.transform.scale(sound_unmute_icon, (40, 40))

    rect = sound_mute_icon.get_rect(topleft=(70, 545))

    return sound_mute_icon, sound_unmute_icon, rect


#  DRAW SOUND ICONS
def draw_sound_button(screen, is_muted, mute_icon, unmute_icon, rect):
    screen.blit(unmute_icon if is_muted else mute_icon, rect)

def draw_sfx_button(screen, sound_muted, sound_mute_icon, sound_unmute_icon, rect):
    screen.blit(sound_unmute_icon if sound_muted else sound_mute_icon, rect)

#  HANDLE ICON CLICKS
def handle_sound_click(event, rect, is_muted):
    if rect.collidepoint(event.pos):
        is_muted = not is_muted
        if is_muted:
            pygame.mixer.music.pause()
        else:
            pygame.mixer.music.unpause()
    return is_muted

def handle_sfx_click(event, rect, sound_muted):
    if rect.collidepoint(event.pos):
        sound_muted = not sound_muted
    return sound_muted

#  MOUSE CLICK SOUND
mouse_click_sound = pygame.mixer.Sound(resource_path("assets/music/key_chalk.wav"))
mouse_click_sound.set_volume(1.0)

def play_mouse_click(sound_muted):
    if not sound_muted:
        mouse_click_sound.play()
