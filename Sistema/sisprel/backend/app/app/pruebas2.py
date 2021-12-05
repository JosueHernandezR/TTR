from typing import Any, List
import numpy as np
import math
from decimal import Decimal

class Ecuaciones:
    n: int = 0  # n = número de iteraciones
    resultados: List = []  # vector de resultados de la ecuación general[Ecuación 6]
    pcr: Decimal = 0.0  # cálculo por medio de aproximación de pc,r [Ecuación 5]
    lambdar: Decimal = 0.0  # cálculo de λr [Ecuación 8]
    pndr: Decimal = 0.0  # cálculo del umbral inferior de credibilidad [Ecuación 12]
    pnfr: Decimal = 0.0  # cálculo del umbral superior de credibilidad [Ecuación 13]

    def factorial(self, numero: int):
        if numero <= 0:
            return 1
        factorial = 1
        while numero > 0:
            factorial = factorial * numero
            numero -= 1
        return factorial

    def evalua_ecuacion_general(self, r: int, l: int, pn: Decimal):
        # a = self.factorial(r)
        # b = self.factorial(l) * self.factorial(r-l)

        return (
            ((self.factorial(r))/((self.factorial(l)) * (self.factorial(r-l)))) *
            (math.pow(pn, l)) *
            (math.pow((1-pn), (r-l)))
        )

    def evalua_ecuacion_general_derivada(self, r: int, l: int, pcr: Decimal):
        a = self.factorial(r)
        b = self.factorial(l) * self.factorial(r-l)
        
        # c = pcr ** l
        c = math.pow(pcr, l)

        d = r-l
        # e = (1-pcr) ** (r-l-1)
        e = math.pow((1-pcr), (r-l-1))
        f = -1

        g = (1-pcr) ** (r-l)
        h = l
        # i = pcr ** (l-1)
        i = math.pow(pcr, l-1)

        return (  (a/b) * ((c*d*e*f) + (g*h*i))
            # ((self.factorial(r))/(self.factorial(l) * self.factorial(r-l))) *
            # ((math.pow(pcr, l) * (r-l) * math.pow((1-pcr), (r-l-1)) * (-1)) +
            # (math.pow((1-pcr), (r-l)) * l * math.pow(pcr, (l-1))))
        )

    def set_lamdar(self, pcr: Decimal, r: int) -> None:
        m: int = 0
        l: int = 0

        if (r % 2) == 0:
            m = (r / 2) + 1
        else:
            m = (r + 1) / 2

        l = m
        for l in np.arange(l, r+1):
            self.lambdar += self.evalua_ecuacion_general_derivada(r, l, pcr)

    def set_pndr(self, lambdar: Decimal, pcr: Decimal, n: int) -> None:
        # Para n subniveles
        self.pndr = (pcr) * (1 - (math.pow(lambdar, (-1 * n))))

    # Umbral superior de credibilidad
    def set_pnfr(self, pndr: Decimal, lamdar: Decimal, n: int) -> None:
        # Para n subniveles
        self.pnfr = pndr + math.pow(lamdar, (-1 * n))

    def set_pcr(self, r: int):
        i: Decimal = 0.0
        iaux: int = 0
        m: int = 0
        l: int = 0
        primera: int = 1
        pr: Decimal = 0.0
        praux: Decimal = 0.0
        resta: Decimal = -1.0
        resta2: Decimal = 0.0

        if (r == 2):
            self.pcr = 1.0
        else:   
            if ((r % 2) == 0):  # Par
                if r == 4:
                    self.pcr = 0.77
                elif r == 6:
                    self.pcr = 0.65
                elif r == 8: 
                    self.pcr = 0.60
                elif r == 10:
                    self.pcr = 0.58
                elif r == 12:
                    self.pcr = 0.56
                elif r == 14:
                    self.pcr = 0.55
                elif r == 16:
                    self.pcr = 0.54
                elif r == 18:
                    self.pcr = 0.54
                elif r == 20:
                    self.pcr = 0.53
                else:
                    return "No hay calculos para estos valores" 

                # Este código no funciona
                # for iaux in np.arange(iaux, 100 + 1):
                #     i = iaux / 100.0
                #     pr = 0.0
                #     praux = 0.0
                #     m = (r / 2) + 1
                #     l = m

                #     for l in np.arange(l, r +1):
                #         pr += self.evalua_ecuacion_general(r=r, l=l, pn=i)

                #     for l in np.arange(l, r +1 ):
                #         praux += self.evalua_ecuacion_general(r, l, pr)
                    
                #     if (((pr - praux) > 0) or ((pr - praux) < 0) and primera == 1):
                #         primera = 0
                #         resta = pr - praux
                #     else:
                #         if (((pr - praux) > 0) or ((pr - praux) < 0) and (primera == 0)):
                #             resta2 = pr - praux
                #             if ((resta > 0) and (resta2 < 0)) or (
                #                 (resta < 0) and (resta2 > 0)
                #             ):
                #                 self.pcr = i
                #                 break
            else:
                if ((r % 2) != 0):  # Impar
                    self.pcr = 0.50

    def set_resultados_ecuacion_general(self, n: int, pn: Decimal, r: int) -> None:  # Ecuacion 6 Grupo de votacion de tamaño r
        pr: Decimal = 0.0
        aux: Decimal = 0.0
        m: int = 0
        l: int = 0
        i: int = 0
        lista_resultados: List = []

        if (r % 2) == 0:
            m = (r / 2) + 1
        else:
            m = (r + 1) / 2
        l = m
        # Calcula eliminacion total
        if n == -1:
            self.n = 0
            while pn > 0.01:
                try:
                    for l in np.arange(l, r + 1):
                        pr += self.evalua_ecuacion_general(r, l, pn)

                    lista_resultados.append(str(pr))
                    self.n += 1
                    if pn == pr:
                        break
                    else:
                        pn = pr
                        pr = 0
                        i += 1
                except:
                    raise Exception("Ocurrio un error :(")

            self.resultados = [0] * self.n
            i = 0
            for elem in lista_resultados:
                self.resultados = elem
                i += 0
        else:
            self.resultados = [0] * self.n
            for i in np.arange(0, n):
                try:
                    for j in np.arange(l, r + 1):
                        pr += self.evalua_ecuacion_general(r, j, pn)
                    #self.resultados[i] =  pr
                    self.resultados.append(pr)
                    pn = pr
                    pr = 0
                except:
                    raise Exception("Ocurrio un error :(")

    def get_pcr(self):
        return self.pcr
    
    def get_lambdar(self):
        return self.lambdar

    def get_pndr(self):
        return self.pndr
    
    def get_pnfr(self):
        return self.pnfr
    
    def get_resultados_ecuacion_general(self):
        return self.resultados
    


Ecuaciones = Ecuaciones()
"""
Pruebas para r = 4
n = 3 -> pndr = 59.4281; pnfr = 82.2488
n = 4 -> pndr = 66.2619; pnfr = 80.2075
n = 5 -> pndr = 70.439 ; pnfr = 78.9601
"""
r = 4
p0 = 45.99/100
n1 = 3; n2 = 4; n3 = 5;
l = (r/2) + 1
# PCR
Ecuaciones.set_pcr(r=r)
pcr = Ecuaciones.get_pcr()
print("PCR", Ecuaciones.get_pcr())
# Lambdar
Ecuaciones.set_lamdar(pcr, r)
lambdar = Ecuaciones.get_lambdar()
print("Lambdar",Ecuaciones.get_lambdar())
lambdar1 = 1.64
# PNDR / PNFR 1
Ecuaciones.set_pndr(lambdar=lambdar, pcr=pcr, n=1)
pndr = Ecuaciones.get_pndr()
print("PNDR: ",pndr)

Ecuaciones.set_pnfr(pndr=pndr, lamdar=lambdar, n=1)
pnfr = Ecuaciones.get_pnfr()
print("PNFR: ",pnfr)

#Resultados n
Ecuaciones.set_resultados_ecuacion_general(n=1,pn=p0, r=r)
ecuacion_general = Ecuaciones.get_resultados_ecuacion_general()
print(ecuacion_general)

# var = 0.0
# for l in np.arange(l, r,1):
#     a = Ecuaciones.factorial(r)
#     b = Ecuaciones.factorial(l) * Ecuaciones.factorial(r-l)
    
#     # v = pcr ** l
#     c = pow(pcr, l)

#     d = r-l
#     # e = (1-pcr) ** (r-l-1)
#     e = pow((1-pcr), (r-l-1))
#     f = -1

#     g = (1-pcr) ** (r-l)
#     h = l
#         # i = pcr ** (l-1)
#     i = pow(pcr, l-1)
#     var = var + (a/b) * ((c*d*e*f) + (g*h*i))
#     print(a)
#     print(b)
#     print(c)
#     print(d)
#     print(e)
#     print(f)
#     print(g)
#     print(h)
#     print(i)
#     #var = var + Ecuaciones.evalua_ecuacion_general_derivada(r=r, l=l, pcr=pcr)

# print(a)
# print(b)
# print(c)
# print(d)
# print(e)
# print(f)
# print(g)
# print(h)
# print(i)

# print(var)
# #print(Ecuaciones.evalua_ecuacion_general_derivada(r=r, l=l, pcr=pcr))
# print(Ecuaciones.factorial(numero=r))
# print(Ecuaciones.factorial(numero=l))
# print(Ecuaciones.factorial(numero=r-l))
