// 20. Crie uma função que retorne a soma dos dígitos de um número.

function somaDigitos(num) {
    let resultado = 0;
    let digitos = num.toString().split('').map(Number);
    for (let i = 0; i < digitos.length; i++) {
        resultado += digitos[i];
    }
    console.log(resultado);
}

somaDigitos(12)