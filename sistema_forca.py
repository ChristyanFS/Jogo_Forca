from palavras import comidas, objetos, animais
from time import sleep
from random import randint

def estrutura_esc():
    while True:
        try:
            esc = int(input('Escolha: '))
        except KeyboardInterrupt:
            print('\033[0;31mUsuário, preferiu não informar os dados.\033[m')
            break
        except ValueError:
            print('\033[0;31mERRO! Digite um opção válida.\033[m')
        else:
            if 1 <= esc <= 3: return esc
            else: print('\033[0;31mEscolha um número entre 1 e 3.\033[m')

def corpo(num):
    if num == 0: print('Você perdeu a PERNA ESQUERDA')
    elif num == 1: print('Você perdeu a PERNA DIREITA')
    elif num == 2: print('Você perdeu o BRAÇO ESQUERDO')
    elif num == 3: print('Você perdeu o BRAÇO DIREITO')
    elif num == 4: print('Você perdeu o TRONCO')
    elif num == 5: print('Você perdeu a CABEÇA')

def introdução():
    print('\033[0;32m-=\033[m' * 20)
    print('\033[0;33mJOGO DA FORCA!\033[m'.center(40))
    print('\033[0;32m-=\033[m' * 20)
    sleep(0.5)
    print('Seja bem-vindo ao jogo da forca, temos dois modos de jogo. No primeiro, você pode escolher\n'
          'qual tipo de palavra você vai querer, ou o sistema escolhe automaticamente, \n'
          'temos as seguintes classes: \033[0;36mcomidas, objetos e animais\033[m')
    print('\033[0;31mREGRAS\033[m: Não é possivel escrever a palavra toda de uma vez, não é necessario colocar acento nas palavras')
    sleep(2)
    print('\033[0;32m-=\033[m' * 20)
    print('Escolha uma das opções para jogar')
    print('\033[0;34m[ 1 ]\033[m Escolher \n\033[0;34m[ 2 ]\033[m Surpresa \n\033[0;34m[ 3 ]\033[m Sair     ')
    print('\033[0;32m-=\033[m' * 20)
    esc = estrutura_esc()
    if esc == 1:
        sleep(1)
        print('\033[0;32m-=\033[m' * 20)
        print('Ótima escolha, agora selecione qual o classe de palavra você deseja.')
        print('\033[0;34m[ 1 ]\033[m Comidas \033[m\n\033[0;34m[ 2 ]\033[m Objetos \n\033[0;34m[ 3 ]\033[m Animais ')
        print('\033[0;32m-=\033[m' * 20)
        sleep(1)
        esc_classe = estrutura_esc()
        return esc_classe
    elif esc == 2:
        print('\033[0;32m-=\033[m' * 20)
        print('O sistema vai escolher para você.')
        for c in range(1, 4):
            sleep(1)
            print(f'{c}', end='.. ')
            esc_classe = randint(1, 3)
        print()
        if esc_classe == 1: print('Classe escolhida foi \033[0;36mCOMIDAS.\033[m')
        elif esc_classe == 2: print('Classe escolhida foi \033[0;36mOBJETOS.\033[m')
        elif esc_classe == 3: print('Classe escolhida foi \033[0;36mANIMAIS.\033[m')
        return esc_classe
    elif esc == 3:
        print('\033[;032mFoi ótimo receber você, volte sempre.\033[m')
        return False


def jogo(num):
    if num == 1:
        palavra = comidas.escolha()
    elif num == 2:
        palavra = objetos.escolha()
    elif num == 3:
        palavra = animais.escolha()

    tentativas = 0
    palavra_secreta = ['_'] * len(palavra)
    letras_usadas = list()

    try:
        while tentativas <= 5:
            print('=' * 20)
            print(palavra)
            print(' '.join(palavra_secreta))
            print(f'Tentativas restantes: {6 - tentativas}')
            print('=' * 20)

            letra = str(input('LETRA: ')).lower()

            if not letra.isalpha() or len(letra) != 1:
                print('ERRO! Digite uma letra válida.')
                continue
            if letra in letras_usadas:
                print(f'Letra \033[0;32m{letra.upper()}\33 já foi utilizada. Tente novamente')
                continue

            if letra in palavra:
                print(f'Letra \033[0;32m{letra.upper()}\33[m está na palavra.')
                for pos, c in enumerate(palavra):
                    if c == letra:
                        palavra_secreta[pos] = letra
                        letras_usadas.append(letra)

            else:
                corpo(tentativas)
                tentativas += 1
                print(f'Letra \033[0;31m{letra.upper()}\33[m não está na palavra.')
                letras_usadas.append(letra)


            if '_' not in palavra_secreta:
                print(f'Parabéns! Você venceu o jogo.\nA palavra era: \033[0;32m{palavra.upper()}\33[m')
                break
        else:
            print('---')
            print(f'Você perdeu! A palavra correta era: \033[0;31m{palavra.upper()}\33[m')
    except KeyboardInterrupt:
        print('\nO jogador desistiu de jogar.')

