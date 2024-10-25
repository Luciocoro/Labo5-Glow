# -*- coding: utf-8 -*-
"""
Created on Fri Sep  6 08:46:05 2024

@author: Publico
"""
import pyvisa as visa
import numpy as np
import time
import matplotlib.pyplot as plt
import instrumental
import pandas as pd
import logging 
import pyvisa as visa

visa.log_to_screen(logging.DEBUG)

rm = visa.ResourceManager()

print(rm.list_resources())

#%%

#dev = rm.open_resource("ASRL3::INSTR", read_termination='\r')

#dev.write("!US3")
#print(dev.query("?GA1"))

#dev.close()

# inicializo comunicacion con equipos
rm = visa.ResourceManager()
#lista de dispositivos conectados, para ver las id de los equipos
rm.list_resources()


#inicializo los instrumentos 
#gf=rm.open_resource('USB0::0x0699::0x0346::C034166::INSTR')
amper=rm.open_resource('GPIB0::24::INSTR') #uno es el agilent --->corriente ok, no mide la corriente mide diferencia d evoltaje, y tengo que usar la ley de ohm para calcular la corriente de la descarga 
volt=rm.open_resource("GPIB0::23::INSTR") #uno es el HP ----> tensión 
pi=rm.open_resource("ASRL3::INSTR", read_termination='\r') #POR QUEEEE NO ANDAAAAAAAAAAAAAAAAAA :( ( :) )

#float(volt.query('MEASURE:VOLTAGE:DC?')) #V


#%%