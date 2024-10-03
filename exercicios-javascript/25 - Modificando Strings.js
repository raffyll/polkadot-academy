// 25. Substitua todas as vogais de uma string por '*'.

function substituirVogais(string) {
    return string.replace(/['aeiouAEIOUáéíóúãâêîôûãÁÉÍÓÚÂÊÎÔÛ']/g, '*');
}

console.log(substituirVogais('Olá, Mundo!'))