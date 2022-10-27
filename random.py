
import random 

x = random.randint(1, 100)


y=int(input("Demana numero"))

while(y!=x):
    if(x>y):
        print("es petit pero valent")
    else:
        print("es gros")
        y=int(input("Demana numero"))

