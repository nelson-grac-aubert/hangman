import pygame 

pygame.init()
(width, height) = (1000, 600)
clock = pygame.time.Clock()
screen = pygame.display.set_mode((width, height))

blackboard = pygame.image.load("blackboard.png")
blackboard = pygame.transform.scale(blackboard, (1000, 600))

pygame.display.flip()
pygame.display.set_caption('Pendu')

running = True
main_menu = True 

while running:
    screen.fill("white")
    screen.blit(blackboard,(0,0))
    clock.tick(30)
    pygame.display.flip()
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
