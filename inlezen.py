import os

def inlezen():
    print ("Opgeslagen Configuraties")

    if os.path.exists("configuraties.txt"):
        with open("configuraties.txt", "r") as bestand:
            regels = bestand.readlines()
            
            if len (regels) == 0:
                print("het configuratiebestand is leeg.")
            else:
               for regel in regels:
                   print(regel.strip())
    else:
        print("Nog geen configuraties gevonden. Sla er eerst eentje op!")