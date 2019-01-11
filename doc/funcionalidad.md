# Documentación del proyecto
---
### Funcionalidad de la aplicación

La idea de principal funcionalidad de la aplicación es poder acceder a la ruta /archivos y en esa ruta acceder al archivo en cuestión que nos interese, que nos devolvería un JSON que contiene información del archivo, por ejemplo:  

#### Ejemplo
En la ruta /ejemplo encontramos un json de ejemplo que nos devuelve:
```
{"datos":
  {"cumpleaños": "15/5/97",
   "edad": 1
  },
 "nombre": "Carlos"
}
```

#### Funcionalidad

Accedemos a ``archivos/file1`` y nos devolvería la información acerca del archivo file.    

En este momento están disponibles tres archivos, llamados file1,file2 y file3 en al ruta ``archivos/<archivo>``. Ejemplo: [File1](https://filecnc.herokuapp.com/archivos/file1)

Estos archivos de formato JSON están almacenados en Redis, de manera que se realizan consultas al mismo para obtener los archivos, como podemos ver en el [código](https://github.com/AGCarlos/IV_1819_Proyecto/blob/master/fileS.py).
