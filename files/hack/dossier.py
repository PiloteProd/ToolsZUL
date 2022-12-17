import tkinter as tk
import tkinter.simpledialog
import os
import random

# Créer la fenêtre principale
fenetre = tk.Tk()
fenetre.title("Répertoire de fichiers")

# Créer la variable de répertoire
repertoire = tk.StringVar()

# Créer la fonction de mise à jour du répertoire
def mettre_a_jour_repertoire():
    repertoire.set(entree_repertoire.get())

# Créer la fonction de création de dossiers
def creer_dossiers():
    # Récupérer le répertoire actuel
    repertoire_actuel = repertoire.get()

    # Demander à l'utilisateur de saisir un nombre de dossiers à créer en utilisant une boîte de dialogue tkinter
    nombre_dossiers = tk.simpledialog.askinteger("Nombre de dossiers", "Combien de dossiers souhaitez-vous créer?", parent=fenetre, minvalue=1)

    # Vérifier si l'utilisateur a saisi un nombre valide
    if nombre_dossiers is not None:
        # Créer les dossiers
        for i in range(nombre_dossiers):
            # Créer un dossier de test avec un nom aléatoire
            nom_dossier = "TEST " + str(random.randint(0, 10000000000))
            os.mkdir(os.path.join(repertoire_actuel, nom_dossier))
    else:
        # Afficher un message d'erreur
        tk.messagebox.showerror("Erreur", "Vous n'avez pas saisi de nombre valide.")

# Créer l'entrée de texte pour le répertoire
entree_repertoire = tk.Entry(fenetre, textvariable=repertoire)
entree_repertoire.pack(pady=10)

# Créer le bouton "Set"
bouton_set = tk.Button(fenetre, text="Set", command=mettre_a_jour_repertoire)
bouton_set.pack(pady=10)

# Créer le bouton de création de dossiers
bouton_dossiers = tk.Button(fenetre, text="Créer des dossiers", command=creer_dossiers)
bouton_dossiers.pack(pady=10)

# Créer le label de confirmation
label_confirmation = tk.Label(fenetre, text="")
label_confirmation.pack(pady=10)

# Afficher la fenêtre
fenetre.mainloop()
