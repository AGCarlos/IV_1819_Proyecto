// flightplan.js
var plan = require('flightplan');

// configuration
plan.target('staging', {
  host: '35.246.63.201',
  username: 'carlosivjj',
  agent: process.env.SSH_AUTH_SOCK
});

// run commands on the target's remote hosts
plan.remote(function(remote) {
    remote.log('Ejecutar el servidor gunicorn');
    var folder = 'app';
    remote.exec('cd ' + folder + ' && sudo gunicorn app:app -b 0.0.0.0:80');
});
