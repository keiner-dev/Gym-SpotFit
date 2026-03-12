print("Bienvenido a SportFit")
print("Te ofrecemos clases segun tu edad")

persona = int(input("ingrese su edad: "))

if persona <= 13:
    print("no puede ingresar")
elif persona <= 17:
    print("Perteneces a la clase juvenil")
elif persona <=59:
    print("Perteneces a la clase general")
else:
    print("Perteneces a la clase senior")