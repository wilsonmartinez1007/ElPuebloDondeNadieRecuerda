screen portada_historia():

    add Solid("#08101699")

    vbox:
        xpos 0.08
        yalign 0.48
        spacing 25

        text "U N A   N O V E L A   V I S U A L":
            size 20
            color "#C4A574"

        text "El pueblo donde\nnadie recuerda":
            font "fonts/Cinzel-VariableFont_wght.ttf"
            size 65
            color "#F1E5CD"
            outlines [(2, "#00000080", 0, 2)]

        text "Una historia de misterio y recuerdos olvidados.":
            size 25
            color "#D8D8D8"
            italic True

        null height 20

        textbutton "Comenzar historia":
            action Return()
            background Solid("#101820DD")
            hover_background Solid("#796344")
            padding (35, 18)
            text_color "#F1E5CD"
            text_hover_color "#FFFFFF"
            text_size 28

    text "EQUIPO 18":
        xpos 0.08
        ypos 0.92
        size 18
        color "#C4A574"


screen carta_historia():

    modal True

    add Solid("#00000055")

    frame:
        align (0.5, 0.5)
        xsize int(config.screen_width * 0.65)
        background Solid("#17130FEF")
        padding (50, 40)

        vbox:
            spacing 25
            xfill True

            text "U N A   C A R T A   I N E S P E R A D A":
                xalign 0.5
                size 20
                color "#C4A574"

            null height 15

            text "Vuelve al pueblo.":
                xalign 0.5
                font "fonts/Cinzel-VariableFont_wght.ttf"
                size 40
                italic True
                color "#F1E5CD"

            text "Pregunta qué pasó el":
                xalign 0.5
                size 30
                color "#F1E5CD"

            text "17 de octubre de 2014.":
                xalign 0.5
                font "fonts/Cinzel-VariableFont_wght.ttf"
                size 42
                color "#D9B77D"

            text "— Elena":
                xalign 0.9
                font "fonts/Cinzel-VariableFont_wght.ttf"
                italic True
                size 32
                color "#F1E5CD"

            null height 15

            textbutton "Continuar":
                xalign 0.5
                action Return()
                background Solid("#493824")
                hover_background Solid("#796344")
                padding (40, 15)
                text_color "#F1E5CD"
                text_hover_color "#FFFFFF"
                text_size 26

screen buscar_fecha():

    modal True

    add Solid("#00000088")

    frame:
        align (0.5, 0.5)
        xsize int(config.screen_width * 0.65)
        background Solid("#17130FEF")
        padding (50, 40)

        vbox:
            spacing 25
            xfill True

            text "A R C H I V O   M U N I C I P A L":
                xalign 0.5
                size 20
                color "#C4A574"

            text "El registro olvidado":
                xalign 0.5
                font "fonts/Cinzel-VariableFont_wght.ttf"
                size 48
                color "#F1E5CD"

            text "Introduce la fecha de los acontecimientos que estás investigando.":
                xalign 0.5
                text_align 0.5
                size 26
                color "#F1E5CD"

            null height 10

            text "Fecha (DD/MM/AAAA)":
                xalign 0.5
                size 23
                color "#C4A574"

            frame:
                xalign 0.5
                xsize 350
                background Solid("#30271D")
                padding (25, 18)

                input:
                    value VariableInputValue("fecha_ingresada")
                    allow "0123456789/"
                    length 10
                    size 35
                    color "#F1E5CD"
                    xalign 0.5

            null height 15

            hbox:
                xalign 0.5
                spacing 25

                textbutton "Consultar carta":
                    action Return("carta")
                    background Solid("#30271D")
                    hover_background Solid("#796344")
                    padding (25, 15)
                    text_color "#F1E5CD"
                    text_size 24

                textbutton "Buscar registro":
                    action Return("buscar")
                    background Solid("#493824")
                    hover_background Solid("#796344")
                    padding (25, 15)
                    text_color "#F1E5CD"
                    text_size 24

screen error_registro(mensaje):

    modal True

    add Solid("#00000099")

    frame:
        align (0.5, 0.5)
        xsize int(config.screen_width * 0.60)
        background Solid("#17130FEF")
        padding (50, 40)

        vbox:
            spacing 30
            xfill True

            text "BÚSQUEDA INCOMPLETA":
                xalign 0.5
                size 20
                color "#C4A574"

            text "Registro no encontrado":
                xalign 0.5
                font "fonts/Cinzel-VariableFont_wght.ttf"
                size 42
                color "#D9A38B"

            text mensaje:
                xalign 0.5
                text_align 0.5
                size 28
                color "#F1E5CD"

            text "Puedes corregir la fecha o consultar nuevamente la carta de Elena.":
                xalign 0.5
                text_align 0.5
                size 23
                color "#C9C0B2"

            hbox:
                xalign 0.5
                spacing 25

                textbutton "Corregir fecha":
                    action Return("corregir")
                    background Solid("#493824")
                    hover_background Solid("#796344")
                    padding (25, 15)
                    text_color "#F1E5CD"
                    text_size 24

                textbutton "Releer carta":
                    action Return("carta")
                    background Solid("#30271D")
                    hover_background Solid("#796344")
                    padding (25, 15)
                    text_color "#F1E5CD"
                    text_size 24