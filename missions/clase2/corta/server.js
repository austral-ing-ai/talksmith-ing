const express = require('express');
const fs = require('fs');
const path = require('path');
const { generarCodigo } = require('./utils');

const app = express();
app.use(express.json());
app.use(express.static('public'));

const DB_FILE = path.join(__dirname, 'links.json');

function leerLinks() {
  return JSON.parse(fs.readFileSync(DB_FILE, 'utf8'));
}

function guardarLinks(links) {
  fs.writeFileSync(DB_FILE, JSON.stringify(links, null, 2));
}

// crear un link corto
app.post('/api/links', (req, res) => {
  const { url } = req.body;
  if (!url) {
    return res.status(400).json({ error: 'Falta la url' });
  }
  const links = leerLinks();
  const codigo = generarCodigo();
  const nuevo = {
    codigo: codigo,
    url: url,
    clicks: 0,
    creado: new Date().toISOString()
  };
  links.push(nuevo);
  guardarLinks(links);
  res.json({ codigo: codigo, corta: '/' + codigo });
});

// redirigir al destino
app.get('/:codigo', (req, res) => {
  const links = leerLinks();
  const link = links.find(function (l) { return l.codigo === req.params.codigo; });
  if (!link) {
    return res.status(404).send('No existe ese link');
  }
  link.clicks = link.clicks + 1;
  res.send(link.url);
});

app.listen(3000, function () {
  console.log('Corta escuchando en http://localhost:3000');
});
