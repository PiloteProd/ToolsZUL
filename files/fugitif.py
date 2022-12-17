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
OBSTACLE_SPEED = 3

# Espacement entre les obstacles
OBSTACLE_SPACING = 500

# Initialisation de Pygame
pygame.init()

# Création de la fenêtre de jeu
screen = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])
pygame.display.set_caption('Fugitif par Pilote | V1.141')

# Création du personnage
character = pygame.Rect(SCREEN_WIDTH /2 - CHARACTER_WIDTH / 2, SCREEN_HEIGHT - CHARACTER_HEIGHT, CHARACTER_WIDTH, CHARACTER_HEIGHT)

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

    # Ajout d'un nouvel obstacle toutes les OBSTACLE_SPACING pixels de déplacement du personnage
    obstacle_y += OBSTACLE_SPEED
    if obstacle_y > OBSTACLE_SPACING:
        # Sélection aléatoire d'un nombre entier entre 0 et SCREEN_WIDTH - OBSTACLE_WIDTH
        obstacle_x = random.randint(0, SCREEN_WIDTH - OBSTACLE_WIDTH)
        # Création de l'obstacle
        obstacle = pygame.Rect(obstacle_x, 0, OBSTACLE_WIDTH, OBSTACLE_HEIGHT)
        obstacles.append(obstacle)
        # Réinitialisation de la position de départ de l'obstacle
        obstacle_y = 0

    # Déplacement des obstacles
    for obstacle in obstacles:
        # Mise à jour de la position de l'obstacle
        obstacle.y += OBSTACLE_SPEED

    # Mise à jour du score
    score += OBSTACLE_SPEED

    # Vérifie si le personnage entre en collision avec un obstacle
    for obstacle in obstacles:
        if character.colliderect(obstacle):
            # Si c'est le cas, affichage du menu de fin de partie
            game_over = True
            if score > best_score:
                best_score = score
            break

    # Effacement de l'écran
    screen.fill(BLACK)

    # Dessin du personn# Affichage du score
    font = pygame.font.Font(None, 36)
    score_text = font.render(f"Score: {score}", 1, WHITE)
    screen.blit(score_text, (10, 10))

    # Affichage du meilleur score
    best_score_text = font.render(f"Meilleur score: {best_score}", 1, WHITE)
    screen.blit(best_score_text, (10, 45))

    # Dessin du personnage
    pygame.draw.rect(screen, WHITE, character)

    # Dessin des obstacles
    for obstacle in obstacles:
        pygame.draw.rect(screen, GREEN, obstacle)

    # Si le menu de fin de partie est affiché, on l'affiche
    if game_over:
        game_over_menu(score)

    # Mise à jour de l'affichage
    pygame.display.flip()



