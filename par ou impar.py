from random import randint
c = 0
opcao = ' '
while True:
    print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
    print('Vamos jogar PAR ou ÍMPAR!')
    print('~~~~~~~~~~~~~~~~~~~~~~~~~~~')
    n = (int(input('Digite um valor: ')))
    p = randint(0, 10)
    soma = n + p
    tipo = ' '
    opcao = str(input('Par ou ímpar? [P/I] ')).strip().upper()[0]
    while opcao not in 'PI':
        opcao = str(input('Par ou ímpar? [P/I] ')).strip().upper()[0]
    print(f'O computador jogou {p} e você {n}. A soma dá {soma}')
    if soma % 2 == 0 and opcao == 'P':
        print('Você ganhou!')
        c += 1

    elif soma % 2 != 0 and opcao == 'I':
        print('Você ganhou!')
        c += 1
    elif soma % 2 == 0 and opcao == 'I':
        print('Você perdeu!')
        break
    elif soma % 2 != 0 and opcao == 'P':
        print('Você perdeu!')
        break
    print('Vamos jogar novamente? ')
print(f'Você ganhou {c} vezes!')