#Autor David Yair Fernández salas
# Matricula A01747088
# Este programa dibuja una figura como si fuera un espirografo en unaventana de pygame

"""Para poder hacer que la ventana de pygame salga, es necesario importar pygame, para poder hacer las operaciones de
manera más rápida tambien importaremos la biblioteca math y para poder hacer los colores de la figura usaremos la
biblipoteca de random"""
import pygame
import math
import random

"Se crean los parametros de la ventana"
ANCHO = 800
ALTO = 800
BLANCO = (255, 255, 255)


"Dentro de los colores se debe de crear una función especial para los colores aleatorios"
BLANCO = (255, 255, 255)  # R,G,B en el rango [0,255], 0 ausencia de color, 255 toda la intensidad
VERDE_BANDERA = (27, 94, 32)    # un poco de rojo, más de verde, un poco de azul
ROJO = (255, 0, 0)      # solo rojo, nada de verde, nada de azul
AZUL = (0, 0, 255)      # nada de rojo, ni verde, solo azul
NEGRO=(0,0,0)
#Dentro de los colores se debe de crear una función especial para los colores aleatorios
def color():
    color = [random.randint(0, 255),
               random.randint(0, 255),
               random.randint(0, 255)]
    return random.choice(color)


"Esta función sirve para dibujar la figura deseada con los parametros que el usario introudce(r,R,l)"
"y mediante uso de ciclos while esta calcula los valores (x, y) con formulas para generar los circulos necesarios "
"y poder mostrarla en la ventana de pygame, con colores alternados "
def dibujar(r, R, l):
    pygame.init()
    ventana = pygame.display.set_mode((ANCHO, ALTO))
    reloj = pygame.time.Clock()
    termina = False

    while not termina:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                termina = True

        ventana.fill(BLANCO)
        k=r/R
        for angulo in range(0, 360 * r // math.gcd(r, R)):


            θ = math.radians(angulo)  # Se convierten los grados a radianes.

            x = int(R * (((1 - k) * math.cos(θ)) + (
                        (l * k) * math.cos((((1 - k) / (k)) * θ)))))

            y = int(R * (((1 - k) * math.sin(θ)) - (l * k) * math.sin((((1 - k) / (k)) * θ))))

            pygame.draw.circle(ventana,color(), ((x + ALTO // 2), (ANCHO // 2 + y)), 1)

        pygame.display.flip()  # Actualiza los trazos.
        reloj.tick(10)  # 10 fps.

    pygame.quit()  # terminar pygame


"""Esta función es la principal, porque pregnta al usario los parametros y los envia a las funciones correspondientes 
para poder realizar el programa"""
def main():

    r = int(float(input("Escriba el valor de r: ")))
    R = int(float(input("Escriba el valor de R: ")))
    l = float(input("Escriba el valor de L: "))

    if r == 0 or R == 0:
        print("error")
    dibujar(r, R, l)


# Se llama a la función main para que se ejecute el programa.
main()



