print("Ingrese opcion")
print("a- Atacar")
print("b- critico")
print("c- dejar")

#Aparcición enemigo
def aparicion():
    global vida
    vida = 10

#Ataque normal
def atacar():
    global vida
    vida = vida - 1

#Golpe critico
def critico ():
    global vida
    vida = vida - 3

#Dejar tranquilo
def dejar ():
    global vida
    vida = vida

#Revivir
def revivir():
    global vida
    aparicion()

#Aparicion
aparicion()
while vida > 0:
    opcion = input("elija su opción:")
    if opcion == "a":
        atacar()
        print("Vida Restante:", vida)
    elif opcion == "b":
        critico()
        print("Vida Restante:", vida)
    elif opcion == "c":
        dejar()
        print("Vida Restante:", vida)


#Revivido
revivir(), print("Ha resucitado!!", vida)
while vida > 0:
    opcion = input("elija su opción:")
    if opcion == "a":
        atacar()
        print("Vida Restante:", vida)
    elif opcion == "b":
        critico()
        print("Vida Restante:", vida)
    elif opcion == "c":
        dejar()
        print("Vida Restante:", vida)
