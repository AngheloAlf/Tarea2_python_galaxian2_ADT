from math import sqrt
from random import choice
from configuracion import *

def crear_mapa(nombre_archivo, superficie, imagen_muralla):

	archivo = open("mapas/"+nombre_archivo, "r")

	jugador_posicionado = False

	posiciones_naves = list()
	posiciones_naves_madres=list()
	posiciones_naves_nivel1=list()
	posiciones_naves_nivel2=list()
	bloques_muralla = set()
	y = 0

	for linea in archivo:
		x = 0

		for letra in linea:
			if letra == 'X':
				superficie.blit(imagen_muralla, (x, y))
				bloques_muralla.add((x, y))
			elif letra == 'J' and not jugador_posicionado:
				posiciones_naves.insert(0, (x, y))
				jugador_posicionado = True
			elif letra == 'E':
				posiciones_naves.append((x, y))
			elif letra == 'M':
				posiciones_naves_madres.append((x, y))
			elif letra == 'F':
				posiciones_naves_nivel1.append((x, y))
			elif letra == 'G':
				posiciones_naves_nivel2.append((x, y))

			x += 30
		y += 30

	archivo.close()

	return posiciones_naves, bloques_muralla,posiciones_naves_madres,posiciones_naves_nivel1,posiciones_naves_nivel2

def distancia(origen, destino):

	x0, y0 = origen
	x1, y1 = destino

	x0, y0, x1, y1 = x0/30, y0/30, x1/30, y1/30
	return sqrt((x1 - x0)**2 + (y1 - y0)**2)

def crear_lista_naves(posiciones_naves,posiciones_naves_madres,posiciones_naves_nivel1,posiciones_naves_nivel2):

	nave_jugador = {
	"posicion": posiciones_naves[0],
	"tipo": 'J',
	"orientacion": ORIENTACION_INICIAL_JUGADOR,
	"escudo": ESCUDO_JUGADOR,
	"municion": MUNICION_JUGADOR
	}

	naves_enemigos = list()
	for posicion_enemigo in posiciones_naves[1:]:
		nave_enemigo = {
		"posicion": posicion_enemigo,
		"tipo": 'E',
		"orientacion": ORIENTACION_INICIAL_ENEMIGOS,
		"escudo": ESCUDO_ENEMIGOS,
		"municion": 999999
		}

		naves_enemigos.append(nave_enemigo)
	naves_madres = list()
	for posicion_enemigo in posiciones_naves_madres:
		nave_enemigo = {
		"posicion": posicion_enemigo,
		"tipo": 'M',
		"orientacion": ORIENTACION_INICIAL_ENEMIGOS,
		"escudo": ESCUDO_ENEMIGOS_MADRE,
		"municion": 999999
		}

		naves_enemigos.append(nave_enemigo)
	naves_nivel1 = list()
	for posicion_enemigo in posiciones_naves_nivel1:
		nave_enemigo = {
		"posicion": posicion_enemigo,
		"tipo": 'F',
		"orientacion": ORIENTACION_INICIAL_ENEMIGOS,
		"escudo": ESCUDO_ENEMIGOS_NIVEL1,
		"municion": 999999
		}

		naves_enemigos.append(nave_enemigo)
	naves_nivel2 = list()
	for posicion_enemigo in posiciones_naves_nivel2:
		nave_enemigo = {
		"posicion": posicion_enemigo,
		"tipo": 'G',
		"orientacion": ORIENTACION_INICIAL_ENEMIGOS,
		"escudo": ESCUDO_ENEMIGOS_NIVEL2,
		"municion": 999999
		}

		naves_enemigos.append(nave_enemigo)

	return nave_jugador, naves_enemigos

def cambiar_orientacion(jugador, direccion):
	jugador['orientacion']=direccion
	return jugador

def obtener_lista_posiciones(enemigos):

	posiciones = []
	for enemigo in enemigos:
		posiciones.append(enemigo["posicion"])

	return posiciones





def mover(posicion, direccion):
	x, y = posicion

	if direccion == 'N':
		y -= 30

	elif direccion == 'E':
		x += 30

	elif direccion == 'S':
		y += 30

	elif direccion == 'O':
		x -= 30

	return (x, y)

def dibujar_potenciador(superficie, potenciador, imagen_powerup):
	superficie.blit(imagen_powerup[potenciador[0]], potenciador[1])

def dibujar_jugador(superficie, jugador, imagen_jugador):
	superficie.blit(imagen_jugador[jugador["orientacion"]], jugador["posicion"])

def dibujar_enemigos(superficie, enemigos, imagen_enemigo,imagen_navemadre,imagen_navenivel1,imagen_navenivel2):
	for enemigo in enemigos:
		if enemigo['tipo']=='E':
			superficie.blit(imagen_enemigo[enemigo["orientacion"]], enemigo["posicion"])
		elif enemigo['tipo']=='M':
			superficie.blit(imagen_navemadre, enemigo["posicion"])
		elif enemigo['tipo']=='F':
			superficie.blit(imagen_navenivel1, enemigo["posicion"])
		elif enemigo['tipo']=='G':
			superficie.blit(imagen_navenivel2, enemigo["posicion"])

def dibujar_proyectiles(superficie, proyectiles, imagen_proyectil):
	for proyectil in proyectiles:
		superficie.blit(imagen_proyectil, proyectil[0])

def jugador_gana(enemigos):
	return len(enemigos) == 0

def jugador_pierde(nave_jugador):
	return nave_jugador["escudo"] <= 0
	

