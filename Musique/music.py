import pygame

pygame.init()
pygame.mixer.init()

# Musique
pygame.mixer.music.load("Musique/mfond.mp3")
pygame.mixer.music.play(-1)

# Fenêtre
screen = pygame.display.set_mode((1000, 600))
white = (255, 255, 255)

# Icônes
mute_icon = pygame.image.load("Musique/music.png")
unmute_icon = pygame.image.load("Musique/music_off.png")

# Redimensionner si besoin
mute_icon = pygame.transform.scale(mute_icon, (40, 40))
unmute_icon = pygame.transform.scale(unmute_icon, (40, 40))

icon_rect = mute_icon.get_rect(topleft=(10, 10))

is_muted = False
running = True

while running:
    screen.fill(white)

    # Affichage de l'icône
    screen.blit(mute_icon if not is_muted else unmute_icon, icon_rect)

    pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.MOUSEBUTTONDOWN:
            if icon_rect.collidepoint(event.pos):
                is_muted = not is_muted
                if is_muted:
                    pygame.mixer.music.pause()
                else:
                    pygame.mixer.music.unpause()

pygame.quit()
