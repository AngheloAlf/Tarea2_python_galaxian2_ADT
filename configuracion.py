#
# Titulo de la ventana.
TITULO_VENTANA = "Galaxian pygame"

# Mapa de juego.
MAPA= 'mapa.txt'


FPS_MAX= 30
# Fondo de pantalla: png o jpeg (800 x 600)
FONDO_MAPA = "fondo.jpg"

# Imagen de inicio y fin del juego.
IMAGEN_INICIAR_JUEGO = "iniciar.png"
IMAGEN_FIN_GANA = "fin_gana.png"
IMAGEN_FIN_PIERDE = "fin_pierde.png"

# Imagenes de naves.
IMAGEN_NAVE_NIVEL2			= 'nave5.png'
IMAGEN_NAVE_NIVEL1			= 'nave4.png'
IMAGEN_NAVE_MADRE			= 'nave2.png'
IMAGEN_EXPLOSION			= "explosion.png"
IMAGEN_NAVE_JUGADOR 		= "nave.png"
IMAGEN_NAVE_ENEMIGO 		= "enemigo.png"
IMAGEN_PROYECTIL 			= "bala.png"
IMAGEN_MURALLA 				= "muralla.png"
IMAGEN_ESCUDO 				= "escudo.png"
IMAGEN_RELOJ				= "reloj.png"
IMAGEN_POTENCIADOR_ESCUDO	= "caja_escudo.png"
IMAGEN_POTENCIADOR_MUNICION	= "caja_municion.png"

# Audio.
MUSICA_FONDO		= "batalla.wav"
SONIDO_DISPARO		= "dis3.wav"
SONIDO_IMPACTO		= "impacto.wav"
SONIDO_FIN_GANA		= "VIC-TORIA.wav"
SONIDO_FIN_PIERDE	= "PERDER.wav"
SONIDO_POTENCIADOR	= "potenciador.wav"

SONIDO_NAVE_MADRE	= "nave_madre.wav"
SONIDO_NAVE_NIVEL2	= "nave_nivel2.wav"
SONIDO_NAVE_NIVEL1 	= "nave_nivel1.wav"
SONIDO_NAVE_ENEMIGA	= "nave_enemiga.wav"
 
# Orientacion inicial, cantidad de escudo y municion maxima del jugador.
ORIENTACION_INICIAL_JUGADOR = 'N'
ESCUDO_JUGADOR = 9
MUNICION_JUGADOR = 150

# Orientacion inicial y cantidad de escudo de los enemigos.
ORIENTACION_INICIAL_ENEMIGOS = 'S'
ESCUDO_ENEMIGOS = 1
ESCUDO_ENEMIGOS_MADRE=4
ESCUDO_ENEMIGOS_NIVEL1=2
ESCUDO_ENEMIGOS_NIVEL2=3

# Nivel del juego (1 a 5).
NIVEL_JUEGO = 4

# Activar/Desactivar el sonido.
PERMITIR_SONIDO = True

# Activar/Desactivar el modo "sin fin".
MODO_SINFIN = True

# Controla cada cuanto tiempo aparece un potenciador (en segundos).##Esto no se usa xD
PERIODO_POTENCIADOR = 10

#Se pregunta si quiere que los enemigos disparen
enemigos_disparan=True

#configura si los proyectiles, al chocar el uno con el otro, se destruyen
proyectiles_explotan=False

#Permite la rotacion del jugador
permitir_rotacion=True

#Posibilita el disparo en diagonal (no funciona si permitir rotacion es False)
permitir_diagonales=True

#Deja al jugador moverse hacia arriba y abajo
movimiento_arriba_abajo=True
#Quita las barreras de movimiento hacia arriba(solo funciona con movimiento_arriba_abajo=True)
movimiento_libre=False
#Quita todas las barreras de movimiento (requiere las 2 variables anteriores en True)
movimiento_completamente_libre=False

#Activa el puntaje
permitir_puntaje=True

#Activa o desactiva el potenciador (no funciona bien sin permitir_puntaje activado)
permitir_potenciador=True