// 24. Crie uma função que retorne os divisores de um número.

function divisores(num) {
    let lista = [];
    for (let i = 1; i <= num; i++) {
        if (num % i == 0) {
            lista.push(i);
        }
    }
    return lista;
}

console.log(divisores(8));