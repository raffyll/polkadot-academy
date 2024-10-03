// 27. Crie uma função que retorne a soma dos números pares de uma lista.

function somaPares(lista) {
    let total = 0;
    for ( let i = 0; i < lista.length; i++) {
        if (lista[i] % 2 == 0){
            total += lista[i];
        }
    }
    return total;
}

const numeros = [2, 4, 3, 6, 9, 12, 5];

console.log(somaPares(numeros));