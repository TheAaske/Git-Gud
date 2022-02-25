#lommeregner opgave


from ast import operator
from asyncio.windows_events import NULL


tal1 = NULL
tal2 = NULL
operator1 = NULL
resultat = 0
forfra = NULL
stoppe = NULL

print("Tryk enter for at gå videre \n")
print("Tryk 'C' og enter for at starte forfra")
print("Tryk 'Q' og enter for at slutte")

while(stoppe != 'Q'):
tal1 = input("Skriv et tal: \n")

operator1 = input("Skriv en operator: \n")

tal2 = input("Skriv et tal mere: \n")

if(operator1 == '+'):
    resultat = tal1 + tal2
    print(f'Resultatet er : {resultat}' )
elif (operator1 == '-'):
    resultat = tal1 - tal2
    print(f'Resultatet er : {resultat}')
elif (operator1 == '*'):
    resultat = tal1 * tal2
    print(f'Resultatet er : {resultat}')
elif (operator1 == '/'):
    resultat = tal1 / tal2
    rest = tal1 % tal2
    print(f'Resultatet er : {resultat}, med en rest på: {rest}')
elif (forfra == 'C'):
    continue