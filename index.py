import os
import random
import readchar

# ======================= MENÚS =======================

def clearConsole():
    os.system('cls' if os.name == 'nt' else 'clear')

def mostrar_menu(titulo, opciones, seleccionada, nombre_equipo):
    clearConsole()
    print("=" * 40)
    print(f"🎮 {titulo} 🎮")
    print("=" * 40)
    for i, opcion in enumerate(opciones):
        prefix = "> " if i == seleccionada else "  "
        print(f"{prefix}{opcion}")
    print("=" * 40)
    print(f"🔧 Consola creada por: {nombre_equipo}")
    print("Usá ↑ ↓ para moverte, ENTER para seleccionar.")

def navegar_menu(titulo, opciones, nombre_equipo):
    seleccion = 0
    while True:
        mostrar_menu(titulo, opciones, seleccion, nombre_equipo)
        tecla = readchar.readkey()
        if tecla == readchar.key.UP:
            seleccion = (seleccion - 1) % len(opciones)
        elif tecla == readchar.key.DOWN:
            seleccion = (seleccion + 1) % len(opciones)
        elif tecla == readchar.key.ENTER:
            return seleccion

# ======================= JUEGO =======================

def juego(dificultad):
    puntos = 0
    
    while True:
        correcta, pregunta, opciones = generar_pregunta(dificultad)
        seleccion = 0

        while True:
            clearConsole()
            print(f"🎯 Puntos: {puntos}")
            print("=" * 40)
            print("❓", pregunta)
            print("-" * 40)
            for i, opcion in enumerate(opciones):
                prefix = "> " if i == seleccion else "  "
                print(f"{prefix}{opcion}")
            print("=" * 40)
            print("Usá ↑ ↓ para moverte, ENTER para responder.")

            tecla = readchar.readkey()
            if tecla == readchar.key.UP:
                seleccion = (seleccion - 1) % len(opciones)
            elif tecla == readchar.key.DOWN:
                seleccion = (seleccion + 1) % len(opciones)
            elif tecla == readchar.key.ENTER:
                if opciones[seleccion] == correcta:
                    puntos += 1
                else:
                    clearConsole()
                    print("=" * 40)
                    print("❌ Incorrecto.")
                    print(f"La respuesta correcta era: {correcta}")
                    print(f"🏁 Juego terminado. Puntos obtenidos: {puntos}")
                    print("=" * 40)
                    input("\nPresioná ENTER para volver al menú.")
                    return
                break

def decimal_a_binario(numero):
    if numero == 0:
        return "0"
    binario = ""
    while numero > 0:
        binario = str(numero%2) + binario
        numero //=2
    return binario

def generar_pregunta(dificultad):
    if dificultad == "Fácil":
        numero = random.randint(1, 15)
        correcta = str(numero)
        pregunta = f"¿Qué número es este en binario? {decimal_a_binario(numero)}"
        opciones = generar_opciones(correcta, base="decimal")
    elif dificultad == "Medio":
        operador = random.choice(["+", "-"])
        if operador == "+":
            a, b = random.randint(1, 20), random.randint(1, 20)
        else:
            a = random.randint(1, 20)
            b = random.randint(1, a)
        expresion = f"{a} {operador} {b}"
        correcta = int(eval(expresion))
        correcta = decimal_a_binario(int(correcta))
        pregunta = f"¿Cuánto da {expresion} en binario?"
        opciones = generar_opciones(correcta, base="binario")
    elif dificultad == "Difícil":
        operador = random.choice(["*", "/"])

        if operador == "*":
            a, b = random.randint(1, 20), random.randint(1, 10)
            resultado = a * b
        else:
            b = random.randint(1, 10)
            resultado = random.randint(2, 10)
            a = resultado * b
        expresion = f"{a} {operador} {b}"
        resultado = eval(expresion)
        resultado = int(resultado) if operador == "/" else resultado
        # formato = random.choice(["binario", "decimal"])
        formato = "binario"
        if formato == "binario":
            correcta = decimal_a_binario(int(resultado))
            pregunta = f"¿Cuál es el resultado de {expresion} en binario?"
            opciones = generar_opciones(correcta, base="binario")
        else:
            correcta = str(int(resultado))
            pregunta = f"¿Cuánto da {expresion}?"
            opciones = generar_opciones(correcta)
    return correcta, pregunta, opciones

def generar_opciones(correcta, base="decimal"):
    opciones = [correcta]
    while len(opciones) < 4:
        if base == "binario":
            fake = decimal_a_binario(random.randint(1, 100))
        else:
            fake = str(random.randint(1, 100))
        if fake not in opciones:
            opciones.append(fake)
    random.shuffle(opciones)
    return opciones

# ======================= FLUJO PRINCIPAL =======================

def menu_principal():
    nombre_equipo = "Capitanes del Espacio"
    dificultad_actual = "Fácil"
    while True:
        opciones = ["Jugar", f"Cambiar Dificultad (Actual: {dificultad_actual})", "Salir"]
        seleccion = navegar_menu("¡Adivineta!", opciones, nombre_equipo)

        if seleccion == 0:  # Jugar
            juego(dificultad_actual)
        elif seleccion == 1:  # Cambiar Dificultad
            dif_opciones = ["Fácil", "Medio", "Difícil"]
            nueva = navegar_menu("Seleccioná la dificultad", dif_opciones, nombre_equipo)
            dificultad_actual = dif_opciones[nueva]
        elif seleccion == 2:  # Salir
            print("¡Gracias por jugar! 👋")
            break

# ======================= INICIO =======================

if __name__ == "__main__":
    menu_principal()
