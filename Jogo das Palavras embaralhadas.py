import random
print('-=-'*30)
print('Vamos jogar? Irei imprimir palavras na tela embaraçadas onde você deve advinhar.\n Vamos tentar?!')
print('-=-'*30)
lista_p = ['cerveja','tribunal','peixe','padaria','escola','faculdade','porco','pedreiro']
sorteada = random.choice(lista_p)
palavra = list(sorteada)
random.shuffle(palavra)
palavra = ''.join(palavra)
tentativas = 6
vezes = 1
print('\nVou te dar 6 chances valendo a primeira agora. A palavra é "{}"\n'.format(palavra))
while tentativas:
    vezes += 1
    tentativas += -1
    pala_dig = input('Informe qual é o nome da palavra embaralhada: ').lower()
    if pala_dig == sorteada:
        print('Parabéns você conseguiu acertar! A palavra é {}! \n'.format(sorteada))
        tentativas = 0
        
    elif tentativas == 1:
        print('-=-'*20)
        print('Lembrando, essa é sua ultima chance')
        print('-=-'*20)
        
    if tentativas > 1:
        print('-=-'*30)
        print('\nOps, vou te dar a {}° chance, a palavra informada está errada. Tente outra vez! \n'.format(vezes))
        print('-=-'*30)
        
    if vezes == 7:
        print('-=-'*20)
        print('\n *Reinicie o jogo você atingiu o limite de tentativas!')
        
    if pala_dig == sorteada and tentativas == 0:
        print('\n *Reinicie o arquivo caso queira joga-lo novamente!')
        
    
                    
