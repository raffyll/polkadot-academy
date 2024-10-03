// 16. Crie uma função que retorne se uma string é um palíndromo.

function e_palindromo(string) {
    let inicial = string.split('').filter(espaço => espaço !== ' ').join('').toLowerCase();
    let invertida = inicial.split('').reverse().join('');

    if (inicial === invertida) {
        console.log(`${string} é um palíndromo: ${inicial} = ${invertida}`);
    } else {
        console.log(`${string} não é um palíndromo: ${inicial} != ${invertida}`)
    }
}

e_palindromo('A grama é amarga')