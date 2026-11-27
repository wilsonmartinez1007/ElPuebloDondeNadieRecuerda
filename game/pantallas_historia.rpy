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