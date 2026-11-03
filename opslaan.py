import datetime

def opslaan():
    print("Nieuwe Configuratie opslaan!")
    config_naam = input("Geef een naam op voor de configuratie (bijv. 'Motoroptie Sport'): ")
    instellingen = input("Geef de instellingen/waarden op: ")

    huidige_tijd = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    regel = f"{huidige_tijd} : {config_naam} - {instellingen}\n"

    with open("configuraties.txt", "a") as bestand:
        bestand.write(regel)

        print("Configuratie succesvol opgeslagen!")