from fabric.api import *
import os

env.hosts = ['35.184.220.234']
env.user = "carlosivjj"
ruta= "./app"

# Elimina el repositorio si ya estaba creado y lo vuelve a clonar para actualizarlo
def prepare_deploy():

    run('sudo rm -rf app')
    run('git clone https://github.com/AGCarlos/IV_1819_Proyecto.git app')
    run('pip3 install -r app/requirements.txt')

# Inicia la app en la maquina
def deploy():

    with shell_env( REDIS_URL=os.environ['REDIS_URL'] ):
        with cd(ruta):
            run('sudo gunicorn app:app -b 0.0.0.0:80')
