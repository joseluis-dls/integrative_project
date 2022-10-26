import pygame, random

#Pantalla - ventana
W, H = 700, 400           #VALORES PARA EL TAMAÑO DE LA VENTANA 
#COLORES
BLANCO = (255,255,255)
NEGRO = (0,0,0)
ROJO = (255,0,0)
AZUL = (0,0,255)
VERDE = (0,255,0)

pygame.init()   #INICIALIZAR PYGAME
pygame.mixer.init()     # INICIALIZAR EL SONIDO
PANTALLA = pygame.display.set_mode((W, H))
pygame.display.set_caption("Arky(Medes)")           # NOMBRE DE LA PANTALLA EN DONDE SE MUESTRA EL JUEGO
icono=pygame.image.load("imagenes/arky.png")    # ICONO DE LA PANTALLA DONDE SE MUESTRA EL JUEGO
pygame.display.set_icon(icono)
clock= pygame.time.Clock()  #CONTROLAR LA CANTIDAD DE FPS DEL JUEGO

#-----------------------------------FUNCIONES-------------------------------------------------------

#----------------------------------TEXTO-------------------------------------------------------------
def draw_text(surface, text, size, x, y): #FUNCION PARA DIBUJAR TEXTO EN LA PANTALLA
    font = pygame.font.SysFont("serif", size)  #SELECCIONAR UNA FUENTE
    text_surface = font.render(text, True, NEGRO) # RENDERIZAR Y SELECCIONAR EL COLOR DEL TEXTO
    text_rect = text_surface.get_rect()
    text_rect.midtop = (x, y)     #MODIFICAR LA POSICION DEL TEXTO
    surface.blit(text_surface, text_rect)     #PINTAR EL TEXTO

#--------------------------BARRA DE VIDA-------------------------------------------------------------
def draw_health_bar(surface, x, y, porcentaje):  #FUNCION BARRA DE VIDA
    BAR_LENGHT = 150     #LARGO DE LA BARRA DE VIDA
    BAR_HEIGHT = 10     #ALTURA DE LA BARRA DE VIDA
    fill = (porcentaje / 100) * BAR_LENGHT        #
    border = pygame.Rect(x, y, BAR_LENGHT, BAR_HEIGHT)
    fill = pygame.Rect(x, y, fill, BAR_HEIGHT)
    pygame.draw.rect(surface, AZUL, fill)  #COLOR DE LA BARRA DE VIDA
    pygame.draw.rect(surface, BLANCO, border, 2)       #BORDE DE LA BARRA DE VIDA Y COLOR


#-------------------------PERSONAJE---------------------------------------------------------------
class Personaje(pygame.sprite.Sprite):     #CREACION DE CLASE PARA EL PERSONAJE
    def __init__(self):             #INICIALIZAR LA CLASE
        super().__init__()          #INICIALIZAR LA SUPER CLASE
        self.image = pygame.image.load("imagenes/arky 2.png").convert()  #AGREGANDO PERSONAJE, #COMANDO CONVERT SIRVE PARA ACELERAR EL JUEGO Y CONSUMIR MENOS RECURSOS
        self.image.set_colorkey(NEGRO) #CON ESTA FUNCION SE REMUEVE EL FONDO NEGRO DE LA IMAGEN
        self.rect = self.image.get_rect()  #OBTENER LA RECTA O CUADRO DEL SPRITE
        self.rect.centerx = W // 2     #PONERLO EN PANTALLA
        self.rect.bottom = H -10        #PONERLO EN PANTALLA
        self.speed_x = 0                #MODIFICAR LA VELOCIDAD DEL PERSONAJE
        self.shield = 100               #MODIFICAR LA VIDA DEL PERSONAJE

    def update(self):
        self.speed_x = 0
        keystate = pygame.key.get_pressed()  #COMADO GET_PRESSED SIRVE PARA PODER DEJAT PRESIONADA UNA LETRA
        if keystate[pygame.K_LEFT]:          #SELECCION DE TECLA PARA MOVER A LA IZQUIERDA
            self.speed_x = -5         #VELOCIDAD PERSONAJE
        if keystate[pygame.K_RIGHT]:         #SELECCION DE TECLA PARA MOVER A LA DERECHA
            self.speed_x = 5          #VELOCIDAD PERSONAJE
        self.rect.x += self.speed_x    
        if self.rect.right > W:        # FUNCION PARA QUE EL PERSONAJE NO SE SALGA D ELA PANTALLA
            self.rect.right = W        # SI EL LADO DERECHO DE MI PERSONAJE ES MAYOR A W SE IGUALA A W PARA QUE YA NO PUEDA SEGUIR MAS
        if self.rect.left < 0:         # SI EL LADO IZQUIERDO DE MI PERSONAJE ES MEMNOR A CERO SE IGUALA A CERO PARA QUE NO PUEDA SEGUIR MAS
            self.rect.left = 0 

#----------------------------ITEMS--------------------------------------------------------------------------------
class Libros(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = random.choice(libros_imagenes)  #ELIGE UN LIBRO AL ALZAR DEL COMANDO LIBROS_IMAGENES PARA SPAWNEAR
        self.image.set_colorkey(BLANCO)               #QUITA EL FONDO NEGRO DE LA IMAGEN
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(W - self.rect.width) #HACER QUE APAREZCAN LOS ITEMS DE MANERA ALEATORIA EN LA PANTALLA
        self.rect.y = random.randrange(-100, -40)    #VALOR DE BAJADA DE LOS ITEMS
        self.speedy = random.randrange(1,3)  # VELOCIDAD ALEATORIA DE LOS ITEMS

    def update(self):
        self.rect.y += self.speedy  #AUMMENTAMOS LA VELOCIDAD
        if self.rect.top > H + 10 or self.rect.left < -25 or self.rect.right > W + 25:
                self.rect.x = random.randrange(W - self.rect.width) 
                self.rect.y = random.randrange(-100, -40)    
                self.speedy = random.randrange(1,3)

class Control(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = random.choice(control_imagenes)     #ELIGE UN LIBRO AL ALZAR DEL COMANDO LIBROS_IMAGENES PARA SPAWNEAR
        self.image.set_colorkey(BLANCO)          #QUITA EL FONDO NEGRO DE LA IMAGEN
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(W - self.rect.width) #HACER QUE APAREZCAN LOS ITEMS DE MANERA ALEATORIA EN LA PANTALLA
        self.rect.y = random.randrange(-100, -40)    #VALOR DE BAJADA DE LOS ITEMS
        self.speedy = random.randrange(2,3)  # VELOCIDAD ALEATORIA DE LOS ITEMS

    def update(self):
        self.rect.y += self.speedy  #AUMMENTAMOS LA VELOCIDAD
        if self.rect.top > H + 10 or self.rect.left < -25 or self.rect.right > W + 25:
                self.rect.x = random.randrange(W - self.rect.width) 
                self.rect.y = random.randrange(-100, -40)    
                self.speedy = random.randrange(2,3)

def rules():
    PANTALLA.blit(instrucciones, [0,0])
    pygame.display.flip()
    waiting = True
    while waiting:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:     #MIENTRAS SE PRESIONE UNA TECLA SE QUITA EL MEMNU
                    waiting = False  # SE DEJA DE ESPERAR


def show_game_over_screen():     #FUNCION GAME OVER
    PANTALLA.blit(go, [0,0])
    pygame.display.flip()
    waiting = True
    while waiting:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.KEYDOWN:     #MIENTRAS SE PRESIONE UNA TECLA SE QUITA EL MENU
                if event.key == pygame.K_SPACE:
                    waiting = False  # SE DEJA DE ESPERAR


def nivel_2():     #FUNCION NIVEL 2
    PANTALLA.blit(intro_nivel_2, [0,0])
    pygame.display.flip()
    waiting = True
    while waiting:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.KEYDOWN:     #MIENTRAS SE PRESIONE UNA TECLA SE QUITA EL MENU
                if event.key == pygame.K_SPACE:
                    waiting = False  # SE DEJA DE ESPERAR

def gana():
    PANTALLA.blit(pantalla_gana, [0,0])
    pygame.display.flip()
    waiting = True
    while waiting:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.KEYDOWN:     #MIENTRAS SE PRESIONE UNA TECLA SE QUITA EL MENU
                if event.key == pygame.K_SPACE:
                    waiting = False  # SE DEJA DE ESPERAR


def final():
    PANTALLA.blit(pantalla_final, [0,0])
    pygame.display.flip()
    waiting = True
    while waiting:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.KEYDOWN:     #MIENTRAS SE PRESIONE UNA TECLA SE QUITA EL MENU
                if event.key == pygame.K_SPACE:
                    waiting = False  # SE DEJA DE ESPERAR
                    while running:
                        running = False





libros_imagenes = []       #CREAMOS UNA LISTA CON TODOS LOS ITEMS PARA DESPUES ASIGANRLO A LA VARIABLE DE LIBROS_IMAGENES
libros_list = ["imagenes/libro 1.png", "imagenes/libro 3.png", "imagenes/libro 4.png", "imagenes/libro 2.png"]

for img in libros_list:
    libros_imagenes.append(pygame.image.load(img).convert())  #PROCESO PARA ASIGNAR LA VARIABLE CON LAS IMAGENES A LA NUEVA VARIABLE

control_imagenes = []
control_list = ["imagenes/control 1.png", "imagenes/tele 1.png"]

for img in control_list:
    control_imagenes.append(pygame.image.load(img).convert())


#FONDO
fondo = pygame.image.load("imagenes/nuevo fondo.jpeg").convert()     #CARGAR EL FONDO
go = pygame.image.load("imagenes/fondo 1.png").convert()
instrucciones = pygame.image.load("imagenes/instrucciones.png").convert()
pantalla_final = pygame.image.load("imagenes/pantalla final.png").convert()
intro_nivel_2 = pygame.image.load("imagenes/intro nivel 2.png").convert()
pantalla_gana = pygame.image.load("imagenes/ganador.png").convert()

#SONIDOS
sonido_libro = pygame.mixer.Sound("sonidolibro.mp3")
sonido_has_perdido = pygame.mixer.Sound("sonidohasperdido.mp3") 

#MUSICA JUEGO
pygame.mixer.music.load("sonidojuego.mp3")
pygame.mixer.music.set_volume(0.2)     #MODIFICADOR DE VOLUMEN DE MUSICA DEL JUEGO

#Grupo de sprites
all_sprites = pygame.sprite.Group()
libro_list = pygame.sprite.Group()
control_list = pygame.sprite.Group()

#INSTANCIAS
personaje = Personaje()     #INSTANCIA DEL PERSONAJE
all_sprites.add(personaje)  #AGREGAR JUGADOR A LA LISTA

for i in range(5): #NUMERO DE LIBROS QUE VAN A CAER
    libro = Libros()
    all_sprites.add(libro)
    libro_list.add(libro)

for i in range(7):
    control = Control()
    all_sprites.add(control)
    control_list.add(control)

#VARIABLE PUNTUACION
score = 0

#MUSICA JUEGO
pygame.mixer.music.play(loops=-1)  #HACER QUE SE ESCUCHE LA MUSICA DEL JUEGO Y QUE ENTRE EN UN LOOP

#GAME OVER
game_over = True
#BUCLE PRINCIPAL
running = True
while running:
    if game_over:

        show_game_over_screen()
        rules()

        game_over = False 
        all_sprites = pygame.sprite.Group()
        libro_list = pygame.sprite.Group()
        control_list = pygame.sprite.Group()

        personaje = Personaje()     
        all_sprites.add(personaje)

        for i in range(5):
            libro = Libros()
            all_sprites.add(libro)
            libro_list.add(libro)

        for i in range(7):
            control = Control()
            all_sprites.add(control)
            control_list.add(control)
        score = 0

    clock.tick(60) #60 FPS
    for event in pygame.event.get():  #EVENTO PARA SALIR DE LA VENTANA
        if event.type == pygame.QUIT:
            running = False
    
    all_sprites.update()

    #COLISIONES
    daño = pygame.sprite.spritecollide(personaje, control_list, True)  #AL TENER UN TRUE SIGNIFICA QUE CUANDO EL PERSONAJE HAGA UNA COLISION CON UN OBJETO ESTE DESAPARECERA
    for daño in daño:
        control = Control()
        all_sprites.add(control)
        control_list.add(control)
        personaje.shield -=25   # MODIFICADOR DE VIDA, #CADA VEZ QUE CHOQUE CON EL ITEMM SE LE RESTAAR 25 
        sonido_has_perdido.play()
        if personaje.shield <= 0:  #SI LA VIDA ES MENOR O IGUAL A CERO TE LLEVA AL GAME OVER
            sonido_has_perdido.play()
            final()
        

    punto = pygame.sprite.spritecollide(personaje, libro_list, True)
    if punto:
        score += 1     #CADA VEZ QUE HAGA COLISIONCON EL OBJETO ESTE  SUMMARA 1  AL PUNTAJE
        sonido_libro.play()
        libro = Libros()
        all_sprites.add(libro)
        libro_list.add(libro)
        if score == 20:
            nivel_2()
            PANTALLA.blit(go, [0,0])
            class Personaje(pygame.sprite.Sprite):     #CREACION DE CLASE PARA EL PERSONAJE
                def __init__(self):             #INICIALIZAR LA CLASE
                    super().__init__()          #INICIALIZAR LA SUPER CLASE
                    self.image = pygame.image.load("imagenes/grad.png").convert()  #AGREGANDO PERSONAJE, #COMANDO CONVERT SIRVE PARA ACELERAR EL JUEGO Y CONSUMIR MENOS RECURSOS
                    self.image.set_colorkey(BLANCO) #CON ESTA FUNCION SE REMUEVE EL FONDO NEGRO DE LA IMAGEN
                    self.rect = self.image.get_rect()  #OBTENER LA RECTA O CUADRO DEL SPRITE
                    self.rect.centerx = W // 2     #PONERLO EN PANTALLA
                    self.rect.bottom = H -10        #PONERLO EN PANTALLA
                    self.speed_x = 0                #MODIFICAR LA VELOCIDAD DEL PERSONAJE
                    self.shield = 100               #MODIFICAR LA VIDA DEL PERSONAJE

            def update(self):
                    self.speed_x = 0
                    keystate = pygame.key.get_pressed()  #COMADO GET_PRESSED SIRVE PARA PODER DEJAT PRESIONADA UNA LETRA
                    if keystate[pygame.K_LEFT]:          #SELECCION DE TECLA PARA MOVER A LA IZQUIERDA
                        self.speed_x = -10         #VELOCIDAD PERSONAJE
                    if keystate[pygame.K_RIGHT]:         #SELECCION DE TECLA PARA MOVER A LA DERECHA
                        self.speed_x = 10          #VELOCIDAD PERSONAJE
                    self.rect.x += self.speed_x    
                    if self.rect.right > W:        # FUNCION PARA QUE EL PERSONAJE NO SE SALGA D ELA PANTALLA
                        self.rect.right = W        # SI EL LADO DERECHO DE MI PERSONAJE ES MAYOR A W SE IGUALA A W PARA QUE YA NO PUEDA SEGUIR MAS
                    if self.rect.left < 0:         # SI EL LADO IZQUIERDO DE MI PERSONAJE ES MEMNOR A CERO SE IGUALA A CERO PARA QUE NO PUEDA SEGUIR MAS
                        self.rect.left = 0 

            class Libros(pygame.sprite.Sprite):
                def __init__(self):
                    super().__init__()
                    self.image = random.choice(libros_imagenes)  #ELIGE UN LIBRO AL ALZAR DEL COMANDO LIBROS_IMAGENES PARA SPAWNEAR
                    self.image.set_colorkey(BLANCO)               #QUITA EL FONDO NEGRO DE LA IMAGEN
                    self.rect = self.image.get_rect()
                    self.rect.x = random.randrange(W - self.rect.width) #HACER QUE APAREZCAN LOS ITEMS DE MANERA ALEATORIA EN LA PANTALLA
                    self.rect.y = random.randrange(-100, -40)    #VALOR DE BAJADA DE LOS ITEMS
                    self.speedy = random.randrange(1,5)  # VELOCIDAD ALEATORIA DE LOS ITEMS

                def update(self):
                     self.rect.y += self.speedy  #AUMMENTAMOS LA VELOCIDAD
                     if self.rect.top > H + 10 or self.rect.left < -25 or self.rect.right > W + 25:
                        self.rect.x = random.randrange(W - self.rect.width) 
                        self.rect.y = random.randrange(-100, -40)    
                        self.speedy = random.randrange(1,5)

            class Control(pygame.sprite.Sprite):
                def __init__(self):
                    super().__init__()
                    self.image = random.choice(control_imagenes)     #ELIGE UN LIBRO AL ALZAR DEL COMANDO LIBROS_IMAGENES PARA SPAWNEAR
                    self.image.set_colorkey(BLANCO)          #QUITA EL FONDO NEGRO DE LA IMAGEN
                    self.rect = self.image.get_rect()
                    self.rect.x = random.randrange(W - self.rect.width) #HACER QUE APAREZCAN LOS ITEMS DE MANERA ALEATORIA EN LA PANTALLA
                    self.rect.y = random.randrange(-100, -40)    #VALOR DE BAJADA DE LOS ITEMS
                    self.speedy = random.randrange(1,5)  # VELOCIDAD ALEATORIA DE LOS ITEMS

                def update(self):
                 self.rect.y += self.speedy  #AUMMENTAMOS LA VELOCIDAD
                 if self.rect.top > H + 10 or self.rect.left < -25 or self.rect.right > W + 25:
                    self.rect.x = random.randrange(W - self.rect.width) 
                    self.rect.y = random.randrange(-100, -40)    
                    self.speedy = random.randrange(1,5)
        if score == 50:
            gana()
            final()
    
    PANTALLA.blit(fondo , [0,0])

    all_sprites.draw(PANTALLA)

    #CONTADOR| 
    draw_text(PANTALLA, str(score), 25, W / 1.8, 1)
    draw_text(PANTALLA, str("Books"), 25, W / 2.1, 1)

    #BARRA DE SALUD
    draw_health_bar(PANTALLA, 5, 5, personaje.shield)

    pygame.display.flip()
pygame.QUIT
