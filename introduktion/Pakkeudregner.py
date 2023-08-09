try:
    vægt = float(input("Indtast vægt: "))
    print("Leveringsmuligheder: Collect Eller Home")
    leveringsform = input("Indtast leveringsformen: ")

    if leveringsform == "Collect":
        if vægt <= 2:
            pris = 50.00
        elif vægt <= 5:
            pris = 60.00
        elif vægt <= 10:
            pris = 80.00
        elif vægt <= 20:
            pris = 100.00
        else:
            print("Dette er ikke en mulighed")
            pris = None
    elif leveringsform == "Home":
        if vægt <= 2:
            pris = 65.00
        elif vægt <= 5:
            pris = 75.00
        elif vægt <= 10:
            pris = 95.00
        elif vægt <= 20:
            pris = 115.00
        elif vægt <= 35:
            pris = 160.00
        else:
            print("Dette er ikke en mulighed")
            pris = None
    else:
        print("Dette er ikke en mulighed")
        pris = None

    if pris is not None:
        print("Prisen for pakken er:", pris, "kr.")

except ValueError:
    print("Du skal skrive vægten")
