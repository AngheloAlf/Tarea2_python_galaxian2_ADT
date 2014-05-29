import pygame
from pygame.locals import *
from sys import exit
from random import choice, randrange
from configuracion import *
from constantes import *
from utilidades import *

# Se importan las funciones del modulo funciones.py 
from funciones import (mover_jugador, disparar, mover_proyectiles, constatar_impacto , mover_enemigo, actualizar_mapa)
# Se inicializan los modulos de pygame.
pygame.init()

# Se crea la ventana de juego.
ventana = pygame.display.set_mode((630, 600))
pygame.display.set_caption(TITULO_VENTANA)

# Creacion de superficies.
superficie_muralla = pygame.Surface((630, 600))
superficie_muralla.fill(NEGRO)
superficie_muralla.set_colorkey(NEGRO)

# Se cargan los graficos del juego.
fondo_mapa          = pygame.image.load("img/"+FONDO_MAPA).convert()
imagen_inicio       = pygame.image.load("img/"+IMAGEN_INICIAR_JUEGO).convert_alpha()
imagen_fin_gana     = pygame.image.load("img/"+IMAGEN_FIN_GANA).convert_alpha()
imagen_fin_pierde   = pygame.image.load("img/"+IMAGEN_FIN_PIERDE).convert_alpha()
imagen_proyectil    = pygame.image.load("img/"+IMAGEN_PROYECTIL).convert_alpha()
imagen_muralla      = pygame.image.load("img/"+IMAGEN_MURALLA).convert()
imagen_escudo       = pygame.image.load("img/"+IMAGEN_ESCUDO).convert_alpha()
imagen_reloj        = pygame.image.load("img/"+IMAGEN_RELOJ).convert_alpha()
imagen_jugador      = pygame.image.load("img/"+IMAGEN_NAVE_JUGADOR).convert_alpha()
imagen_enemigo      = pygame.image.load("img/"+IMAGEN_NAVE_ENEMIGO).convert_alpha()
imagen_explosion    = pygame.image.load("img/"+IMAGEN_EXPLOSION).convert_alpha()
imagen_navemadre    = pygame.image.load("img/"+IMAGEN_NAVE_MADRE).convert_alpha()
imagen_navenivel1   = pygame.image.load("img/"+IMAGEN_NAVE_NIVEL1).convert_alpha()
imagen_navenivel2   = pygame.image.load("img/"+IMAGEN_NAVE_NIVEL2).convert_alpha()

# Imagenes de los potenciadores.
imagen_potenciador = {
"escudo": pygame.image.load("img/"+IMAGEN_POTENCIADOR_ESCUDO).convert_alpha(),
"municion": pygame.image.load("img/"+IMAGEN_POTENCIADOR_MUNICION).convert_alpha()
}

# Se obtienen las imagenes de jugador y de los enemigos en distintas orientaciones.
imagen_jugador = {
'N': imagen_jugador,
'E': pygame.transform.rotate(imagen_jugador, 0),
'S': pygame.transform.rotate(imagen_jugador, 0),
'O': pygame.transform.rotate(imagen_jugador, 0)
}
imagen_enemigo = {
'N': imagen_enemigo,
'E': pygame.transform.rotate(imagen_enemigo, 0),
'S': pygame.transform.rotate(imagen_enemigo, 0),
'O': pygame.transform.rotate(imagen_enemigo, 0)
}

# Se cargan las fuentes de escritura.
fuente_de_texto         = pygame.font.Font("fuentes/PressStart2P.ttf", 11)
fuente_de_texto_grande  = pygame.font.Font("fuentes/PressStart2P.ttf", 14)

# Se carga el audio del juego.
musica_fondo        = pygame.mixer.Sound("audio/"+MUSICA_FONDO)
sonido_disparo      = pygame.mixer.Sound("audio/"+SONIDO_DISPARO)
sonido_impacto      = pygame.mixer.Sound("audio/"+SONIDO_IMPACTO)
sonido_fin_gana     = pygame.mixer.Sound("audio/"+SONIDO_FIN_GANA)
sonido_fin_pierde   = pygame.mixer.Sound("audio/"+SONIDO_FIN_PIERDE)
sonido_potenciador  = pygame.mixer.Sound("audio/"+SONIDO_POTENCIADOR)

# Se crea el mapa de juego.
posiciones_naves, bloques_muralla,posiciones_naves_madres,posiciones_naves_nivel1,posiciones_naves_nivel2 = crear_mapa(MAPA, superficie_muralla, imagen_muralla)

# Se crea la lista de naves presentes en el mapa.
jugador, enemigos = crear_lista_naves(posiciones_naves,posiciones_naves_madres,posiciones_naves_nivel1,posiciones_naves_nivel2)

# Se crea un conjunto vacio de proyectiles.
proyectiles = set()

# Se renderizan los textos que aparecen en el hud.
texto_escudo        = fuente_de_texto.render("Vidas", True, BLANCO)
texto_municion      = fuente_de_texto.render("Municion", True, BLANCO)
texto_tiempo        = fuente_de_texto.render("Tiempo", True, BLANCO)
#texto_n_municion    = fuente_de_texto_grande.render("{0}".format(MUNICION_JUGADOR), True, BLANCO)
texto_n_escudo      = fuente_de_texto_grande.render("{0}".format(jugador["escudo"]), True, BLANCO)
texto_n_tiempo      = fuente_de_texto_grande.render("00:00", True, BLANCO)
texto_progra        = fuente_de_texto.render("Programacion", True, BLANCO)
texto_utfsm         = fuente_de_texto.render("UTFSM", True, BLANCO)
texto_nivel         = fuente_de_texto.render("Nivel", True, BLANCO)
juego               = True
nivel               = 1

while juego:
    texto_n_municion    = fuente_de_texto_grande.render("{0}".format(MUNICION_JUGADOR), True, BLANCO)
    texto_n_nivel   = fuente_de_texto.render(str(nivel), True, BLANCO)

    # Se crea el mapa de juego.
    posiciones_naves, bloques_muralla,posiciones_naves_madres,posiciones_naves_nivel1,posiciones_naves_nivel2 = crear_mapa(actualizar_mapa(nivel), superficie_muralla, imagen_muralla)

    # Se crea la lista de naves presentes en el mapa.
    jugador, enemigos = crear_lista_naves(posiciones_naves,posiciones_naves_madres,posiciones_naves_nivel1,posiciones_naves_nivel2)

    # Se crea un conjunto vacio de proyectiles.
    proyectiles = set()

    # Se dibuja el hud.
    superficie_muralla.blit(texto_nivel, (480,580))
    superficie_muralla.blit(texto_tiempo, (20, 10))
    superficie_muralla.blit(texto_n_tiempo, (100, 10))
    superficie_muralla.blit(texto_municion, (450, 10))
    superficie_muralla.blit(imagen_proyectil, (20, 150))
    superficie_muralla.blit(superficie_muralla, (0, 0))
    superficie_muralla.blit(texto_progra, (10, 580))
    superficie_muralla.blit(texto_utfsm, (150, 580))
    #superficie_muralla.blit(texto_n_municion, (550, 10))

    # Se dibujan todos los elementos del juego en la pantalla.
    ventana.blit(fondo_mapa, (0, 0))
    ventana.blit(superficie_muralla, (0, 0))
    dibujar_enemigos(ventana, enemigos, imagen_enemigo,imagen_navemadre,imagen_navenivel1,imagen_navenivel2)
    dibujar_proyectiles(ventana, proyectiles, imagen_proyectil)
    dibujar_jugador(ventana, jugador, imagen_jugador)

    # Se dibuja el mensaje de comienzo del juego.
    ventana.blit(imagen_inicio, (0, 0))

    # Se refresca la pantalla.
    pygame.display.flip()

    # Definicion de eventos.
    MOVIMIENTO              = USEREVENT + 1
    MOVIMIENTO_ENEMIGOS     = USEREVENT + 2
    RETIRADA                = USEREVENT + 3
    PERSECUCION             = USEREVENT + 4
    MOVIMIENTO_PROYECTILES  = USEREVENT + 5
    RESPAWN                 = USEREVENT + 6
    POTENCIADOR             = USEREVENT + 7

    # Se establecen los tipos de eventos que maneja el juego.
    eventos_permitidos = [QUIT, KEYDOWN, KEYUP, RETIRADA, PERSECUCION,
                          MOVIMIENTO, MOVIMIENTO_ENEMIGOS, MOVIMIENTO_PROYECTILES]

    if MODO_SINFIN:
        eventos_permitidos.append(RESPAWN)

    pygame.event.set_allowed(eventos_permitidos)

    # Definicion de periodos para los eventos.
    TIEMPO_RETIRADA             = (6 - NIVEL_JUEGO) * 1000
    TIEMPO_PERSECUCION          = NIVEL_JUEGO * 1000
    PERIODO_JUGADOR             = 125
    PERIODO_ENEMIGOS            = int((1.2 - 0.2 * NIVEL_JUEGO) * 1000)
    PERIODO_PROYECTILES         = 50
    PERIODO_RESPAWN             = (6 - NIVEL_JUEGO) * 1000
    PERIODO_POTENCIADOR         *= 1000

    # Variables de juego.
    activo              = True
    victoria            = False
    persecucion         = False
    direcciones         = list()
    destinos            = posiciones_naves[1:]
    posiciones_enemigos = list()
    potenciador         = None
    FPS_MAX             = 30
    tiempo              = 0.0
    minutos             = 0
    contadorjugadas     = 0
    
    # Se espera hasta que el usuario presione la tecla Enter para comenzar.
    esperando_tecla = True
    while esperando_tecla:
        for event in pygame.event.get():
            if event.type == QUIT:
                exit()
            elif event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    exit()
                elif event.key == K_RETURN:
                    esperando_tecla = False
                    break

    # Se reproduce la melodia principal.
    if PERMITIR_SONIDO:
        musica_fondo.play(-1)

    # Se da inicio a los temporizadores de eventos.
    pygame.time.set_timer(MOVIMIENTO_ENEMIGOS, PERIODO_ENEMIGOS)
    pygame.time.set_timer(MOVIMIENTO_PROYECTILES, PERIODO_PROYECTILES)

    if MODO_SINFIN:
        pygame.time.set_timer(RESPAWN, PERIODO_RESPAWN)

    tiempo = -0.99 * pygame.time.get_ticks()
    tiempo = 0.0
    minutos = 0

    # Se instancia el reloj del juego.
    reloj = pygame.time.Clock()

    while activo:
        # Se limita el numero de cuadros por segundo y se cuenta el tiempo entre cada cuadro.
        tiempo += reloj.tick(FPS_MAX)

        # Se actualiza el titulo de la ventana.
        pygame.display.set_caption("{0} | FPS: {1}".format(TITULO_VENTANA, int(reloj.get_fps())))

        # Se calcula la cantidad de segundos transcurridos.
        segundos = int(tiempo / 1000)

        # Se ajustan las variables de tiempo.
        if segundos == 60:
            minutos += 1
            segundos = 0
            tiempo = tiempo % 60

        # Se renderiza el texto que muestra el tiempo transcurrido.
        texto_n_tiempo = fuente_de_texto_grande.render("{0:02}:{1:02}".format(minutos, segundos), True, BLANCO)

        # Se refrezca el fondo del mapa y se dibujan sobre el las murallas.

        ventana.blit(fondo_mapa, (0, 0))
        ventana.blit(superficie_muralla, (0, 0))

        dibujado_enemigos = False
        dibujado_proyectiles = False

        # Manejo de eventos de entradas del usuario y comportamientos de los naves enemigos.
        for event in pygame.event.get([QUIT, KEYDOWN, KEYUP, RETIRADA, PERSECUCION]):
            if event.type == QUIT:
                exit()
            elif event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    exit()

                elif event.key == K_RIGHT:
                    if 'E' not in direcciones:
                        direcciones.append('E')
                        jugador = cambiar_orientacion(jugador, 'E')
                        pygame.time.set_timer(MOVIMIENTO, PERIODO_JUGADOR)

                elif event.key == K_LEFT:
                    if 'O' not in direcciones:
                        jugador = cambiar_orientacion(jugador, 'O')
                        direcciones.append('O')
                        pygame.time.set_timer(MOVIMIENTO, PERIODO_JUGADOR)
                elif event.key == K_SPACE:
                    if jugador["municion"] > 0:
                        if PERMITIR_SONIDO:
                            sonido_disparo.play()
                        proyectiles = disparar(jugador, proyectiles)
                        texto_n_municion = fuente_de_texto_grande.render("{0}".format(jugador["municion"]), True, BLANCO)

            elif event.type == KEYUP:
                if event.key == K_UP:
                    if 'N' in direcciones:
                        direcciones.remove('N')
                elif event.key == K_RIGHT:
                    if 'E' in direcciones:
                        direcciones.remove('E')
                elif event.key == K_DOWN:
                    if 'S' in direcciones:
                        direcciones.remove('S')
                elif event.key == K_LEFT:
                    if 'O' in direcciones:
                        direcciones.remove('O')

        # Manejo del evento movimiento de proyectiles.
        for event in pygame.event.get(MOVIMIENTO_PROYECTILES):
            if event.type == MOVIMIENTO_PROYECTILES:
                proyectiles = mover_proyectiles(proyectiles )

            # Contatar impactos (se debe hacer tanto para el mov. de proyectiles como
            # para el mov. de enemigos).
            escudo_antes = jugador["escudo"]
            jugador, enemigos, proyectiles = constatar_impacto(jugador, enemigos, proyectiles,ventana,imagen_explosion)

            # Se revisa si el jugador ha perdido cada vez que su escudo disminuye.
            if jugador["escudo"] != escudo_antes:
                if PERMITIR_SONIDO:
                    sonido_impacto.play()

                if jugador_pierde(jugador):
                    victoria = False
                    activo = False
                    texto_n_escudo = fuente_de_texto_grande.render("0", True, BLANCO)
                    juego=False
                else:
                    texto_n_escudo = fuente_de_texto_grande.render("{0}".format(jugador["escudo"]), True, BLANCO)

            # Se revisa si el jugador gana (solo con modo "sin fin" desactivado).
            if (not MODO_SINFIN) and jugador_gana(enemigos):
                victoria = True
                activo = False

        # Manejo de eventos de movimiento del jugador y de los enemigos.
        for event in pygame.event.get([MOVIMIENTO, MOVIMIENTO_ENEMIGOS]):
            if event.type == MOVIMIENTO:
                if len(direcciones) > 0:
                    jugador = mover_jugador(jugador, direcciones[-1])

                    # Si el jugador se posiciona sobre un potenciador, se activa su efecto y desaparece.
                    if potenciador != None and obtiene_potenciador(jugador, potenciador):
                        jugador = activar_potenciador(jugador, potenciador)
                        if PERMITIR_SONIDO:
                            sonido_potenciador.play()
                        potenciador = None
                        texto_n_escudo = fuente_de_texto_grande.render("{0}".format(jugador["escudo"]), True, BLANCO)
                        texto_n_municion = fuente_de_texto_grande.render("{0}".format(jugador["municion"]), True, BLANCO)
                else:
                    pygame.time.set_timer(MOVIMIENTO, 0)

            elif event.type == MOVIMIENTO_ENEMIGOS:
                contadorjugadas+=1

                posiciones_enemigos = obtener_lista_posiciones(enemigos)
                for i in range(len(enemigos)):
                    enemigos[i] = mover_enemigo(enemigos[i],contadorjugadas)
                    posiciones_enemigos[i] = enemigos[i]["posicion"]

                # Se dibujan los enemigos en pantalla.
                dibujado_enemigos = True
                dibujar_enemigos(ventana, enemigos, imagen_enemigo,imagen_navemadre,imagen_navenivel1,imagen_navenivel2)

            # Contatar impactos (se debe hacer tanto para el mov. de proyectiles como
            # para el mov. de enemigos).
            escudo_antes = jugador["escudo"]
            jugador, enemigos, proyectiles = constatar_impacto(jugador, enemigos, proyectiles,ventana,imagen_explosion)

            # Se revisa si el jugador ha perdido cada vez que su escudo disminuye.
            if jugador["escudo"] != escudo_antes:
                if PERMITIR_SONIDO:
                    sonido_impacto.play()

                if jugador_pierde(jugador):
                    victoria = False
                    activo = False
                    texto_n_escudo = fuente_de_texto_grande.render("0", True, BLANCO)
                    juego=False
                else:
                    texto_n_escudo = fuente_de_texto_grande.render("{0}".format(jugador["escudo"]), True, BLANCO)

            # Se revisa si el jugador gana (solo con modo "sin fin" desactivado).
            if jugador_gana(enemigos):
                victoria = True
                activo = False
                nivel+=1
            if jugador["municion"]==0:
                victoria = False
                activo = False
                juego=False
            for i in range(len(enemigos)):

                    if (enemigos[i]["posicion"][1])>510:
                        victoria = False
                        activo = False
        # Se dibuja en la pantalla.

        superficie_muralla.fill(NEGRO)
        superficie_muralla.blit(superficie_muralla, (0, 0))
        superficie_muralla.blit(texto_municion, (450, 10))
        superficie_muralla.blit(texto_progra, (10, 580))
        superficie_muralla.blit(texto_utfsm, (150, 580))
        superficie_muralla.blit(texto_n_municion, (550, 10))
        superficie_muralla.blit(texto_tiempo, (20, 10))
        superficie_muralla.blit(texto_n_tiempo, (100, 10))
        superficie_muralla.blit(texto_nivel, (480,580))
        superficie_muralla.blit(texto_n_nivel, (550,580))
        ventana.blit(superficie_muralla, (630, 0))

        if potenciador != None:
            dibujar_potenciador(ventana, potenciador, imagen_potenciador)
        dibujar_proyectiles(ventana, proyectiles, imagen_proyectil)
        dibujar_enemigos(ventana, enemigos, imagen_enemigo,imagen_navemadre,imagen_navenivel1,imagen_navenivel2 )
        dibujar_jugador(ventana, jugador, imagen_jugador)

        # Se refrezca la pantalla.
        pygame.display.flip()

    # Se crea una imagen con la ultima jugada en el directorio de main.py.
    pygame.image.save(ventana, "ultima_jugada.png")

    # Se detiene la musica de fondo.
    if PERMITIR_SONIDO:
        musica_fondo.stop()

    # Se exhiben imagenes y sonidos distintos dependiendo de si
    # el jugador ha salido victorioso.
    if victoria:
        if PERMITIR_SONIDO:
            sonido_fin_gana.play()
        ventana.blit(imagen_fin_gana, (0, 0))
    else:
        if PERMITIR_SONIDO:
            sonido_fin_pierde.play()
        ventana.blit(imagen_fin_pierde, (0, 0))
        juego=False

    # Se refrezca la pantalla con los nuevos graficos dibujados.
    pygame.display.flip()

    # Se espera a que el usuario presione la tecla Enter para salir.
    esperando_tecla = True
    while esperando_tecla:
        for event in pygame.event.get():
            if event.type == QUIT:
                exit()
            elif event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    exit()
                elif event.key == K_RETURN:
                    esperando_tecla = False

# Se finalizan los modulos de pygame.
pygame.quit()


