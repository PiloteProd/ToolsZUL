import pygame
import random
import sys 

# Définition des couleurs
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)

# Taille de la fenêtre de jeu
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# Taille du personnage
CHARACTER_WIDTH = 50
CHARACTER_HEIGHT = 50

# Taille de l'obstacle
OBSTACLE_WIDTH = 50
OBSTACLE_HEIGHT = 50

# Vitesse de déplacement du personnage et de l'obstacle
CHARACTER_SPEED = 5
OBSTACLE_SPEED = 5

# Espacement entre les obstacles
OBSTACLE_SPACING = 200

# Initialisation de Pygame
pygame.init()

# Création de la fenêtre de jeu
screen = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])
pygame.display.set_caption('Fugitif par Pilote | V1.141')

# Création du personnage
character = pygame.Rect(SCREEN_WIDTH / 2 - CHARACTER_WIDTH / 2, SCREEN_HEIGHT - CHARACTER_HEIGHT, CHARACTER_WIDTH, CHARACTER_HEIGHT)

# Création de la liste d'obstacles
obstacles = []

# Position de départ de l'obstacle
obstacle_y = 0

# Initialisation du score
score = 0

# Initialisation du meilleur score
best_score = 0

# Flag pour savoir si le menu de fin de partie est affiché
game_over = False

def game_over_menu(score):
    """Affiche le menu de fin de partie avec le score final"""
    # Dessin du texte "Vous êtes mort"
    font = pygame.font.Font(None, 48)
    game_over_text = font.render("Vous êtes mort !", 1, WHITE)
    screen.blit(game_over_text, (300, 250))

    # Dessin du bouton "Réessayer"
    pygame.draw.rect(screen, WHITE, (300, 300, 275, 50))
    font = pygame.font.Font(None, 36)
    retry_text = font.render("Réessayer", 1, BLACK)
    screen.blit(retry_text, (315, 315))

    # Dessin du score final
    score_text = font.render(f"Score final: {score}", 1, WHITE)
    screen.blit(score_text, (300, 365))

# Démarrage de la boucle de jeu
while True:
    # Gestion des événements de jeu
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONUP:
            # Vérifie si le curseur de la souris est positionné sur le bouton "Réessayer"
            mouse_x, mouse_y = pygame.mouse.get_pos()
            if game_over and mouse_x > 300 and mouse_x < 500 and mouse_y > 300 and mouse_y < 350:
                # Réinitialise le score et les obstacles
                score = 0
                obstacles = []
                obstacle_y = 0
                game_over = False

    # Si le menu de fin de partie est affiché, on ne fait rien de plus
    if game_over:
        continue

    # Récupération des touches pressées
    keys = pygame.key.get_pressed()

    # Déplacement du personnage
    if keys[pygame.K_LEFT]:
        character.x = max(0, character.x - CHARACTER_SPEED)
    elif keys[pygame.K_RIGHT]:
        character.x = min(SCREEN_WIDTH - CHARACTER_WIDTH, character.x + CHARACTER_SPEED)
        # Déplacement des obstacles
        for obstacle in obstacles:
            obstacle.y += OBSTACLE_SPEED

        # Suppression des obstacles sortis de l'écran
        obstacles = [o for o in obstacles if o.y < SCREEN_HEIGHT]

        # Ajout d'un nouvel obstacle si nécessaire
        if len(obstacles) == 0 or obstacles[-1].y > OBSTACLE_SPACING:
            obstacle_y -= OBSTACLE_SPACING
            obstacles.append(pygame.Rect(random.randint(0, SCREEN_WIDTH - OBSTACLE_WIDTH), obstacle_y, OBSTACLE_WIDTH, OBSTACLE_HEIGHT))

        # Détection des collisions avec les obstacles
        if any(obstacle.colliderect(character) for obstacle in obstacles):
            game_over = True

        # Incrémentation du score
        score += 1

    # Effacement de l'écran
    screen.fill(BLACK)

    # Dessin des éléments de jeu
    pygame.draw.rect(screen, WHITE, character)
    for obstacle in obstacles:
        pygame.draw.rect(screen, GREEN, obstacle)

    # Affichage du score
    font = pygame.font.Font(None, 36)
    text = font.render(str(f"Score actuel: {score}"), 1, WHITE)
    screen.blit(text, (10, 10))


    # Dessin du meilleur score
    font = pygame.font.Font(None, 36)
    best_score_text = font.render(f"Meilleur score: {best_score}", 1, WHITE)
    screen.blit(best_score_text, (10, 50))
    # Si le menu de fin de partie est affiché, on dessine le menu
    if game_over:
        game_over_menu(score)

    # Mise à jour de l'affichage
    pygame.display.update()
