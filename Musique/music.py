import pygame

#Reduce latency
pygame.mixer.pre_init(44100, -16, 1, 64)
pygame.init()
pygame.mixer.init()

#Music
pygame.mixer.music.load("Musique/mfond.mp3")
pygame.mixer.music.play(-1)
pygame.mixer.music.set_volume(1.0)

#Sound chalk
key_sound = pygame.mixer.Sound("Musique/key_chalk.wav")
key_sound.set_volume(1.0)

#Window
screen = pygame.display.set_mode((1000, 600))
white = (255, 255, 255)

#Icon
mute_icon = pygame.image.load("Musique/music.png")
unmute_icon = pygame.image.load("Musique/music_off.png")

mute_icon = pygame.transform.scale(mute_icon, (40, 40))
unmute_icon = pygame.transform.scale(unmute_icon, (40, 40))

icon_rect = mute_icon.get_rect(topleft=(10, 10))

is_muted = False
running = True

#Loop
while running:
    screen.fill(white)

    #Show icons
    screen.blit(mute_icon if not is_muted else unmute_icon, icon_rect)

    pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        #Key sound
        if event.type == pygame.KEYDOWN:
            key_sound.play()
            print("Touche pressée :", pygame.key.name(event.key))

        #Mute/Unmute
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if icon_rect.collidepoint(event.pos):
                is_muted = not is_muted
                if is_muted:
                    pygame.mixer.music.pause()
                else:
                    pygame.mixer.music.unpause()

pygame.quit()
