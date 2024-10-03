// 12. Crie uma função que calcule o fatorial de um número.

function fatorial(num) {
  let total = 1;
  for (let i = 1; i <= num; i++) {
    total *= i;
  }
  return total;
}

console.log(fatorial(7));
