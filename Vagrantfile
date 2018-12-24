Vagrant.configure("2") do |config|
  config.vm.box = "google/gce"

  config.vm.provider :google do |google, override|
    google.google_project_id = ENV['PROJECT_ID']
    google.google_client_email = ENV['CLIENT_EMAIL']
    google.google_json_key_location = ENV['JSON_KEY_LOCATION']

    google.image_family = 'ubuntu-1604-lts'

    override.ssh.username = "carlosivjj"
    override.ssh.private_key_path = "~/.ssh/id_rsa"
  end

  config.vm.provision :ansible do |ansible|
      ansible.playbook = "provision/playbook.yml"
  end

end
