// 13. Imprima a sequência de Fibonacci até o décimo termo.

function fibonacci(num) {
  if (num <= 1) return num;
  return fibonacci(num-1) + fibonacci(num-2);
}

console.log(fibonacci(10));