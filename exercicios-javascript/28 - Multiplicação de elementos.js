// 28. Crie uma função que multiplique todos os elementos de uma lista.

function multiplicacaoElementos(lista) {
    let total = 1;
    for ( let i = 0; i < lista.length; i++) {
        total *= lista[i];
    }
    return total;
}

const numeros = [2, 4, 3, 6, 9, 12, 5];

console.log(multiplicacaoElementos(numeros));