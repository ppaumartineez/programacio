#llegir
#mirar si es nombre
#mostrar misatge de sí o no

def llegirIP():
    print("Escriu una ip")
    x = input()
    return x 

def nombreValid(nombre):
#mirar si el nombre està entre 0 i 255
    if (nombre >= 0) and (nombre <= 255):
        return True
    else:
        return False

def comprovaIP(x):
    x = x.split(".")
    print(x)
    a = int(x[0])
    b = int(x[1])
    c = int(x[2])
    d = int(x[3])
    if (nombreValid(a) and nombreValid(b) and nombreValid(c) and nombreValid(d)):
        print("És una ip vàlida. ", ip)   
        return True 
    else:
        print("És una ip NO vàlida. ", ip)
        return False

sortir = False
#llegir ip sencera (192.168.1.2)

while not sortir:
    ip = llegirIP()
    #la dividim en quatre parts (a=192,b=168,c=1,d=2)
    #comprovar tots els trossos amb nombreValid()
    if ip != 'sortir':
        comprovaIP(ip)
    else:
        sortir = True
    #mostram que es valid
    #nombreValid(ip)

print ("Ha acabat l'excursió")
