
# Programa: Semáforo 
# Descripción: El usuario ingresa un color y el programa
#              responde el estado correspondiente.

# Pedimos al usuario que ingrese un color
color = input("Ingresa un color (rojo, amarillo, verde): ")

# Usamos condicionales para determinar el estado
if color == "rojo":
    print("Estado: ALTO – Detenerse")
elif color == "amarillo":
    print("Estado: PRECAUCIÓN – espere")
elif color == "verde":
    print("Estado: AVANZAR – Puede continuar")
else:
    print("Error: color no reconocido")
