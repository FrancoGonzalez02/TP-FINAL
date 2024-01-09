import random
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

class adivina_el_numero():
    def __init__(self):
        self.numero_buscado = random.randint(1, 10)
        self.intentos = 0
        self.max_intentos = 3

    def jugar(self):
        print("Bienvenido al juego de adivinanzas. Adivina el número entre 1 y 10.")
        while True:
            intento = int(input("Introduzca un número: "))
            self.intentos += 1

            if self.numero_buscado == intento:
                print(f"Correcto, encontraste el número {self.numero_buscado} en {self.intentos} intentos.")
                break
            elif self.numero_buscado < intento:
                print("El número es más bajo, inténtalo de nuevo.")
            else:
                print("El número es más alto, inténtalo de nuevo.")
            if self.intentos == self.max_intentos:
                print(f"Llegaste a la cantidad máxima de intentos ({self.max_intentos}). El número correcto era {self.numero_buscado}.")
                break
        
class Dados():
    def lanzar_dados(self):
        return random.randint(1, 6), random.randint(1, 6)

    def jugar(self):
        rondas_para_ganar = 2
        rondas_j1 = 0
        rondas_j2 = 0
        
        while rondas_j1 < rondas_para_ganar and rondas_j2 < rondas_para_ganar:
            dado_1_jugador_1, dado_2_jugador_1 = self.lanzar_dados()
            dado_1_jugador_2, dado_2_jugador_2 = self.lanzar_dados()
            print(f"Resultados de los dados del jugador 1: [{dado_1_jugador_1}, {dado_2_jugador_1}]")
            print(f"Resultados de los dados del jugador 2: [{dado_1_jugador_2}, {dado_2_jugador_2}]")
            
            if dado_1_jugador_1 in [dado_1_jugador_2, dado_2_jugador_2] or dado_2_jugador_1 in [dado_1_jugador_2, dado_2_jugador_2]:
                rondas_j1 += 1
                print("Jugador 1 gana la ronda")
            else:
                rondas_j2 += 1
                print("Jugador 2 gana la ronda")
                
        if rondas_j1 > rondas_j2:
            print("El jugador 1 gana la partida")
        else:
            print("El jugador 2 gana la partida")
            
class FuncionCuadratica:
    def __init__(self, x_values):
        self.x_values = x_values
        self.y_values = self.calcular_y()

    def calcular_y(self):
        """Calcula los valores de la función para los valores dados de x."""
        return np.sqrt(self.x_values + 2)

    def generar_tabla(self):
        """Genera una tabla de los valores de la función."""
        tabla = pd.DataFrame(list(zip(self.x_values, self.y_values)), columns=['x', 'f(x)'])
        return tabla

    def graficar_funcion(self):
        """Grafica la función."""
        x_range = np.linspace(min(self.x_values) - 2, max(self.x_values) + 2, num=100)
        ax = self.move_spines()
        ax.grid()
        ax.plot(x_range, np.sqrt(x_range + 2))
        plt.title(r"Grafico de $f(x)=\sqrt{x+2}$")
        plt.ylabel('f(x)')
        plt.xlabel('x')
        plt.show()

    def move_spines(self):
        """Esta función coloca el eje y en el valor 0 de x para dividir
        claramente los valores positivos y negativos."""
        fig, ax = plt.subplots()
        for spine in ["left", "bottom"]:
            ax.spines[spine].set_position("zero")
        
        for spine in ["right", "top"]:
            ax.spines[spine].set_color("none")
        
        return ax
          
class PiedraPapelTijera():
    def jugar(self):
        #determinar las opciones
        opciones = ('piedra', 'papel', 'tijera')

        #pedir al usuario que elija una opción
        usuario = input('Listos para jugar\n¿Cuál eliges: piedra, papel, tijera? ').lower()

        #generar la opción automática de la PC
        pc = random.choice(opciones)

        #verificar si la opción del usuario es válida
        if usuario not in opciones:
            print('Opción inválida')
            return

        #mostrar las opciones elegidas
        print(f'Usuario: {usuario}')
        print(f'PC: {pc}')

        #determinar el ganador
        if usuario == pc:
            print('Empate!')
        elif usuario == 'piedra' and pc == 'tijera' or usuario == 'papel' and pc == 'piedra' or usuario == 'tijera' and pc == 'papel':
            print(f'{usuario.capitalize()} gana a {pc}')
            print('Usuario ha ganado')
        else:
            print(f'{pc.capitalize()} gana a {usuario}')
            print('PC ha ganado')
  #verson 1.1 de Gonzalez Gustavo, Franco Gonzalez
  
  
def mostrar_menu():
    print('Binvenido a "GonzalezGames"\n=== Menú de Juegos ===')
    print("1. Adivina el Número")
    print("2. Juego de Dados")
    print("3. Función Cuadrática")
    print("4. Piedra, Papel, Tijera")
    print("5. Salir")

def main():
    while True:
        mostrar_menu()
        opcion = input("Selecciona un juego (1-5): ")

        if opcion == "1":
            juego_adivinanza = adivina_el_numero()
            juego_adivinanza.jugar()
        elif opcion == "2":
            juego_dados = Dados()
            juego_dados.jugar()
        elif opcion == "3":
            x_values = np.array([3, 9, 0, 7, 5, -1])
            funcion_cuadratica = FuncionCuadratica(x_values)
            print(funcion_cuadratica.generar_tabla())
            funcion_cuadratica.graficar_funcion()
        elif opcion == "4":
            juego_PPT = PiedraPapelTijera()
            juego_PPT.jugar()
            pass
        elif opcion == "5":
            print("Saliendo del programa. ¡Hasta luego!")
            break
        else:
            print("Opción no válida. Inténtalo de nuevo.")

if __name__ == "__main__":
    main()