numerosecreto = 46
tentativas = 5
while tentativas > 0:
    chute = int(input('digite um numero: '))
    print(f'voce digitou {chute}')
    if chute < numerosecreto:
        print('Voce errou, o numero secreto e maior')
    elif chute > numerosecreto:
        print('voce errou, o numero secreto e menor')
    else:
        print('acertou')
        break
    tentativas -= 1
else:
    print(f'suas tentativas acabaram. O numero secreto era {numerosecreto}')