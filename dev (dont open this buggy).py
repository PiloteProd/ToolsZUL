import time
import tkinter as tk
import os
import subprocess

# Dictionnaire de clés de licence valides
VALID_KEYS = {"MADEBYPILOTE", "TEST", "FREE"}

def check_key(key):
  # Vérifie si la clé se trouve dans le dictionnaire de clés valides
  if key in VALID_KEYS:
    return True
  else:
    return False

# Demande à l'utilisateur d'entrer une clé de licence
print("Bienvenue dans l'application !")
print("Clé gratuite (en majuscules) : FREE")
print("")
key = input("Entrez votre clé de licence : ")

# Vérifie la clé de licence
if check_key(key):
  # Si la clé est valide, affiche un message de succès et ouvre l'application
  print("Clé de licence valide. Bienvenue dans l'application.")
  subprocess.run(["python", "files/hackingtools.py"])
else:
  # Si la clé est invalide, affiche un message d'erreur et quitte l'application
  print("Clé de licence invalide. Veuillez vérifier votre clé de licence et réessayer.")
  time.sleep(10)

