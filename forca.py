print('*' * 25)
print('*' * 9, "forca", '*' * 9)
print('*' * 25)

secret_word = 'laranja'
qnt = len(secret_word)
# print(f'qnt: {qnt} - secret word: {secret_word}')
second_list = []
list = []
list.extend('_' * qnt)
print(list)

while True:
    letter = input('Qual a letra q vc quer?')
    if letter == 'exit':
        break
    elif letter == secret_word:
        print(f'Deu sorte, mas acertou!!!')
        break
    else:
        index_list = 0
        for counter in secret_word:
            if letter == counter:
                list[index_list] = letter
            elif letter == 'exit':
                print('saindo...')
            index_list += 1

        print(f'Por enquanto a palavra está assim>  {list}')
        print(f'CASO SAIBA A RESPOSTA, FIQUE A VONTADE PARA DIGITAR!')
