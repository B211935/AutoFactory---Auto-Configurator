import datetime

def opslaan(configuraties):
    print("\nNieuwe configuraties opslaan!")

    huidige_tijd = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    with open("configuraties.txt", "a") as bestand:

        for configuratie in configuraties:
            config_naam = input(
                "\nGeef een naam op voor de configuratie: "
            )

            regel = (
                f"{huidige_tijd} : {config_naam} - "
                f"{configuratie}\n"
            )

            bestand.write(regel)

    print("\nAlle configuraties succesvol opgeslagen!")