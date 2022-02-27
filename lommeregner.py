#lommeregner opgave
import keyboard
from asyncio.windows_events import NULL
 

<<<<<<< HEAD
<<<<<<< HEAD
# Importerer classen: plusMinus, fra filen plus_minus.py
from plus_minus import plusMinus
# Importere classen: multiDivi, fra filen multi_Divi
from multi_Divi import multiDivi
=======
# Plus funktion
def plus(x, y):
    return x + y

# Minus funktion
def minus(x, y):
    return x - y
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> parent of f69bb66 (commit)
=======
>>>>>>> parent of f69bb66 (commit)
=======
>>>>>>> parent of f69bb66 (commit)

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
=======
tal1 = NULL
tal2 = NULL
operator1 = NULL
resultat = 0
forfra = NULL
stoppe = 0

print("Tryk enter for at gå videre \n")
print("Tryk 'C' og enter for at starte forfra")
print("Tryk 'Q' og enter for at slutte")


while(keyboard.on_press_key(key='q' ) != 'q'):
    print("Start")
    tal1 = input("Skriv et tal: \n")
    operator1 = input("Skriv en operator: \n")
    tal2 = input("Skriv et tal mere: \n")
    
>>>>>>> parent of 0bed2cb (commmit on master)
    
    if((operator1 == 'Q') or (tal1 == 'Q') or (tal2 == 'Q')):
        break
    elif(operator1 == '+'):
        resultat = int(tal1) + int(tal2)
        print('Resultatet er : ' + str(resultat) )
    elif(operator1 == '-'):
        resultat = int(tal1) - int(tal2)
        print('Resultatet er : ' + str(resultat))
    elif(operator1 == '*'):
        resultat = int(tal1) * int(tal2)
        print('Resultatet er : ' + str(resultat))
    elif(operator1 == '/'):
        resultat = int(tal1) / int(tal2)
        rest = int(tal1) % int(tal2)
        print('Resultatet er : ' + str(resultat))
        print('Med en rest på: ' + str(rest)) 
    