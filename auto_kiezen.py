def auto_kiezen():
    prijs = 0

    print("\n--- Auto configureren ---")

    # Automodel kiezen
    print("\nKies een automodel:")
    print("1. SUV")
    print("2. Stationwagon")
    print("3. Hatchback")
    print("4. MPV")

    model_keuze = input("Maak een keuze (1-4): ")

    if model_keuze == "1":
        model = "SUV"
        prijs = prijs + 35000
    elif model_keuze == "2":
        model = "Stationwagon"
        prijs = prijs + 30000
    elif model_keuze == "3":
        model = "Hatchback"
        prijs = prijs + 25000
    elif model_keuze == "4":
        model = "MPV"
        prijs = prijs + 40000
    else:
        print("Ongeldige keuze.")
        return

    # Merk kiezen
    print("\nKies een merk:")
    print("1. Peugeot")
    print("2. Volkswagen")
    print("3. Toyota")
    print("4. Ford")

    merk_keuze = input("Maak een keuze (1-4): ")

    if merk_keuze == "1":
        merk = "Peugeot"
    elif merk_keuze == "2":
        merk = "Volkswagen"
    elif merk_keuze == "3":
        merk = "Toyota"
    elif merk_keuze == "4":
        merk = "Ford"
    else:
        print("Ongeldige keuze.")
        return

    # Motor kiezen
    print("\nKies een motor:")
    print("1. Benzine")
    print("2. Diesel")
    print("3. Elektrisch")
    print("4. Hybride")

    motor_keuze = input("Maak een keuze (1-4): ")

    if motor_keuze == "1":
        motor = "Benzine"
        prijs = prijs + 2000
    elif motor_keuze == "2":
        motor = "Diesel"
        prijs = prijs + 3000
    elif motor_keuze == "3":
        motor = "Elektrisch"
        prijs = prijs + 8000
    elif motor_keuze == "4":
        motor = "Hybride"
        prijs = prijs + 5000
    else:
        print("Ongeldige keuze.")
        return

    # Kleur kiezen
    print("\nKies een kleur:")
    print("1. Zwart")
    print("2. Wit")
    print("3. Grijs")
    print("4. Rood")
    print("5. Blauw")

    kleur_keuze = input("Maak een keuze (1-5): ")

    if kleur_keuze == "1":
        kleur = "Zwart"
    elif kleur_keuze == "2":
        kleur = "Wit"
    elif kleur_keuze == "3":
        kleur = "Grijs"
    elif kleur_keuze == "4":
        kleur = "Rood"
    elif kleur_keuze == "5":
        kleur = "Blauw"
    else:
        print("Ongeldige keuze.")
        return

    # Uitvoering kiezen
    print("\nKies een uitvoering:")
    print("1. Standaard")
    print("2. Comfort")
    print("3. Sport")
    print("4. Luxury")

    uitvoering_keuze = input("Maak een keuze (1-4): ")

    if uitvoering_keuze == "1":
        uitvoering = "Standaard"
        prijs = prijs + 0
    elif uitvoering_keuze == "2":
        uitvoering = "Comfort"
        prijs = prijs + 3000
    elif uitvoering_keuze == "3":
        uitvoering = "Sport"
        prijs = prijs + 5000
    elif uitvoering_keuze == "4":
        uitvoering = "Luxury"
        prijs = prijs + 8000
    else:
        print("Ongeldige keuze.")
        return

    # Extra opties kiezen
    opties = []

    while True:
        print("\n--- Extra opties ---")
        print("1. Climate control (€500)")
        print("2. Cruise control (€750)")
        print("3. Stoelverwarming (€400)")
        print("4. Stuurverwarming (€300)")
        print("5. Geen extra opties meer")

        optie_keuze = input("Maak een keuze (1-5): ")

        if optie_keuze == "1":
            if "Climate control" not in opties:
                opties.append("Climate control")
                prijs = prijs + 500
            else:
                print("Deze optie is al gekozen.")

        elif optie_keuze == "2":
            if "Cruise control" not in opties:
                opties.append("Cruise control")
                prijs = prijs + 750
            else:
                print("Deze optie is al gekozen.")

        elif optie_keuze == "3":
            if "Stoelverwarming" not in opties:
                opties.append("Stoelverwarming")
                prijs = prijs + 400
            else:
                print("Deze optie is al gekozen.")

        elif optie_keuze == "4":
            if "Stuurverwarming" not in opties:
                opties.append("Stuurverwarming")
                prijs = prijs + 300
            else:
                print("Deze optie is al gekozen.")

        elif optie_keuze == "5":
            break

        else:
            print("Ongeldige keuze.")

    # Configuratie opslaan in een dictionary
    configuratie = {
        "model": model,
        "merk": merk,
        "motor": motor,
        "kleur": kleur,
        "uitvoering": uitvoering,
        "opties": opties,
        "prijs": prijs
    }

    # Configuratie overzichtelijk tonen
    print("\n================================")
    print("       AUTO CONFIGURATIE")
    print("================================")
    print("Model:", model)
    print("Merk:", merk)
    print("Motor:", motor)
    print("Kleur:", kleur)
    print("Uitvoering:", uitvoering)

    print("\nExtra opties:")

    if len(opties) == 0:
        print("Geen extra opties gekozen.")
    else:
        for optie in opties:
            print("-", optie)

    print("\nTotaalprijs: €", prijs)
    print("================================")

    return configuratie