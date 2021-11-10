import time
import sys 
import sqlite3
import os
import getpass
import datetime
import module1 as md1
import module2 as md2

filestoshow = os.listdir(os.getcwd())
cwd = os.getcwd()
x = datetime.datetime.now()
registeredUser = md1.User
registeredPW = md1.Password

def sistem():
    #poner lista de comandos *NO URGENTE*
    ans=input(">/ ")

    if ans=="date":
     print(x.strftime("%c"))
     sistem()
     
    if ans=="touch":
     filetocreate = input("Nombre al nuevo archivo:")
     f = open(filetocreate, "w") 
     if os.path.exists(filetocreate):
        print("El archivo " + filetocreate + " ha sido creado correctamente")
        sistem()
     else:
       print("ERROR: el archivo ya existe")
       sistem()

    if ans=="cat":
        filetoread = input("¿Que archivo quiere ver?") 
        a = open(filetoread)
        print(a)  
        input("Pulse la tecla 'b' para continuar.")
        if ans == 'b':
           sistem()

    if ans=="pwd":
        print(cwd) 
        time.sleep(2)
        sistem()                   
    
    if ans=="ls":
        print(filestoshow)
        time.sleep(2)
        sistem()

    if ans=="write":
        filetoedit = input("¿Qué archivo quiere abrir?")
        with open(filetoedit, 'w') as f:
                newtext = input("Escriba:")
                f.write(newtext)
                f.close()
                time.sleep(2)
                print("El nuevo texto se guardó exitosamente")
                sistem()

    if ans=="cd":
        directorytogo = input("¿A qué directorio se dirige?")
        os.chdir(directorytogo)  
        print(os.getcwd() )  
        sistem()

    if ans=="credit":
        md1.credits()
        sistem()    

    if ans=="calculator":
        md2  
       
    else:
       print('Error: no se encuentra el comando.')
       sistem()

def passwordlogin():
    passw = getpass.getpass('Contraseña: ')
    if passw == registeredPW:
        sistem()

def login():
     userinput=input('Usuario: ')
     if userinput == registeredUser:
      passwordlogin()  

     else: 
      print("Usuario incorrecto")
      login()      


print("""


             █████╗ ███╗   ███╗███████╗     ██████╗ ███████╗    
            ██╔══██╗████╗ ████║██╔════╝    ██╔═══██╗██╔════╝    
            ███████║██╔████╔██║███████╗    ██║   ██║███████╗    
            ██╔══██║██║╚██╔╝██║╚════██║    ██║   ██║╚════██║    
            ██║  ██║██║ ╚═╝ ██║███████║    ╚██████╔╝███████║    
            ╚═╝  ╚═╝╚═╝     ╚═╝╚══════╝     ╚═════╝ ╚══════╝    
_______________________ BETA     TERMINAL EDITION _________________________                                                   

""")

login()