# Maak een programma dat:
# - een lege lijst aanmaakt
# - drie dieren vraagt aan de user
# - deze dieren toevoegt aan de lijst
# - de lijst met dieren toont aan de user
lijst = []
print("geef 3 dieren")

for i in range(3):
    dier = input("dier" +str(i+1)+ ":")
    lijst.append(dier)
print(lijst)