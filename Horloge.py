import time
import threading

# Initialisation de l'heure actuelle et du mode d'affichage
mode_affichage = "24h"
pause = False

def afficher_heure():
    while True:
        if not pause:
            # Récupération de l'heure actuelle
            heure_actuelle = time.localtime()
            # Affichage de l'heure selon le mode d'affichage sélectionné
            if mode_affichage == "12h":
                print(time.strftime("%I:%M:%S %p", heure_actuelle))
            else:
                print(time.strftime("%H:%M:%S", heure_actuelle))
            # Mise à jour de l'heure toutes les secondes
            time.sleep(1)
        else:
            time.sleep(1)

def regler_heure(nouvelle_heure):
    # Mise à jour de l'heure actuelle
    global heure_actuelle
    heure_actuelle = time.struct_time((nouvelle_heure[0], nouvelle_heure[1], nouvelle_heure[2], *heure_actuelle[3:6], *heure_actuelle[6:9]))

def regler_alarme(heure_alarme):
    heure_actuelle = time.localtime()
    alarm_set = True
    while alarm_set:
        if not pause:
            # Vérifie si l'heure actuelle correspond à l'heure de l'alarme
            if (heure_actuelle.tm_hour, heure_actuelle.tm_min, heure_actuelle.tm_sec) == heure_alarme:
                print("Alarme!")
                alarm_set = False
                break
            # Mise à jour de l'heure toutes les secondes
            time.sleep(1)
            heure_actuelle = time.localtime()
        else:
            time.sleep(1)
def annuler_alarme():
    global alarm_set
    alarm_set = False



def choisir_mode_affichage():
    global mode_affichage
    print("Sélectionnez le mode d'affichage:")
    print("1. 24 heures")
    print("2. 12 heures")
    choice = input("Entrez votre choix (1 ou 2): ")
    if choice == "1":
        mode_affichage = "24h"
    elif choice == "2":
        mode_affichage = "12h"
    else:
        print("Choix non valide.")
        choisir_mode_affichage()

def mettre_en_pause():
    global pause
    pause = True






choisir_mode_affichage()
afficher_heure_thread = threading.Thread(target=afficher_heure)
afficher_heure_thread.start()
globals-regler_alarme(regler_alarme((11, 22, 00)))

