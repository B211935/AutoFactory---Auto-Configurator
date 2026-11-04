
def auto_kiezen():
    print("\n--- Auto configureren ---")

    print("\nKies een automodel:")
    print("1. SUV")
    print("2. Stationwagon")
    print("3. Hatchback")
    print("4. MPV")

    model_keuze = input("Maak een keuze (1-4): ")

    if model_keuze == "1":
        model = "SUV"
    elif model_keuze == "2":
        model = "Stationwagon"
    elif model_keuze == "3":
        model = "Hatchback"
    elif model_keuze == "4":
        model = "MPV"
    else:
        print("Ongeldige keuze.")
        return

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
    elif motor_keuze == "2":
        motor = "Diesel"
    elif motor_keuze == "3":
        motor = "Elektrisch"
    elif motor_keuze == "4":
        motor = "Hybride"
    else:
        print("Ongeldige keuze.")
        return

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

    print("\nKies een uitvoering:")
    print("1. Standaard")
    print("2. Comfort")
    print("3. Sport")
    print("4. Luxury")

    uitvoering_keuze = input("Maak een keuze (1-4): ")

    if uitvoering_keuze == "1":
        uitvoering = "Standaard"
    elif uitvoering_keuze == "2":
        uitvoering = "Comfort"
    elif uitvoering_keuze == "3":
        uitvoering = "Sport"
    elif uitvoering_keuze == "4":
        uitvoering = "Luxury"
    else:
        print("Ongeldige keuze.")
        return

    configuratie = {
        "model": model,
        "merk": merk,
        "motor": motor,
        "kleur": kleur,
        "uitvoering": uitvoering
    }

    print("\nAuto succesvol geconfigureerd!")

    return configuratie