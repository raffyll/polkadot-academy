// 11. Verifique se um número está presente em uma lista.

function verificarNumero(lista, num) {
  for (numero of lista) {
    if (numero === num) {
      return `O número ${num} está na lista!`;
    }
  }
  return `O número ${num} não está na lista!`;
}

const random = [4, 12, 74, 81, 19];

console.log(verificarNumero(random, 74));