# Proyecto IV: Migues
## Microservicio Web
---
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
Para la realización de tests sobre el proyecto, se utilizará el framework [Pytest](https://docs.pytest.org/en/latest/)

### Colaboración
Este micro-servicio pretende sincronizarse con el [micro-servicio de Fernando Talavera Mendoza](https://github.com/Thejokeri/IV-18-19-Proyecto), de manera que mi proyecto obtenga los documentos a enviar del micro-servicio de Fernando.

| [![Fernando Talavera Mendoza](https://github.com/Thejokeri.png?size=100)](https://github.com/Thejokeri) | [![Carlos Ariza García](https://github.com/AGCarlos.png?size=100)](https://github.com/AGCarlos) |
| :---: | :---: |
| [Fernando Talavera Mendoza](https://github.com/Thejokeri) | [Carlos Ariza García](https://github.com/AGCarlos) |
