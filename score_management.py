# scores_management.py
import pygame
from txt_file_management import get_difficulty

def ask_player_name(screen, blackboard, button_font):
    name = ""
    entering = True

    input_rect = pygame.Rect(250, 300, 300, 60)

    while entering:
        screen.blit(blackboard, (0, 0))

        label = button_font.render("Enter your name:", True, (255, 255, 255))
        screen.blit(label, (250, 240))

        pygame.draw.rect(screen, (255, 255, 255), input_rect, 2)

        name_surf = button_font.render(name, True, (255, 255, 255))
        screen.blit(name_surf, (input_rect.x + 10, input_rect.y + 10))

        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    return name.strip()

                elif event.key == pygame.K_BACKSPACE:
                    name = name[:-1]

                else:
                    if len(name) < 15:
                        name += event.unicode

    return name

def calculate_score(word, lives_left):
    score = lives_left * 100 + len(word) * 30
    if get_difficulty() == "Impossible" : 
        score += 500
    return score

def save_score(player_name, word, lives_left, filename="scores.txt"):
    """Append a formatted score line to the score file."""
    
    score = calculate_score(word, lives_left)

    line = f"{player_name} : {score}"
    with open(filename, "a", encoding="utf-8") as f:
        f.write(line)

def load_scores(filename="scores.txt", limit=10):
    scores = []
    try:
        with open(filename, "r", encoding="utf-8") as f:
            for i, line in enumerate(f):
                if i >= limit:
                    break
                scores.append(line.strip())
    except FileNotFoundError:
        pass

    return scores