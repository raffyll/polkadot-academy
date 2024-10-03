// 29. Verifique se uma lista está em ordem crescente.

function verificarOrdem(lista) {
    for (let i = 0; i < lista.length - 1; i++) {
        if (lista[i] > lista[i + 1]) {
            return false;
        }
    }    
    return true;
}

const numeros = [8, 13, 36, 72];

console.log(verificarOrdem(numeros));

