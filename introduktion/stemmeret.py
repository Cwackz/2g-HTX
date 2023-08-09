try:
    alder = int(input("Hvor gammel er du? "))
    if alder >= 18:
        print("Du er gammel nok til at stemme")
    else:
        print("Du er ikke gammel nok til at stemme")

except ValueError:
    print("Du skal indtaste en alder")
