from typing import Any, List
import numpy as np
import math


class Ecuaciones:
    n: int = 0  # n = número de iteraciones
    resultados: List = []  # vector de resultados de la ecuación general[Ecuación 6]
    pcr: float = 0.0  # cálculo por medio de aproximación de pc,r [Ecuación 5]
    lambdar: float = 0.0  # cálculo de λr [Ecuación 8]
    pndr: float = 0.0  # cálculo del umbral inferior de credibilidad [Ecuación 12]
    pnfr: float = 0.0  # cálculo del umbral superior de credibilidad [Ecuación 13]

    def factorial(self, numero: int):
        if numero <= 0:
            return 1
        factorial = 1
        while numero > 0:
            factorial = factorial * numero
            numero -= 1
        return factorial

    def evalua_ecuacion_general(self, r: int, l: int, pn: float) -> float:
        return (
            ((self.factorial(r)) / (self.factorial(l) * self.factorial(r - l)))
            * ((math.pow(pn, l)))
            * (math.pow((1 - pn), (r - l)))
        )

    def evalua_ecuacion_general_derivada(self, r: int, l: int, pcr: float) -> float:
        return (
            (self.factorial(r) / (self.factorial(l) * self.factorial(r - l)))
            * ((-1) 
            * (math.pow(pcr, l)) 
            * (r - l) 
            * (math.pow((1 - pcr), (r - l - 1)))
            + (l) * (math.pow((1 - pcr), (r - l))) * (math.pow(pcr, (l - 1))))
        )

    def set_lamdar(self, pcr: float, r: int) -> None:
        m: int = 0
        l: int = 0

        if (r % 2) == 0:
            m = (r / 2) + 1
        else:
            m = (r + 1) / 2

        l = m
        for l in np.arange(l, r):
            self.lambdar += self.evalua_ecuacion_general_derivada(r, l, pcr)

    def set_pndr(self, lambdar: float, pcr: float, n: int) -> None:
        # Para n subniveles
        self.pndr = (pcr) * (1 - (math.pow(lambdar, (-1 * n))))

    # Umbral superior de credibilidad
    def set_pnfr(self, pndr: float, lamdar: float, n: int) -> None:
        # Para n subniveles
        self.pndr = pndr + math.pow(lamdar, (-1 * n))

    def set_pcr(self, r: int):
        i: float = 0.0
        iaux: int = 0
        m: int = 0
        l: int = 0
        primera: int = 1
        pr: float = 0.0
        praux: float = 0.0
        resta: float = -1.0
        resta2: float = 0.0

        if r == 2:
            self.pcr = 1.0
        else:   
            if (r % 2) == 0:  # Par
                for iaux in np.arange(iaux, 100):
                    i = iaux / 100.0
                    pr = 0.0
                    praux = 0.0
                    m = (r / 2) + 1
                    l = m

                    for l in np.arange(l, r):
                        pr += self.evalua_ecuacion_general(r=r, l=l, pn=i)

                    for l in np.arange(l, r):
                        praux += self.evalua_ecuacion_general(r, l, pr)
                    
                    if ((pr - praux) > 0) or ((pr - praux) < 0) and primera == 1:
                        primera = 0
                        resta = pr - praux
                    else:
                        if ((pr - praux) > 0) or ((pr - praux) < 0) and (primera == 0):
                            resta2 = pr - praux
                            if ((resta > 0) and (resta2 < 0)) or (
                                (resta < 0) and (resta2 > 0)
                            ):
                                self.pcr = i
                                break
            else:
                if (r % 2) != 0:  # Par
                    self.pcr = 0.50

    def set_resultados_ecuacion_general(self, n: int, pn: float, r: int) -> None:  # Ecuacion 6 Grupo de votacion de tamaño r
        pr: float = 0.0
        aux: float = 0.0
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
                    for l in np.arange(l, r):
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
                    for j in np.arange(l, r):
                        pr += self.evalua_ecuacion_general(r, j, pn)
                    self.resultados[i] =  pr
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
    


r = 4
p0 = 69
n =3
m = (r / 2) + 1
l = m
iaux = 0
Ecuaciones = Ecuaciones()
# for iaux in np.arange(iaux, 100):
#     i = iaux / 100.0
#     pr = 0.0
#     praux = 0.0
#     m = (r / 2) + 1
#     l = m
#     for l in np.arange(l, r):
#         pr = pr + Ecuaciones.evalua_ecuacion_general(r=r, l=l, pn=i)

#     for l in np.arange(l, r):
#         praux = praux + Ecuaciones.evalua_ecuacion_general(r, l, pr)

Ecuaciones.set_pcr(r)
print("PCR", Ecuaciones.get_pcr())
# print("Prueba", pr)
# print("Prueba", praux)

# Lambdar: Hay errores en Ecuacion general 
Ecuaciones.set_lamdar(Ecuaciones.get_pcr(), r)
print("Lambdar",Ecuaciones.get_lambdar())