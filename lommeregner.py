# Lommeregner opgave

# Plus funktion
from pkg_resources import register_namespace_handler


def plus(x, y):
    return x + y

# Minus funktion
def minus(x, y):
    return x - y

# En lille menu til lommeregner-funktioner
print("Vælg en operator")
print("1. Plus")
print("2. Minus")
print("3. Multiplikation")
print("1. Division")

# Loop til valg og udregning
while True:
    # Input til variabel for menuvalg
    menuValg = input("skriv operator(1, 2, 3, 4): \n")
    
    # Se om inputtet er en af menupunkterne
    if menuValg in ('1', '2', '3', '4'):
        tal1 = float(input("Indtast første nummer: \n"))
        tal2 = float(input("Indtast andet nummer: \n"))
    
        if(menuValg == '1'):
            print(tal1, "+", tal2, "=", plus(tal1, tal2))
        elif(menuValg == '2'):
            print(tal1, "+", tal2, "=", minus(tal1, tal2))
        elif(menuValg == '3'):
            print(tal1, "+", tal2, "=", multiplikation(tal1, tal2))
        elif(menuValg == '4'):
            rest = int(tal1) % int(tal2)
            print(tal1, "+", tal2, "=", division(tal1, tal2), "\nmed en rest på: ", rest)

        # Se efter om brugeren vil regne videre
        regneMere = input("Vil du lave endnu en udregning? (ja/nej): \n")
        # Stop hvis man skriver nej
        if regneMere == "nej":
            break
    
    # Hvis inputtet ikke er en af menupunkterne skriver den fejl
    else:
        print("Input er ikke et menupunkt!")