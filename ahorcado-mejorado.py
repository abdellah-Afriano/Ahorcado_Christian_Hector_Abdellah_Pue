# import palabra_aleatoria as palabra
# import Ranking
import time

class Ranking:
    def puntuar(tiempo):
        pass


def seleccionarPalabras():
    return 'ecuatorial'




class Ahorcado:
    def __solicitarLetra(self):
        pass
    def __mostrarCadalso(self,contadorErrores):
        puppet = '''
        +---+
        |   |
            |
            |
            |
            |
        =========''', '''
        +---+
        |   |
        O   |
            |
            |
            |
        =========''', '''
        +---+
        |   |
        O   |
        |   |
            |
            |
        =========''', '''
        +---+
        |   |
        O   |
       /|   |
            |
            |
        =========''', '''
        +---+
        |   |
        O   |
       /|\  |
            |
            |
        =========''', '''
        +---+
        |   |
        O   |
       /|\  |
       /    |
            |
        =========''', '''
        +---+
        |   |
        O   |
       /|\  |
       / \  |
            |
        =========''' 
        print(puppet[contadorErrores])

    def __mostrarPalabra(self,letras):
        print('\n', ''.join([ ' _' if not letra  else ' ' + letra for letra in letras ]))

    def __dibujarTablero(self, letras, contadorErrores=0):
        ''' Dibuja el tablero, es decir una secuencia con rayas o letras acertadas, así como el monigte ahorcado
            recibe: 
                - la lista de letras acertadas y 
                - el número de intentos erroneos
        '''
        self.__mostrarPalabra(letras)
        if contadorErrores > 0:
            self.__mostrarCadalso(contadorErrores - 1)

    def __solicitarLetra(self):
        abc = [ letra for letra in 'abcçdefghijklmnñopqrstuvwxyz+']
        entrada = None
        while entrada not in abc:
            entrada = input('Introduzca su jugada --> ').lower()
        return entrada

    def jugarAhorcado():

        aho = Ahorcado()
        ESCAPE = '+'

        print('Bienvenido al cadalso\nDispones de 7 oportunidades para adivinar la palabra que te perdonará la vida.\nNo las desperdicies!')

#        palabraSeleccionada = palabra()
        palabraSeleccionada = seleccionarPalabras()

        display = ['' for l in palabraSeleccionada]
        palabraCompleta = False
        ahorcado = False
        errores = 0
        aho.__dibujarTablero(display, errores)
        tiempo = time.time_ns()
        while (not palabraCompleta) and (not ahorcado):
            letraJugada = aho.__solicitarLetra()
            if letraJugada == ESCAPE:
                break
            # analizar jugada
            if letraJugada in display:
                errores += 1
            else:
                ocurrencias = palabraSeleccionada.count(letraJugada)
                inicio = 0
                if ocurrencias > 0:
                    for n in range(ocurrencias):
                        idx = palabraSeleccionada.find(letraJugada, inicio )
                        display[idx] = letraJugada
                        inicio = idx + 1
                    pass
                else:
                    errores += 1
            aho.__dibujarTablero(display, errores)
            palabraCompleta = ''.join(display) == palabraSeleccionada
            ahorcado = errores == 7
        else:
            elapsed = time.time_ns()
            tiempoTotal = (elapsed - tiempo) 
            if not ahorcado:
                Ranking.puntuar(tiempoTotal)
                print(tiempoTotal)
            else:
                print('RIP')





#______________________________________________

if __name__ == "__main__":
    Ahorcado.jugarAhorcado()
