#proyecto taller de programacion
#Adrián López

import pygame #se importa pygame, math y json ya que son las bibliotecas q se desean usar
import math
import json


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
color=[]
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



mainloop=True 
menu=True#condición para el menú

pygame.init() # se inicia pygame

class Fondo:       #clase que define las propiedades del fondo como el menu o si hay clicks o interaciones con el mouse
    def __init__(self): #se inicializa la clase
         pass

    def menu(self):    # función que define el fondo de el menu y los recuadros de texto
        background=pygame.image.load("menufondo.png")
        background = background.convert()
        screen.blit(background, (0,0))
        pygame.draw.rect(screen,white,(700,450,1100,500))
        pygame.draw.rect(screen,black,(750,500,1100,500))
        pygame.draw.rect(screen,red,(800,550,1000,100))
        pygame.draw.rect(screen,red,(800,850,1000,100))
        font1= pygame.font.SysFont("impact", 100)
        font2= pygame.font.SysFont("impact", 20)
        texto1=font1.render("Iniciar Partida", 1, white)
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


    def click1(self): #función click para iniciar
        if 800<mouse[0]<1800 and 550<mouse[1]<650: #rango de valores del mouse 
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
            return True
        else:
            return False
        
    def encontrarmayorespuntajes(self): #función que permite abrir un json y encontrar las mayores puntuaciones
        with open("jsonfile.json", "r") as read_file: # se abre el archivo json
            data = json.load(read_file)  
        namelist=[]
        pointslist=[]            #se inicializan algunas variables
        valor1=0
        valor2=0
        valor3=0
        nombreprimero=''
        nombresegundo=''
        nombretercero=''
        
        for name in data['nombres']:    #se obtiene del json los "nombres"
            namelist+=[name]
        for points in data['puntaje']:  #se obtiene del json los "puntajes"
            pointslist+=[int(points)]

        primerlugar=max(pointslist)      #se obtiene el primer máximo
        
        for i in range(0,len(pointslist)):            #se utiliza la lista de puntuaciones para obtener la posición del primer máximo
            if str(primerlugar)==pointslist[i]:
                valor1=i-1
        nombreprimero=namelist[valor1]

        pointslist.remove(pointslist[valor1])
        namelist.remove(namelist[valor1])


        segundolugar=max(pointslist)

        for j in range(0,len(pointslist)-1):          #se utiliza la lista de puntuaciones quitando el primer maximo para obtener la posición del segundo maximo
            if str(segundolugar)==j:
                valor2=j-1
        nombresegundo=namelist[valor2]

        pointslist.remove(pointslist[valor2])
        namelist.remove(namelist[valor2])

        

        tercerlugar=max(pointslist)                    #se utiliza la lista de puntuaciones quitando el segundo máximo para obtener la posición del tercer maximo
        for k in range(0,len(pointslist)-2):
            if str(tercerlugar)==k:
                valor3=k-1
        nombretercero=namelist[valor3]

        pointslist.remove(pointslist[valor3])
        namelist.remove(namelist[valor3])
    #con esto se obtiene las posiciones y los valores maximos y nombres del archivo json
        
        return (primerlugar,segundolugar,tercerlugar,nombreprimero,nombresegundo,nombretercero) #salidas de la funcion
        
                


        

        
    
back=Fondo()
angulo=0
bala1=False
pixelx=0
pixely=0
tiempotranscurrido1=0
tiempotranscurrido2=0
tiempotranscurrido3=0
spritegroup=pygame.sprite.Group()
spritegroup1=pygame.sprite.Group()

class Carros(pygame.sprite.Sprite):  # se define una clase que permite la obtencion los carros usando parametros
    def __init__(self, width, height,image,x,y): # se inicializa la clase y se tienen como entradas  una foto, ancho, largo y la posicion a la q se quiere el objeto

        super().__init__()
        

        self.image = pygame.Surface([width, height])
        self.image = pygame.image.load(image)
        self.image= pygame.transform.rotate(self.image,180)
        self.numvueltas=0
        

        self.image.convert_alpha()

        self.rect = self.image.get_rect()
    
        self.x=self.rect.x+x
        self.y=self.rect.y+y
        self.angle=angulo
        self.factorgiro=0
        self.original = self.image.copy()
    
        
    def rotar(self): # función que detecta si se apretan las flechas o a y d para así rotar el carro
        pressedkeys = pygame.key.get_pressed()

        if self==player1: #si se tiene el carro del jugador 1

            if pressedkeys[pygame.K_LEFT]: # se define una constante que varia dependiendo del sentido de giro si se presionan las teclas izquierda o derecha
                self.factorgiro=1
            if pressedkeys[pygame.K_RIGHT]:
                self.factorgiro=-1
        if self==player2: #si se tiene el carro del jugador 2
            if pressedkeys[pygame.K_a]: # se define una constante que varia dependiendo del sentido de giro si se presionan las teclas a o d
                self.factorgiro=1
            if pressedkeys[pygame.K_d]:
                self.factorgiro=-1
            
        self.angle+=self.factorgiro*180*0.004 # se define el angulo como el sentido de rotación y factores que permiten que el giro sea más suave
        self.factorgiro=0
           
        
        
    def avance(self,angulo,aceleration): # clase que recibe un angulo y una aceleracion y permite que el carro avance estas son calculadas anteriormente
        pressedkeys = pygame.key.get_pressed()

        if self==player1: # si se tiene el carro 1
            if pressedkeys[pygame.K_UP]: #se define que si se apreta la tecla up o w el carro va a avanzar en la direcci{on que traia este.
                self.x+=math.sin(math.radians(angulo))*aceleration*0.6 # se vale de la matemática para proyectar vectores y permitir que el carro avance en la direccion que se tenia anteriormente
                self.y+=math.cos(math.radians(angulo))*aceleration*0.6
                aceleration+=0.0001 # si se deja la tecla up presionada se define que el carro acelere constantemente
                self.rect.x=self.x
                self.rect.y=self.y
                return(self.x,self.y)
            if pressedkeys[pygame.K_DOWN]: #función reversa
                self.x-=math.sin(math.radians(angulo))*aceleration*0.6
                self.y-=math.cos(math.radians(angulo))*aceleration*0.6
                self.rect.x=self.x
                self.rect.y=self.y
                return(self.x,self.y)
            
        if self==player2: # si se tiene el carro 2
            if pressedkeys[pygame.K_w]: # igual que en los casos anteriores
                self.x+=math.sin(math.radians(angulo))*aceleration*0.6
                self.y+=math.cos(math.radians(angulo))*aceleration*0.6
                aceleration+=0.0001
                self.rect.x=self.x
                self.rect.y=self.y
                return(self.x,self.y)
            
            if pressedkeys[pygame.K_s]:
                self.x-=math.sin(math.radians(angulo))*aceleration*0.6
                self.y-=math.cos(math.radians(angulo))*aceleration*0.6
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
        self.image = pygame.Surface([width, height])
        self.image = pygame.image.load(image)
        self.image=pygame.transform.scale(self.image,(4,5)) # se escala la imagen
        self.rect = self.image.get_rect()
        self.rect.x=x
        self.rect.y=y
        self.angulo=angle
        self.x=self.rect.x
        self.y=self.rect.y
        
    def update(self): # función que actualiza la posición de la bala
        pressedkeys = pygame.key.get_pressed()

        self.x+=math.sin(math.radians(self.angulo))*3 #al igual que como se hizo en la parte anterior se obtienen las proyecciones para así seguir un nuevo sistema de coordenadas
        self.y+=math.cos(math.radians(self.angulo))*3
        return(self.x,self.y) # se retorna la posición de la bala

        
        
class Dummyvehicles(pygame.sprite.Sprite): #se define la clase que determina los movimientos de los dummy vehicles
    def __init__(self, width, height,image,x,y,pos): # se inicializa mandando usando como parametros, altura, ancho, posicion e imagen
        super().__init__()
        self.image = pygame.Surface([width, height])
        self.image = pygame.image.load(image)
        self.image=pygame.transform.rotate(self.image,180)
        self.rect = self.image.get_rect()
        self.rect.x+=x
        self.rect.y+=y
    def update(self): # se define una función que determina la actualización de la posición de los dummy vehicles
        if self.rect.y==675:
            self.rect.x+=math.sin(math.radians(45))
            self.rect.y+=math.cos(math.radians(45))
        else:
            self.rect.y+=1
        screen.blit(self.image,(self.rect.x,self.rect.y))
        
        

        

player1=Carros(20, 15,"we.png",300,420)
player2=Carros(20, 15,"we.png",335,420) # se definen algunas variables y se inicializan algunos objetos
jugadores=pygame.sprite.Group
jugadores.add(player1)
jugadores.add(player2)
carros=pygame.sprite.Group()
carros.add(player1)
bala1=Balas(4,5,"balafoto.png",0, 0 ,0)
bala2=Balas(4,5,"balafoto.png",0, 0 ,0)


dummy1=Dummyvehicles(20, 15,"we.png",370,420,4)
dummy2=Dummyvehicles(20, 15,"we.png",265,420,1)
dummy3=Dummyvehicles(20, 15,"we.png",405,420,5)
dummy_list=pygame.sprite.Group()
dummy_list.add(dummy1)
dummy_list.add(dummy2)
dummy_list.add(dummy3)
nombreplayer1=''
nombreplayer2=''
pedirnombre1=True
pedirnombre2=True
input_box1 = pygame.Rect(200, 280, 1500, 200)
input_box2 = pygame.Rect(200, 600, 1500, 200)
active1 = False
inicio1=False
inicio2=False
active2 = False
fontnombre = pygame.font.Font(None, 280)


while mainloop:    # se inicializa el loop principal
    font2= pygame.font.SysFont("impact", 20)
    font6= pygame.font.SysFont("impact", 100)# se inicializan algunos fonts
    mouse = pygame.mouse.get_pos() # se obtien la posicion del mouse
    for event in pygame.event.get(): # si se da un evento
        if event.type == pygame.quit: # si se sale de aqui se sale del loop
            mainloop = False
        if event.type == pygame.KEYDOWN: # si se presiona una tecla
            if event.key == pygame.K_ESCAPE: # si se presiona escape se sale del juego
                mainloop = False
    if menu==True: # se inicializa el menú
        back.menu()

        if back.click1(): #como se menciono anteriormente se uso la clase Fondo para determinar las interacciones del mouse
            menu=False # se inicializa el juego
            print("HOLA")
    
        if back.click2(): # se entra a ver las puntuaciones
            menu=False
            inicio=2
        if back.click3(): # se sale del loop
            mainloop=False

    if menu==False and inicio==0: # se inicia el juego y se sale del menu, se pide el nombre del jugador
        background=pygame.image.load("menufondo.png") # se define el fondo
        background = background.convert()
        textonombre=fontnombre.render("Ingrese nombres: ", True, white)
        
        screen.blit(background,(0,0))
        screen.blit(textonombre, (50, 50))
        
        if  inicio1==False: # se entra en este ciclo para que el usuario ingrese el nombre del jugador 1
            for event1 in pygame.event.get():
                if event1.type == pygame.MOUSEBUTTONDOWN: # si se da click en la casilla empieza a aceptar texto
                    if input_box1.collidepoint(event1.pos):
                        active1 = True
                    else:
                        active1 = False
                if event1.type == pygame.KEYDOWN: 
                    if active1==True:
                        if event1.key == pygame.K_RETURN: # si se presiona enter se sale de este ciclo y se obtiene el nombre del jugador 1
                            print(nombreplayer1)
                            inicio1=True
                        elif event1.key == pygame.K_BACKSPACE: #permite que se borre si se equivoca digitando el nombre
                            nombreplayer1 = nombreplayer1[:-1]
                        else:
                            nombreplayer1 += event1.unicode
                # se obtiene el nombre del jugador 1
                    
        txt_surface1 = fontnombre.render(nombreplayer1, True, white)
        
        screen.blit(txt_surface1, (input_box1.x, input_box1.y))
        
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

        if inicio1==True and inicio2==True: #si ambas variables son iguales se digitaron ambos nombres por lo que se procede a iniciar el juego
            inicio=True
            background=pygame.image.load("ruta3.png") # pone el fondo del juego
            background = background.convert()
            time1=pygame.time.get_ticks() # determina el tiempo transcurrido hasta este momento
            
    if menu==False and inicio==1: # se inicializa el juego
                

            
            
            
        if  (pygame.time.get_ticks()-time1)//1000==180: #se vuelve a obtener el tiempo transcurrido y se le resta el anterior para así determinar el tiempo desde que inicio. Se pone como l{imite 180 seg(3 minutos)
            with open("jsonfile.json", "r") as read_file: # si se pasaron los 3 minutos se detiene el juego y se lee el json y se le añade la puntuación y nombres de los jugadores de la última partida
                data = json.load(read_file)
                namelist=[]
                pointslist=[]
            for name in data['nombres']: # se extrae del json los "nombres"
                
                namelist+=[name]
            for points in data['puntaje']: # se extrae del json los puntos
                pointslist+=[points]

            print(namelist)





            
            puntaje1=vueltas1 # se define el puntaje del jugador 1
            puntaje2=vueltas2 # se define el puntaje del jugador 2 
            menu=True # permite la devolucion en el siguiente ciclo al menu


            
            jsonfile={"nombres":[str(nombreplayer1), str(nombreplayer2)]+namelist,"puntaje":[str(puntaje1), str(puntaje2)]+pointslist} # se sobreescribe el jsonfile
            print (jsonfile)
            with open("jsonfile.json", "w") as write_file:
                json.dump(jsonfile, write_file)
        
            
            
        

        #if pygame.sprite.collide_rect(player1,rect)==True:
        if (background.get_at((int(player1.x),int(player1.y)))==(17,17,17)):  # se define la aceleración del vehículo, si este esta en la calle(color negro(17,17,17)) la aceleracion es maxima si no la aceleracion es minima
            aceleration1+=0.001
        else:
            aceleration1=0.4

        if aceleration1==4:
            aceleration1=4
            

        if (background.get_at((int(player2.x),int(player2.y)))==(17,17,17)): # igual que en el caso anterior pero para el jugador 2
            aceleration2+=0.001
        else:
            aceleration2=0.4

        if aceleration2==4:
            aceleration2=4

      

        

            


        
        
        
        

        #if pygame.sprite.collide_rect(player1,rect)==True:
       
            
            
    
                    
        screen.blit(background, (0,0)) # se limpia la pantalla
        
        crono=font2.render("Tiempo transcurrido: "+ str((pygame.time.get_ticks()-time1)//1000), 1, white) # con esto se obtiene un cronómetro en segundos para seguir el tiempo del juego
        screen.blit(crono,(1200,1050))

        

        


        player1.rotar() # se llama a las funciones de rotación de los carros para saber la dirección en la que este debe avanzar
        player2.rotar()
        

        oldrect1 = player1.image.get_rect() # se obtiene el rectangulo del vehiculo 
        player1.image = pygame.transform.rotate(player1.original, player1.angle) # se transforma la imagen para que parezca el carro roto
        newrect1 = player1.image.get_rect() # se obtiene el rectangulo del vehiculo nuevo
        
        player1.x += oldrect1.centerx - newrect1.centerx # se restan las componentes de ambos rectangulos para así obtener la verdadera posición del carro y simular sus movimientos
        player1.y += oldrect1.centery - newrect1.centery

 
        oldrect2 = player2.image.get_rect() # misma situaci{on pero para el jugador 2
        player2.image = pygame.transform.rotate(player2.original, player2.angle) # se transforma la imagen para que parezca el carro roto
        newrect2 = player2.image.get_rect() 
    
        player2.x += oldrect2.centerx - newrect2.centerx
        player2.y += oldrect2.centery - newrect2.centery

       
        



        player1.avance(player1.angle,aceleration1) # se inicializan las funciones que permiten que el vehiculo avance mandando como parametro las condiciones de angulo y posicion obtenidas anteriormente
        player2.avance(player2.angle,aceleration2)
        
        
        screen.blit(player1.image,(player1.x,player1.y))# se hace un blit para aparentar que el vehiculo se movio a una nueva posición
        screen.blit(player2.image,(player2.x,player2.y))


        tiempotranscurrido1=pygame.time.get_ticks()//1000

            



        

        for t in range(195,500):


            if int(player1.y)==550 and int(player2.x)==t and tiempotranscurrido1-tiempotranscurrido2>13: # se inicializa la funcion que determina si el pixel por el que esta el vehículo es negro, el tiempo se debe tomar en cuenta
                vueltas1+=1 # si es asi se suman las vueltas
                tiempotranscurrido2=pygame.time.get_ticks()//1000
            if int(player2.y)==550 and int(player2.x)==t and tiempotranscurrido1-tiempotranscurrido3>13:# mismo situación que en el caso anterior pero para el jugador 2
                vueltas2+=1
                tiempotranscurrido3=pygame.time.get_ticks()//1000
                
            

                


        myfont= pygame.font.SysFont("monospace", 20)
        scoretext=myfont.render("Vueltas jugador1 ="+str(vueltas1)+" ,"+"Vueltas jugador2 =" +str(vueltas2), 1, white)
        screen.blit(scoretext, (5,10))

        scoretext=myfont.render("Presione esc para salir", 1, white)
        screen.blit(scoretext, (700,10))

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
           

       
           
           

            

        #dummy_list.update()

    if inicio==2 and menu==False: # se inicializa la pantalla de puntuaciones
        background=pygame.image.load("menufondo.png")   # se define un fondo
        background = background.convert()
        textoscore=fontnombre.render("Mejores puntajes: ", True, white)
        
        screen.blit(background,(0,0)) # se limpia la pantalla
        screen.blit(textoscore, (50, 50))
        
        m=back.encontrarmayorespuntajes() # se llama a la funcion que contiene los nombres y puntajes de los primeros tres jugadores


        primerlugar=m[0]
        segundolugar=m[1] # se obtienen los valores del return de la función
        tercerlugar=m[2]
        nombreprimero=m[3]
        nombresegundo=m[4]
        nombretercero=m[5]


        textoprimero=font6.render("Primer lugar: " +str(nombreprimero)+"= "+str(primerlugar), True, white)
        textosegundo=font6.render("Segundo lugar: "+str(nombresegundo)+"= "+str(segundolugar), True, white)
        textotercero=font6.render("Tercer lugar: "+str(nombretercero)+"= "+str(tercerlugar), True, white)

        screen.blit(textoprimero, (50, 300))
        screen.blit(textosegundo, (50, 500))
        screen.blit(textotercero, (50, 700))

        backbutton=pygame.image.load("images.png")# se define un boton de salida
        screen.blit(backbutton,(1600,600))

        if back.click4()==True: # condición en la que se apreta el boton de salida
            inicio=0
            menu=True
            
   

        
        
        
    

        
            

            
    
        
           
    pygame.display.flip()
    
pygame.quit() # se cierra pygame
        

