secret = 7
x = input("Get det hemmelige tal: ")
x = int(x)
if x == secret:
    print("Tillykke!")
else:
    print("Forkert! Du har tabt.")

# # Fejl beskeder betydning:
#
# Fejl ved brug af bogstaver:
#
# Exception has occurred: ValueError
# invalid literal for int() with base 10: 'b'
#   File "C:\Users\benja\Untitled-1.py", line 3, in <module>
#     x = int(x)
# ValueError: invalid literal for int() with base 10: 'b'
#
# Fejlen kommer pga linje 3 hvor du definere at det skal være en "int" (integer) og ikke en "str" (string)
# 
# Denne fejl vil komme uanset hvad du inputter så længe det ikke er en integer (et nummer uden decimaler)
# Dette kan fixes ved brug af en try/except statement som vil fange fejlen og give en besked til brugeren
except ValueError:
    print("Fejl! Du skal indtaste et heltal.")
