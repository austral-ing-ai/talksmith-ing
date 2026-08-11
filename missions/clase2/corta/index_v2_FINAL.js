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

// crear un link corto
app.post('/api/links', (req, res) => {
  const { url } = req.body;
  const links = leerLinks();
  const codigo = generarCodigo();
  links.push({ codigo: codigo, url: url, clicks: 0 });
  fs.writeFileSync(DB_FILE, JSON.stringify(links, null, 2));
  res.json({ codigo: codigo });
});

// redirigir al destino
app.get('/:codigo', (req, res) => {
  const links = leerLinks();
  const link = links.find(function (l) { return l.codigo === req.params.codigo; });
  if (!link) {
    return res.status(404).send('No existe');
  }
  res.send(link.url);
});

app.listen(3000, function () {
  console.log('escuchando en 3000');
});
