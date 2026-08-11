// VERSION VIEJA - no usar (dejo por las dudas)
const express = require('express');
const fs = require('fs');

const app = express();
app.use(express.json());

app.post('/acortar', (req, res) => {
  const links = JSON.parse(fs.readFileSync('./links.json', 'utf8'));
  const codigo = Math.random().toString(36).substring(2, 5);
  links.push({ codigo: codigo, url: req.body.url, clicks: 0 });
  fs.writeFileSync('./links.json', JSON.stringify(links));
  res.send(codigo);
});

app.get('/:codigo', (req, res) => {
  const links = JSON.parse(fs.readFileSync('./links.json', 'utf8'));
  const link = links.find(l => l.codigo === req.params.codigo);
  res.send(link.url);
});

app.listen(3000);
