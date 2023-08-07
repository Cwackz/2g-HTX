import math
print("Vælg en figur:")
print("1. Cirkel")
print("2. rektangel")

valg = int(input("Vælg en figur: "))
if valg == 1:
    print ("indtast radius")
    r = float(input())
    print(math.pi * r**2)
elif valg == 2:
    print ("indtast længde")
    l = float(input())
    print ("indtast bredde")
    b = float(input())
    print(l * b)
