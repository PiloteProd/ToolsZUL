import tkinter as tk
import tkinter.ttk as ttk
import os
import subprocess
from PIL import Image, ImageTk

def shutdown():
  os.system("shutdown /s /t 1")

def quit():
  root.destroy()

def open_game_one():
    subprocess.run(["python", "files/fugitif.py"])
def open_game_two():
    subprocess.run(["python", "files/snake.py"])
def hack_dossier():
    subprocess.run(["python", "files/hack/dossier.py"])

root = tk.Tk()
root.title("Hacking Tools V0.1")

# Définition de la taille de l'écran
root.geometry("740x477")

# Définition de la couleur de fond de l'application
root.configure(bg="#191919")

# Chargement de l'image GIF
image = Image.open('files/img/logo.gif')
image = ImageTk.PhotoImage(image)

# Création d'un widget Label pour afficher l'image
image_label = tk.Label(root, image=image)
image_label.pack(pady=10) # Ajout d'un espace de 10 pixels en haut et en bas de l'image

# Création d'un objet Style
style = ttk.Style()

# Définition du style à utiliser
style.theme_use("clam")

# Création d'un widget Frame pour disposer les boutons à gauche de l'écran
left_frame = tk.Frame(root)
left_frame.pack(side="left", fill="both", expand=True)

shutdown_button = tk.Button(left_frame, text="Éteindre", command=shutdown, bg="#202020", fg="white")
shutdown_button.pack(pady=10) # Ajout d'un espace de 10 pixels en haut et en bas du premier bouton

button = tk.Button(left_frame, text="Jeu 01 : Le fugitif", command=open_game_one, bg="#202020", fg="white")
button.pack(pady=10)

button = tk.Button(left_frame, text="Jeu 02 : Le Snake", command=open_game_two, bg="#202020", fg="white")
button.pack(pady=10)

# Création d'un widget Frame pour disposer le bouton Hack 1 à droite de l'écran
right_frame = tk.Frame(root)
right_frame.pack(side="right", fill="both", expand=True)

button = tk.Button(right_frame, text="Hack 1 : Les dossiers infinis", command=hack_dossier, bg="#202020", fg="white")
button.pack(pady=10)

# Création d'un widget Frame pour disposer le bouton Quitter au milieu en bas de l'écran
bottom_frame = tk.Frame(root)
bottom_frame.pack(side="bottom", fill="both", expand=True)

quit_button = tk.Button(bottom_frame, text="Quitter", command=quit, bg="#202020", fg="white")
quit_button.pack(pady=10)

root.mainloop()

