// 30. Crie uma função que conte quantos números ímpares existem em uma lista.

function qtdImpares(lista) {
    let total = 0;
    for (let i = 0; i < lista.length; i++) {
        if (lista[i] % 2 !== 0) {
            total++;
        }
    }
    return total;
}

const numeros = [2, 4, 3, 6, 9, 12, 5];

console.log(qtdImpares(numeros));