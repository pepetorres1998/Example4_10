

class Heroe:
    def __init__(self, name, element):
        self.name = name
        self.element = element
        self.vida = 100

class Samurai(Heroe):
    def __init__(self, name, element):
        super().__init__(name, element)
        self.defensa = 1.2
        self.ataque = 0.8
        self.energia = 12
        self.recuperacion = 15
        self.vida = 200

class Asesino(Heroe):
    def __init__(self, name, element):
        super().__init__(name, element)
        self.defensa = 0.4
        self.ataque = 2
        self.energia = 6
        self.recuperacion = 0

class Guerrero(Heroe):
    def __init__(self, name, element):
        super().__init__(name, element)
        self.defensa = 1.2
        self.ataque = 1
        self.energia = 10
        self.recuperacion = 5

class KOer(Heroe):
    def __init__(self, name, element):
        super().__init__(name, element)
        self.defensa = 0.3
        self.ataque = 3
        self.energia = 3
        self.recuperacion = 0
        self.vida = 100

#BASE
class Golpe():
    def __init__(self):
        self.consumo = 1
        self.element = ''
        self.damage = 20
        self.recoil = 0

class Bola():
    def __init__(self):
        self.consumo = 2
        self.element = ''
        self.damage = 40
        self.recoil = 0.2

class Medio():
    def __init__(self):
        self.consumo = 3
        self.element = ''
        self.damage = 50
        self.recoil = 0.3

class Alto():
    def __init__(self):
        self.consumo = 4
        self.element = ''
        self.damage = 100
        self.recoil = 0.4

#FUEGO
class GolpeFuego(Golpe):
    def __init__(self):
        super().__init__()
        self.element = 'Fuego'

class BolaFuego(Bola):
    def __init__(self):
        super().__init__()
        self.element = 'Fuego'

class Llamarada(Medio):
    def __init__(self):
        super().__init__()
        self.element = 'Fuego'

class Explosion(Alto):
    def __init__(self):
        super().__init__()
        self.element = 'Fuego'


#RAYO
class GolpeRayo(Golpe):
    def __init__(self):
        super().__init__()
        self.element = 'Rayo'

class BolaRayo(Bola):
    def __init__(self):
        super().__init__()
        self.element = 'Rayo'

class Relampago(Medio):
    def __init__(self):
        super().__init__()
        self.element = 'Rayo'

class Tormenta(Alto):
    def __init__(self):
        super().__init__()
        self.element = 'Rayo'



#AGUA
class GolpeAgua(Golpe):
    def __init__(self):
        super().__init__()
        self.element = 'Agua'

class BolaAgua(Bola):
    def __init__(self):
        super().__init__()
        self.element = 'Agua'

class Ciclon(Medio):
    def __init__(self):
        super().__init__()
        self.element = 'Agua'

class Tsunami(Alto):
    def __init__(self):
        super().__init__()
        self.element = 'Agua'



#AIRE
class GolpeAire(Golpe):
    def __init__(self):
        super().__init__()
        self.element = 'Aire'

class BolaAire(Bola):
    def __init__(self):
        super().__init__()
        self.element = 'Aire'

class Ventisca(Medio):
    def __init__(self):
        super().__init__()
        self.element = 'Aire'

class Tornado(Alto):
    def __init__(self):
        super().__init__()
        self.element = 'Aire'



#TIERRA
class GolpeRoca(Golpe):
    def __init__(self):
        super().__init__()
        self.element = 'Tierra'

class BolaTierra(Bola):
    def __init__(self):
        super().__init__()
        self.element = 'Tierra'

class Derrumbe(Medio):
    def __init__(self):
        super().__init__()
        self.element = 'Tierra'

class Terremoto(Alto):
    def __init__(self):
        super().__init__()
        self.element = 'Tierra'



#MAIN
a1 = Asesino('RandomName1', 'Fuego')
s1 = Samurai('SadBunny', 'Rayo')
g1 = Guerrero('NotToday', 'Agua')
k1 = KOer('SaltyRabbit', 'Aire')

list1 = [a1, s1, g1, k1]

def Printall(l):
    print('Nombre', 'Elemento', 'Vida', 'Defensa', 'Ataque', 'Energia', 'Recuperacion')
    for h1 in l:
        print(h1.__class__.__name__)
        print(h1.name, h1.element, h1.vida, h1.defensa, h1.ataque, h1.energia, h1.recuperacion)
        print()

#Printall(list1)
