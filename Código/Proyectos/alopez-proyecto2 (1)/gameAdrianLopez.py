#proyecto taller de programacion 2.0
#Adrián López

import pygame #se importa pygame, math y json ya que son las bibliotecas q se desean usar
import math # se importa math ya que se requiere proyectar vectores para trasladar imagenes por cosenos y senos
import json # se importa json 
import random # se importa random para que los obstaculos esten de manera aleatoria en el juego

pygame.mixer.init() # Se inicia el mixer que permite la implementacion de sonido en el juego
pygame.mixer.pre_init(44100, -16, 2, 2048)


black = (0, 0, 0)# se importan una serie de colores que pueden llegar a usarse

white = (255, 255, 255)

red = (200, 0, 0)

green = (0,200,0)
fondocolor=(17,17,17)
FPS = 60

screen = pygame.display.set_mode((0,0),pygame.FULLSCREEN)#se define un tamaño de pantalla, se desea pantalla completa
background = pygame.Surface((screen.get_size()))#se define una superfice, el fondo
background.fill(white)
centro=pygame.Surface((1920,150))



inicio=0 #se definen una serie de constantes que se desean usar más adelante
color=[]     # estos valores iniciales se definen para poder ser declarados mas adelante
aceleration1=1
aceleration2=aceleration1
vueltas1=0
vueltas2=0
posbala1x=0
posbala1y=0
posbala2x=0
posbala2y=0
angulo1=0
angulo2=0
contador=0
seconds=0
clock = pygame.time.Clock() # se define un reloj
intromusic=pygame.mixer.Sound("intro.wav") # se declaran varios archivos de sonido usando el mixer que fue iniciado anteriormente
acsound=pygame.mixer.Sound("ac.wav")#sonido aceleracion
acsound.set_volume(.1) # se define un volumen a algunos sonidos
normalsound=pygame.mixer.Sound("normal.wav")#sonido manejo normal
frenosound=pygame.mixer.Sound("freno.wav")#sonido freno
choquesound=pygame.mixer.Sound("Choque.wav") # sonido choque
savebutton=pygame.image.load("guardar.png")#boton guardado
metasound=pygame.mixer.Sound("meta.wav")#sonido al pasar por la meta
metasound.set_volume(1)
hitsound=pygame.mixer.Sound("hit.wav") # sonido de disparo acertado
normalsound.set_volume(0.1)
savebutton=pygame.transform.scale(savebutton,(100,100)) # se transforma el boton de guardado a un tamaño adecuado usando el pygame.transform y escalandolo
kills1=0
kills2=0
salidas1=0
salidas2=0
contador1=0
contador2=0
time1=0
time2=0
time3=0
reloj=0
time01=0
time02=0
time03=0
time4=0
reloj1=0




mainloop=True  # condicion definida que permite que el juego sea un ciclo y se repita hasta que se salga de este y mediante actualizaciones funcione
menu=True#condición para el menú

pygame.init() # se inicia pygame

class Fondo:       #clase que define las propiedades del fondo como el menu o si hay clicks o interaciones con el mouse
    def __init__(self): #se inicializa la clase
         pass

    def menu(self):    # función que define el fondo de el menu y los recuadros de texto
        background=pygame.image.load("menufondo.png") # se carga la imagen del fondo
        background = background.convert()
        screen.blit(background, (0,0))
        pygame.draw.rect(screen,white,(700,450,1100,500)) # se dibujan varios rectangulos  que representan los botones del juego
        pygame.draw.rect(screen,black,(750,500,1100,500)) # mediante el draw de pygeme se dibujan los rectangulos
        pygame.draw.rect(screen,red,(800,550,1000,100))
        pygame.draw.rect(screen,red,(800,850,1000,100))
        pygame.draw.rect(screen,red,(800,700,1000,100))
        font1= pygame.font.SysFont("impact", 100) # se definen fuentes
        font2= pygame.font.SysFont("impact", 20)
        texto1=font1.render("Iniciar Partida", 1, white) # texto presente en los botones 
        screen.blit(texto1,(1000,540))
        texto2=font1.render("Ver puntajes", 1, white)
        screen.blit(texto2,(1000,840))
        carrofondo=pygame.image.load("lambo31.png")
        carrofondo=pygame.transform.rotate(carrofondo,40)
        screen.blit(carrofondo,(50,100))
        nombrejuego=pygame.image.load("titulopy.png")
        nombrejuego=pygame.transform.scale(nombrejuego,(1500,500))
        screen.blit(nombrejuego,(300,0))
        texto3=font2.render("Creado por Adrián López Vásquez (2018)", 1, white)
        screen.blit(texto3,(1200,1050))
        quitbutton=pygame.image.load("quitbutton.png")
        screen.blit(quitbutton,(50,600))
        texto4=font1.render("Reiniciar partida", 1, white)
        screen.blit(texto4,(1000,690))


    def click1(self): #función click para iniciar     
        if 800<mouse[0]<1800 and 550<mouse[1]<650: #rango de valores del mouse   # si el mouse se encuentra en este rango donde mouse[0] representa el eje x y mouse[y[ representa el eje y el mouse se apreta se cumplen los if y se retorna True
            if pygame.mouse.get_pressed()[0]==True: # si se da click su salida es True
                return True
        else:
            return False
    def click2(self): #función click para ver puntuación  
        if 800<mouse[0]<1800 and 850<mouse[1]<950: # rango del mouse
            if pygame.mouse.get_pressed()[0]==True: # si se presiona su salida es True
                return True
        else:
            return False

    def click3(self): #función click para salir del juego
        if 50<mouse[0]<580 and 600<mouse[1]<860: #posiciones del mouse para que la salida sea True
            return True
        else:
            return False
    def click4(self): #click para hacer back en la ventana de puntuaciones
        if 1600<mouse[0]<1900 and 550<mouse[1]<850: # posiciones del mouse para que la salida sea True
            if pygame.mouse.get_pressed()[0]==True: # si se presiona su salida es True
                return True
        else:
            return False
    def click5(self): #click para cargar partida guardada
        if 800<mouse[0]<1800 and 700<mouse[1]<800: # posiciones del mouse para que la salida sea True
            if pygame.mouse.get_pressed()[0]==True: # si se presiona su salida es True
                return True
        else:
            return False
    def click6(self): #click para cargar partida guardada
        if 1800<mouse[0]<1900 and 950<mouse[1]<1050: # posiciones del mouse para que la salida sea True
            if pygame.mouse.get_pressed()[0]==True: # si se presiona su salida es True
                return True
        else:
            return False

        
    def encontrarmayorespuntajes(self): #función que permite abrir un json y encontrar las mayores puntuaciones
        # json permite guardar un archivo .json y leer este o escribir sobre este
        # se cargo previamente un json con todas las puntuaciones de todos los jugadores y sus nombres y se debe buscar los nombres de las puntuaciones mas altas asi como de sus valores
        with open("jsonfile.json", "r") as read_file: # se abre el archivo json
            data = json.load(read_file)   # se declara el archivo json en una variable
        namelist=[]                 # lista de los nombres
        pointslist=[]            #se inicializan algunas variables   #lista de los puntos
        valor1=0
        valor2=0                #posiciones de la lista
        valor3=0
        valor4=0
        valor5=0
        nombreprimero=''        
        nombresegundo=''
        nombretercero=''
        nombrecuarto=''
        nombrequinto=''
        print(data)         
        for name in data['nombres']:    #se obtiene del json los "nombres"
            namelist+=[name]        # se concaten los valores del json en nombres en una lista
        for points in data['puntaje']:  #se obtiene del json los "puntajes"
            pointslist+=[int(points)]   # se concatenan los valores del json en puntaje en una lista

        

        primerlugar=max(pointslist)      #se obtiene el primer máximo de la lista 
        
        for i in range(0,len(pointslist)):            #se utiliza la lista de puntuaciones para obtener la posición del primer máximo
            if primerlugar==pointslist[i]:
                valor1=i                          # se obtiene la posicion del maximo
                
        nombreprimero=namelist[valor1]            # se obtiene el nombre del primer puntaje

   
        pointslist[valor1]=0                     # se debe quitar el maximo encontrado de la lista para que no vuelva a ser encontrado               
 

        segundolugar=max(pointslist)             # se obtiene el otro maximo sin contar el obtenido anteriormente

        for j in range(0,len(pointslist)-1):          #se utiliza la lista de puntuaciones quitando el primer maximo para obtener la posición del segundo maximo
            if segundolugar==pointslist[j]:
                valor2=j                          # se encuentra la posicion de este
        nombresegundo=namelist[valor2]            # se encuentra el nombre se este

        pointslist.remove(pointslist[valor2])        # al igual que en el caso anterior se deben quitar los valores actuales para que no sigan siendo leidos 
        namelist.remove(namelist[valor2])

        

        tercerlugar=max(pointslist)                    #se utiliza la lista de puntuaciones quitando el segundo máximo para obtener la posición del tercer maximo
        for k in range(0,len(pointslist)-2):
            if tercerlugar==pointslist[k]:
                valor3=k                              # se obtiene posicion y nombre del tercer mayor puntaje
        nombretercero=namelist[valor3]

        pointslist.remove(pointslist[valor3])
        namelist.remove(namelist[valor3])           
    

        cuartolugar=max(pointslist)                    #se utiliza la lista de puntuaciones quitando el tercer máximo para obtener la posición del cuarto maximo
        for n in range(0,len(pointslist)-3):
            if cuartolugar==pointslist[n]:
                valor4=n
        nombrecuarto=namelist[valor4]

        pointslist.remove(pointslist[valor4])
        namelist.remove(namelist[valor4])
        

        quintolugar=max(pointslist)                    #se utiliza la lista de puntuaciones quitando el cuarto máximo para obtener la posición quinto maximo
        for m in range(0,len(pointslist)-4):
            if quintolugar==pointslist[m]:
                valor5=m
        nombrequinto=namelist[valor5]

        pointslist.remove(pointslist[valor5])
        namelist.remove(namelist[valor5])

        #con esto se obtiene las posiciones y los valores maximos y nombres del archivo json
        return (primerlugar,segundolugar,tercerlugar,cuartolugar,quintolugar,nombreprimero,nombresegundo,nombretercero,nombrecuarto,nombrequinto) #salidas de la funcion
    # se retorna una lista para ser usada mas adelante con los valores de 0 a 4 de los nombres de los primeros y de 5 a 9 de los valores de las puntuaciones maximas
    # se usa el manejo de  listas y el json para este metodo, obteniendo posiciones, maximos y longitudes de la lista
        
                


        

        
    
back=Fondo()
angulo=0 # se declaran mas variables para ser usadas mas adelante 
bala1=False
pixelx=0
pixely=0
tiempotranscurrido1=0
tiempotranscurrido2=0
tiempotranscurrido3=0
spritegroup=pygame.sprite.Group()
spritegroup1=pygame.sprite.Group()
scorekill=0



class Carros(pygame.sprite.Sprite):  # se define una clase que permite la obtencion los carros usando parametros
    def __init__(self, width, height,image,x,y): # se inicializa la clase y se tienen como entradas  una foto, ancho, largo y la posicion a la q se quiere el objeto

        super().__init__()
        

        self.image = pygame.Surface([width, height])     # como se ve en la doncumentacion de pygame se manejan sprites y para ello se puede colocar imagenes 
        self.image = pygame.image.load(image)              # se coloca una imagen al carro del jugador
        self.image= pygame.transform.rotate(self.image,180) # se rota ya que la imagen original esta al reves de como se desea originalmente
        self.numvueltas=0
        

        self.image.convert_alpha()

        self.rect = self.image.get_rect()     # se obtiene un rectangulo de la imagen del carro que permite posteriormente la deteccion de colisiones
    
        self.x=self.rect.x+x           #se declara la posicion del rectangulo definido anteriormente con las posiciones del carro iniciales
        self.y=self.rect.y+y       
        self.angle=angulo                # como la imagen debe ser rotada se introduce un angulo
        self.factorgiro=0                   # el factor de giro permite definir el sentido del giro
        self.original = self.image.copy()
    
        
    def rotar(self): # función que detecta si se apretan las flechas o a y d para así rotar el carro
        # se utiliza de pygame la deteccion de pulsar una tecla y mediante esto se rota la imagen 
        pressedkeys = pygame.key.get_pressed()            # esta funcion de pygame permite saber cuando se apreta una tecla del teclado

        if self==player1: #si se tiene el carro del jugador 1

            if pressedkeys[pygame.K_LEFT]: # se define una constante que varia dependiendo del sentido de giro si se presionan las teclas izquierda o derecha
                self.factorgiro=1          # variable 1 si el giro es a la izquierda y -1 si es a la derecha
            if pressedkeys[pygame.K_RIGHT]:
                self.factorgiro=-1
        if self==player2: #si se tiene el carro del jugador 2
            if pressedkeys[pygame.K_a]: # se define una constante que varia dependiendo del sentido de giro si se presionan las teclas a o d
                self.factorgiro=1        # variable 1 si el giro es a la izquierda y -1 si es a la derecha
            if pressedkeys[pygame.K_d]:
                self.factorgiro=-1
            
        self.angle+=self.factorgiro*180*0.004 # se define el angulo como el sentido de rotación y factores que permiten que el giro sea más suave
        # el angulo propio se calcula multiplicando las variables anteriores
        self.factorgiro=0
           
        
        
    def avance(self,angulo,aceleration): # clase que recibe un angulo y una aceleracion y permite que el carro avance estas son calculadas anteriormente
        pressedkeys = pygame.key.get_pressed() # se utiliza esta funcion que permite la deteccion de si se pulsa la tecla deseada o no

        if self==player1: # si se tiene el carro 1
            if pressedkeys[pygame.K_DOWN] or (pressedkeys[pygame.K_UP]and pressedkeys[pygame.K_DOWN]) : #función reversa y freno
                aceleration=-0.1  # la aceleracion se va disminuyendo hasta que se hace negativa y funciona como reversa

                
                self.x+=math.sin(math.radians(angulo))*aceleration*0.6
                self.y+=math.cos(math.radians(angulo))*aceleration*0.6   # se cambian las coordenadas para desplazar el carro
                self.rect.x=self.x
                self.rect.y=self.y
                pygame.mixer.stop()    # se pausan todos los sonidos para que el sonido deseado suene mejor
                
                frenosound.play()        # el sonido antes declarado se utliza el play para reproducirlo una vez
                return(self.x,self.y)
            if pressedkeys[pygame.K_UP]: #se define que si se apreta la tecla up o w el carro va a avanzar en la direcci{on que traia este.
                self.x+=math.sin(math.radians(angulo))*aceleration*0.6 # se vale de la matemática para proyectar vectores y permitir que el carro avance en la direccion que se tenia anteriormente
                self.y+=math.cos(math.radians(angulo))*aceleration*0.6 
                aceleration+=0.0001 # si se deja la tecla up presionada se define que el carro acelere constantemente
                self.rect.x=self.x
                self.rect.y=self.y
                return(self.x,self.y)
            
            
        if self==player2: # si se tiene el carro 2
            if pressedkeys[pygame.K_s] or (pressedkeys[pygame.K_w]and pressedkeys[pygame.K_s]) :        # funcion freno y reversa
                aceleration=-0.1
                self.x+=math.sin(math.radians(angulo))*aceleration*0.6
                self.y+=math.cos(math.radians(angulo))*aceleration*0.6                #traslacion de ejes
                self.rect.x=self.x             # se mueve el rectangulo a la posicion querida
                self.rect.y=self.y
                pygame.mixer.stop()            # se para la musica para enfocar el sonido del freno
                frenosound.play()
                return(self.x,self.y)              # se retornan las posiciones del carro
        
            if pressedkeys[pygame.K_w]: # igual que en los casos anteriores
                self.x+=math.sin(math.radians(angulo))*aceleration*0.6
                self.y+=math.cos(math.radians(angulo))*aceleration*0.6
                aceleration+=0.0001    
                self.rect.x=self.x
                self.rect.y=self.y
                return(self.x,self.y)
            
            
        #aceleracion+=0.01
    def update(value):#funcion que permite actualizar la posicion del carro
        screen.blit(self.image,(self.x,self.y)) # se hace un blit y la imagen se coloca en la posicion calculada
        
    def vueltas(self): # se define con esta función la ubicación de la meta
        if self.x==range(195,500) and self.y==450 : #ubicacion de la meta
            self.numvueltas+=1 # se contabiliza cuantas veces pasa el carro por la meta
            return self.numvueltas
             
            
        
            


class Balas(pygame.sprite.Sprite): #clase que define las balas
    def __init__(self, width, height,image,x,y,angle): # se inicializa la clase pasando como entradas una imagen, altura, ancho, posicion a la que se inicializa y el angulo que determina la dirección de la bala

        super().__init__()
        self.image = pygame.Surface([width, height]) # las balas tambien son sprites que se colocan en un grupo posteriormente
        self.image = pygame.image.load(image)       # se carga una imagen 
        self.image=pygame.transform.scale(self.image,(4,5)) # se escala la imagen con el pygame y transform con un ancho de 4 y una altura de 5
        self.rect = self.image.get_rect()  # se obtiene el rectangulo a partir de la imagen cargada
        self.angulo=angle   
        self.rect.x=x
        self.rect.y=y
        self.angulo=angle # se inicializan algunas variables para las balas
        self.x=x
        self.y=y
        
    def update(self): # función que actualiza la posición de la bala
        pressedkeys = pygame.key.get_pressed() # se obtiene si las teclas se han presionado o no 

        self.x+=math.sin(math.radians(self.angulo))*3 #al igual que como se hizo en la parte anterior se obtienen las proyecciones para así seguir un nuevo sistema de coordenadas
        self.y+=math.cos(math.radians(self.angulo))*3
        self.rect = self.image.get_rect()
        self.rect.x=self.x   # se mueve la imagen a la posicion deseada en coordenadas x y y
        self.rect.y=self.y 
        return(self.x,self.y) # se retorna la posición de la bala

        
        
class Dummyvehicles(pygame.sprite.Sprite): #se define la clase que determina los movimientos de los dummy vehicles
    def __init__(self, width, height,image,x,y,pos): # se inicializa mandando usando como parametros, altura, ancho, posicion e imagen
        super().__init__()
        self.image = pygame.Surface([width, height])
        self.image = pygame.image.load(image)        # se carga una imagen a los dummy
        self.image=pygame.transform.rotate(self.image,180)
        self.rect = self.image.get_rect()  # se obtiene un rectangulo con las dimensiones de la imagen
        self.x=self.rect.x+x    # se mueve el rectangulo a las posiciones iniciales
        self.y=self.rect.y+y
        self.a=x
        self.b=y
        self.posi=pos
        self.contador=0            # contador que permite ir rotando las imagenes
        self.image1 = self.image
    def update(self): # se define una función que determina la actualización de la posición de los dummy vehicles
# los dummy se mueven en una trayectoria definida que depepende de la forma de la pista
#como cada nivel posee una pista distinta
        if nivel==0 or nivel==-1:          # para el primer nivel
            

            if self.x==self.a:        # se mueve hacia abajo hasta que sucede la proxima condicion
                self.y+=1
                if self.contador==3:
                    self.image=pygame.transform.rotate(self.image,90)   # si ya venia moviendose se rota la imagen
                    self.contador=0
            
            if self.y==700+self.posi*30:  # si la imagen llega a un y establecido la imagen se empieza a mover en x positivo
                self.x+=1
                if self.contador==0:
                    self.image=pygame.transform.rotate(self.image,90)  # se rota la imagen
                    self.contador+=1
            

            if int(self.x)==1900-self.a:    # si llega a el x establecido la imagen se mueve en y negativo
                self.y-=1
                if self.contador==1:
                    self.image=pygame.transform.rotate(self.image,90)  # se rota como si hubiera doblado
                    self.contador+=1
            
            if int(self.y)==250-self.posi*30:    # si la imagen llega al y establecido esta se mueve en x positivo hasta llegar a el x inicial y se repite el ciclo
                self.x-=1
                if self.contador==2:
                    self.image=pygame.transform.rotate(self.image,90)  # se rota la imagen
                    self.contador+=1
            # se deben definir contadores para ir rotando la imagen
        if nivel==1 or nivel==-2:        # si se esta en el nivel 1
            if self.x==self.a:   #se mueve hacia abajo en la misma linea de la x inicial hasta llegar a una y establecida
                self.y+=1
                if self.contador==7:
                    self.image=pygame.transform.rotate(self.image,90)  # se rota la imagen si ya se venia moviendo esta
                    self.contador=0    # se reinicia el contador
            
            if self.y==700+self.posi*30: # si y toma el valor mostrado la imagen se empieza a mover en x y ya no en y
                self.x+=1
                if self.contador==0 or self .contador==4:
                    self.image=pygame.transform.rotate(self.image,90) # se rota la imagen
                    self.contador+=1
                
            

            if int(self.x)==1100-self.a and self.y in range(310,1080): # la imagen se empieza a mover en y si se llega al x calculado  y se esta en el rando de y mostrado para delimitar el movimiento
                self.y-=1
                if self.contador==1:
                    self.image=pygame.transform.rotate(self.image,90) # se rota la imagen
                    self.contador+=1
            
            if int(self.y)==400+self.posi*30 and int(self.x) in range(600,1320): #Si se llega al y mostrado se mueve en x positivo la imagen hasta llegar a la siguiente condicion
                self.x+=1
                if self.contador==2:
                    self.image=pygame.transform.rotate(self.image,-90)   # se rota la imagen 
                    self.contador+=1                                   # el contador va subiendo de valor
                    
            if int(self.x)==900+self.a and self.y in range(310,1080):   # si se llega al x y se esta en el rango se mueve en y positivo
                self.y+=1
                if self.contador==3:
                    self.image=pygame.transform.rotate(self.image,-90) # se rota la imagen
                    self.contador+=1
                    
            if int(self.x)==1900-self.a :            #Se mueve en y negativo subiendo si se llega al x 1900 - posicion inicial en x de la imagen
                self.y-=1
                if self.contador==5:
                    self.image=pygame.transform.rotate(self.image,90)   # se rota la imagen
                    self.contador+=1
                    
            if int(self.y)==250-self.posi*30:   # si se esta en el y mostrado se empieza a mover enx negativo hasta cerrar el ciclo llegando a la posicion inicial
                self.x-=1
                if self.contador==6:
                    self.image=pygame.transform.rotate(self.image,90) # se ota la imagen para dar continuidad
                    self.contador+=1
                    
        if nivel==2 or nivel==-3:         # si se esta en el ultimo nivel
            if self.x==self.a:   #Inicialmente se mueve hacia abajo en linea recta hasta llegar a un y especifico
                self.y+=1
                if self.contador==5:
                    self.image=pygame.transform.rotate(self.image,90) # se rota la imagen
                    self.contador=0
            
            if self.y==750+self.posi*30: # si se llega al y mostrado se empieza a mover en x como segundo movimiento
                self.x+=1
                if self.contador==0 or self .contador==4:
                    self.image=pygame.transform.rotate(self.image,90) # se rota la imagen
                    self.contador+=1  # el contador peermite saber en que vuelta se esta
                
            

            if int(self.x)==1200-self.a and self.y in range(310,1080): # si se esta en el x y en el rango se mueve en y negativo la imagen hasta llegar a la proxima condicion
                self.y-=1
                if self.contador==1:
                    self.image=pygame.transform.rotate(self.image,90) # se rota la imagen
                    self.contador+=1
            
            if int(self.y)==500+self.posi*30 and int(self.x) in range(600,1900): #se empieza a mover en x positivo si se cumple el if
                self.x+=1
                if self.contador==2:
                    self.image=pygame.transform.rotate(self.image,-90) # se rota la imagen dando continuidad
                    self.contador+=1
                    
                    
            if int(self.x)==1900-self.a : # si se llega al x se mueve en y negativo como penultimo paso
                self.y-=1
                if self.contador==3:
                    self.image=pygame.transform.rotate(self.image,90) # se rota la imagen
                    self.contador+=1
                    
            if int(self.y)==250-self.posi*30: #si con la condicion anterior se llega al y se empieza a mover en x negativo hasta completar el ciclo
                self.x-=1
                if self.contador==4:
                    self.image=pygame.transform.rotate(self.image,90) # se rota la imagen
                    self.contador+=1
            
            
           #como se ve se toma el valor entero de las posiciones calculadas ya que si no se obtienen decimales y puede que nunca se llegue al valor con decimales
            
            
                    
               
           
             
             
                    
            
            
            
            

        self.rect=self.image.get_rect()  # se obtiene un rectangulo de la imagen para asi detectar colisiones facilmente


        self.rect.x=self.x # se mueve el rectangulo a las posiciones calculadas con el metodo
        self.rect.y=self.y # se obtiene el (x,y) de este
        

        screen.blit(self.image,(self.x,self.y)) #se hace un blit de los dummy que permite la ilusion de movimiento ya que la imagen se va moviendo pixel por pixel a un cierto valor de actualizacion lo que permite ver la fluidez de movimiento

class Obstaculos(pygame.sprite.Sprite):
    def __init__(self,image,x,y): # se inicializa mandando usando como parametros, altura, ancho, posicion e imagen
        super().__init__()

        self.image = pygame.image.load(image)
        self.image=pygame.transform.scale(self.image,(70,70)) # se vale del transform para escalar las imaganes para que tenga valores de tamaños apropiados
        self.rect = self.image.get_rect() # se obtiene un rectangulo de las imagenes cargadas con el load
        self.rect.x=x # se coloca el rectangulo en las posiciones x y y que se llaman
        self.rect.y=y
    
        
    def update(self):

        screen.blit(self.image,(self.rect.x,self.rect.y)) # se crea un metodo que actualiza los obstaculos y les hace un blit que los muestra en pantalla
       

        

     
        
        
        
        

        

player1=Carros(20, 15,"we4.png",300,420)  # se inicializan los carros de los jugadores definiendo una imagen y posicion inicial
player2=Carros(20, 15,"we5.png",335,420) # se definen algunas variables y se inicializan algunos objetos
jugadores=pygame.sprite.Group         # se añaden estos objetos a un grupo para permitir una actualizacion mas sencillas
jugadores.add(player1)
jugadores.add(player2)
carros=pygame.sprite.Group()
carros.add(player1)
bala1=Balas(4,5,"balafoto.png",0, 0 ,0)
bala2=Balas(4,5,"balafoto.png",0, 0 ,0)


dummy1=Dummyvehicles(20, 15,"we2.png",370,420,2)       # se inician los dummy se les coloca una imagen de carros y se ponen las posiciones iniciales donde se quiere que estos objetos esten
dummy2=Dummyvehicles(20, 15,"we3.png",265,420,3)
dummy3=Dummyvehicles(20, 15,"we1.png",405,420,1)
dummy_list=pygame.sprite.Group()        # como son sprites se añaden estos a un grupo para que sea mas facil su manipulacion
dummy_list.add(dummy1)                  # se añaden
dummy_list.add(dummy2)
dummy_list.add(dummy3)
nombreplayer1=''
nombreplayer2=''
pedirnombre1=True
pedirnombre2=True
input_box1 = pygame.Rect(200, 280, 1500, 200)           # se definen los rectangulos donde se pide texto
input_box2 = pygame.Rect(200, 600, 1500, 200)
active1 = False
inicio1=False
inicio2=False
active2 = False
fontnombre = pygame.font.Font(None, 280)
music1=True
nivel=0
guard=False
new=True

lista_obstaculos=pygame.sprite.Group()              # se crean un grupo para los obstaculos










while mainloop:    # se inicializa el loop principal
    font2= pygame.font.SysFont("impact", 20)
    font3= pygame.font.SysFont("impact", 50)# se inicializan algunos fonts
    font6= pygame.font.SysFont("impact", 100)# se inicializan algunos fonts
    mouse = pygame.mouse.get_pos() # se obtien la posicion del mouse
    for event in pygame.event.get(): # si se da un evento
        if event.type == pygame.quit: # si se sale de aqui se sale del loop
            mainloop = False
        if event.type == pygame.KEYDOWN: # si se presiona una tecla
            if event.key == pygame.K_ESCAPE: # si se presiona escape se sale del juego
                mainloop = False
        
    if menu==True: # se inicializa el menú
        
        acsound.stop() # se paran los sonidos que se tenian en el juego si se vuelve al menu y se estaba jugando
        player1=Carros(20, 15,"we4.png",300,420)      # se reinician las variables por si se estaba jugando y se vuelve al menu
        player2=Carros(20, 15,"we5.png",335,420)

        dummy1.kill()
        dummy2.kill()                 # se eliminan los dummy
        dummy3.kill()
                
        dummy1=Dummyvehicles(20, 15,"we2.png",370,420,2)   # se vuelven a crear
        dummy2=Dummyvehicles(20, 15,"we3.png",265,420,5)
        dummy3=Dummyvehicles(20, 15,"we1.png",405,420,1)
            
        dummy_list.add(dummy1)
        dummy_list.add(dummy2)       # se añaden al grupo
        dummy_list.add(dummy3)
        nivel=0
        puntuacion1=0
        inicio=0
        puntuacion2=0
        if music1==True:       # para que la musica de la intro solo suene una vez se define una variable y apenas se inicia la cancion se vuelve falsa esta variable
            intromusic.play()       # se usa el sonido previamente definido y se reproduce una vez
            music1=False
        back.menu()            # se llama a la clase y se cargan los rectangulos, fondo e imagenes deseadas en el menu

        if back.click1(): #como se menciono anteriormente se uso la clase Fondo para determinar las interacciones del mouse
            menu=False # se inicializa el juego
            print("HOLA")
    
        if back.click2(): # se entra a ver las puntuaciones
            menu=False          # para ello ya la variable menu es falsa
            inicio=2
        if back.click3(): # se sale del loop
            mainloop=False       # la variable es falsa por lo que no vuelve a entrar en el loop
        if back.click5():   # si se clickea se reinicia la ultima partida jugada
            guard=True       # se definn variables para entrar en estas condiciones dentro del loop principal
            menu=False
    if menu==False and guard==True:
        pygame.mixer.stop()    # se para el mixer para reiniciar los sonidos que se estaban reproduciendo

        with open("guardado.json", "r") as read_file: # se abre el archivo json
            data = json.load(read_file)  # se guarda el json en la variable data
        m=[]



        
        for t in data['var']:    #se obtiene del json los "var"
            m+=[t]  # se concatenan los valores en una lista
        player1.x=m[0]           # los valores obtenidos en el json mediante la lista son declarados como variables del juego que permite que se continue con el juego tal como estaba cuando este se guardo
        player2.x=m[1]
        player1.y=m[2]
        player2.y=m[3]
        kills1=m[4]
        kills2=m[5]
        vueltas1=m[6]
        vueltas2=m[7]
        time1=m[8]
        time2=m[9]
        time3=m[10]
        aceleration1=m[11]
        player1.angle=m[12]
        aceleration2=m[13]
        player2.angle=m[14]
        contador1=m[15]
        contador2=m[16]
        salidas1=m[17]
        salidas2=m[18]
        dummy1.x=m[19]
        dummy1.y=m[20]
        nivel=m[21]
        dummy2.x=m[22]
        dummy2.y=m[23]
        dummy3.x=m[24]
        dummy3.y=m[25]
        nombreplayer1=m[26]
        nombreplayer2=m[27]
        dummy1.contador=m[28]
        dummy2.contador=m[29]
        dummy3.contador=m[30]
        reloj1=m[31]
        tipo=m[32]
        lar=m[33]
        al=m[34]
        
        dummy1.image=pygame.transform.rotate(dummy1.image,90*(dummy1.contador))   # se giran las imagenes cierto valor de contador para que este posicionadas en la direccion correcta y se puedan reutilizar los metodos anteriores
        dummy2.image=pygame.transform.rotate(dummy2.image,90*(dummy2.contador))
        dummy3.image=pygame.transform.rotate(dummy3.image,90*(dummy3.contador))
        time4=pygame.time.get_ticks()


        if nivel==0 or nivel==-1:    # se utiliza este if para hacer que nivel tome un valor especifico
            nivel=0

        if nivel==1 or nivel==-2:
            nivel=2

        if nivel==3 or nivel==-3:
            nivel=2
        

        

        for n in range(0,len(tipo)):    # para guardar los obstaculos creados se vale de el numero calculado para definir el tipo de obstaculo
            num=tipo[n]
            if num==0:
                image="arbol1.png"
            if num==1:
                image="roca1.png"
            if num==2:
                image="roca2.png"
            x=lar[n]          # mediante el json se trae la posicion x y y del obstaculo
            y=al[n]
            obstacle=Obstaculos(image,x,y)   # se crea el objeto y se añade a la lista
            lista_obstaculos.add(obstacle)


        menu=False         # se realiza una declaracion para permitir iniciar el juego
        inicio=1
    
        new=False
        guard=False
        time5=pygame.time.get_ticks()      # se obtiene el tiempo hasta esta fase

       


       
            

    if menu==False and inicio==0: # se inicia el juego y se sale del menu, se pide el nombre del jugador
        background=pygame.image.load("menufondo.png") # se define el fondo
        background = background.convert()
        textonombre=fontnombre.render("Ingrese nombres: ", True, white)  # se coloca texto
        
        screen.blit(background,(0,0)) # se limpia el fondo para permitir la actualizacion de este
        screen.blit(textonombre, (50, 50)) 
        
        if  inicio1==False: # se entra en este ciclo para que el usuario ingrese el nombre del jugador 1
            for event1 in pygame.event.get():   
                if event1.type == pygame.MOUSEBUTTONDOWN: # si se da click en la casilla empieza a aceptar texto
                    if input_box1.collidepoint(event1.pos):   # con ello se sabe que se clickeo en este
                        active1 = True
                    else:
                        active1 = False
                if event1.type == pygame.KEYDOWN:  # detecta si se presiona una tecla
                    if active1==True:
                        if event1.key == pygame.K_RETURN: # si se presiona enter se sale de este ciclo y se obtiene el nombre del jugador 1
                            print(nombreplayer1)
                            inicio1=True # con esto se inicia el juego
                        elif event1.key == pygame.K_BACKSPACE: #permite que se borre si se equivoca digitando el nombre
                            nombreplayer1 = nombreplayer1[:-1]  # se elimina una letra del nombre si se requeria
                        else:
                            nombreplayer1 += event1.unicode      # se obtiene la tecla presionada y se concatena
                # se obtiene el nombre del jugador 1
                    
        txt_surface1 = fontnombre.render(nombreplayer1, True, white) # se va mostrando en pantalla el nombre
        
        screen.blit(txt_surface1, (input_box1.x, input_box1.y)) # se blitea el nombre 
        
        pygame.draw.rect(screen, white, input_box1, 2)

        if  inicio2==False: # se entra en este ciclo para que el usuario ingrese el nombre del jugador 2
            for event2 in pygame.event.get():
                if event2.type == pygame.MOUSEBUTTONDOWN: # si se da click en la casilla empieza a aceptar texto
                    if input_box2.collidepoint(event2.pos):
                    # Toggle the active variable.
                        active2 = True
                    else:
                        active2 = False
                if event2.type == pygame.KEYDOWN: 
                    if active2==True:
                        if event2.key == pygame.K_RETURN: # si se presiona enter se sale de este ciclo y se obtiene el nombre del jugador 2
                            print(nombreplayer2)
                            inicio2=True
                        elif event2.key == pygame.K_BACKSPACE: #permite que se borre si se equivoca digitando el nombre
                            nombreplayer2 = nombreplayer2[:-1]
                        else:
                            nombreplayer2 += event2.unicode
                    # se obtiene el nombre del jugador 2
        txt_surface2 = fontnombre.render(nombreplayer2, True, white)
        
        screen.blit(txt_surface2, (input_box2.x, input_box2.y))
        
        pygame.draw.rect(screen, white, input_box2, 2)

        # mismo codiogo pero para el jugador 2

        if inicio1==True and inicio2==True: #si ambas variables son iguales se digitaron ambos nombres por lo que se procede a iniciar el juego
            inicio=True
            pygame.mixer.stop() # se para la musica para reinicioara
       
    

            
    if menu==False and inicio==1: # se inicializa el juego
  
        reloj=pygame.time.get_ticks()+reloj1      # se define un tiempo inicial que permite determinar el tiempo transcurrado hasta que se inicio el juego o si se cargo una partida se le suma el tiempo anterior

        if nivel==0: # para el primer nivel
            background=pygame.image.load("pista2.png") # pone el fondo del juego
            background = background.convert()
            
            




            if new==True: # si es una partida nueva
                time1=pygame.time.get_ticks() # se define un tiempo
                player1=Carros(20, 15,"we4.png",300,420) # se reinician las variables para permitir su actualizacion
                player2=Carros(20, 15,"we5.png",335,420)

                dummy1.kill()
                dummy2.kill()
                dummy3.kill()
                
                dummy1=Dummyvehicles(20, 15,"we2.png",370,420,2)
                dummy2=Dummyvehicles(20, 15,"we3.png",265,420,5)
                dummy3=Dummyvehicles(20, 15,"we1.png",405,420,1)
            
                dummy_list.add(dummy1)
                dummy_list.add(dummy2)
                dummy_list.add(dummy3)
               

                for n in lista_obstaculos:   
                    n.kill()
                tipo=[]
                lar=[]
                al=[]
        
        
            
                for s in range(7):  # se quieren obtener 7 obstaculos 
                    num=random.randint(0,2) # se obtiene un numero random entre 0 y 2 que permite que se tengan diferentes obstaculos en la partida y asi la imagen es variada entre dos tipos de roca y un arbol
                    if num==0:
                        image="arbol1.png"
                    if num==1:
                        image="roca1.png"
                    if num==2:
                        image="roca2.png" # dependiendo del numero se carga una imagen
                    largo=random.randint(0,1920)  # la posicion de la piedra tambien se obtiene mediante numeros aleatorias en toda la pantalla
                    alto=random.randint(0,1080)
                    x=largo # se define la posicion de el obstaculo
                    y=alto
                    tipo+=[num] #se concatenan los valores por si es requerido cargar la partida y asi se sabe el tipo de imagen y su posicion
                    lar+=[x]
                    al+=[y]


                    obstacle=Obstaculos(image,x,y) # se define el obstaculo
                    lista_obstaculos.add(obstacle) # se añaden en la pantalla
                nivel=-1
                    
            if new==False: # si la partida es cargada
                player1.x  # se definen variables especificas para este caso
                player1.y
                player1.image
                nivel=-1
                time1=pygame.time.get_ticks()+time1# el tiempo son los ticks obtenidos hasta ahora mas el tiempo guardado
                
            timenew=pygame.time.get_ticks()

            
              

        if nivel==1: # si se esta en el nivel 2
            screen.blit(background, (0,0)) # se reinicia la pantalla
            background=pygame.image.load("pista3.png") # pone el fondo del juego
            background = background.convert()

            if new==True:
                time2=pygame.time.get_ticks() # se obtiene el tiempo
                player1=Carros(20, 15,"we4.png",300,420)
                player2=Carros(20, 15,"we5.png",335,420)

                dummy1.kill()
                dummy2.kill()
                dummy3.kill()
                
                dummy1=Dummyvehicles(20, 15,"we2.png",370,420,2)# se reinician los valores ya que se paso de nivel
                dummy2=Dummyvehicles(20, 15,"we3.png",265,420,3)
                dummy3=Dummyvehicles(20, 15,"we1.png",405,420,1)
            
                dummy_list.add(dummy1)
                dummy_list.add(dummy2)
                dummy_list.add(dummy3)

                for n in lista_obstaculos:
                    n.kill()

                tipo=[]
                lar=[]
                al=[]
        
            
                for s in range(8): # se crean 8 obstaculos y se sigue el procedimiento explicado anteriormente
                    num=random.randint(0,2) # generacion de numeros aleatorios, implica imagen aleatoria
                    if num==0:
                        image="arbol1.png"
                    if num==1:
                        image="roca1.png"
                    if num==2:
                        image="roca2.png"
                    largo=random.randint(0,1920)
                    alto=random.randint(0,1080) # posicion aleatoria
                    x=largo
                    y=alto
                    
                    tipo+=[num]
                    lar+=[x]
                    al+=[y]
                    

                    obstacle=Obstaculos(image,x,y)
                    lista_obstaculos.add(obstacle)
                nivel=-2 # se define esto para que se salga del ciclo
                    
            if new==False: # si la partida es cargada
                player1.x
                player1.y
                player1.image
                nivel=-2
                time2=pygame.time.get_ticks()+time2 # el tiempo nuevo es la suma de dos variables
            timenew=pygame.time.get_ticks()

            
              

        if nivel==2: # si se esta en el ultimo nivel
            screen.blit(background, (0,0)) # se reinicia la pantalla
            background=pygame.image.load("pista4.png") # pone el fondo del juego
            background = background.convert()
            
            
            
            
            if new==True: # si la partida es nuvea
                time3=pygame.time.get_ticks() # se obtiene el tiempo transcurrido
                player1=Carros(20, 15,"we4.png",300,420)
                player2=Carros(20, 15,"we5.png",335,420)# se reinician las variables pues se esta en un escenario nuevo

                dummy1.kill()
                dummy2.kill()
                dummy3.kill()
                
                dummy1=Dummyvehicles(20, 15,"we2.png",370,420,2)
                dummy2=Dummyvehicles(20, 15,"we3.png",265,420,5)
                dummy3=Dummyvehicles(20, 15,"we1.png",405,420,1)
            
                dummy_list.add(dummy1)
                dummy_list.add(dummy2)
                dummy_list.add(dummy3)

                for n in lista_obstaculos:
                    n.kill()
                tipo=[]
                lar=[]
                al=[]
        
            
                for s in range(8): # se generan 8 obstaculos con imagenes aleatorias
                    num=random.randint(0,2)
                    if num==0:
                        image="arbol1.png"
                    if num==1:
                        image="roca1.png"  # se definen las imagenes
                    if num==2:
                        image="roca2.png"
                    largo=random.randint(0,1920) # posicion aleatoria del obstaculo en el rango
                    alto=random.randint(0,1080)
                    x=largo
                    y=alto
                    tipo+=[num] # se concatenan las variables por si se van a guardar que se sepa la posicion e imagen de los obstaculos
                    lar+=[x]
                    al+=[y]


                    obstacle=Obstaculos(image,x,y) # se crea el objeto
                    lista_obstaculos.add(obstacle)
                nivel=-3
                    
            if new==False: # si la partida no es nueva
                player1.x
                player1.y
                player1.image
                nivel=-3
                time3=time3+pygame.time.get_ticks() # se obtiene el tiempo
            timenew=pygame.time.get_ticks()

        
              


        

        

        
        if new==True:   # Condicion para pasar de nivel
            if  (pygame.time.get_ticks()-time1)//1000==180 and time1!=0 and nivel==-1: # si se cumplen 180 minutos
                if contador1==0 or contador2==0: # su no se ha colisionado
                    nivel=1 # se pasa de menu
                else:
                    menu=True # si esto no se cumple se termina la partida 
                
                
              




        if new==False:   # misma condicion pero si la partida es cargada
            if  (reloj-time4-time1)//1000==180 and time1!=0 and nivel==-1: #si se cumplen 3 minutos y no se ha chocado se pasa de nivel
                if contador1==0 or contador2==0:
                    nivel=1
                else:
                    menu=True
                    
        














        if new==True:  # para partida nueva si se cumplen 6 minutos y no se ha chocado se pasa al ultimo nivel 
            if  (pygame.time.get_ticks()-time2)//1000==180 and time2!=0 and nivel==-2: 


                if contador1==0 or contador2==0:
                    nivel=2
                else:
                    menu=True

        if new==False: # para partida cargada si se cumplen 360 minutos y no se ha chocado se pasa de nivel
            if  (reloj-time4-time1)//1000==360 and time2!=0 and nivel==-2: 


                if contador1==0 or contador2==0:
                    nivel=2
                else:
                    menu=True

        if new==True:
                
            if  (pygame.time.get_ticks()-time3)//1000==10 and time3!=0 and nivel==-3: #se vuelve a obtener el tiempo transcurrido y se le resta el anterior para así determinar el tiempo desde que inicio. Se pone como limite 180 seg(3 minutos)
                with open("jsonfile.json", "r") as read_file: # si se pasaron los 3 minutos se detiene el juego y se lee el json y se le añade la puntuación y nombres de los jugadores de la última partida
                    data = json.load(read_file) # se lee el json para poder actualizarlo y no borrarlo
                    namelist=[] # se obtienen los nombres y posiciones
                    pointslist=[]
                for name in data['nombres']: # se extrae del json los "nombres"
                
                    namelist+=[name]
                for points in data['puntaje']: # se extrae del json los puntos
                    pointslist+=[points]

                print(namelist)





            
                puntaje1=int(50*vueltas1+10*kills1+salidas1)# se define el puntaje del jugador 1
                puntaje2=int(50*vueltas2+10*kills2+salidas2) # se define el puntaje del jugador 2

                # las vueltas dan 50 puntos, las kills 10 y por cada vez que se salga de la pista se va restando

                menu=True # permite la devolucion en el siguiente ciclo al menu
            
                jsonfile={"nombres":[str(nombreplayer1), str(nombreplayer2)]+namelist,"puntaje":[str(puntaje1), str(puntaje2)]+pointslist} # se sobreescribe el jsonfile
                print (jsonfile) 
                with open("jsonfile.json", "w") as write_file:
                    json.dump(jsonfile, write_file)# se escriben los nuevos valores en el json

        if new==False: # si se tiene partida cargada
                
            if  (reloj-time4-time1)//10==540 and nivel==-3 and time3!=0: #se vuelve a obtener el tiempo transcurrido y se le resta el anterior para así determinar el tiempo desde que inicio. Se pone como l{imite 180 seg(3 minutos)
                with open("jsonfile.json", "r") as read_file: # si se pasaron los 3 minutos se detiene el juego y se lee el json y se le añade la puntuación y nombres de los jugadores de la última partida
                    data = json.load(read_file)
                    namelist=[]
                    pointslist=[]
                for name in data['nombres']: # se extrae del json los "nombres"
                
                    namelist+=[name]
                for points in data['puntaje']: # se extrae del json los puntos
                    pointslist+=[points]

                print(namelist)





            
                puntaje1=int(50*vueltas1+10*kills1+salidas1)# se define el puntaje del jugador 1
                puntaje2=int(50*vueltas2+10*kills2+salidas2) # se define el puntaje del jugador 2

                menu=True # permite la devolucion en el siguiente ciclo al menu
            
                jsonfile={"nombres":[str(nombreplayer1), str(nombreplayer2)]+namelist,"puntaje":[str(puntaje1), str(puntaje2)]+pointslist} # se sobreescribe el jsonfile
                print (jsonfile)
                with open("jsonfile.json", "w") as write_file:
                    json.dump(jsonfile, write_file)

            
        
        
            
            
        

        #if pygame.sprite.collide_rect(player1,rect)==True:
        if (background.get_at((int(player1.x),int(player1.y)))==(17,17,17)) or (background.get_at((int(player1.x),int(player1.y)))==(0,0,0)) or int(player1.y) in range(450,550):  # se define la aceleración del vehículo, si este esta en la calle(color negro(17,17,17)) la aceleracion es maxima si no la aceleracion es minima
            if aceleration1==1:
                acsound.play() # si se esta acelerando suena 


            aceleration1+=0.001 #La aceleracion va aumentando
        else:
            aceleration1=0.4    # si se sale la aceleracion es minima
            salidas1-=0.1       # por cada vez q se salga se crea una variable que permite restar puntos

        if int(aceleration1)==2:
            aceleration1=2
            

        if (background.get_at((int(player2.x),int(player2.y)))==(17,17,17))  or (background.get_at((int(player2.x),int(player2.y)))==(0,0,0)) or int(player2.y) in range(450,550):  # igual que en el caso anterior pero para el jugador 2
            aceleration2+=0.001
        else:
            aceleration2=0.4  # mismo caso pero para el jugador 2
            salidas2-=0.1

        if int(aceleration2)==2:
            aceleration2=2

        
      

        

            


        
        
        
        

        #if pygame.sprite.collide_rect(player1,rect)==True:
       
            
            
    
                    
        screen.blit(background, (0,0)) # se limpia la pantalla

        if new==True:
        
            crono=font2.render("Tiempo transcurrido: "+ str((reloj-time1)//1000), 1, white) # con esto se obtiene un cronómetro en segundos para seguir el tiempo del juego
            screen.blit(crono,(1200,1050)) # se vale de la funcion blit para colocar el reloj
        if new==False:
            crono=font2.render("Tiempo transcurrido: "+ str((reloj-time4-time1)//1000), 1, white) # con esto se obtiene un cronómetro en segundos para seguir el tiempo del juego
            screen.blit(crono,(1200,1050))
            

        

        if contador1!=3: # si no se tienen 3 colisiones se pueden jugar

            player1.rotar() # se llama a las funciones de rotación de los carros para saber la dirección en la que este debe avanzar
           
        

            oldrect1 = player1.image.get_rect() # se obtiene el rectangulo del vehiculo 
            player1.image = pygame.transform.rotate(player1.original, player1.angle) # se transforma la imagen para que parezca el carro roto
            newrect1 = player1.image.get_rect() # se obtiene el rectangulo del vehiculo nuevo
        
            player1.x += oldrect1.centerx - newrect1.centerx # se restan las componentes de ambos rectangulos para así obtener la verdadera posición del carro y simular sus movimientos
            player1.y += oldrect1.centery - newrect1.centery

 


            player1.avance(player1.angle,aceleration1) # se inicializan las funciones que permiten que el vehiculo avance mandando como parametro las condiciones de angulo y posicion obtenidas anteriormente
        
            screen.blit(player1.image,(player1.x,player1.y))# se hace un blit para aparentar que el vehiculo se movio a una nueva posición
      

        if contador2!=3: # mismo caso pero para el jugador 2
             
            player2.rotar() # rotacion vehiculo 2
        
 
            oldrect2 = player2.image.get_rect() # misma situaci{on pero para el jugador 2
            player2.image = pygame.transform.rotate(player2.original, player2.angle) # se transforma la imagen para que parezca el carro roto
            newrect2 = player2.image.get_rect() 
    
            player2.x += oldrect2.centerx - newrect2.centerx
            player2.y += oldrect2.centery - newrect2.centery

       
        



            player2.avance(player2.angle,aceleration2)
        
        
            screen.blit(player2.image,(player2.x,player2.y))
            
        if contador1==3 and contador2==3: # si se choco 3 veces se sale al menu
            menu=True



        


        tiempotranscurrido1=pygame.time.get_ticks()//1000

            



        

        


        if int(player1.y) in range(470,550) and int(player1.x) in range (182,500) and tiempotranscurrido1-tiempotranscurrido2>13: # determinar si se pasa por la meta que esta en las coordenadas colocadas
            vueltas1+=1 # si es asi se suman las vueltas
            tiempotranscurrido2=pygame.time.get_ticks()//1000
            pygame.mixer.stop() # se reporduce una musica si se pasa por la meta
            metasound.play()
        if int(player2.y)in range(470,550)and int(player2.x) in range (182,500) and tiempotranscurrido1-tiempotranscurrido3>13:# mismo situación que en el caso anterior pero para el jugador 2
            vueltas2+=1
            tiempotranscurrido3=pygame.time.get_ticks()//1000
            pygame.mixer.stop()
            metasound.play()
                
            

                


        myfont= pygame.font.SysFont("monospace", 20)
        scoretext=myfont.render("Puntuación jugador1 ="+str(int(50*vueltas1+10*kills1+salidas1))+" ,"+"Puntuación jugador2 =" +str(int(50*vueltas2+10*kills2+salidas2)), 1, white) # se colocan en pantalla las vueltas, puntuaciones y kills
        screen.blit(scoretext, (5,10))

        scoretext=myfont.render("Presione esc para salir", 1, white)
        screen.blit(scoretext, (700,10))

        scoretext=myfont.render("Vueltas jugador1 ="+str(int(vueltas1))+" ,"+"Vueltas jugador2 =" +str(int(vueltas2)), 1, white)
        screen.blit(scoretext, (5,80))

        scoretext=myfont.render("Kills jugador1 ="+str(int(kills1))+" ,"+"Kills jugador2 =" +str(int(kills2)), 1, white)
        screen.blit(scoretext, (5,150))

        scoretext=myfont.render("Vidas jugador1 ="+str(3-int(contador1))+" ,"+"Vidas jugador2 =" +str(3-int(contador2)), 1, white)
        screen.blit(scoretext, (5,220))

        espacio = pygame.key.get_pressed()
        
        if espacio[pygame.K_SPACE]and  tiempotranscurrido1-tiempotranscurrido3>2: # si se presiona space se inicializan las balas como objetos
            bala1=Balas(4,5,"balafoto.png",player1.x,player1.y,player1.angle)
            spritegroup.add(bala1) # se añaden a un grupo
       

        for sprite in spritegroup.sprites():
            if 0<sprite.rect.x<screen.get_width() and 0<sprite.rect.y<screen.get_height(): # se mueven las balas si no se sobrepasa de las dimensiones dadas
                screen.blit(sprite.image,(sprite.update()))


        if espacio[pygame.K_e ]and  tiempotranscurrido1-tiempotranscurrido3>2: # misma situación pero para el jugador 2
            bala2=Balas(4,5,"balafoto.png",player2.x,player2.y,player2.angle)
            spritegroup1.add(bala2)

        for sprite1 in spritegroup1.sprites(): # misma situación pero para el jugador 2
            if 0<sprite1.rect.x<screen.get_width() and 0<sprite1.rect.y<screen.get_height():
                screen.blit(sprite1.image,(sprite1.update()))


        if espacio[pygame.K_r]: # si se pulsa la tecla r se sale al menu
            menu=True

        
        screen.blit(savebutton,(1800,950))
        
                
           

       
           
           

            

        dummy_list.update() # se hace update a los dummy para que estos se muevan
        choques1= pygame.sprite.spritecollide(bala1, dummy_list, False)# se añaden a una lista los dummy que han colisionado
        choques2= pygame.sprite.spritecollide(bala2, dummy_list, False)
      

        for s in choques1: # para todos los que estan en la lista de choques
            pygame.mixer.stop()
            s.kill()   # se eliminan
            kills1+=1     # se añaden kills
            acsound.stop()     
            hitsound.play(0)    # se pone una musica

            
        for t in choques2: # mismo caso pero para los del jugador 2
            pygame.mixer.stop()
            t.kill()
            kills2+=1
            acsound.stop()
            hitsound.play(0)
   

            print("colision")
            
        if len(dummy_list)==0: # si no hay dummys aparecen nuevos

            dummy1=Dummyvehicles(20, 15,"we.png",370,420,2) # se inicializan los dummy
            dummy2=Dummyvehicles(20, 15,"we.png",265,420,5)
            dummy3=Dummyvehicles(20, 15,"we.png",405,420,1)
            
            dummy_list.add(dummy1)
            dummy_list.add(dummy2)
            dummy_list.add(dummy3)

        



        lista_obstaculos.update() # se actualizan los obstaculos

        for obs in lista_obstaculos: #para los obstaculos en la lista

            if pygame.sprite.collide_rect(player1,obs) : # si hay colision con el jugador 1
                pygame.mixer.stop()
                obs.kill() #se detruyen los obstaculos
                acsound.stop()
                choquesound.play(0)
                
                contador1+=1 # se suma un contador de choque al carro

                if(background.get_at((int(player1.x),int(player1.y)))!=(17,17,17)) and (background.get_at((int(player1.x),int(player1.y)))!=(0,0,0)) and int(player1.y) not in range(450,550): # si el choque es fuera de la pista
                    contador1=3  # el contador es 3 y el carro se destruye inmediatamente
            if pygame.sprite.collide_rect(player2,obs) : # mismo caso pero para el jugador 2
                pygame.mixer.stop()
                obs.kill()
                acsound.stop()
                choquesound.play(0)
                
                contador2+=1

                if(background.get_at((int(player2.x),int(player2.y)))!=(17,17,17)) and (background.get_at((int(player2.x),int(player2.y)))!=(0,0,0)) and int(player2.y) not in range(450,550):
                    contador2=3

        for dum in dummy_list:
            if pygame.sprite.collide_rect(dum,player1) :
                pygame.mixer.stop()
                dum.kill()
                contador1+=1
                acsound.stop()
                choquesound.play(0)
            if pygame.sprite.collide_rect(dum,player2) :
                pygame.mixer.stop()
                dum.kill()
                contador2+=1
                acsound.stop()
                choquesound.play(0)


             

        
        if (pygame.key.get_pressed()[pygame.K_UP]!=0 or pygame.key.get_pressed()[pygame.K_w]!=0): # define el sonido de si se esta acelerando si se esta acelerando suena indefinidamente el sonido
            acsound.play(-1)
        else:
            acsound.stop() # si no se apretan el sonido para

        #posicion guardado

       
            

        if back.click6():  # se definen algunas variables para hacer el guardado mas visualmente atractivo
            t3=player1.x
            t4=player2.x
            t5=player1.y
            t6=player2.y
            t8=kills1
            t9=kills2
            t10=vueltas1
            t11=vueltas2
            t12=time1
            t13=time2
            t14=time3
            t15=aceleration1
            t16=player1.angle
            t17=aceleration2
            t18=player2.angle
            t19=contador1
            t20=contador2
            t21=salidas1
            t22=salidas2
            t23=dummy1.x
            t24=dummy1.y
            t25=nivel
            t26=dummy2.x
            t27=dummy2.y
            t28=dummy3.x
            t29=dummy3.y
            t30=nombreplayer1
            t31=nombreplayer2
            t32=dummy1.contador
            t33=dummy2.contador
            t34=dummy3.contador
            t35=reloj
            t36=tipo
            t37=lar
            t38=al


            
            jsonfile={"var":[t3,t4,t5,t6,t8,t9,t10,t11,t12,t13,t14,t15,t16,t17,t18,t19,t20,t21,t22,t23,t24,t25,t26,t27,t28,t29,t30,t31,t32,t33,t34,t35,t36,t37,t38] } # se añaden a una variable las variables como un diccionario
            print (jsonfile)
            with open("guardado.json", "w") as write_file:
                json.dump(jsonfile, write_file) # se crean un json con las variables mostradas
            
            
        




        
            




    if inicio==2 and menu==False: # se inicializa la pantalla de puntuaciones
        background=pygame.image.load("menufondo.png")   # se define un fondo
        background = background.convert()
        textoscore=fontnombre.render("Mejores puntajes: ", True, white)
        
        screen.blit(background,(0,0)) # se limpia la pantalla
        screen.blit(textoscore, (50, 50))
        
        r=back.encontrarmayorespuntajes() # se llama a la funcion que contiene los nombres y puntajes de los primeros tres jugadores


        primerlugar=r[0]
        segundolugar=r[1] # se obtienen los valores del return de la función
        tercerlugar=r[2]
        cuartolugar=r[3]
        quintolugar=r[4]
        nombreprimero=r[5]
        nombresegundo=r[6]
        nombretercero=r[7]
        nombrecuarto=r[8]
        nombrequinto=r[9]


        textoprimero=font3.render("Primer lugar: " +str(nombreprimero)+"= "+str(primerlugar), True, white) # se obtiene las puntuaciones y nombres como texto
        textosegundo=font3.render("Segundo lugar: "+str(nombresegundo)+"= "+str(segundolugar), True, white)
        textotercero=font3.render("Tercer lugar: "+str(nombretercero)+"= "+str(tercerlugar), True, white)
        textocuarto=font3.render("Tercer lugar: "+str(nombrecuarto)+"= "+str(cuartolugar), True, white)
        textoquinto=font3.render("Tercer lugar: "+str(nombrequinto)+"= "+str(quintolugar), True, white)

        screen.blit(textoprimero, (50, 300)) # se imprimen las puntuaciones
        screen.blit(textosegundo, (50, 400))
        screen.blit(textotercero, (50, 500))
        screen.blit(textocuarto, (50, 600))
        screen.blit(textoquinto, (50, 700))

        backbutton=pygame.image.load("images.png")# se define un boton de salida
        screen.blit(backbutton,(1600,600))

        if back.click4()==True: # condición en la que se apreta el boton de salida
            inicio=0
            menu=True
            new=True # si se apreta el boton de salida se definen unas variables para que en la entrada del ciclo se llegue al menu

            
   

   


        
            

            
    
        
           
    pygame.display.flip()
    
pygame.quit() # se cierra pygame
        

