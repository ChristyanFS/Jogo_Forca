from random import choice
comidas = {
  "frutas": [
    "maca", "banana", "laranja", "morango", "uva", "abacaxi", "manga",
    "melancia", "pessego", "goiaba", "limao", "kiwi"
  ],
  "doces": [
    "bolo", "pudim", "brigadeiro", "chocolate", "sorvete", "bala",
    "bombom", "donuts", "mousse", "torta", "manjar", "churros"
  ],
  "salgados": [
    "pao de queijo", "coxinha", "pastel", "risole", "empada", "esfirra",
    "pizza", "lasanha", "batata frita", "pipoca salgada", "tacos",
    "sushi"
  ],
  "verduras": [
    "alface", "couve", "espinafre", "agriao", "rucula", "salsa",
    "cebolinha", "alecrim", "hortela", "manjericao", "repolho", "brocolis"
  ],
  "legumes": [
    "cenoura", "batata", "cebola", "tomate", "pimentao", "abobora",
    "berinjela", "pepino", "milho", "vagem", "chuchu", "mandioca"
  ]
}

def escolha():
    categoria = choice(list(comidas.keys()))
    palavra = choice(comidas[categoria])
    return palavra


escolha()
