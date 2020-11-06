import pygame, sys
from pygame.locals import *

class Termometro ():
    def __init__ (self):
        self.custom = pygame.image.load ("images/termo1.png")
        
    def convertir (self, grados, tounidad):
        resultado = 0
        if tounidad == 'F':
            resultado = grados*9/5 + 32
        elif tounidad == 'C':
            resultado = (grados -32)*5/9
        else:
            resultado = grados
            
        return int (resultado)        

class Selector ():
    __tipoUnidad = None
    
    def __init__ (self, unidad = 'C'):
        self.__customes = []
        self.__customes.append (pygame.image.load ('images/posiF.png'))
        self.__customes.append (pygame.image.load ('images/posiC.png'))
        
        self.__tipoUnidad = unidad
        
    def custome (self):
        if self.__tipoUnidad == 'F':
            return self.__customes [0]
        else:
            return self.__customes [1]
        
    def change (self):
        if self.__tipoUnidad == 'F':
            self.__tipoUnidad = 'C'
        else:
            self.__tipoUnidad = 'F'
            
    def unidad (self):
        return self.__tipoUnidad


class NumberInput ():
    __value = 0
    __strValue = ""
    __position = [0, 0]
    __size = [0, 0]
    __pointCount = 0
    
    def __init__ (self, value=0):
        self.__font = pygame.font.SysFont('Arial', 28)
        self.__strValue = str(value)
        self.value(value)
    
    def on_event (self, event):
        if event.type == KEYDOWN:
            if event.unicode.isdigit() and len(self.__strValue) < 10 or (event.unicode == "." and self.__pointCount == 0):
                self.__strValue += event.unicode
                self.value (self.__strValue)
                if event.unicode == ".":
                    self.__pointCount += 1
                    
            elif event.key == K_BACKSPACE:
                if self.__strValue [-1] == ".":
                    self.__pointCount -= 1
                self.__strValue = self.__strValue [:-1]
                self.value (self.__strValue)
                
                    
    def render (self):
        textBlock = self.__font.render (self.__strValue, True, (74, 74, 74))
        rect = textBlock.get_rect()
        rect.left = self.__position [0]
        rect.top = self.__position [1]
        rect.size = self.__size
        
        return (rect, textBlock)
        
    def value (self, val=None):
        if val == None:
            return self.__value
        else:
            val = str(val)
            try:
                self.__value = int(val)
                self.__strValue = val
                if "." in self.__value:
                    self.__pointCount = 1
                else:
                    self.pointCount = 0
            except:
                pass
    
    def width (self, val=None):
        if val == None:
            return self.__size [0]
        else:
            try:
                self.__size [0] = int(val)
            except:
                pass
            
    def height (self, val=None):
        if val == None:
            return self.__size [1]
        else:
            try:
                self.__size [1] = int(val)
            except:
                pass
    
    def size (self, val=None):
        if val == None:
            return self.__size
        else:
            try:
                w = int(val[0])
                h = int(val[1])
                self.__size = [int(val[0]), int(val[1])]
            except:
                pass
      
    def posX (self, val=None):
        if val == None:
            return self.__position [0]
        else:
            try:
                self.__position [0] = int(val)
            except:
                pass
            
    def posY (self, val=None):
        if val == None:
            return self.__position [1]
        else:
            try:
                self.__position [1] = int(val)
            except:
                pass
    
    def pos (self, val=None):
        if val == None:
            return self.__position
        else:
            try:
                self.__position = [int(val[0]), int(val[1])]
            except:
                pass

class mainApp ():
    termometro = None
    entrada = None
    selector = None
    
    def __init__ (self):
        self.__screen = pygame.display.set_mode ((290, 415))
        pygame.display.set_caption ('Termómetro')
        self.__screen.fill ((244, 236, 203))
        
        self.termometro = Termometro ()
        self.entrada = NumberInput ()
        self.entrada.pos ((106, 58))
        self.entrada.size ((133, 28))
        
        self.selector = Selector ()
        
    def __on_close (self):
        pygame.quit()
        sys.exit()
        
    def start (self):
        while True:
            for event in pygame.event.get():
                if event.type == QUIT:
                    self.__on_close ()
                
                self.entrada.on_event (event)
                
                if event.type == pygame.MOUSEBUTTONDOWN:
                    self.selector.change ()
                    grados = self.entrada.value()
                    nuevaUnidad = self.selector.unidad()
                    temperatura = self.termometro.convertir (grados, nuevaUnidad)
                    self.entrada.value (int(temperatura))
            
            # Pintamos otra vez el fondo de pantalla
            self.__screen.fill ((244, 236, 203))
               
            # Pintamos termómetro en su posición.
            self.__screen.blit (self.termometro.custom, (50, 34))
            
            # Pintamos el cuadro de texto con el valor.
            text = self.entrada.render() # Obtenemoos el rectángulo blanco y foto de texto y la asignamos a text.
            pygame.draw.rect(self.__screen, (255, 255, 255), text[0]) # Creámos rectángulo blanco con datos en su posición tamaño.
            self.__screen.blit (text[1], self.entrada.pos()) # Pintamos la foto del texto en el cuadro
            
            # Pintamos el selector
            self.__screen.blit (self.selector.custome(), (112, 153))
            
            pygame.display.flip()
    
    
                                                                       

if __name__ == '__main__':
    pygame.init()
    app = mainApp()
    app.start()