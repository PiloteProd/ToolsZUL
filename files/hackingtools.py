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

# Chargement de l'image GIF
image = Image.open('files/img/logo.gif')
image = ImageTk.PhotoImage(image)

# Création d'un widget Label pour afficher l'image
image_label = tk.Label(root, image=image)
image_label.pack(pady=10) # Ajout d'un espace de 10 pixels en haut et en bas de l'image

# Création d'un objet Style
style = ttk.Style()

# Définition du style à utiliser
style.theme_use("alt")

shutdown_button = tk.Button(root, text="Éteindre", command=shutdown)
shutdown_button.pack(pady=10) # Ajout d'un espace de 10 pixels en haut et en bas du premier bouton

button = tk.Button(root, text="Jeu 01 : Le fugitif", command=open_game_one)
button.pack(pady=10)

button = tk.Button(root, text="Jeu 02 : Le Snake", command=open_game_two)
button.pack(pady=10)

button = tk.Button(root, text="Hack 1 : Les dossiers infinis", command=hack_dossier)
button.pack(pady=10)

quit_button = tk.Button(root, text="Quitter", command=quit)
quit_button.pack(pady=10)

root.mainloop()
