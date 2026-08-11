// pruebas rapidas a mano - correr con el server levantado: node test.js
const axios = require('axios');

axios.post('http://localhost:3000/api/links', { url: 'https://www.google.com' })
  .then(function (r) {
    console.log('creado:', r.data);
    return axios.get('http://localhost:3000' + r.data.corta);
  })
  .then(function (r) {
    console.log('redirect ok?', r.status);
  });

// TODO probar los clicks
// TODO probar stats cuando este hecho el endpoint
