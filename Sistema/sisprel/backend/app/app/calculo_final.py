from typing import Any, List
import numpy as np
import math
from decimal import Decimal

from .ecuaciones import Ecuaciones

class Calculo_final:
    n: int = 0
    p0: Decimal = 0.0
    r: int = 0
    pndr: Decimal = 0.0
    pnfr: Decimal = 0.0
    pcr: Decimal = 0.0
    lambdar_result: Decimal = 0.0
    resultados: List= []
    n_resultados_eliminacion: int = 0
    eliminacion_resultados: List = []
    n_resultados: int = 0
    ecs = Ecuaciones()

    def __init__(self):
        self.reset()

    
    def calculo_final(self, n:int, p0: float, r: int):
        self.n = n
        self.p0 = p0
        self.r = r
        self.ecs.set_pcr(self.r)
        self.pcr = self.ecs.get_pcr()
        self.ecs.set_lamdar(self.pcr, self.r)
        self.lambdar_result =  self.ecs.get_lambdar()
        self.ecs.set_pndr(self.lambdar_result, self.pcr, self.n)
        self.pndr = self.ecs.get_pndr()
        self.ecs.set_pnfr(self.pndr, self.lambdar_result, self.n)
        self.pnfr = self.ecs.get_pnfr()


    def get_pn(self):
        pn: float
        i: int = 0
        lista_aux: List = []

        self.ecs.set_resultados_ecuacion_general(self.n, self.p0, self.r)
        self.n_resultados = self.n
        lista_aux = self.ecs.get_resultados_ecuacion_general()
        pn = lista_aux[self.n_resultados-1]
        self.resultados = [100 * i for i in lista_aux]
        pn *= 100
        return pn

    def calcular_eliminacion_total(self):
        i: int = 0
        self.ecs.set_resultados_ecuacion_general(-1, self.p0, self.r)
        self.n_resultados_eliminacion = self.ecs.get_n()
        lista_aux = self.ecs.get_resultados_ecuacion_general()
        self.eliminacion_resultados = [100 * i for i in lista_aux]

        return self.n_resultados_eliminacion + 1

    def get_resultados(self):
        return self.resultados


    def get_pndr(self):
        return self.pndr * 100

    def get_pnfr(self):
        return self.pnfr * 100

    def reset(self):
        self.n: int = 0
        self.p0: Decimal = 0.0
        self.r: int = 0
        self.pndr: Decimal = 0.0
        self.pnfr: Decimal = 0.0
        self.pcr: Decimal = 0.0
        self.lambdar_result: Decimal = 0.0
        self.resultados: List= []
        self.n_resultados_eliminacion: int = 0
        self.eliminacion_resultados: List = []
        self.n_resultados: int = 0
        self.ecs.reset()

    def __del__(self):
        self.n: int = 0
        self.p0: Decimal = 0.0
        self.r: int = 0
        self.pndr: Decimal = 0.0
        self.pnfr: Decimal = 0.0
        self.pcr: Decimal = 0.0
        self.lambdar_result: Decimal = 0.0
        self.resultados: List= []
        self.n_resultados_eliminacion: int = 0
        self.eliminacion_resultados: List = []
        self.n_resultados: int = 0

