// 7. Verifique se um número é primo.

function e_primo(num) {
  if (num < 2) {
    return false;
  }
  for (let i = 2; i < num; i++) {
    if (num % i == 0) {
      return false;
    }
  }
  return true;
}

let num = 6;

if (e_primo(num)) {
    console.log(`O número ${num} é primo!`);
} else {
    console.log(`O número ${num} não é primo!`);
}