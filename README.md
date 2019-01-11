# Proyecto IV: Migues
## Microservicio Web
[![Build Status](https://travis-ci.org/AGCarlos/IV_1819_Proyecto.svg?branch=master)](https://travis-ci.org/AGCarlos/IV_1819_Proyecto)


### Descripción del proyecto  
En este proyecto se pretende desarrollar un micro-servicio encargado de enviar documentos desde algún lugar en la nube hasta un destinatario.  
Para ello haré uso de librerías, módulos y frameworks de _python_ encargados de realizar las conexiones y comprobaciones necesarias y enviar los documentos.
#### Descripción de la clase  
La clase que contiene las funciones del proyecto se llama _FileDownload_. Esta clase va a realizar mediante sus funciones:
- La identificación del usuario
- La comprobación de archivos disponibles para descarga del usuario
- La descarga de los archivos para el usuario  
---
### Herramientas  
La herramientas a utilizar serán:
- [_Python_](https://www.python.org/) se utilizará como lenguaje de programación
- [_Flask_](http://flask.pocoo.org/) se utilizará como framework (is Fun)
- [_Redis_](https://redis.io/) se utilizará como BBDD en memoria.
---
### Librerias
- En cuanto a la descarga de los archivos, se usará el módulo [_urllib.request_](https://docs.python.org/3/library/urllib.html)
- Se utilizará el modulo de logs [_loggin_](https://docs.python.org/2/library/logging.html) de Python para manejar los logs.
---
### Tests
Para la realización de tests sobre el proyecto, se utilizará el framework [Pytest](https://docs.pytest.org/en/latest/). Podemos encontrar los test en el archivo _test.py_.  
Los test pasan a través del servicio de integración continua [Travis-CI](https://travis-ci.org/), que se encuentra configurado para este repositorio.

### Despliegue
[![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://filecnc.herokuapp.com)  

Encontramos la aplicación desplegada en [Heroku](https://dashboard.heroku.com/apps), que se puede encontrar en el siguiente enlace:
- Despliegue: [Aplicación en Heroku](https://filecnc.herokuapp.com/)

Encontramos la aplicación desplegada en Heroku con Docker, que se puede encontrar en el siguiente enlace:
- Enlace a DockerHub: App en [DockerHub](https://hub.docker.com/r/carlosag/iv_1819_proyecto/)
- Contenedor: [Aplicación en Heroku](https://filecnc-docker.herokuapp.com/status)

### Despliegue en IaaS
Encontramos la aplicación desplegada con Google Cloud en la siguiente IP:
- Despliegue final: 35.246.63.201

### Documentación
Encontramos la documentación [aquí](./doc/README.md)
