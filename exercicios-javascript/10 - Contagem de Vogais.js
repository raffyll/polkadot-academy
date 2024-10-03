// 10. Conte quantas vogais existem em uma string.

function contarVogais(string) {
  const vogais = 'aeiouAEIOUáéíóúãâêîôûãÁÉÍÓÚÂÊÎÔÛ';

  let contador = 0;
  for (let letras of string) {
    if (vogais.includes(letras)) {
        contador++;
    }
  }
  return contador;
}

console.log(contarVogais('Olá, Mundo!'));
