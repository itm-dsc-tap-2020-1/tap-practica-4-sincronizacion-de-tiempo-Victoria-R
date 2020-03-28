import datetime
from time import ctime
import ntplib
import datetime
import os

servidor_de_tiempo = "time-b-wwv.nist.gov"

#Fecha y hora al incio de petición
t1 = datetime.datetime.now()
print ("Fecha y hora al inicio de la petición: %s" % t1)

#Fecha y hora del servidor
print("\nObteniendo la hora del servidor NTP...")
cliente_ntp = ntplib.NTPClient()
respuesta = cliente_ntp.request(servidor_de_tiempo)
hora_actual = datetime.datetime.strptime(ctime(respuesta.tx_time), "%a %b %d %H:%M:%S %Y")
print("Fecha y hora de " + servidor_de_tiempo +  ": " + str(hora_actual) + "\n")

#Fecha y hora despues de la petición
t2 = datetime.datetime.now()
print ("Fecha y hora al llegar de la petición: %s" % t2)

#Tiempo de retraso
dif=(t2-t1)/2
print()
print('El ajuste es de:' + str(dif) )

#Reloj
rel= hora_actual+dif
print()
print ( 'Reloj: '+ str(rel))

#Ajuste de tiempo
os.system(f"date --set '{rel}'")

