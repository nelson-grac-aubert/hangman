import pygame 

pygame.init()
(width, height) = (1000, 600)
clock = pygame.time.Clock()
screen = pygame.display.set_mode((width, height))

blackboard = pygame.image.load("assets/blackboard.png")
blackboard = pygame.transform.scale(blackboard, (1000, 600))

chalk_font = pygame.font.Font('assets/fonts/FrederickatheGreat-Regular.ttf', 45)

title_surface = chalk_font.render('Hangman X _ X', False, (255, 255, 255))

pygame.display.flip()
pygame.display.set_caption('Pendu')

running = True
main_menu = True 

while running:
    screen.fill("white")
    screen.blit(blackboard,(0,0))
    screen.blit(title_surface, (305,120))
    clock.tick(30)
    pygame.display.flip()
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
