// 15. Crie uma função que conte quantas vezes um caractere aparece em uma string.

function contadorCaractere(string, char) { 
  if (string.toLowerCase().includes(char.toLowerCase())) {
    console.log(string.toLowerCase().split(char.toLowerCase()).length - 1);
  } else {
    console.log('O caractere não está presente!');
  }
}

contadorCaractere('Frase de teste', 'e');