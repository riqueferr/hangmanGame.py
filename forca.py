print('*' * 25)
print('*' * 9, "forca", '*' * 9)
print('*' * 25)

secret_word = 'laranja'.upper()
qnt = len(secret_word)
print(f'qnt: {qnt} - secret word: {secret_word}')
second_list = []
list = []
list.extend('_' * qnt)
print(list)
correct = False

while True:
    correct = '_' not in list
    if correct:
        print(f'Deu sorte, mas acertou! A palavra é {secret_word.upper()}')
        break

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
        print(f'CASO SAIBA A RESPOSTA, FIQUE A VONTADE PARA DIGITAR!')
