# Universidad Simon Bolivar
# Laboratorio de Ingenieria de Software
# Tarea 2
# Autores:
#	- Fabiola Martinez 1310838
#	- Amanda Camacho 1210644
# Descripcion: suite de pruebas unitarias.

from codeBase import calcularServicio, finDeSemana, Tarifa
import unittest
import sys
import datetime
import time
from datetime import datetime, date, time, timedelta

class TestSuite(unittest.TestCase):

	# Servicio dura 15 minutos
	def testMinimo(self):
		tarifa = Tarifa(10,20)
		fechaInicio = datetime(2017,2,20,10,0,0)
		fechaFin = datetime(2017,2,20,10,15,0,0)
		self.assertEqual(calcularServicio(tarifa, [fechaInicio,fechaFin]), 10)

	# Servicio dura 7 dias
	def testMaximo(self):
		tarifa = Tarifa(10,20)
		fechaInicio = datetime(2017,2,20,10,0,0)
		fechaFin = datetime(2017,2,27,10,0,0)
		self.assertEqual(calcularServicio(tarifa, [fechaInicio,fechaFin]), 2160)

	# Servicio dura 15 minutos mas un segundo
	def testEsquinaInferior(self):
		tarifa = Tarifa(10,20)
		fechaInicio = datetime(2017,2,20,10,0,0)
		fechaFin = datetime(2017,2,20,10,15,1)
		self.assertEqual(calcularServicio(tarifa, [fechaInicio,fechaFin]), 10)


	# Servicio dura 7 dias mas un segundo
	def testEsquinaSuperior(self):
		tarifa = Tarifa(10,20)
		fechaInicio = datetime(2017,2,20,10,0,0)
		fechaFin = datetime(2017,2,27,9,59,59)
		self.assertEqual(calcularServicio(tarifa, [fechaInicio,fechaFin]), 2160)


	# Serivicio inicia en un mes y termina en otro
	def testMalicia1(self):
		tarifa = Tarifa(10,20)
		fechaInicio = datetime(2017,9,30,10,0,0)
		fechaFin = datetime(2017,10,2,10,0,0)
		self.assertEqual(calcularServicio(tarifa, [fechaInicio,fechaFin]), 860)


	# Servicio incia en la madrugada de un dia y termina en la madrugada del otro
	def testMalicia2(self):
		tarifa = Tarifa(10,20)
		fechaInicio = datetime(2017,10,1,0,0,0)
		fechaFin = datetime(2017,10,2,0,0,0)
		self.assertEqual(calcularServicio(tarifa, [fechaInicio,fechaFin]), 480)


if __name__ == '__main__':
	unittest.main()




