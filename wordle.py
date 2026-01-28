# 1 Definimos la palabra secreta y el modo de juego
palabra_secreta = "arbol"
numero_de_intentos = 6
# Saludamos al jugador
print("Bienvenido a Wordle Pingu")
# 2 Empezamos a definir el bucle 
while numero_de_intentos > 0:
    numero_de_intentos = numero_de_intentos - 1
    print(f"Te quedan {numero_de_intentos} intentos")
     # 3 Pedimos la palabra al usuario
    palabra_ingresada = input("Ingresa una palabar de 5 letras")
