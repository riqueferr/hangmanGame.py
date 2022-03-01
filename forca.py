import random

print('*' * 25)
print('*' * 9, "forca", '*' * 9)
print('*' * 25)


def jogar_forca():
    secret_word = ler_arquivo()
    secret_list = inserir_caracteres_palavra_secreta(secret_word)
    logica_forca(secret_word, secret_list)


def ler_arquivo():
    words = []
    with open('words.txt', 'r') as fruit_file:
        for line in fruit_file:
            line = line.strip().upper()
            words.append(line)

    print(words)
    sorteio = random.randrange(0, len(words))
    secret_word = words[sorteio]
    return secret_word

def inserir_caracteres_palavra_secreta(secret_word):
    qnt = len(secret_word)
    print(f'qnt: {qnt} - secret word: {secret_word}')
    list = []
    list.extend('_' * qnt)
    print(list)
    return list

def logica_forca(secret_word, list):
    while True:
        correct = '_' not in list
        if correct:
            print(f'Deu sorte, mas acertou! A palavra é {secret_word.upper()}')
            break
        print(f'CASO SAIBA A RESPOSTA, FIQUE A VONTADE PARA DIGITAR!')
        letter = input('Qual a letra q vc quer?').upper()
        if letter == 'exit':
            break
        elif letter == secret_word:
            print(f'Deu sorte, mas acertou! A palavra é {secret_word.upper()}')
            break
        else:
            index_list = 0
            for counter in secret_word:
                if letter == counter:
                    list[index_list] = letter
                index_list += 1
            print(f'Por enquanto a palavra está assim> {list}')

if __name__ == '__main__':
    jogar_forca()
