import pygame 

(width, height) = (1000, 600)
clock = pygame.time.Clock()
screen = pygame.display.set_mode((width, height))

pygame.display.flip()
pygame.display.set_caption('Pendu')

running = True
main_menu = True 

while running:
    clock.tick(30)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # while main_menu == True : 
