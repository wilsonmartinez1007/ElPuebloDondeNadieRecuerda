# Continuación narrativa S10-S17 para El pueblo donde nadie recuerda
# Desde el final de S09, usar: jump s10
# D01 debe asignar pista_s10 = "archivo" o pista_s10 = "elena".

define narrador_s10 = Character(None)
define daniel_s10 = Character("Daniel")
define elena_s10 = Character("Elena")
define julian_s10 = Character("Don Julián")

default pista_s10 = "archivo"
default decision_final_s10 = None
default movimiento_reducido_s10 = False

# S10 - La niebla entra
label s10:
    scene black
    narrador_s10 "La niebla cruza el marco de la puerta. Las letras tiemblan, pero ninguna desaparece."
    elena_s10 "Si la campana vuelve a sonar, la noche empezará otra vez."
    narrador_s10 "Puedes continuar o ajustar el movimiento de la escena."
    jump s10_menu

label s10_menu:
    menu:
        "Continuar":
            jump s11
        "Activar movimiento reducido" if not movimiento_reducido_s10:
            $ movimiento_reducido_s10 = True
            narrador_s10 "Movimiento reducido activado. La historia y sus textos no cambian."
            jump s10_menu
        "Desactivar movimiento reducido" if movimiento_reducido_s10:
            $ movimiento_reducido_s10 = False
            narrador_s10 "Movimiento reducido desactivado."
            jump s10_menu

# S11 - La fotografía conecta la pista con Daniel
label s11:
    scene black
    if pista_s10 == "elena":
        narrador_s10 "En el reverso de la fotografía, Elena escribió: 'Daniel y yo, frente al archivo, el verano de 2014'. La imagen muestra a Daniel junto a la puerta del sótano."
    else:
        narrador_s10 "La inicial D de la ficha coincide con el nombre de Daniel en una fotografía de los visitantes de aquel verano. El dibujo de la campana señala el sótano del archivo."
    elena_s10 "Ahora recuerdo que estabas conmigo. No entendía por qué la foto te señalaba, pero sabía que debías volver."
    narrador_s10 "La pista que elegiste apunta a Daniel y al archivo."
    menu:
        "Recordar lo ocurrido":
            jump s12

# S12 - La revelación
label s12:
    scene black
    daniel_s10 "Yo toqué la campana. Pedí que nadie recordara aquella noche."
    elena_s10 "Éramos niños. Pensaste que olvidar borraría el miedo."
    julian_s10 "La campana alcanzó a quienes estaban aquí, incluido tú. Tu familia se marchó al día siguiente; tú también olvidaste. Yo guardé el libro para evitar que la niebla volviera."
    elena_s10 "Te escribí porque la foto nos ponía a los dos junto al archivo. Necesitaba saber qué habíamos olvidado."
    narrador_s10 "La verdad puede devolver recuerdos o despertar el fenómeno."
    menu:
        "Decidir qué hacer":
            jump s13
        "Repasar las pistas":
            call repasar_pistas_s10
            jump s13

label repasar_pistas_s10:
    narrador_s10 "La carta nombra el 17 de octubre de 2014. El registro ubica el incidente en el sótano del archivo."
    if pista_s10 == "elena":
        narrador_s10 "La fotografía de Elena muestra a Daniel junto a la entrada del sótano, en el verano de 2014."
    else:
        narrador_s10 "La ficha lleva la inicial D y un dibujo de la campana con una flecha al sótano."
    narrador_s10 "Elena conserva un recuerdo incompleto. Julián confirma que la campana respondió a una petición."
    return

# S13 - D03: elegir una respuesta a la verdad
label s13:
    scene black
    narrador_s10 "La campana espera bajo el archivo. El libro conserva lo que el pueblo perdió."
    narrador_s10 "Elige qué hará Daniel. Podrás confirmar o cambiar tu elección en la siguiente pantalla."
    menu:
        "Leer el registro en voz alta. El pueblo recuperará recuerdos y afrontará la verdad.":
            $ decision_final_s10 = "verdad"
            jump s14
        "Cerrar el libro y guardar el secreto. El pueblo seguirá sin recordar; Daniel se marchará con la verdad.":
            $ decision_final_s10 = "secreto"
            jump s14
        "Escribir mi nombre en la última página. Daniel asumirá el olvido; el pueblo podría olvidarlo.":
            $ decision_final_s10 = "sacrificio"
            jump s14

# S14 - Confirmar o corregir la elección
label s14:
    scene black
    if decision_final_s10 == "verdad":
        narrador_s10 "Daniel leerá el registro en voz alta. El pueblo recuperará recuerdos y deberá afrontar la verdad. ¿Confirmas esta decisión?"
        menu:
            "Confirmar: leer el registro en voz alta":
                jump s15
            "Volver a elegir":
                jump s13
    elif decision_final_s10 == "secreto":
        narrador_s10 "Daniel cerrará el libro y guardará el secreto. El pueblo continuará sin recordar; Daniel se marchará con la verdad. ¿Confirmas esta decisión?"
        menu:
            "Confirmar: cerrar el libro y guardar el secreto":
                jump s16
            "Volver a elegir":
                jump s13
    elif decision_final_s10 == "sacrificio":
        narrador_s10 "Daniel escribirá su nombre para detener la niebla. El pueblo podría olvidarlo y él quedará en el archivo. ¿Confirmas esta decisión?"
        menu:
            "Confirmar: escribir mi nombre":
                jump s17
            "Volver a elegir":
                jump s13
    else:
        jump s13

# S15 - F01: la verdad compartida
label s15:
    scene black
    narrador_s10 "Daniel lee el registro en voz alta. La campana suena una sola vez."
    narrador_s10 "Los habitantes recuerdan la noche del 17 de octubre de 2014: el miedo, la niebla y al niño que pidió olvidar."
    elena_s10 "No teníamos que cargar esto a solas."
    narrador_s10 "El pueblo recupera sus recuerdos. La verdad duele, pero ya puede compartirse."
    narrador_s10 "Fin: el pueblo recuerda."
    jump menu_final_s10

# S16 - F02: el secreto permanece
label s16:
    scene black
    narrador_s10 "Daniel cierra el libro. La campana calla y la niebla retrocede."
    narrador_s10 "El pueblo seguirá sin recordar aquella noche. Daniel se marcha sabiendo lo ocurrido y por qué Elena lo llamó."
    narrador_s10 "La verdad permanece con él, mientras la vida del pueblo continúa."
    narrador_s10 "Fin: el secreto permanece."
    jump menu_final_s10

# S17 - F03: el nuevo olvidado
label s17:
    scene black
    narrador_s10 "Daniel escribe su nombre en la última página. La campana calla."
    elena_s10 "Daniel, no te voy a olvidar."
    narrador_s10 "Al salir, ella lo mira sin reconocerlo. Él permanece en el archivo; el pueblo puede seguir viviendo, aunque ya no recuerde quién lo protegió."
    narrador_s10 "Fin: Daniel queda atrapado en el misterio."
    jump menu_final_s10

label menu_final_s10:
    menu:
        "Volver al título":
            $ pista_s10 = "archivo"
            $ decision_final_s10 = None
            $ movimiento_reducido_s10 = False
            jump start