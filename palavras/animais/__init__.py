from random import choice

animais = {
  "mamiferos": [
    "alce", "antilope", "baleia", "boi", "bufalo", "cabra", "camelo",
    "canguru", "castor", "cavalo", "cachorro", "chimpanze", "coala",
    "coelho", "elefante", "esquilo", "foca", "gato", "girafa", "gorila",
    "guaxinim", "hiena", "hipopotamo", "jaguar", "leao", "leopardo",
    "lobo", "macaco", "morcego", "onca-pintada", "porco", "rinoceronte"
  ],
  "voadores": [
    "aguia", "andorinha", "avestruz", "cegonha", "coruja", "flamingo",
    "gaivota", "morcego", "pato"
  ],
  "aquaticos": [
    "baleia", "foca", "peixe", "tartaruga"
  ],
  "outros": [
    "cobra", "crocodilo"
  ]
}

def escolha():
    categoria = choice(list(animais.keys()))
    palavra = choice(animais[categoria])
    return palavra