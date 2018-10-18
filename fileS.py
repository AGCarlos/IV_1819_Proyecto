import urllib.request
import redis
#import validators

class FileDownload:

    def checkUser(self,user,passwd):
        """Check if a user has a pending file to download.
        Also connect to Redis DDBB.

        Parameters:
        user -- User used to search files
        passwd -- Password of the user
        """


        if type(user) != str or type(passwd) != str:
            return "None"
        else:
            r = redis.Redis()
            archivo = str(r.get(user+":"+passwd))
            if archivo == "None":
                print("El user "+user+" no tiene ningun archivo pendiente")
                return "None"
            else:
                print("Tiene disponible el archivo:\n "+archivo[2:-1])
                return archivo

    def Download(self,archivo):
        """Ask the user to download a file.
        Download the file in the case yes.

        Parameters:
        archivo -- The file to download
        """
        dl = FileDownload();
        print("Descargar el archivo ? [si/no]")
        respuesta = str(input())
        if respuesta == "si":
            print( "Descargando el archivo con urllib en carpeta de descargas")
            urllib.request.urlretrieve(archivo[2:-1], '/home/carlos/Descargas/noelleSilva.jpg')
        elif respuesta == "no":
            print("No se descargará el archivo")
        else:
            print("""Responda con "si" o "no" """)
            dl.Download(archivo)

    def createFile(self,user,passwd,file):
        """Associate a user to a file

        Parameters:
        user -- The user to associate.
        passwd -- The passwd of the user
        file -- The file to associate from the user

        """
        #if validators.url(file) != "True":
            #print("URL no válida")
            #return False
        #else:
        if type(user) != str or type(passwd) != str or type(file) != str:
            return "None"
        else:
            r = redis.Redis()
            r.set(user+":"+passwd, file)
            print("Archivo almacenado")

    def deleteFile(self,user,passwd):
        """Delete a user entry

        Parameters:
        user -- The user to delete.
        passwd -- The passwd of the user
        """
        if type(user) != str or type(passwd) != str:
            return "None"
        else:
            r = redis.Redis()
            r.set(user+":"+passwd, "None")

    def devuelveTrue(self):
        return True

if __name__ == "__main__":

    r = redis.Redis()
    print (str(r.get(1)))
    print (str(r.get(-1)))
    print (str(r.get(0.0)))
    str(r.get(1+":"+1))


    """Declarar un objeto de la clase"""
    dl = FileDownload()

    """Pedir credenciales al user"""
    print("Introduzca su user")
    user = str(input())
    print("Introduzca su contraseña")
    passwd = str(input())

    """Comprobar si el user tiene disponible algun archivo"""
    archivo = dl.checkUser(user,passwd)

    """Si el user tiene disponible algun archivo, dar opción de descargarlo"""
    if archivo != "None":
        dl.Download(archivo)
        print("Donete")
