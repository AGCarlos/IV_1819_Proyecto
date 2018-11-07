# Documentación del proyecto
### Despliegue de la Aplicación
Para realizarlo he utilizado la documentación de [Heroku](https://dashboard.heroku.com/apps) y este [tutorial](https://github.com/datademofun/heroku-basic-flask) de un repositorio de Github de _datademofun_.  
Podemos encontrar desplegada la aplicación en :
-  [App en Heroku](https://filecnc.herokuapp.com/) donde encontramos el status
-  [Ejemplo de la aplicación](https://filecnc.herokuapp.com/ejemplo) donde se devuelve un JSON también

### Configuración del despliegue

#### Archivos de configuración
- El archivo [**Procfile**](https://github.com/AGCarlos/IV_1819_Proyecto/blob/master/Procfile) se utiliza para especificar a Heroku como iniciar la aplicación web, en este caso con el servidor web gunicorn, de esta manera:  
```
web: gunicorn app:app --log-file=-
```
Especificamos el servidor, la aplicación que vamos a usar y además añadimos opciones para logs.
- Utilizamos el archivo [**runtime**](https://github.com/AGCarlos/IV_1819_Proyecto/blob/master/runtime.txt) para especificarle a Heroku que estamos desplegando una aplicación de Python, añadiendo esto al archivo:  
```
python-3.6.6
```

#### Despliegue automático

En Heroku he configurado los despliegues automáticos para que cada vez que suba los archivos fuentes a github se despliegue en Heroku automáticamente.  

![autoDesploysOnHeroku](../img/autoDep.png)
