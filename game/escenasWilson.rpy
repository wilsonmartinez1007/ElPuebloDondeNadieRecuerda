# PERSONAJES

define d = Character("Daniel", color="#A9C9DF")
define e = Character("Elena", color="#D8C3A5")
define j = Character("Don Julián", color="#C5C9A4")
define n = Character(None)

# VARIABLES

default decision_01 = ""
default decision_02 = ""

default pista_01 = ""
default pista_02 = ""

default fecha_ingresada = ""
default error_fecha = ""

# =========================
# S01 - PORTADA
# =========================

label S01:

    scene bg portada at fondo_completo
    with fade

    call screen portada_historia

    jump S02
# =========================
# S02 - LA CARTA
# =========================

label S02:

    scene bg carta at fondo_completo
    with fade

    n "Después de varios años lejos del pueblo, Daniel recibe una carta inesperada."

    n "La carta está firmada por Elena, una amiga de su infancia."

    call screen carta_historia

    d "¿El 17 de octubre de 2014?"

    d "¿Por qué no consigo recordar nada de aquel día?"

    n "Intrigado por el mensaje, Daniel decide regresar."

    jump S03

# =========================
# S03 - LA PLAZA
# =========================

label S03:

    scene bg plaza at fondo_completo
    with fade

    n "Daniel llega a la plaza del pueblo."

    n "Las calles están cubiertas por una extraña niebla."

    n "Todo parece familiar, pero algo ha cambiado."

    d "Es como si el tiempo se hubiera detenido."

    e "Daniel... sabía que vendrías."

    d "Elena, ¿qué ocurrió aquel día?"

    e "Hay cosas que no puedo recordar. Pero creo que podemos encontrar respuestas."

    n "Daniel debe decidir cómo comenzar su investigación."

    menu:

        "Revisar el archivo municipal":

            $ decision_01 = "archivo"

            jump S04A

        "Seguir a Elena":

            $ decision_01 = "elena"

            jump S04B

label S04A:

    scene bg archivo at fondo_completo
    with fade

    n "Daniel entra al archivo municipal."

    n "Entre los documentos antiguos encuentra una ficha que llama su atención."

    scene objeto ficha at fondo_completo
    with dissolve

    d "¿Una campana?"

    d "Espera... esa firma parece ser la mía."

    $ pista_01 = "ficha"

    n "Has obtenido una pista: ficha con una firma y el dibujo de una campana."

    jump S05

label S04B:

    scene bg calle at fondo_completo
    with fade

    n "Daniel sigue a Elena por las calles del pueblo."

    e "Encontré algo que necesitas ver."

    scene objeto fotografia at fondo_completo
    with dissolve

    d "¿Somos nosotros?"

    e "Sí. Pero no consigo recordar cuándo fue tomada."

    d "Ese edificio parece ser el archivo municipal."

    $ pista_01 = "fotografia"

    n "Has obtenido una pista: una fotografía antigua de Daniel y Elena."

    jump S05


label S05:

    scene bg pasillo at fondo_completo
    with fade

    n "Continuará..."

    return