# Maak een lijst met getallen.
# Schrijf een functie vind_grootste_getal die de grootste waarde uit een lijst teruggeeft.
# Gebruik een for-loop om de grootste waarde te vinden.
getal = [1,5,2]
def vind_grootste_getal_traag():
    getal.sort()
    getal.reverse()
    print(getal[0])
vind_grootste_getal_traag()