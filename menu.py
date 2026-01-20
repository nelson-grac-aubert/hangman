import pygame 
pygame.init()
pygame.mixer.init()
pygame.display.init()

from word_list_editor import *
from score_board import *
from sound_control import *
from current_game import *

pygame.mixer.music.load("assets/music/background_music.mp3")
pygame.mixer.music.play(-1)

(width, height) = (1000, 600)
clock = pygame.time.Clock()
screen = pygame.display.set_mode((width, height))

# SOUND ICONS
mute_icon, unmute_icon, sound_rect = load_sound_icons()
sound_mute_icon, sound_unmute_icon, sfx_rect = load_sfx_icons()

# BACKGROUND 

blackboard = pygame.image.load("assets/images/blackboard.png")
blackboard = pygame.transform.scale(blackboard, (1000, 600))

# TITLE
title_font = pygame.font.Font('assets/fonts/FrederickatheGreat-Regular.ttf', 60)
title_surface = title_font.render('Hangman', False, (255, 255, 255))
title_rect = title_surface.get_rect(center=(width // 2, 120))

# BUTTONS
button_font = pygame.font.Font('assets/fonts/FrederickatheGreat-Regular.ttf', 30)
# buttons size
btn_w, btn_h = 220, 55
btn_x = width // 2 - btn_w // 2
# buttons position
start_y = 200
spacing = 65
btn1_rect = pygame.Rect(btn_x, start_y + spacing * 0, btn_w, btn_h)  # New Game
btn2_rect = pygame.Rect(btn_x, start_y + spacing * 1, btn_w, btn_h)  # Edit Word List
btn3_rect = pygame.Rect(btn_x, start_y + spacing * 2, btn_w, btn_h)  # Score
btn4_rect = pygame.Rect(btn_x, start_y + spacing * 3, btn_w, btn_h)  # Difficulty

# difficulty arrows
difficulty_levels = ["Easy", "Medium", "Hard", "Impossible"]
difficulty_index = 1  # Starts at medium
arrow_size = 35
left_arrow_rect  = pygame.Rect(btn4_rect.x - arrow_size - 70, btn4_rect.y + 10, arrow_size, arrow_size)
right_arrow_rect = pygame.Rect(btn4_rect.right + 70, btn4_rect.y + 10, arrow_size, arrow_size)

def draw_button(surface, rect, text, font):
    """ Draws a main menu button """
    txt = font.render(text, True, (255, 255, 255))
    txt_rect = txt.get_rect(center=rect.center)
    surface.blit(txt, txt_rect)

def draw_arrow(surface, rect, direction):
    """ Draws the arrow for the difficulty selection """
    
    if direction == "left":
        points = [
            (rect.centerx + 6, rect.centery - 10),
            (rect.centerx - 6, rect.centery),
            (rect.centerx + 6, rect.centery + 10)
        ]
    else:  # right
        points = [
            (rect.centerx - 6, rect.centery - 10),
            (rect.centerx + 6, rect.centery),
            (rect.centerx - 6, rect.centery + 10)
        ]

    pygame.draw.polygon(surface, (255, 255, 255), points)

pygame.display.flip()
pygame.display.set_caption('Hangman')

running = True
is_muted = False
sound_muted = False
main_menu = True 

while running:
    screen.fill("white")
    screen.blit(blackboard,(0,0))

    screen.blit(title_surface, title_rect)

    draw_sound_button(screen, is_muted, mute_icon, unmute_icon, sound_rect)
    draw_sfx_button(screen, sound_muted, sound_mute_icon, sound_unmute_icon, sfx_rect)
    
    clock.tick(30)

    draw_button(screen, btn1_rect, "New Game", button_font)
    draw_button(screen, btn2_rect, "Edit Word List", button_font)
    draw_button(screen, btn3_rect, "Score", button_font)
    draw_button(screen, btn4_rect, f"Difficulty: {difficulty_levels[difficulty_index]}", button_font)

    draw_arrow(screen, left_arrow_rect, "left")
    draw_arrow(screen, right_arrow_rect, "right")

    pygame.display.flip()

    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            if left_arrow_rect.collidepoint(event.pos):
                difficulty_index = (difficulty_index - 1) % len(difficulty_levels)
            elif right_arrow_rect.collidepoint(event.pos):
                difficulty_index = (difficulty_index + 1) % len(difficulty_levels)
            
            is_muted = handle_sound_click(event, sound_rect, is_muted)
            sound_muted = handle_sfx_click(event, sfx_rect, sound_muted)

            if btn1_rect.collidepoint(event.pos): 
                new_game_menu(screen, blackboard, button_font,
                mute_icon, unmute_icon, sound_rect, is_muted, sound_muted, 6)

            if btn2_rect.collidepoint(event.pos):
                word_list_menu(screen, width, blackboard, button_font,
                mute_icon, unmute_icon, sound_rect, is_muted, sound_muted)

            if btn3_rect.collidepoint(event.pos):  
                score_board_menu(screen, width, blackboard, button_font, is_muted, sound_muted)

        if event.type == pygame.QUIT:
            running = False
