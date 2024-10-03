// 8. Crie uma função que retorne a média de uma lista de números.

function media(lista) {
    let soma = 0;
    for (let i = 0; i < lista.length; i++) {
        soma += lista[i];
    }
    let resultado = soma / lista.length;
    return resultado;
}

const numeros = [2, 4, 6];

console.log(`A média de todos os números da lista é: ${media(numeros)}`);