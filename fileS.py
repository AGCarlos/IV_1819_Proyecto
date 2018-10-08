import urllib.request
import redis

class FileDownload:

    def checkUser(self,usuario,contraseña):
        """Comprueba si un usuario tiene algun archivo pendiente.
        Además realiza la conexión a la BBDD Redis.
        """
        r = redis.Redis()
        archivo = str(r.get(usuario+":"+contraseña))
        if archivo == "None":
            print("El usuario "+usuario+" no tiene ningun archivo pendiente")
            return "None"
        else:
            print("Tiene disponible el archivo:\n "+archivo[2:-1])
            return archivo

    def Download(self,archivo):
        """Pregunta al usuario si quiere descargar un archivo.
        Descarga el archivo en caso de responder si.
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

if __name__ == "__main__":

    """Declarar un objeto de la clase"""
    dl = FileDownload()

    """Pedir credenciales al usuario"""
    print("Introduzca su usuario")
    usuario = str(input())
    print("Introduzca su contraseña")
    contraseña = str(input())

    """Comprobar si el usuario tiene disponible algun archivo"""
    archivo = dl.checkUser(usuario,contraseña)

    """Si el usuario tiene disponible algun archivo, dar opción de descargarlo"""
    if archivo != "None":
        dl.Download(archivo)
        print("Donete")
