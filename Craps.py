#EP1 - Design de Software
#Rodrigo Paoliello de Medeiros

import random

din = 1000
print('Voce tem {0} dinheiros'.format(din))
print('')
print('Para cada aposta digite o numero que quiser apostar ou 0 se nao quiser apostar')
print('')


while True:

    print('Voce esta agora na fase Come Out')
    print('')
    
    if din == 0:
        print('Seu dinheiro acabou!')
        break
    
    apostafield = input('Quanto quer apostar em field? ')
    apostafield = int(apostafield)
    if apostafield > din:
        print ('Voce nao tem esse dinheiro')
        print('')
        continue
    din -= apostafield
    print('Voce tem {0} dinheiros'.format(din))
    print('')
    
    apostaanycraps = input('Quanto quer apostar em any craps? ')
    apostaanycraps = int(apostaanycraps)
    if apostaanycraps > din:
        print ('Voce nao tem esse dinheiro')
        print('')
        continue
    din -= apostaanycraps
    print('Voce tem {0} dinheiros'.format(din))
    print('')
    
    apostatwelve = input('Quanto quer apostar em twelve? ')
    apostatwelve = int(apostatwelve)
    if apostatwelve > din:
        print ('Voce nao tem esse dinheiro')
        print('')
        continue
    din -= apostatwelve
    print('Voce tem {0} dinheiros'.format(din))
    print('')

    apostaplb = input('Quanto quer apostar em pass line bet? ')
    apostaplb = int(apostaplb)
    if apostaplb > din:
        print ('Voce nao tem esse dinheiro')
        print('')
        continue
    din -= apostaplb
    print('Voce tem {0} dinheiros'.format(din))
    print('')

    dado1 = random.randint(1,6)
    dado2 = random.randint(1,6)
    soma = dado1 + dado2
    print('No primeiro dado caiu {0}, no segundo dado caiu {1} e a soma deu {2}'.format(dado1,dado2,soma))
    print('')
        
    #Field:
    if apostafield != 0 :
        print('Field: ')
        if soma == 3 or soma == 4 or soma == 9 or soma == 10 or soma == 11:
            din += apostafield + apostafield
            print('Vc ganhou Field! Agora tem {0} dinheiros.'.format(din))
            print('')

        elif soma == 2:
            din += apostafield + apostafield * 2
            print('Vc ganhou Field! Agora tem {0} dinheiros.'.format(din))
            print('')

        elif soma == 12:
            din += apostafield + apostafield * 3
            print('Vc ganhou Field! Agora tem {0} dinheiros.'.format(din))
            print('')
    
        else:
            print('Vc perdeu Field!')
            print('')

    #Any craps:
    if apostaanycraps != 0 :
        print('Any Craps: ')
        if soma == 2 or soma == 3 or soma == 12:
            din += apostaanycraps + apostaanycraps * 7
            print('Vc ganhou Any Craps! Agora esta com {0} dinheiros.'.format(din))
            print('')

        else:
            print('Vc perdeu Any Craps!')
            print('')

    #Twelve:
    if apostatwelve != 0 :
        print('Twelve: ')
        if soma == 12:
            din += apostatwelve + apostatwelve * 30
            print('Vc ganhou Twelve! Agora esta com {0} dinheiros.'.format(din))
            print('')

        else:
            print('Vc perdeu Twelve!')
            print('')

    #Pass line bet:
    if apostaplb != 0:
        print('Pass line bet: ')
        if soma == 7 or soma == 11:
            din += apostaplb + apostaplb
            print('Vc ganhou Pass Line Bet! Agora tem {0} dinheiros.'.format(din))
            print('')

        #Point:
        elif soma == 4 or soma == 5 or soma == 6 or soma == 8 or soma == 9 or soma == 10:
            point = soma           
            
            while True:

                print('Vc esta agora na fase Point')
                print('')

                apostafield = input('Quanto quer apostar em field? ')
                apostafield = int(apostafield)
                if apostafield > din:
                    print ('Voce nao tem esse dinheiro')
                    print('')
                    continue
                din -= apostafield
                print('Voce tem {0} dinheiros'.format(din))
                print('')
    
                apostaanycraps = input('Quanto quer apostar em any craps? ')
                apostaanycraps = int(apostaanycraps)
                if apostaanycraps > din:
                    print ('Voce nao tem esse dinheiro')
                    print('')
                    continue
                din -= apostaanycraps
                print('Voce tem {0} dinheiros'.format(din))
                print('')
    
                apostatwelve = input('Quanto quer apostar em twelve? ')
                apostatwelve = int(apostatwelve)
                if apostatwelve > din:
                    print ('Voce nao tem esse dinheiro')
                    print('')
                    continue
                din -= apostatwelve
                print('Voce tem {0} dinheiros'.format(din))
                print('')
                
                dado1 = random.randint(1,6)
                dado2 = random.randint(1,6)
                soma = dado1 + dado2
                print('No primeiro dado caiu {0}, no segundo dado caiu {1} e a soma deu {2}'.format(dado1,dado2,soma))
                print('')

                if apostafield != 0 :
                    print('Field: ')
                    if soma == 3 or soma == 4 or soma == 9 or soma == 10 or soma == 11:
                        din += apostafield + apostafield
                        print('Vc ganhou Field! Agora tem {0} dinheiros.'.format(din))
                        print('')

                    elif soma == 2:
                        din += apostafield + apostafield * 2
                        print('Vc ganhou Field! Agora tem {0} dinheiros.'.format(din))
                        print('')

                    elif soma == 12:
                        din += apostafield + apostafield * 3
                        print('Vc ganhou Field! Agora tem {0} dinheiros.'.format(din))
                        print('')
    
                    else:
                        print('Vc perdeu Field!')
                        print('')

                if apostaanycraps != 0 :
                    print('Any Craps: ')
                    if soma == 2 or soma == 3 or soma == 12:
                        din += apostaanycraps + apostaanycraps * 7
                        print('Vc ganhou Any Craps! Agora esta com {0} dinheiros.'.format(din))
                        print('')

                    else:
                        print('Vc perdeu Any Craps!')
                        print('')

                if apostatwelve != 0 :
                    print('Twelve: ')
                    if soma == 12:
                        din += apostatwelve + apostatwelve * 30
                        print('Vc ganhou Twelve! Agora esta com {0} dinheiros.'.format(din))
                        print('')

                    else:
                        print('Vc perdeu Twelve!')
                        print('')

                if soma == point:
                    din += apostaplb + apostaplb
                    print('Pass Line Bet:')
                    print('Vc ganhou Pass Line Bet! Agora tem {0} dinheiros.'.format(din))
                    print('')
                    break
                if soma == 7:
                    print('Pass Line Bet:')
                    print('Vc perdeu Pass Line Bet!'.format(din))
                    print('')
                    break

        elif soma == 12:
            din += apostaplb + apostaplb * 3
            print('Vc ganhou Pass Line Bet! Agora tem {0} dinheiros.'.format(din))
            print('')
    
        else:
            print('Vc perdeu Pass Line Bet!'.format(din))
            print('')

    continuar = input('Voce quer continuar o jogo? (s/n) ')
    print('')
    if continuar == 'n':
        print('Obrigado por jogar! Voce acabou com {0} dinheiros!'.format(din))
        break
    
    continue
