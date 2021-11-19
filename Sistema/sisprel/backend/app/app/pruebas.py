
from typing import Any, List
import numpy as np
import math

def factorial(numero):
    if numero <= 0:
        return 1
    factorial = 1
    while numero > 0:
        factorial = factorial * numero
        numero -= 1
    return factorial

def evalua_ecuacion_general(r:int,l:int, pn: float):
    fact: float = 0
    fact += ((factorial(r))/(factorial(l)*factorial(r-l)))*((math.pow(pn,l)))*(math.pow((1-pn),(r-l)))
    return fact

def evalua_ecuacion_general_derivada(r:int, l: int,pcr: float):
    fact = (factorial(r)/(factorial(l)*factorial(r-l)))*((-1)*math.pow(pcr,l)*(r-l)*(math.pow((1-pcr),(r-l-1)))+(l)*(math.pow((1-pcr),(r-l)))*(math.pow(pcr,(l-1))))
    return fact

def set_lamdar(pcr: float, r:int):
    lambdar: float = 0
    i: int = 0
    m: int
    l: int

    if((r%2)==0):
        m = (r/2) + 1
    else:
        m = (r+1) / 2
    l = m

    for l in np.arange(l,r,1):
        lambdar += evalua_ecuacion_general_derivada(r,l,pcr)
    
    return lambdar

def set_resultados_ecuacion_general(n: int, pn: float, r:int):  #Ecuacion 6 Grupo de votacion de tamaño r
    pr: float = 0.0
    aux: float
    m: int
    l: int
    i: int = 0
    lista_resultados: list = list()

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
        for i in np.arange(0,n,1):
            try:
                for l in np.arange(l,r,1):
                    pr+=evalua_ecuacion_general(r,l,pn)
                lista_resultados.append(pr)
                pn=pr
                pr=0
            except:
                print("Fallo")
        return lista_resultados

def set_pcr(r:int):
    i: float = 0.0
    iaux: int = 0
    m: int
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
            for iaux in np.arange(iaux,100,1):
                i = iaux/100.0
                m = (r/2)+1
                l = m
                for l in np.arange(l,r,1):
                    pr += evalua_ecuacion_general(r,l,i)
                for l in np.arange(l,r,1):
                    praux += evalua_ecuacion_general(r,m,pr)

                if (((pr-praux) > 0) or ((pr-praux) < 0) and primera == 1):
                    primera = 0
                    resta = pr-praux
                else:
                    if (((pr-praux) > 0) or ((pr-praux) < 0) and (primera == 0)):
                        resta2 = pr-praux
                        if (((resta > 0) and (resta2 < 0)) or ((resta < 0) and (resta2 > 0))):
                            pcr = i
                            return pcr
            
        else:
            if ((r%2) != 0): #Par
                pcr = 0.50
                return pcr

def set_pndr(lambdar: float, pcr: float, n: int):
    #Para n subniveles
    pndr = (pcr)*(1-(math.pow(lambdar,(-1*n))))
    # Devolviendolo en porcentaje
    return pndr

#Umbral superior de credibilidad
def set_pnfr(pndr: float, lamdar: float, n: int):
    #Para n subniveles
    pnrf = pndr + math.pow(lamdar,(-1*n))
    # Devolviendolo en porcentaje
    return pnrf
def set_pn(n:int, p0:float, r:int):
    n_resultados:int
    resultados: list
    pn: float
    i: int = 0
    resultados = set_resultados_ecuacion_general(n,p0,r)
    n_resultados = n
    pn=resultados[(n_resultados-1)]
    for i in np.arange(i, n_resultados, 1):
        resultados[i] *=100
    pn *=100
    #Aqui hay error
    print(resultados)
    return pn

p0: float = 69



i: int =0
r:int=4
n = 3
pcr = set_pcr(r)

if((r%2)==0):
    m = (r/2) + 1
else:
    m = (r+1) / 2

print("PCR", pcr)
# pr: float = 0.0
if (r%2)==0:
    m=(r/2)+1
else:
    m=(r+1)/2
l=m
pn_test = set_pn(n,p0,r)
print("pn", pn_test)
lambdar = set_lamdar(pcr,r)
pndr = set_pndr(lambdar,pcr,n)
pnfdr = set_pnfr(pndr,lambdar,n)
ecuacion_general_derivada = evalua_ecuacion_general_derivada(r,l,pcr)
ecuacion_general = evalua_ecuacion_general(r,l,pn_test)
eliminacion_total = set_resultados_ecuacion_general(-1,p0,r)


print("Lambdar",lambdar)
print("PNDR",pndr)
print("PNFDR",pnfdr)
print("Ecuacion general derivada", ecuacion_general)

resultados_ecuacion_general = set_resultados_ecuacion_general(n,pn_test,r)
print("Resultados ecuacion general", resultados_ecuacion_general)
print("PN test",pn_test)
print("eliminacion total", eliminacion_total)