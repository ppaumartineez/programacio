import random

x = random.randint(1, 100)

endevinat = True

torn = 1
llista = []




while (endevinat) :        
    torn += 1
    y = int(input("Adivina el numero escrivint-hi un: "))
   
    if (x>y):
        print("Es petit, torna a provar")
    elif (x<y):
        print("Es gran, torna a provar")
    else:
        endevinat = False
    
    llista.append(y)

print("Enorabona! Aconseguit en" , torn , "vegades.")
print(llista)
print("En efectiu x era", x)
