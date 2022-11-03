import random

#cream el random
x = random.randint(1, 100)
print("el nombre es", x)


endevinat = False
#comptador de torns
torn = 1
llista = []


while (endevinat):
    torn += 1
    y = int(input("demana numero")) 
    if (x>y):
        print ("es petit però valent")
    elif (x<y):
        print ("es gros")
    else:
        endevinat = True
    llista.append(y)
   


print("molt be has endivinat")
print("has emprat", torn, "torns")
print(llista)
