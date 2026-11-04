import auto_kiezen
import opslaan
import inlezen

configuraties = []

while True:
    print("\n================================")
    print("            AutoFactory")
    print("         Auto Configurator")
    print("=================================\n")
    print("1. Nieuwe auto configureren")
    print("2. Configuraties opslaan")
    print("3. Opgeslagen configuraties bekijken")
    print("4. Programma afsluiten")

    keuze = input("\nMaak een keuze (1-4): ")

    if keuze == "1":
        configuratie = auto_kiezen.auto_kiezen()

        if configuratie is not None:
            configuraties.append(configuratie)

    elif keuze == "2":
        if len(configuraties) > 0:
            opslaan.opslaan(configuraties)
            configuraties = []
        else:
            print("Er zijn geen configuraties om op te slaan.")

    elif keuze == "3":
        inlezen.inlezen()

    elif keuze == "4":
        print("Bedankt voor het gebruiken van AutoFactory!")
        print("\nHet programma wordt nu afgesloten...")
        break

    else:
        print("Ongeldige keuze. Kies een nummer van 1 t/m 4.")