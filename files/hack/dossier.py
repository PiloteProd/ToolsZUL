import tkinter as tk
import tkinter.simpledialog
import os
import random

# Créer la fenêtre principale
fenetre = tk.Tk()
fenetre.title("Répertoire de fichiers")
fenetre.geometry("328x132")  # Définir la taille de la fenêtre
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
            nom_dossier = "HACKED " + str(random.randint(0, 10000000000))
            os.mkdir(os.path.join(repertoire_actuel, nom_dossier))
    else:
        # Afficher un message d'erreur
        tk.messagebox.showerror("Erreur", "Vous n'avez pas saisi de nombre valide.")

def effacer_texte(event):
    # Réinitialiser le texte de l'entrée de texte
    texte_entree.set("")

# Créer la variable de texte pour l'entrée de texte
texte_entree = tk.StringVar()
texte_entree.set("Entrez le répertoire de fichier ici")

# Créer un cadre pour l'entrée de texte et le bouton "Set"
cadre_entree_set = tk.Frame(fenetre)
cadre_entree_set.pack(pady=10)
# Créer l'entrée de texte pour le répertoire
entree_repertoire = tk.Entry(cadre_entree_set, textvariable=texte_entree, font=("Arial", 10), width=27)
entree_repertoire.pack(side="left")

# Lier l'événement <FocusIn> à la fonction effacer_texte
entree_repertoire.bind("<FocusIn>", effacer_texte)


# Créer le bouton "Set" et le placer dans le cadre à droite de l'entrée de texte
bouton_set = tk.Button(cadre_entree_set, text="Set", command=mettre_a_jour_repertoire)
bouton_set.pack(side="left", padx=10)
# Créer le bouton de création de dossiers
bouton_dossiers = tk.Button(fenetre, text="Créer des dossiers", command=creer_dossiers)
bouton_dossiers.pack(pady=10)

# Créer le label de confirmation
label_confirmation = tk.Label(fenetre, text="")
label_confirmation.pack(pady=10)

# Afficher la fenêtre
fenetre.mainloop()
