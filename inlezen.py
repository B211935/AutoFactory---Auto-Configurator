import os
import ast

def inlezen():
    print("\n================================")
    print("       Opgeslagen Configuraties")
    print("================================")

    if os.path.exists("configuraties.txt"):
        with open("configuraties.txt", "r") as bestand:
            regels = bestand.readlines()

            if len(regels) == 0:
                print("Het configuratiebestand is leeg.")
                return

            configuraties = []

            for regel in regels:
                delen = regel.strip().split(" - ", 1)

                if len(delen) != 2:
                    continue

                tijd_en_naam = delen[0]
                instellingen = delen[1]

                configuratie = ast.literal_eval(instellingen)

                configuraties.append({
                    "naam": tijd_en_naam,
                    "instellingen": configuratie
                })

            # Menu met configuraties
            print("\nKies een configuratie:\n")

            for i, config in enumerate(configuraties, start=1):
                print(f"{i}. {config['naam']}")

            print("0. Terug naar hoofdmenu")

            keuze = input("\nMaak een keuze: ")

            if keuze == "0":
                return

            if keuze.isdigit() and 1 <= int(keuze) <= len(configuraties):
                gekozen = configuraties[int(keuze) - 1]
                config = gekozen["instellingen"]

                # Volledige configuratie tonen
                print("\n================================")
                print("       AUTO CONFIGURATIE")
                print("================================")

                print("Naam:", gekozen["naam"])
                print("Model:", config["model"])
                print("Merk:", config["merk"])
                print("Motor:", config["motor"])
                print("Kleur:", config["kleur"])
                print("Uitvoering:", config["uitvoering"])

                print("\nExtra opties:")

                if len(config["opties"]) == 0:
                    print("Geen extra opties.")
                else:
                    for optie in config["opties"]:
                        print("-", optie)

                print("\nTotaalprijs: €", config["prijs"])
                print("================================")

            else:
                print("Ongeldige keuze.")

    else:
        print("Nog geen configuraties gevonden. Sla er eerst eentje op!")