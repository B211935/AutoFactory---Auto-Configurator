import auto_kiezen
import opslaan
import inlezen

while True:
    print("\n================================")
    print("            AutoFactory")
    print("         Auto Configurator")
    print("=================================\n")
    print("1. Nieuwe auto configureren")
    print("2. Configuratie opslaan")
    print("3. Opgeslagen configuraties bekijken")
    print("4. Programma afsluiten")

    keuze = input("\nMaak een keuze (1-4): ")

    if keuze == "1":
        auto_kiezen.auto_kiezen()

    elif keuze == "2":
        opslaan.opslaan()

    elif keuze == "3":
        inlezen.inlezen()

    elif keuze == "4":
        print("Bedankt voor het gebruiken van AutoFactory!")
        print("\nHet programma wordt nu afgesloten...")
        break

    else:
        print("Ongeldige keuze. Kies een nummer van 1 t/m 4.")