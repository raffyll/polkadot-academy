// 26. Verifique se uma string contém uma substring.

function verificarSubstring(string, substring) {
  return string.includes(substring);
}

console.log(verificarSubstring('Olá, Mundo!', 'Mundo'));