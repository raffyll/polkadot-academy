// 18. Gere um número aleatório entre 1 a 100.

function numeroAleatorio(min, max) {
    return Math.floor(Math.random() * (max - min) + min);
}

console.log(numeroAleatorio(1, 100))