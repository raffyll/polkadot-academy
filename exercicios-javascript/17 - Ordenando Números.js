// 17. Crie uma função que ordene uma lista de números.

function ordenarNumeros(lista) {
    return lista.sort((a, b) => a - b);
}

const numeros = [8, 13, 36, 72, 17, 22, 25, 19];

console.log(ordenarNumeros(numeros));