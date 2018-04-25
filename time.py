from time import time

def incio():
    global ti #Tiempo inicial
    ti = time

def terminado():
    global tt #Tiempo Transcurrido
    tt = time() - ti
    if tt >60:
        minutos = (tt %3600 / 60)
        print("minutos %d" %minutos)
    else:
         print("segundos: %.2f seconds." % tt)
