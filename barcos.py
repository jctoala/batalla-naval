TIPO_BARCO = { 'destructor': 'dd', 'acorazado': 'aaa', 'submarino': 'ssss'}
TAMANIO = 8

def ingresa_numero():
    while True:
        try:
            z = int(input(f"ingresa coordenada [0-{TAMANIO-1}]: "))
            if  0 <= z < TAMANIO:
                return z
            print(f"No has ingresado un numero entre 0 y {TAMANIO-1}. Repita el movimiento")

        except ValueError:
            print ("has ingresado un caracter. Repita el movimiento")

def ingresa_direccion():
    while True:
        z = input("ingresa horizontal o vertical (H,V): ").upper()
        if z in ('H', 'V'):
            return z
        print("invalido. Debes ingresar 'H' o 'V' ")

class JuegoBarco:
    def __init__(self):
        self.grilla = [ [' ']*TAMANIO for _ in range(TAMANIO) ]

    def mostrarGrilla(self):
        print("---------------")
        for row in self.grilla:
            print(' '.join(row))
    
    def jugada(self, x, y, direccion, barco):
        for b in TIPO_BARCO[barco]:
            self.grilla[x][y] = b
            if direccion in ('H'):
                y +=1
            elif direccion in ('V'):
                x +=1
    
    def validar_movimiento(self, x, y, direccion, barco):
        bandera = len(TIPO_BARCO[barco]) -1
        if direccion in 'H':
            bandera += y
            if 0<=bandera<=TAMANIO-1:
                for temp in range(len(TIPO_BARCO[barco])):
                    if not self.grilla[x][y] in (' '):
                        print(f"No se puede ingresar valor aqui ({x},{y})")
                        return False
                    y += 1    
                return True
            return False
        elif direccion in 'V':
            bandera += x
            if 0<=bandera<=TAMANIO-1:
                for temp in range(len(TIPO_BARCO[barco])):
                    if not self.grilla[x][y] in (' '):
                        print(f"No se puede ingresar valor aqui ({x},{y})")
                        return False
                    x += 1    
                return True
            return False
        
    def iniciarJuego(self):
        print("Ubicar los barcos")
        for barco in TIPO_BARCO:
            print(f"El barco {barco} tiene {len(TIPO_BARCO[barco])} espacios por ubicar")
            
            while True:
                print(f"Indique el inicio de la jugada para {barco}. Coordenada Horizontal")
                x = ingresa_numero()
                print(f"Indique el inicio de la jugada para {barco}. Coordenada Vertical")
                y = ingresa_numero()
                print("Indique el movimiento.")
                direccion = ingresa_direccion()

                if self.validar_movimiento(x, y, direccion, barco):
                    print("Jugada correcta")
                    self.jugada(x, y, direccion, barco)
                    self.mostrarGrilla()
                    break
                else:
                    print(f"No has ingresado una jugada valida. El {barco} no puede jugar en ({x},{y})")
                    print("Repita")
        self.mostrarGrilla()

class TableroJuego:
    def __init__(self):
        self.jugadores = []
        self.turno = 0
        self.ganador = False
    
    def ingresar_jugador(self, jugador):
        self.jugadores.append(jugador)
        print("jugador ingresado correctamente")

    def set_turno(self):
        if not self.get_ganador():
            if self.turno == 0:
                self.turno = 1
            elif self.turno == 1:
                self.turno = 0
    
    def get_turno(self):
        return self.turno

    def get_ganador(self):
        return self.ganador
    
    def set_ganador(self):
        self.ganador = True

    def comprobar_ganador(self,turno):
        grilla = self.jugadores[turno].grilla
        for row in grilla:
            for r in row:
                if not r in (' ','x'):
                    return False         
        return True

    def disparar(self, x, y):
        grilla = self.jugadores[self.get_turno()].grilla
        if not grilla[x][y] in (' '):
            grilla[x][y]='x'
            print("has dado en el blanco")
            self.mostrar_grilax(self.get_turno())
            hay_ganador = self.comprobar_ganador(self.get_turno())
            if hay_ganador:
                self.set_ganador()
        else:
            print("Al agua")
        self.set_turno()
        
    def mostrar_grilax(self, turno):
        grilla = self.jugadores[turno].grilla
        for row in grilla:
            print(' '.join(char if char == 'x' else ' ' for char in row))

    #funcion para mostrar todos los jugadores
    '''
    def mostrar_todo(self):
        for i in range(TAMANIO):
            print(f"----jugador {i}----")
            for grilla in self.jugadores[i].grilla:
                print(" ".join(grilla))
    '''


print("Se ha creado jugador 1")
jugador1 = JuegoBarco()
print("Turno jugador 1") 
jugador1.iniciarJuego()

print("Se ha creado jugador 2")
jugador2 = JuegoBarco()
print("Turno jugador 2") 
jugador2.iniciarJuego()

print("Han ingresado a jugar")
batallaNaval = TableroJuego()
print("Jugador 1 esta ingresando al juego")
batallaNaval.ingresar_jugador(jugador1)
print("Jugador 2 esta ingresando al juego")
batallaNaval.ingresar_jugador(jugador2)

print("Ahora a disparar: ")
while True:
    print(f"Turno del jugador {batallaNaval.get_turno()+1}")
    x = ingresa_numero()
    y = ingresa_numero()
    batallaNaval.disparar(x, y)
    if batallaNaval.get_ganador():
        print(f"Has ganado el juego jugador {batallaNaval.get_turno()+1}")
        break
