# Funciones de las variables usadas
# int n Numero de iteraciones
# float resultados [] vector de resultados de la ecuacion general [Ecuacion 6]
# float pcr Cálculo por medio de aproximacion de pc,r [Ecuacion 5]
# float lambdar calculo λr [Ecuacion 8]
# float pndr Cálculo del umbral inferior de credibilidad [Ecuacion 12]
# float pnfr Cálculo del umbral superior de credibilidad [Ecuacion 13]

#Adaptación

# Ecuaciones
from typing import Any, List
import numpy as np

#Listo
def factorial(numero):
    if numero <= 0:
        return 1
    factorial = 1
    while numero > 0:
        factorial = factorial * numero
        numero -= 1
    return factorial
#Listo
def evalua_ecuacion_general(r:int, l: int, m:int, pn: float)-> float:
    fact = ((factorial(r))/(factorial(l)*factorial(r-l)))*(pn**l)*((1-pn)**(r-l))
    return fact
#Listo
def evalua_ecuacion_general_derivada(r:int, l: int, m: int,pcr: float) -> float:
    fact = ((factorial(r)/(factorial(l)*factorial(r-l))))*(((-1)*pow(pcr,l)*(r-l)*(pow((1-pcr),(r-l-1)))+(l)*(pow((1-pcr),(r-l)))*(pow(pcr,(l-1)))))
    return fact
#Listo
def set_resultados_ecuacion_general(n: int, pn: float, r:int):  #Ecuacion 6 Grupo de votacion de tamaño r
    pr: float = 0.0
    m: int
    l: int
    i: int = 0
    lista_resultados: List[Any] = []

    if (r%2)==0:
        m=(r/2)+1
    else:
        m=(r+1)/2
    l=m
    # Calcula eliminacion total
    if n==-1:
        n = 0
        while pn>0.01:
            try:
                for l in np.arange(l, r, 1):
                    pr += evalua_ecuacion_general(r,l,pn)

                lista_resultados.append(pr)
                n += 1
                if pn == pr:
                    break
                else:
                    pn=pr
                    pr = 0
                    i +=1
            except:
                print("Fallo")

        return lista_resultados

    else:
        for i in range(0,n-1,1):
            try:
                for l in np.arange(l,r,1):
                    pr+=evalua_ecuacion_general(r,l,pn)
                lista_resultados.append(pr)
                pn=pr
                pr=0
            except:
                print("Fallo")
        return lista_resultados
#Listo
#Calcular PCR
def set_pcr(r:int):
    i: float = 0.0
    iaux: float
    m: float
    l: int
    primera=1
    pr = 0.0
    praux=0.0
    resta=-1.0
    resta2=0.0
    pcr: float

    if r==2:
        pcr=1.0
        return pcr
    else:
        if (r%2)==0: #Par
            iaux = 0
            while iaux <= 100:
                i = iaux/100.0
                m = (r/2)+1
                l = m
                while l<=r:
                    pr += evalua_ecuacion_general(r,l,i)
                    l += 1
                
                l=m
                while l<=r:
                    praux += evalua_ecuacion_general(r,l,pr)
                    l += 1

                if (((pr-praux) > 0) or ((pr-praux) < 0) and primera == 1):
                    primera = 0
                    resta = pr-praux
                else:
                    if (((pr-praux) > 0) or ((pr-praux) < 0) and (primera == 0)):
                        resta2 = pr-praux
                        if (((resta > 0) and (resta2 < 0)) or ((resta < 0) and (resta2 > 0))):
                            pcr = i
                            return pcr
                            break
                iaux += 1
        else:
            if ((r%2) != 0): #Par
                pcr = 0.50
                return pcr
#Umbral inferior de credibilidad
def set_pndr(lamdar: float, pcr: float, n: int):
    #Para n subniveles
    pndr = (pcr)*(1-(lamdar ** (-1*n))) * 100
    # Devolviendolo en porcentaje
    return pndr

#Umbral superior de credibilidad
def set_pnfdr(pndr: float, lamdar: float, n: int):
    #Para n subniveles
    pnrf = pndr + (lamdar ** (-1*n)) * 100
    # Devolviendolo en porcentaje
    return pnrf

def set_lamdar(pcr: float, r:int):
    lamdar: float = 0
    m: int
    l: int

    if((r%2)==0):
        m = (r/2) + 1
    else:
        m = (r+1) / 2
    l = m
    while l <= r:
        lamdar += evalua_ecuacion_general_derivada(r, l, pcr)
        l += 1
    
    return lamdar


#Funcion de evaluacion de algoritmo genetico

#Funcion de optimiza A

#Calculo final es la funcion para realizar los calculos de prediccion, umbrales y eliminación total

def set_pn() -> float:
    n_resultados: int
    resultados: List()  #Resultados de la ecuacion general(Ecuacion 6)
    pn: float           #Aceptación final
    i: int
    n: int
    r: int
    p0: float
    n_resultados = set_resultados_ecuacion_general(n, p0, r)