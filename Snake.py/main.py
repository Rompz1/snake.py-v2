import pygame
import time
import random

# Initialisation des dimensions de la fenêtre
window_x = 720
window_y = 480

# Initialisation de Pygame
pygame.init()

# Couleurs
green = pygame.Color(0, 255, 0)
black = pygame.Color(0, 0, 0)
red = pygame.Color(255, 0, 0)

# Fonction pour afficher "Game Over"
def game_over(game_window):
    font = pygame.font.SysFont('arial', 50)
    game_over_surface = font.render('Game Over', True, red)
    game_window.blit(game_over_surface, (window_x // 4, window_y // 3))
    pygame.display.flip()
    time.sleep(2)
    pygame.quit()
    quit()

# Boucle principale du jeu
def game_loop():
    # Initialisation de la fenêtre et des variables
    game_window = pygame.display.set_mode((window_x, window_y))
    pygame.display.set_caption('Snake')
    fps = pygame.time.Clock()

    direction_x, direction_y = 10, 0
    snake_body = [[100, 50], [90, 50], [80, 50], [70, 50]]
    pomme = [random.randrange(1, (window_x // 10)) * 10,
             random.randrange(1, (window_y // 10)) * 10]
    running = True
    speed = 10

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP and direction_y == 0:
                    direction_x = 0
                    direction_y = -10
                if event.key == pygame.K_DOWN and direction_y == 0:
                    direction_x = 0
                    direction_y = 10
                if event.key == pygame.K_LEFT and direction_x == 0:
                    direction_x = -10
                    direction_y = 0
                if event.key == pygame.K_RIGHT and direction_x == 0:
                    direction_x = 10
                    direction_y = 0

        # Mise à jour de la position du serpent
        head = [snake_body[0][0] + direction_x, snake_body[0][1] + direction_y]
        snake_body.insert(0, head)

        # Vérification de la collision avec la pomme
        if head == pomme:
            pomme = [random.randrange(1, (window_x // 10)) * 10,
                     random.randrange(1, (window_y // 10)) * 10]
            speed += 1
        else:
            snake_body.pop()

        # Vérification des collisions avec les murs ou le corps
        if (head[0] < 0 or head[0] >= window_x or
                head[1] < 0 or head[1] >= window_y or
                head in snake_body[1:]):
            game_over(game_window)

        # Affichage du jeu
        game_window.fill(green)
        for pos in snake_body:
            pygame.draw.rect(game_window, black, pygame.Rect(pos[0], pos[1], 10, 10))
        pygame.draw.rect(game_window, red, pygame.Rect(pomme[0], pomme[1], 10, 10))

        pygame.display.update()
        fps.tick(speed)

    pygame.quit()

# Lancer le jeu
game_loop()
