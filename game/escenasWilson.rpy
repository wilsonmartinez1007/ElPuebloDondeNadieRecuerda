# Personajes
define d = Character("Daniel")
define e = Character("Elena")
define n = Character(None)

# =========================
# S01 - PORTADA
# =========================

label S01:

    scene black
    with fade

    centered "EL PUEBLO DONDE NADIE RECUERDA"

    pause 2

    n "Una historia sobre recuerdos que nunca debieron desaparecer."

    n "Algunas cosas se olvidan. Otras, simplemente, nadie quiere recordar."

    jump S02

# =========================
# S02 - LA CARTA
# =========================

label S02:

    scene black
    with dissolve

    n "Daniel recibe una carta que cambiará su regreso al pueblo."

    n "La carta está firmada por Elena."

    n "En ella, hay un mensaje breve:"

    centered "Vuelve al pueblo."
    centered "Pregunta qué pasó el 17 de octubre de 2014."

    n "Daniel no recuerda qué ocurrió aquel día."

    n "Pero algo en aquella fecha le resulta inquietantemente familiar."

    jump S03