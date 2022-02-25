#lommeregner opgave

from asyncio.windows_events import NULL


tal1 = NULL
tal2 = NULL
operator1 = NULL
resultat = 0
forfra = NULL
stoppe = 0

print("Tryk enter for at gå videre \n")
print("Tryk 'C' og enter for at starte forfra")
print("Tryk 'Q' og enter for at slutte")

print("Start")
tal1 = input("Skriv et tal: \n")
operator1 = input("Skriv en operator: \n")
tal2 = input("Skriv et tal mere: \n")

while(stoppe == 0):
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
    