const CARACTERES = 'abcdefghijklmnopqrstuvwxyz0123456789';

// genera un codigo corto de 3 caracteres
function generarCodigo() {
  let codigo = '';
  for (let i = 0; i < 3; i++) {
    codigo += CARACTERES[Math.floor(Math.random() * CARACTERES.length)];
  }
  return codigo;
}

module.exports = { generarCodigo };
