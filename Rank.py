#Módulo 2: Rank
#Class Ranking?
	
#	def FooPuntuar() “Transformación de tiempo a puntos”
#		rk = Ranking
#		rk.cargar
#		rk.

#	def __init__(self)
#		inicializar estructuras

#	def Cargar JSON del ranking como lista de tuplas (punt,nomb)
#	def Añadir nueva puntuación, ordenar y eliminar la última si supera len(x)
#	def Pintar el nuevo top ranking
#	def Descarga JSON con el nuevo ranking


class Ranking:
    def puntuar(tiempo):
        "Transforma el tiempo con sus condiciones de puntuacion a puntos para el ranking."
        puntuacion = 100 - ((tiempo // 30) * 10)
        if puntuacion < 0:
            puntuacion = 0
        rnk = Ranking()
        rnk.cargarJSON()
        rnk.addPuntuacion(puntuacion)
        rnk.showRanking(puntuacion)
        rnk.descargaJSON()

    def __init__(self):
        "Inicializacion de estructura de datos a usar"
        self.tops = []
        self.JSON = None

    def cargarJSON(self):
        """Cargara un archivo JSON si ya existe, sino creara uno. Se cargara como una
        lista de tuplas (puntuacion,nombre)"""
        crear_fichero("top15-ahorcado.json")
        with open("top15-ahorcado.json","r") as fichero:
            self.JSON = fichero.read()
        self.JSON = json.loads(self.JSON)
        self.tops = [(valor, clave) for clave, valor in self.JSON]
        
    def addPuntuacion(self,puntuacion):
        """Adicionamos la nueva puntuacion como tupla a la lista cargada de puntuaciones,
        ordenamos la lista y eliminamos las ultimas puntuaciones si se exceden de 
        15 tuplas."""
        nombre = input("Introduce el alias para la puntuacion: ") ##Saneamiento
        newtop = (puntuacion, nombre)
        self.tops.append(newtop)
        self.tops.sort()  #### o sorted
        if len(self.tops) > 15:
            self.tops.pop()  ####Cambiar a un slice
    
    def showRanking(self,puntuacion):
        """Dibujara el ranking de las 15 tuplas de la lista cargada."""
        print("Tu puntuacion es {}".format(puntuacion))
        print("#"*20)
        print(self.tops)

    def descargaJSON(self):
        """Volcaremos la lista de tuplas al archivo JSON, sobreescribiendolo."""
        self.JSON = [{clave : valor} for (valor, clave) in self.tops]
        with open("top15-ahorcado.json","w") as file:
            file.write(self.JSON)

    def crear_fichero(nombre_fichero):
        try:
            fichero = open(nombre_fichero,"r")
        except:
            fichero.open(nombre_fichero,"w")
        finally:
            fichero.close()