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

    def __init__(self) -> None:
        self.reset()

    def factorial(self, numero: int):
        if numero <= 0:
            return 1
        factorial = 1
        while numero > 0:
            factorial = factorial * numero
            numero -= 1
        return factorial

    def evalua_ecuacion_general(self, r: int, l: int, pn: Decimal):
        return (
            ((self.factorial(r))/((self.factorial(l)) * (self.factorial(r-l)))) *
            (math.pow(pn, l)) *
            (math.pow((1-pn), (r-l)))
        )

    def evalua_ecuacion_general_derivada(self, r: int, l: int, pcr: Decimal):

        return (
            ((self.factorial(r))/(self.factorial(l) * self.factorial(r-l))) *
            ((math.pow(pcr, l) * (r-l) * math.pow((1-pcr), (r-l-1)) * (-1)) +
            (math.pow((1-pcr), (r-l)) * l * math.pow(pcr, (l-1))))
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
        
    def get_n(self):
        return self.n

    def reset(self):
        self.n: int = 0  # n = número de iteraciones
        self.resultados: List = []  # vector de resultados de la ecuación general[Ecuación 6]
        self.pcr: Decimal = 0.0  # cálculo por medio de aproximación de pc,r [Ecuación 5]
        self.lambdar: Decimal = 0.0  # cálculo de λr [Ecuación 8]
        self.pndr: Decimal = 0.0  # cálculo del umbral inferior de credibilidad [Ecuación 12]
        self.pnfr: Decimal = 0.0  # cálculo del umbral superior de credibilidad [Ecuación 13]
