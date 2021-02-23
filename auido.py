import pyaudio  
import wave  

from pynput import keyboard as kb



def sondido():
  


    salir = False
    opcion = 0
    while not salir:
        def pulsa(tecla):
            
           
       
        chunk = 1024  

        #ABRIMOS UBICACIÓN DEL AUDIO.  
        f = wave.open("Thunderstruck.wav","rb")

        #INICIAMOS PyAudio.
        p = pyaudio.PyAudio()  

        #ABRIMOS STREAM
        stream = p.open(format = p.get_format_from_width(f.getsampwidth()),  
                        channels = f.getnchannels(),  
                        rate = f.getframerate(),  
                        output = True)

        #LEEMOS INFORMACIÓN  
        data = f.readframes(chunk)  

        #REPRODUCIMOS "stream"  
        while data:  
            stream.write(data)  
            data = f.readframes(chunk)  

        #PARAMOS "stream".  
        stream.stop_stream()  
        stream.close()  

        #FINALIZAMOS PyAudio  
        p.terminate() 
 
print ("Fin")

def pedirNumeroEntero():
     
    correcto=False
    num=0
    while(not correcto):
        try:
            num = int(input("Introduce un numero entero: "))
            correcto = True
        except ValueError:
            print('Error, introduce un numero entero')
     
    return num
 
salir = False
opcion = 0
 
while not salir:
 
    print ("1. Opcion 1")
    print ("2. Opcion 2")
    print ("3. Opcion 3")
    print ("4. Salir")
     
    print ("Elige una opcion")
 
    opcion = pedirNumeroEntero()
 
    if opcion == 1:
        print ("Opcion 1")
        sondido()

    elif opcion == 2:
        print ("Opcion 2")
        
    elif opcion == 3:
        print("Opcion 3")
    elif opcion == 4:
        salir = True
    else:
        print ("Introduce un numero entre 1 y 3")
 
print ("Fin")
    