# Import Fabric's API module
from fabric.api import *
import os

# Elimina el repositorio si ya estaba creado y lo vuelve a clonar para actualizarlo
def CrearApp():

    run('sudo rm -rf app')
    run('git clone https://github.com/AGCarlos/IV_1819_Proyecto.git app')
    run('pip3 install -r app/requirements.txt')

# Inicia la app en la maquina
def IniciarApp():

    run('cd app/ && sudo gunicorn app:app -b 0.0.0.0:80')
