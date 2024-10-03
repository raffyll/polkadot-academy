// 14. Remova todos os espaços de uma string.

function removerEspaços(string) {
    return string.split('').filter((espaço) => espaço !== ' ').join('');
}

console.log(removerEspaços('Esta é uma frase de teste'));