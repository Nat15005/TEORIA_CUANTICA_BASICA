import numpy as np

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


def main():
    v = [(4+3j),(6-4j),(12-7j),(13j)]
    v3 = [(5+2j),(-3j)]
    v4 = [(5+2j),(1-1j)]
    p = (4+3j)
    print(superposicion(v,p))
    print (prob_ket(v3,v4))

main()