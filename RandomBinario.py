import random
import sys
import Heroe as h
import Calculos as c

GolpeFuego = h.GolpeFuego()
BolaFuego = h.BolaFuego()
Llamarada = h.Llamarada()
Explosion = h.Explosion()

GolpeRayo = h.GolpeRayo()
BolaRayo = h.BolaRayo()
Relampago = h.Relampago()
Tormenta = h.Tormenta()

GolpeAgua = h.GolpeAgua()
BolaAgua = h.BolaAgua()
Ciclon = h.Ciclon()
Tsunami = h.Tsunami()

GolpeAire = h.GolpeAire()
BolaAire = h.BolaAire()
Ventisca = h.Ventisca()
Tornado = h.Tornado()

GolpeRoca = h.GolpeRoca()
BolaTierra = h.BolaTierra()
Derrumbe = h.Derrumbe()
Terremoto = h.Terremoto()


poder_list = [GolpeFuego, BolaFuego, Llamarada, Explosion, GolpeRayo, BolaRayo, Relampago, Tormenta,
            GolpeAgua, BolaAgua, Ciclon, Tsunami, GolpeAire, BolaAire, Ventisca, Tornado,
            GolpeRoca, BolaTierra, Derrumbe, Terremoto]
iter = int(sys.argv[2])
a = sys.argv[1]

def generate_binary(a):
    list_r = []
    for i in range(int(a)):
        random_ones = "{0:020b}".format(random.randint(0, (2**4)))
        templist = list(random_ones)
        random.shuffle(templist)
        list_r.append("".join(templist))
    return list_r

def posicion_true(lista):
    posicion = []
    for i in lista:
        p = []
        #print(i)
        for j in range(len(i)):
            #print(i[j])
            if(i[j] == '1'):
                p.append(j)
        posicion.append(p)
    return posicion

def poderes_true(poder, pos):
    for i in range(int(a)):
        for j in range(20):
            if(j in pos[i]):
                print(j+1)
                print(poder[j].__class__.__name__)
                print(poder[j].damage)
                print()

def poderes_main(poder, pos, h1, h2):
    peso_cromosomas = []
    for i in range(int(a)):#for para lista de cromosomas
        peso_total = 0
        for j in range(20):#for para cromosoma
            if(j in pos[i]):
                if(c.Peso(h1, h2, poder[j]) == 0):
                    peso_cromosomas.append(0)
                    #print('if')
                    #print(peso_cromosomas)
                    break
                else:
                    peso_total = peso_total+c.Peso(h1, h2, poder[j])
                    #print('else')
                    #print(peso_total)
            if(j in pos[i] and c.Peso(h1, h2, poder[j]) == 0):#Rompe el for del cromosoma si es igual a 0
                break
        if(j in pos[i] and c.Peso(h1, h2, poder[j]) == 0): #Continua con la sig iteracion de la lista si es igual a 0
            continue
        #print(peso_total)
        peso_cromosomas.append(peso_total)
        #print(peso_cromosomas)
    return peso_cromosomas

def seleccion_cromosomas(peso_cromo, peso_gen):
    generacion_temporal = []
    cromo_prob = []
    for i in peso_cromo:
        cromo_prob.append(i/peso_gen)
    #print(cromo_prob)
    #print(sum(cromo_prob))
    while(len(generacion_temporal) < 20):
        ruleta = random.random()
        #print(ruleta) #sumar valores de cromo_prob y si es mayor que ruleta, es el cromosoma elegido
        ruleta_sum = 0
        for i in range(len(cromo_prob)):
            ruleta_sum = ruleta_sum+cromo_prob[i]
            #print(ruleta_sum)
            if(ruleta_sum > ruleta):
                generacion_temporal.append(blist[i])
                #print(generacion_temporal)
                break
            else:
                #print('still minor')
                continue
    #print(generacion_temporal)
    for i in range(0, len(generacion_temporal), 2):
        r_temp = random.randint(1, 20)
        t1_inicio = generacion_temporal[i][:r_temp]
        t1_final = generacion_temporal[i][r_temp:]
        t2_inicio = generacion_temporal[i+1][:r_temp]
        t2_final = generacion_temporal[i+1][r_temp:]
        generacion_temporal[i] = t1_inicio+t2_final
        generacion_temporal[i+1] = t2_inicio+t1_final
    #print()
    #print(generacion_temporal)
    for i in range(len(generacion_temporal)):
        tlist = list(generacion_temporal[i])
        for j in range(len(tlist)):
            r_temp = random.randint(1, 11)
            #print(r_temp)
            if(r_temp == 1):
                #print('changed ', j)
                #print(tlist)
                #print(tlist[j])
                if(tlist[j] == '0'):
                    tlist[j] = '1'
                else:
                    tlist[j] = '0'
                #print(tlist[j])
                #print(tlist)
        generacion_temporal[i] = "".join(tlist)
    #print()
    return generacion_temporal
#Esto es un comentario para probar si el commit se aplica y se diferencian las branches
#GRACIAS :* SI FUNCIONAAAA!!!!

for i in range(iter):
    blist = generate_binary(a)
    pos = posicion_true(blist)
    print(blist)
    #print(pos)
    print()
    #print()
    peso_cromosomas = poderes_main(poder_list, pos, c.k1, c.s2)
    #print(peso_cromosomas)
    peso_generacion = sum(peso_cromosomas)
    #print(peso_generacion)
    nueva_generacion = seleccion_cromosomas(peso_cromosomas, peso_generacion)
    print(nueva_generacion)
    print()
