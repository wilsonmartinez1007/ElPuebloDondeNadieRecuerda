init python:
    import re
    from datetime import date


# PERSONAJES

define d = Character("Daniel", color="#A9C9DF")
define e = Character("Elena", color="#D8C3A5")
define j = Character("Don Julián", color="#C5C9A4")
define n = Character(None)

# VARIABLES

default decision_01 = ""
default decision_02 = ""
default dia_ingresado = ""
default mes_ingresado = ""
default anio_ingresado = ""

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


# =========================
# S05 - EL PASILLO
# =========================

label S05:

    scene bg pasillo at fondo_completo
    with fade

    n "Daniel y Elena recorren un antiguo pasillo del archivo municipal."

    n "Al fondo aparece Don Julián, el bibliotecario del pueblo."

    j "No deberían estar buscando respuestas sobre aquel día."

    d "¿Por qué? ¿Qué ocurrió realmente?"

    j "Hay recuerdos que es mejor dejar enterrados."

    e "Daniel, no le hagas caso. Hay algo más que necesitas saber."

    menu:

        "Confiar en Elena":

            $ decision_02 = "elena"

            jump S06A

        "Confrontar a Don Julián":

            $ decision_02 = "julian"

            jump S06B

label S06A:

    scene bg pasillo at fondo_completo
    with dissolve

    e "Hay algo que recuerdo, aunque no consigo entenderlo."

    e "Aquella noche escuché una campana."

    e "Después apareció la niebla y todo se volvió confuso."

    d "¿Una campana? ¿De dónde provenía?"

    e "Creo que del archivo. Pero no estoy segura."

    $ pista_02 = "recuerdo_elena"

    n "Has obtenido una pista: el recuerdo fragmentado de Elena."

    jump S07

label S06B:

    scene bg despacho at fondo_completo
    with fade

    j "Si realmente quieres saber la verdad, debes empezar por esto."

    scene objeto libro at fondo_completo
    with dissolve

    n "Don Julián coloca un antiguo libro sobre el escritorio."

    d "¿Qué significa esa campana en la portada?"

    j "Es parte de una historia que este pueblo ha olvidado."

    j "Busca el registro de aquella noche. Allí encontrarás algunas respuestas."

    $ pista_02 = "libro"

    n "Has obtenido una pista: el libro antiguo."

    jump S07

# =========================
# S07 - INTRODUCIR FECHA
# =========================

label S07:

    scene bg archivo at fondo_completo
    with fade

    n "Daniel encuentra el lugar donde se conservan los registros del pueblo."

    d "Necesito encontrar el registro de aquella noche."

    jump S07_busqueda


label S07_busqueda:

    scene bg archivo at fondo_completo

    call screen buscar_fecha

    if _return == "carta":

        scene bg carta at fondo_completo
        with dissolve

        call screen carta_historia

        jump S07_busqueda

    # Validar campos vacíos
    if not dia_ingresado or not mes_ingresado or not anio_ingresado:

        $ error_fecha = "vacia"

        jump S08

    # Validar longitud del año
    if len(anio_ingresado) != 4:

        $ error_fecha = "formato"

        jump S08

    # Validar que la fecha exista
    python:
        try:
            fecha_validada = date(
                int(anio_ingresado),
                int(mes_ingresado),
                int(dia_ingresado)
            )

            fecha_ingresada = fecha_validada.strftime("%d/%m/%Y")
            fecha_valida = True

        except ValueError:
            fecha_valida = False

    if not fecha_valida:

        $ error_fecha = "invalida"

        jump S08

    # Comprobar la fecha del acontecimiento
    if fecha_ingresada != "17/10/2014":

        $ error_fecha = "incorrecta"

        jump S08

    jump S09

# =========================
# S08 - RECUPERACION
# =========================
label S08:

    if error_fecha == "vacia":

        $ mensaje_error = "Completa los campos de día, mes y año."

    elif error_fecha == "formato":

        $ mensaje_error = "El año debe contener cuatro dígitos."

    elif error_fecha == "invalida":

        $ mensaje_error = "La fecha introducida no es válida. Revisa el día, el mes y el año."

    else:

        $ mensaje_error = "No se encontró un registro para esa fecha."

    call screen error_registro(mensaje_error)

    if _return == "carta":

        scene bg carta at fondo_completo
        with dissolve

        call screen carta_historia

    jump S07_busqueda
# =========================
# S09 - REGISTRO ENCONTRADO
# =========================

label S09:

    scene bg registro at fondo_completo
    with fade

    n "Registro encontrado: 17 de octubre de 2014."

    d "Aquí está... la fecha de la carta."

    n "Daniel examina cuidadosamente las anotaciones del registro."

    d "Hay una referencia al sótano del archivo municipal."

    e "Entonces debemos buscar allí."

    n "El registro confirma la fecha y el lugar relacionados con los acontecimientos."

    n "Sin embargo, todavía queda una pregunta por resolver."

    d "¿Qué ocurrió realmente aquella noche?"

    jump s10