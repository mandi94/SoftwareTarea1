# Universidad Simon Bolivar
# Laboratorio de Ingenieria de Software
# Tarea 2
# Autores:
#   - Fabiola Martinez 1310838
#   - Amanda Camacho 1210644
# Descripcion: funcion que calcula el monto a pagar de un servicio.

import sys
import datetime
import time
from datetime import datetime, date, time, timedelta

class Tarifa:
    def __init__(self,semana,finSemana):
        self.semana = semana
        self.finSemana = finSemana
        

def calcularServicio(tarifa, tiempoServicio):
    
    tiempo = tiempoServicio[1] - tiempoServicio[0]
    fechaInicio = tiempoServicio[0]
    fechaFin = tiempoServicio[1]
    #print(tiempo)

    # Verificamos un servicio que dure menos de un dia completo dure mas de 15 min
    try:
    	assert( (fechaInicio.day!=fechaFin.day) or tiempo.seconds >= 900)
    except:
    	print("La duracion de un servicio debe ser mayr o ogual a 15 minutos\n")
    	print("EL programa terminara")
    	sys.exit()	

    # Verificamos que el servicio no sea mayor a una semana
    try:
   		assert((tiempo.days!= 7 or tiempo.seconds==0) or tiempo.days < 7)
    except:
    	print("La duracion de un servicio debe ser menor o igual a siete dias\n")
    	print("EL programa terminara")
    	sys.exit()
    
    # Transformamos todo a segundos 
    tiempoHora = tiempo.seconds//3600
    tiempoMin = (tiempo.seconds%3600)*60
    tiempoSeg = (tiempo.seconds%3600)

    monto = 0
    i=0

    # Servicio dura un dia
    if(tiempo.days == 0):

    	# Verificamos que tarifa usar
    	if(finDeSemana(fechaInicio)):
    		tarif = tarifa.finSemana
    	else:
    		tarif = tarifa.semana
    	# Calculamos el monto de acuerdo al tiempo trabajado 	
    	if(tiempoHora == 0):
            monto = tarif 
    	else:
            if (tiempoMin > 0):
    			hora = tiempoHora + 1
    			monto = tarif * hora
            monto=tarif
	
	# Servicio dura mas de un dia   
    else:
    	if(fechaFin.hour < fechaInicio.hour):
    		condicionParada = tiempo.days + 1

    	elif(fechaInicio.hour == fechaFin.hour and fechaFin.second < fechaInicio.second):
    		condicionParada = tiempo.days + 1

    	else:
    		condicionParada = tiempo.days

    	while (i <= condicionParada): 
    		# Verificamos que tarifa usar
            if (finDeSemana(fechaInicio)):
                tarif = tarifa.finSemana
            else:
                tarif =tarifa.semana

            # Si el dia es el primero
            if i == 0:
                if fechaInicio.minute > 0 or fechaInicio.second > 0:
                    monto += (24 - fechaInicio.hour) * tarif
                else:
                    monto += (24 - fechaInicio.hour) * tarif
            # Si el dia es el ultimo del monto
            elif i == condicionParada:
                if fechaFin.minute > 0 or fechaFin.second > 0:
                    monto += (fechaFin.hour + 1 ) * tarif
                else:
                    monto += fechaFin.hour * tarif
            else:
                monto += 24 * tarif
               
        
            i += 1
            
            fechaInicio = fechaInicio + timedelta(days=1)

    print monto
    return monto

def finDeSemana(fecha):
    
    dia=int(fecha.strftime("%w"))

    if (dia == 6 or dia == 0):
    
        return True
    
    return False
