import random

def obtener_eleccion_usuario():
    opciones = ['piedra', 'papel', 'tijera']
    eleccion = input("Elige piedra, papel o tijera: ").strip().lower()
    while eleccion not in opciones:
        eleccion = input("Opción inválida. Elige piedra, papel o tijera: ").strip().lower()
    return eleccion

def obtener_eleccion_computadora():
    return random.choice(['piedra', 'papel', 'tijera'])

def determinar_ganador(usuario, computadora):
    if usuario == computadora:
        return "Empate"
    elif (usuario == 'piedra' and computadora == 'tijera') or \
         (usuario == 'papel' and computadora == 'piedra') or \
         (usuario == 'tijera' and computadora == 'papel'):
        return "¡Ganaste!"
    else:
        return "Perdiste..."

def jugar():
    print("¡Bienvenido al juego de Piedra, Papel o Tijera!")
    usuario = obtener_eleccion_usuario()
    computadora = obtener_eleccion_computadora()
    
    print(f"Tú elegiste: {usuario}")
    print(f"La computadora eligió: {computadora}")
    
    resultado = determinar_ganador(usuario, computadora)
    print(resultado)

if __name__ == "__main__":
    jugar()
    