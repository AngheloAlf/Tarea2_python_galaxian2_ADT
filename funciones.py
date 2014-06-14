def mover_jugador(nave_jugador, direccion):
	pos=nave_jugador['posicion']
	if 'E' in direccion:
		if pos[0]!=600:
			nave_jugador['posicion']=(pos[0] + 30,pos[1])
	elif 'O' in direccion:
		if pos[0]!=0:
			nave_jugador['posicion']=(pos[0] - 30,pos[1])
	elif 'N' in direccion:
		if pos[1]!=390:
			nave_jugador['posicion']=(pos[0],pos[1]-30)
	elif 'S' in direccion:
		if pos[1]!=540:
			nave_jugador['posicion']=(pos[0],pos[1]+30)
	return nave_jugador

def disparar(nave, proyectiles):
	nave["municion"] -= 1
	lista=((nave['posicion']),nave['tipo'],nave['orientacion'])
	proyectiles.add(lista)
	return proyectiles

def mover_proyectiles(proyectiles):
	proyectil=list(proyectiles)
	for i in proyectil:
		if i[2]=='N':
			pos_proyectil=list(i[0])
			pos_proyectil=(pos_proyectil[0],pos_proyectil[1]-30)
			proyectil_nuevo=(pos_proyectil,i[1],i[2])
			proyectiles.remove(i)
			proyectiles.add(proyectil_nuevo)
		if i[2]=='S':
			pos_proyectil=list(i[0])
			pos_proyectil=(pos_proyectil[0],pos_proyectil[1]+30)
			proyectil_nuevo=(pos_proyectil,i[1],i[2])
			proyectiles.remove(i)
			proyectiles.add(proyectil_nuevo)
		if i[2]=='E':
			pos_proyectil=list(i[0])
			pos_proyectil=(pos_proyectil[0]+30,pos_proyectil[1])
			proyectil_nuevo=(pos_proyectil,i[1],i[2])
			proyectiles.remove(i)
			proyectiles.add(proyectil_nuevo)
		if i[2]=='O':
			pos_proyectil=list(i[0])
			pos_proyectil=(pos_proyectil[0]-30,pos_proyectil[1])
			proyectil_nuevo=(pos_proyectil,i[1],i[2])
			proyectiles.remove(i)
			proyectiles.add(proyectil_nuevo)
		if i[2]=='D1':
			pos_proyectil=list(i[0])
			pos_proyectil=(pos_proyectil[0]-30,pos_proyectil[1]-30)
			proyectil_nuevo=(pos_proyectil,i[1],i[2])
			proyectiles.remove(i)
			proyectiles.add(proyectil_nuevo)
		if i[2]=='D2':
			pos_proyectil=list(i[0])
			pos_proyectil=(pos_proyectil[0]+30,pos_proyectil[1]-30)
			proyectil_nuevo=(pos_proyectil,i[1],i[2])
			proyectiles.remove(i)
			proyectiles.add(proyectil_nuevo)
	return proyectiles

def constatar_impacto(jugador, enemigos, proyectiles,superficie,imagen_explosion,puntaje):
	lista_proyectiles=list(proyectiles)
	lista_enemigos=list(enemigos)
	for i in lista_proyectiles:
		pos_proyectil=i[0]
		if pos_proyectil[1]<0:
			proyectiles.remove(i)
		for ene in lista_enemigos:
			pos_enemigo=ene['posicion']
			escudo_enemigo=ene['escudo']
			if pos_enemigo==pos_proyectil and i[1]=='J':
				proyectiles.remove(i)
				ene['escudo']-=1
				if ene['escudo']==0:
					superficie.blit(imagen_explosion,pos_enemigo)
					enemigos.remove(ene)
					if ene['tipo']=='M':
						aumentar_municion(jugador)
						puntaje+=750
					if ene['tipo']=='E':
						puntaje+=50
					if ene['tipo']=='F':
						puntaje+=250
					if ene['tipo']=='G':
						puntaje+=500
		if jugador['posicion']==pos_proyectil and i[1]!='J':
			if pos_proyectil==jugador['posicion']:
				proyectiles.remove(i)
				jugador['escudo']-=1
				print jugador['escudo']
				if jugador['escudo']==0:
					superficie.blit(imagen_explosion,jugador['posicion'])
					#del jugador
	return jugador, enemigos, proyectiles,puntaje

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
    if nivel==2 or (nivel-2)%10==0:
    	mapa='mapa2.txt'
    if nivel==3 or (nivel-3)%10==0:
    	mapa='mapa3.txt'
    if nivel==4 or (nivel-4)%10==0:
    	mapa='mapa4.txt'
    # if nivel==5 or (nivel-5)%10==0:
    # 	mapa='mapa5.txt'
    # if nivel==6 or (nivel-6)%10==0:
    # 	mapa='mapa6.txt'
    # if nivel==7 or (nivel-7)%10==0:
    # 	mapa='mapa7.txt'
    # if nivel==8 or (nivel-8)%10==0:
    # 	mapa='mapa8.txt'
    # if nivel==9 or (nivel-9)%10==0:
    # 	mapa='mapa9.txt'
    # if nivel==10 or (nivel-10)%10==0:
    # 	mapa='mapa10.txt'

    return mapa

def aumentar_municion(jugador):
	jugador['municion']+=50
	return jugador


def obtiene_potenciador(jugador,potenciador):
	if jugador['posicion']==potenciador[1]:
		return True
	return False

def activar_potenciador(jugador,potenciador,puntaje):
	if potenciador[0]=='municion':
		jugador['municion']+=25
	elif potenciador[0]=='escudo':
		jugador['escudo']+=2
	puntaje+=2000
	return jugador,puntaje

def mover_potenciador(potenciador):
	return (potenciador[0],(potenciador[1][0],potenciador[1][1]+30))

def puntos_por_municion(jugador,puntaje):
	agregar=(jugador['municion']-1)/10
	puntaje=puntaje + agregar*10
	#jugador['municion']=1
	return jugador,puntaje