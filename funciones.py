def mover_jugador(nave_jugador, direccion):
	pos=nave_jugador['posicion']
	if 'E' in direccion:
		if pos[0]!=600:
			nave_jugador['posicion']=(pos[0] + 30,pos[1])
	elif 'O' in direccion:
		if pos[0]!=0:
			nave_jugador['posicion']=(pos[0] - 30,pos[1])
    return nave_jugador

def disparar(nave, proyectiles):
	nave["municion"] -= 1
    return proyectiles

def mover_proyectiles(proyectiles):
    return proyectiles

def constatar_impacto(jugador, enemigos, proyectiles,superficie,imagen_explosion):
    return jugador, enemigos, proyectiles

def mover_enemigo(enemigo, contadorjugadas):
	pos_ene = enemigo['posicion']
	if contadorjugadas>0 and contadorjugadas<6 and contadorjugadas%2!=0:
		enemigo['posicion']=(pos_ene[0] - 30,pos_ene[1])
	if contadorjugadas==7:
		enemigo['posicion']=(pos_ene[0],pos_ene[1]+30)
	if contadorjugadas>8 and contadorjugadas<18 and contadorjugadas%2!=0:
		enemigo['posicion']=(pos_ene[0] + 30,pos_ene[1])
	if contadorjugadas==19:
		enemigo['posicion']=(pos_ene[0],pos_ene[1]+30)
	if contadorjugadas>20 and contadorjugadas<30 and contadorjugadas%2!=0:
	 	enemigo['posicion']=(pos_ene[0] - 30,pos_ene[1])
	if contadorjugadas==31:
		enemigo['posicion']=(pos_ene[0],pos_ene[1]+30)
	if contadorjugadas>32 and contadorjugadas<42 and contadorjugadas%2!=0:
		enemigo['posicion']=(pos_ene[0] + 30,pos_ene[1])
	if contadorjugadas==43:
		enemigo['posicion']=(pos_ene[0],pos_ene[1]+30)
	if contadorjugadas>44 and contadorjugadas<54 and contadorjugadas%2!=0:
	 	enemigo['posicion']=(pos_ene[0] - 30,pos_ene[1])
	if contadorjugadas==55:
	 	enemigo['posicion']=(pos_ene[0],pos_ene[1]+30)
	if contadorjugadas>56 and contadorjugadas<66 and contadorjugadas%2!=0:
	 	enemigo['posicion']=(pos_ene[0] + 30,pos_ene[1])
	if contadorjugadas==67:
	 	enemigo['posicion']=(pos_ene[0],pos_ene[1]+30)
	if contadorjugadas>68 and contadorjugadas<78 and contadorjugadas%2!=0:
	 	enemigo['posicion']=(pos_ene[0] - 30,pos_ene[1])
	if contadorjugadas==79:
	 	enemigo['posicion']=(pos_ene[0],pos_ene[1]+30)
	if contadorjugadas>80 and contadorjugadas<90 and contadorjugadas%2!=0:
	 	enemigo['posicion']=(pos_ene[0] + 30,pos_ene[1])
	if contadorjugadas==91:
	 	enemigo['posicion']=(pos_ene[0],pos_ene[1]+30)
	if contadorjugadas>92 and contadorjugadas<102 and contadorjugadas%2!=0:
	 	enemigo['posicion']=(pos_ene[0] - 30,pos_ene[1])
	if contadorjugadas==103:
	 	enemigo['posicion']=(pos_ene[0],pos_ene[1]+30)
	if contadorjugadas>104 and contadorjugadas<114 and contadorjugadas%2!=0:
	 	enemigo['posicion']=(pos_ene[0] + 30,pos_ene[1])
	if contadorjugadas==115:
	 	enemigo['posicion']=(pos_ene[0],pos_ene[1]+30)
	if contadorjugadas>116 and contadorjugadas<126 and contadorjugadas%2!=0:
	 	enemigo['posicion']=(pos_ene[0] - 30,pos_ene[1])
	if contadorjugadas==127:
	 	enemigo['posicion']=(pos_ene[0],pos_ene[1]+30)
	if contadorjugadas>128 and contadorjugadas<138 and contadorjugadas%2!=0:
	 	enemigo['posicion']=(pos_ene[0] + 30,pos_ene[1])
	if contadorjugadas==139:
	 	enemigo['posicion']=(pos_ene[0],pos_ene[1]+30)
	if contadorjugadas>140 and contadorjugadas<150 and contadorjugadas%2!=0:
	 	enemigo['posicion']=(pos_ene[0] - 30,pos_ene[1])
	if contadorjugadas==151:
	 	enemigo['posicion']=(pos_ene[0],pos_ene[1]+30)
	if contadorjugadas>152 and contadorjugadas<162 and contadorjugadas%2!=0:
	 	enemigo['posicion']=(pos_ene[0] + 30,pos_ene[1])
	if contadorjugadas==163:
	 	enemigo['posicion']=(pos_ene[0],pos_ene[1]+30)
	if contadorjugadas>164 and contadorjugadas<174 and contadorjugadas%2!=0:
	 	enemigo['posicion']=(pos_ene[0] - 30,pos_ene[1])
	if contadorjugadas==175:
	 	enemigo['posicion']=(pos_ene[0],pos_ene[1]+30)
    return enemigo


#Bonificacion
def actualizar_mapa(nivel):
    mapa='mapa.txt'
    return mapa

def aumentar_municion(jugador):
    return jugador



