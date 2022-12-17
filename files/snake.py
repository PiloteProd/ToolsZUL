import pygame
import random

# Initialiser pygame
pygame.init()

# Définir la largeur et la hauteur de l'écran
largeur_ecran = 700
hauteur_ecran = 500
ecran = pygame.display.set_mode((largeur_ecran, hauteur_ecran))

# Définir le titre de la fenêtre
pygame.display.set_caption('Snake')

# Définir les couleurs
noir = pygame.Color(0, 0, 0)
blanc = pygame.Color(255, 255, 255)
rouge = pygame.Color(255, 0, 0)
vert = pygame.Color(0, 255, 0)

# Définir les dimensions du serpent
taille_bloc_serpent = 10
vitesse_serpent = 15

# Définir le style de police
police_style = pygame.font.SysFont("bahnschrift", 25)
police_score = pygame.font.SysFont("comicsansms", 35)

# Créer le score
def votre_score(score):
    valeur = police_score.render("Votre score: " + str(score), True, blanc)
    ecran.blit(valeur, [0, 0])

# Créer le serpent
def notre_serpent(taille_bloc_serpent, liste_serpent):
    for x in liste_serpent:
        pygame.draw.rect(ecran, vert, [x[0], x[1], taille_bloc_serpent, taille_bloc_serpent])

# Créer le message
def message(msg, couleur, police, taille, decalage_x=0, decalage_y=0):
    mesg = police.render(msg, True, couleur)
    ecran.blit(mesg, [largeur_ecran / 6 + decalage_x, hauteur_ecran / 3 + decalage_y])

# Boucle de jeu
def boucle_jeu():
    # Mettre fin_jeu à False
    fin_jeu = False
    fin_partie = False

    # Définir la position de départ du serpent
    x1 = largeur_ecran / 2
    y1 = hauteur_ecran / 2

    # Définir les variables de déplacement
    x1_change = 0
    y1_change = 0

    # Définir la liste du serpent
    liste_serpent = []
    longueur_serpent = 1

    # Définir la position de départ de la nourriture
    nourriture_x = round(random.randrange(0, largeur_ecran - taille_bloc_serpent) / 10.0) * 10.0
    nourriture_y = round(random.randrange(0, hauteur_ecran - taille_bloc_serpent) / 10.0) * 10.0
    # Définir l'horloge
    horloge = pygame.time.Clock()

    # Boucle de jeu
    while not fin_jeu:
        while fin_partie:
            ecran.fill(noir)
            message("Vous avez perdu! Appuyez sur C pour recommencer ou sur Q pour quitter", rouge, police_style, taille="small")
            votre_score(longueur_serpent - 1)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        fin_jeu = True
                        fin_partie = False
                    if event.key == pygame.K_c:
                        boucle_jeu()

        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_change = -taille_bloc_serpent
                    y1_change = 0
                elif event.key == pygame.K_RIGHT:
                    x1_change = taille_bloc_serpent
                    y1_change = 0
                elif event.key == pygame.K_UP:
                    y1_change = -taille_bloc_serpent
                    x1_change = 0
                elif event.key == pygame.K_DOWN:
                    y1_change = taille_bloc_serpent
                    x1_change = 0

        # Mettre à jour la position du serpent
        x1 += x1_change
        y1 += y1_change

        # Définir la surface de jeu
        ecran.fill(noir)

        # Dessiner la nourriture
        pygame.draw.rect(ecran, rouge, [nourriture_x, nourriture_y, taille_bloc_serpent, taille_bloc_serpent])

        # Créer la tête du serpent
        tete_serpent = []
        tete_serpent.append(x1)
        tete_serpent.append(y1)
        liste_serpent.append(tete_serpent)

        # Limiter la taille du serpent
        if len(liste_serpent) > longueur_serpent:
            del liste_serpent[0]

        # Dessiner le serpent
        notre_serpent(taille_bloc_serpent, liste_serpent)
        votre_score(longueur_serpent - 1)

        # Vérifier si le serpent est sorti de l'écran
        if x1 < 0 or x1 >= largeur_ecran or y1 < 0 or y1 >= hauteur_ecran:
            fin_partie = True

        # Vérifier si le serpent s'est mordu lui-même
        for x in liste_serpent[:-1]:
            if x == tete_serpent:
                fin_partie = True
        # Vérifier si le serpent a mangé de la nourriture
        if x1 == nourriture_x and y1 == nourriture_y:
            nourriture_x = round(random.randrange(0, largeur_ecran - taille_bloc_serpent) / 10.0) * 10.0
            nourriture_y = round(random.randrange(0, hauteur_ecran - taille_bloc_serpent) / 10.0) * 10.0
            longueur_serpent += 1

        # Mettre à jour l'écran
        pygame.display.update()

        # Définir la vitesse du serpent
        horloge.tick(vitesse_serpent)

    # Quitter pygame
    pygame.quit()
    quit()

# Exécuter la boucle de jeu
boucle_jeu()
