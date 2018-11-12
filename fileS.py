import urllib.request
import redis
import os

#import validators
class FileDownload:

    def conexion(self):
        """Connect to Redis"""

        redis_url = 'redis://h:p90d63f49afeefa17c338b0345f951b144e3f5e9bd649b4a2e625c3513fd1a5c6@ec2-52-54-174-93.compute-1.amazonaws.com:42199'
        r = redis.from_url(redis_url)
        return r

    def checkUser(self,user):
        """Check if a user has a pending file to download.
        Also connect to Redis DDBB.

        Parameters:
        user -- User used to search files
        """


        if type(user) != str:
            return "None"
        else:
            r = self.conexion()
            archivo = str(r.get(1))
            #if archivo == "b'None'":
                #print("El user "+user+" no tiene ningun archivo pendiente")
            return "OK"
            #else:
                #print("Tiene disponible el archivo:\n "+archivo[2:-1])
                #return "OK"

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

    def createFile(self,id,json):
        """Associate an id to a json

        Parameters:
        id -- The id to associate.
        json -- The json to associate to the id

        """
        if type(id) != str or type(json) != type(dict()):
            return "None"
        else:
            r = self.conexion()
            r.delete(id)
            r.hmset(id, json)
            return "OK"

    def deleteFile(self,id):
        """Delete a user entry

        Parameters:
        id -- The json id to delete.
        """
        if type(id) != str:
            return "None"
        else:
            r = self.conexion()
            r.delete(id)
            return "OK"

    def devuelveTrue(self):
        return True


if __name__ == "__main__":


    # """Declarar un objeto de la clase"""
    # dl = FileDownload()
    #
    # """Pedir credenciales al user"""
    # print("Introduzca su user")
    # user = str(input())
    # print("Introduzca su contraseña")
    # passwd = str(input())
    #
    # """Comprobar si el user tiene disponible algun archivo"""
    # archivo = dl.checkUser(user,passwd)
    #
    # """Si el user tiene disponible algun archivo, dar opción de descargarlo"""
    # if archivo != "None":
    #     dl.Download(archivo)
    #     print("Donete")
    r = redis.Redis()
    r.hmset("archivaso",{'lmao1':'lmao2','lmao1':'lmao4'})
    print(r.hmget("archivaso","lmao1"))
