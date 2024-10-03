// 21. Verifique se dois números são múltiplos.

function e_multiplo(num1, num2) {
  if (num1 === num2) {
    console.log('Os números são iguais.');
  }
  if (num1 % num2 == 0 || num2 % num1 == 0) {
    console.log('Os números são múltiplos.');
  } else {
    console.log('Os números não são múltiplos.');
  }
}

e_multiplo(32, 8);