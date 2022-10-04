import numpy as np
import math

# El sistema debe calcular la probabilidad de encontrarlo en una posición en particular
def superposicion (v,p):
    norma = 0
    for i in range (len(v)):
        n = abs(v[i])**2
        norma += n
    c = p*p
    return c/norma

#El sistema si se le da otro vector Ket debe buscar la probabilidad de transitar del primer vector al segundo.
def prob_ket(v1,v2):

    pro_int = np.inner(v1,v2)  #saca el producto interno de los dos vectores
    print (pro_int)
    norma1 = 0
    norma2= 0
    for i in range(len(v1)):    #norma del primer vector
        n = abs(v1[i])
        norma1 += n
    for i in range(len(v2)):   #norma del segundo vector
        n = abs(v2[i])
        norma2 += n
    normas = norma1*norma2      #producto de las 2 normas
    return pro_int/normas       #resultado

#Amplitud de transición. El sistema puede recibir dos vectores y calcular la probabilidad de transitar de el uno al otro después de hacer la observación
def complejo(c):
    mod = abs(c)**2
    return mod

def normaVector2(v):
    suma = 0
    for i in range(len(v)):
        suma += complejo(v[i])
    return math.sqrt(suma)

def transition(vec1, vec2):
    productoInterno = np.inner(vec1, vec2)
    normaVec1 = normaVector2(vec1)
    normaVec2 = normaVector2(vec2)
    ket = productoInterno /( (normaVec1)*(normaVec2))
    return np.round(ket)

vec1 = [(-1j), (1)]
vec2 = [(1), (-1j)]
print(transition(vec1, vec2))

#Ahora con una matriz que describa un observable y un vector ket, el sistema revisa que la matriz sea hermitiana, y si lo es, calcula la
# media y la varianza del observable en el estado dado
def Traspuesta(m1):
    result = [[0 for i in range(len(m1))] for j in range(len(m1[0]))]

    for i in range(len(m1[0])):
        for j in range(len(m1)):
            result[i][j] = m1[j][i]

    return(result)

#conjugada de una Matriz o un vector

def conjugarMtrx (m1):
    for i in range(len(m1)):
        for j in range(len(m1[0])):
            m1[i][j] = (m1[i][j][0], (-1) * m1[i][j][1])
    return (m1)

def dagaMtrz (m1):
    m = Traspuesta(m1)
    n = conjugarMtrx(m)
    return (n)

def hermitiana(m1):
    daga = dagaMtrz(m1[:])
    result = daga == m1
    if result == False:
        return False
    else:
        return True

def accion_matriz(m1,v1):
    accion = [[None for j in range(len(m1))] for i in range(len(v1[0]))]
    for i in range(len(m1)):
        for j in range(len(v1[0])):
            aux = (0, 0)
            for k in range(len(v1)):
                component1  = v1[k][j]
                component2 = m1[i][k]
                aux = sumacplx(aux, multcplx(component1, component2))
            accion[i][j] = aux
    return(accion)
def sumacplx(a,b):
    real = a[0] + b[0]
    img = a[1] + b[1]
    return (real, img)

# Multiplica complejos representados como una tupla
def multcplx(a,b):
    real = (a[0] * b[0]) - (a[1]* b[1])
    img = (a[0] * b[1]) + (b[0]*a[1])
    return (real, img)


def media(obser, vec_Estado):

    if hermitiana(obser) == True:
        multi = accion_matriz(obser, vec_Estado)
        media = np.inner(multi, vec_Estado)

    return media

def varianza(obser, vec_Estado):
    media1= media(obser, vec_Estado)
    identity = np.identity(len(vec_Estado))
    multi = media1*identity
    rest = (obser - multi)**2
    media (media(rest, vec_Estado))
    return media


#PRUEBAS
v = [(4+3j),(6-4j),(12-7j),(13j)]
v3 = [(5+2j),(-3j)]
v4 = [(5+2j),(1-1j)]
p = (4+3j)

def main():

    print(superposicion(v,p))
    print (prob_ket(v3,v4))

main()



