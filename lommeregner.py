# Lommeregner opgave

# Importerer classen: plusMinus, fra filen plus_minus.py
from plus_minus import plusMinus
# Importere classen: multiDivi, fra filen multi_Divi
from multi_Divi import multiDivi

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
            print(tal1, "+", tal2, "=", plusMinus.plus(tal1, tal2))
        elif(menuValg == '2'):
            print(tal1, "+", tal2, "=", plusMinus.minus(tal1, tal2))
        elif(menuValg == '3'):
            print(tal1, "+", tal2, "=", multiDivi.multiplikation(tal1, tal2))
        elif(menuValg == '4'):
            rest = int(tal1) % int(tal2)
            print(tal1, "+", tal2, "=", multiDivi.division(tal1, tal2), "\nmed en rest på: ", rest)

        # Se efter om brugeren vil regne videre
        regneMere = input("Vil du lave endnu en udregning? (ja/nej): \n")
        # Stop hvis man skriver nej
        if regneMere == "nej":
            break
    
    # Hvis inputtet ikke er en af menupunkterne skriver den fejl
    else:
        print("Input er ikke et menupunkt!")