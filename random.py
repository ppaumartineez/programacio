import random

x = random.randint(1, 100)
print("el nombre es", x)

y=int(input("demana numero"))

#comptador de torns
torn = 1

while (y!=x):
    torn += 1
    if (x>y):
        print ("es petit però valent")
    else:
        print ("es gros")
    y=int(input("demana numero")) 

print("molt be has endivinat")
print("has emprat", torn, "torns")
