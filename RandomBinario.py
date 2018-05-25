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

#PERSONAJES
KOerFuego = h.KOer('Arthit', 'Fuego')
KOerAgua = h.KOer('Sasithorn', 'Agua')
KOerTierra = h.KOer('Ubon', 'Tierra')
KOerRayo = h.KOer('Pakpao', 'Rayo')
KOerAire = h.KOer('Sukhon', 'Aire')

SamuraiFuego = h.Samurai('Huo', 'Fuego')
SamuraiAgua = h.Samurai('Shui', 'Agua')
SamuraiTierra = h.Samurai('Tu', 'Tierra')
SamuraiRayo = h.Samurai('Kyon', 'Rayo')
SamuraiAire = h.Samurai('Fei', 'Aire')

AsesinoFuego = h.Asesino('Ryu', 'Fuego')
AsesinoAgua = h.Asesino('Yoko', 'Agua')
AsesinoTierra = h.Asesino('Riku', 'Tierra')
AsesinoRayo = h.Asesino('Toshio', 'Rayo')
AsesinoAire = h.Asesino('Sayaka', 'Aire')

GuerreroFuego = h.Guerrero('Lena', 'Fuego')
GuerreroAgua = h.Guerrero('Ondina', 'Agua')
GuerreroTierra = h.Guerrero('Jorgen', 'Tierra')
GuerreroRayo = h.Guerrero('Thor', 'Rayo')
GuerreroAire = h.Guerrero('Aren', 'Aire')

personajes_list = [SamuraiFuego, SamuraiAgua, SamuraiTierra, SamuraiAire, SamuraiRayo,
                GuerreroFuego, GuerreroAgua, GuerreroTierra, GuerreroAire, GuerreroRayo,
                KOerFuego, KOerAgua, KOerTierra, KOerAire, KOerRayo,
                AsesinoFuego, AsesinoAgua, AsesinoTierra, AsesinoAire, AsesinoRayo]

poder_list = [GolpeFuego, BolaFuego, Llamarada, Explosion, GolpeRayo, BolaRayo, Relampago, Tormenta,
            GolpeAgua, BolaAgua, Ciclon, Tsunami, GolpeAire, BolaAire, Ventisca, Tornado,
            GolpeRoca, BolaTierra, Derrumbe, Terremoto]
iter = 40
a = 40

#Funcion que genera los cromosomas binarios, recibe el primer argumento del cmd
def generate_binary(a):
    list_r = []
    for i in range(int(a)):
        random_ones = "{0:020b}".format(random.randint(0, (2**4)))
        templist = list(random_ones)
        random.shuffle(templist)
        list_r.append("".join(templist))
    return list_r

#Funcion que obtiene la posicion de los '1' en los cromosomas
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

#Funcion que verifica cuales poderes estan en la lista de cromosomas dependiendo
#de la posicion de los '1'
def poderes_true(poder, pos):
    for i in range(int(a)):
        for j in range(20):
            if(j in pos[i]):
                print(j+1)
                print(poder[j].__class__.__name__)
                print(poder[j].damage)
                print()

#Funcion que verifica cuales poderes estan en el cromosoma de mayor peso
def poderes_recomendados(poder, pos):
    for j in range(20):
        if(j in pos[0]):
            print(j+1)
            print(poder[j].__class__.__name__)
            print(poder[j].damage)
            print()

#Funcion que define el peso de los diferentes cromosomas
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
        if(j in pos[i] and c.Peso(h1, h2, poder[j]) == 0):#Continua con la sig iteracion de la lista si es igual a 0
            continue
        #print(peso_total)
        peso_cromosomas.append(peso_total)
        #print(peso_cromosomas)
    return peso_cromosomas

#Funcion que regresa los 3 poderes de mayor peso, del cromosoma de mayor peso, de todas las
#generaciones.
def poderes_indiv(poder, pos, h1, h2):
    peso_cromosomas = []
    peso_cromo_1 = {}
    poderes_sorted = []
    for j in range(20):#for para cromosoma
        if(j in pos[0]):
            peso_cromosomas.append(c.Peso(h1, h2, poder[j]))
            peso_cromo_1[c.Peso(h1, h2, poder[j])] = poder[j].__class__.__name__#Hacer todo en peso_cromosomas
        peso_sorted = sorted(peso_cromosomas)
        peso_sorted = peso_sorted[::-1]
    for i in range(len(peso_sorted)):
        poderes_sorted.append(peso_cromo_1.get(peso_sorted[i]))
    #print(poderes_sorted)
    #print(peso_sorted)
    mejores = poderes_sorted[:3]
    #print(mejores)
    return mejores
    #return peso_sorted


#Funcion que combina dos listas en un índice
def combinar_listas(lista1, lista2):
    return dict(zip(lista1, lista2))

#Funcion que define el mayor peso en la lista de pesos de una generacion
def mayor_peso(peso_cromosomas):
    sorteados = sorted(peso_cromosomas)
    mejor = sorteados[len(peso_cromosomas)-1]
    return mejor

#Funcion que define el cromosoma del mayor peso de una generacion
def mayor_peso_index(index_cromosomas):
    sorteados = sorted(index_cromosomas)
    mejor = sorteados[len(index_cromosomas)-1]
    return index_cromosomas[mejor]

#Funcion que devuelve el mayor de los pesos mayores de todas las generaciones
def mayor_todos(mayores_lista):
    t_temporal = sorted(mayores_lista)
    return(t_temporal[len(t_temporal)-1])

#Funcion que devuelve el cromosoma del mayor de los pesos mayores
def mayor_todos_index(mayores_lista, mayores_index, mayores_todos_lista):
    for i in range(len(mayores_lista)):
        if(mayores_lista[i] == mayores_todos_lista):
            pos_temp = i
            break
    return mayores_index[i]

#Funcion que devuelve la nueva generacion de cromosomas
def seleccion_cromosomas(peso_cromo, peso_gen, blist):
    generacion_temporal = []
    cromo_prob = []
    for i in peso_cromo:
        cromo_prob.append(i/peso_gen)
    #print(cromo_prob)
    #print(sum(cromo_prob))
    while(len(generacion_temporal) < int(a)):#Mientras la nueva generaicon sea menor a la vieja
        ruleta = random.random()
        #print(ruleta) #sumar valores de cromo_prob y si es mayor que ruleta, es el cromosoma elegido
        ruleta_sum = 0
        for i in range(len(cromo_prob)):#For i en el rango de la lista de probabilidades de los cromosomas
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
    for i in range(0, len(generacion_temporal), 2):#for i en el rango de la nueva generacion
        r_temp = random.randint(1, 20)#Numero random para cortar las parejas de cromosomas
        t1_inicio = generacion_temporal[i][:r_temp]
        t1_final = generacion_temporal[i][r_temp:]
        t2_inicio = generacion_temporal[i+1][:r_temp]
        t2_final = generacion_temporal[i+1][r_temp:]
        generacion_temporal[i] = t1_inicio+t2_final
        generacion_temporal[i+1] = t2_inicio+t1_final
    #print()
    #print(generacion_temporal)
    for i in range(len(generacion_temporal)):#for i en rango del tamaño de nueva generacion
        tlist = list(generacion_temporal[i])#lista temporal para no cambiar valores a str
        for j in range(len(tlist)):#for j en rango del cromosoma hecho lista
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
        generacion_temporal[i] = "".join(tlist)#devolver el cromosoma a string
    #print()
    return generacion_temporal

#Funcion main
def main_program(h1, h2):
    mayores_lista = []
    mayores_index = []
    for i in range(iter):
        if(i == 0):
            blist = generate_binary(a)
        pos = posicion_true(blist)
        print(blist)
        #print(pos)
        print()
        #print()
        peso_cromosomas = poderes_main(poder_list, pos, h1, h2)
        print(peso_cromosomas)
        index_cromosomas = combinar_listas(peso_cromosomas, blist)
        print(index_cromosomas)
        mayores_index.append(mayor_peso_index(index_cromosomas))
        mayores_lista.append(mayor_peso(peso_cromosomas))
        peso_generacion = sum(peso_cromosomas)
        #print(peso_generacion)
        blist = seleccion_cromosomas(peso_cromosomas, peso_generacion, blist)
        print(blist)
        print()
    print(mayores_index)
    print(mayores_lista)
    mayores_todos_lista = mayor_todos(mayores_lista)
    mayores_todos_index = mayor_todos_index(mayores_lista, mayores_index, mayores_todos_lista)
    print(mayores_todos_lista, mayores_todos_index)
    pos = posicion_true([mayores_todos_index])
    print(pos)
    poderes_recomendados(poder_list, pos)
    mejores_3 = poderes_indiv(poder_list, pos, h1, h2)
    #print(h1.name)

def checar_personaje(strh):
    if(strh == 'Samurai Fuego'):
        return SamuraiFuego
    elif(strh == 'Samurai Agua'):
        return SamuraiAgua
    elif(strh == 'Samurai Tierra'):
        return SamuraiTierra
    elif(strh == 'Samurai Aire'):
        return SamuraiAire
    elif(strh == 'Samurai Rayo'):
        return SamuraiRayo
    elif(strh == 'Guerrero Fuego'):
        return GuerreroFuego
    elif(strh == 'Guerrero Agua'):
        return GuerreroAgua
    elif(strh == 'Guerrero Tierra'):
        return GuerreroTierra
    elif(strh == 'Guerrero Aire'):
        return GuerreroAire
    elif(strh == 'Guerrero Rayo'):
        return GuerreroRayo
    elif(strh == 'Asesino Fuego'):
        return AsesinoFuego
    elif(strh == 'Asesino Agua'):
        return AsesinoAgua
    elif(strh == 'Asesino Tierra'):
        return AsesinoTierra
    elif(strh == 'Asesino Aire'):
        return AsesinoAire
    elif(strh == 'Asesino Rayo'):
        return AsesinoRayo
    elif(strh == 'KOer Fuego'):
        return KOerFuego
    elif(strh == 'KOer Agua'):
        return KOerAgua
    elif(strh == 'KOer Tierra'):
        return KOerTierra
    elif(strh == 'KOer Aire'):
        return KOerAire
    elif(strh == 'KOer Rayo'):
        return KOerRayo

def main_recomendacion_interfaz(strh1, strh2):
    h1 = checar_personaje(strh1)
    h2 = checar_personaje(strh2)
    mayores_lista = []
    mayores_index = []
    for i in range(iter):
        if(i == 0):
            blist = generate_binary(a)
        pos = posicion_true(blist)
        #print(blist)
        #print(pos)
        #print()
        #print()
        peso_cromosomas = poderes_main(poder_list, pos, h1, h2)
        #print(peso_cromosomas)
        index_cromosomas = combinar_listas(peso_cromosomas, blist)
        #print(index_cromosomas)
        mayores_index.append(mayor_peso_index(index_cromosomas))
        mayores_lista.append(mayor_peso(peso_cromosomas))
        peso_generacion = sum(peso_cromosomas)
        #print(peso_generacion)
        blist = seleccion_cromosomas(peso_cromosomas, peso_generacion, blist)
        #print(blist)
        #print()
    #print(mayores_index)
    #print(mayores_lista)
    mayores_todos_lista = mayor_todos(mayores_lista)
    mayores_todos_index = mayor_todos_index(mayores_lista, mayores_index, mayores_todos_lista)
    #print(mayores_todos_lista, mayores_todos_index)
    pos = posicion_true([mayores_todos_index])
    #print(pos)
    #poderes_recomendados(poder_list, pos)
    mejores_3 = poderes_indiv(poder_list, pos, h1, h2)
    #print(h1.name)
    return mejores_3

if(__name__ == '__main__'):
    main_program(SamuraiFuego, GuerreroRayo)
