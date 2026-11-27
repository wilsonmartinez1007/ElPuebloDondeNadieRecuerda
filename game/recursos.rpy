# FONDOS
image bg portada = "images/fondos/portada.jpeg"
image bg carta = "images/fondos/carta.jpeg"
image bg plaza = "images/fondos/plaza.jpeg"
image bg archivo = "images/fondos/archivo.png"
image bg calle = "images/fondos/calle.png"
image bg pasillo = "images/fondos/pasillo.png"
image bg despacho = "images/fondos/despacho.png"
image bg registro = "images/fondos/registro.png"

# OBJETOS
image objeto ficha = "images/objetos/ficha.png"
image objeto fotografia = "images/objetos/fotografia.png"
image objeto libro = "images/objetos/libro.png"

# Ajustar fondos al tamaño de la pantalla
transform fondo_completo:
    xysize (config.screen_width, config.screen_height)
    fit "cover"
    align (0.5, 0.5)