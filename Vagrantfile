Vagrant.configure("2") do |config|
  config.vm.box = "google/gce" # Box de Google CE

  config.vm.provider :google do |google, override|

    # Configuración del proyecto
    google.google_project_id = ENV['PROJECT_ID'] # ID del proyecto
    google.google_client_email = ENV['CLIENT_EMAIL'] # Email de cliente
    google.google_json_key_location = ENV['JSON_KEY_LOCATION'] # Credenciales

    # Configuración de la instancia
    google.image_family = 'ubuntu-1604-lts' # Distribución a usar
    google.machine_type = 'n1-standard-1' # Tipo de máquina
    google.disk_size = '10' # Tamaño del disco
    google.disk_name = 'disk-iv' # Nombre del disco
    google.disk_type = 'pd-standard' # Tipo del disco
    google.metadata = {'REDIS_URL' => ENV['REDIS_URL']} # Variables de entorno
    google.external_ip = '35.246.63.201' # IP externa de la máquina
    google.tags = ['http-server'] # Activar conexiones http
    google.name = 'filecnc' # Nombre para la instancia
    google.zone = "europe-west2-a" # Zona

    # Configuración de SSH
    override.ssh.username = "carlosivjj" # Usuario para SSH
    override.ssh.private_key_path = "~/.ssh/id_rsa" # Ruta a las claves SSH
  end

  config.vm.provision :ansible do |ansible|
      ansible.compatibility_mode = "2.0" # Acorde con la versión de Ansible 2.5.1
      ansible.playbook = "provision/playbook.yml"
  end

end
