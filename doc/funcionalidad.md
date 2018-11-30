# Documentación del proyecto
---
### Funcionalidad de la aplicación

La idea de  principal funcionalidad de la aplicación es poder acceder a la ruta /archivos y en esa ruta acceder al archivo en cuestión que nos interese, que nos devolvería un JSON que contiene información del archivo, por ejemplo:  

Accedemos a ``archivos/file1`` y nos devolvería la información acerca del archivo file.    

En este momento están disponibles tres archivos, llamados file1,file2 y file3 en al ruta ``archivos/<archivo>``. Ejemplo: [File1](https://filecnc.herokuapp.com/archivos/file1)

Si los archivos no se visualizaran, se pueden generar entrando en la ruta ``/addFiles``, que los añadirá de nuevo a Redis, debido a que el Add-on para Redis en licencia gratuita de Heroku no mantiene persistencia en algunos casos.  
