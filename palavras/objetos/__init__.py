from random import choice

objetos = {
  "geral": [
    "celular", "chave", "livro", "caneta", "copo", "cadeira", "mesa", "lampada",
    "garrafa", "oculos", "relogio", "mochila", "sapato", "tesoura", "regua",
    "carro", "bicicleta", "bola", "computador", "monitor", "teclado", "mouse",
    "fone de ouvido", "controle remoto", "prato", "talher", "colher",
    "garfo", "faca", "cartao"
  ]
}

def escolha():
    categoria = choice(list(objetos.keys()))
    palavra = choice(objetos[categoria])
    return palavra