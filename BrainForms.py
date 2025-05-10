def validar_email(email):
    if "@gmail.com" in email or "@hotmail.com" in email or "@icloud.com"  in email:
        return True
    else:
        return False
    
def validar_senha(senha):
    if len(senha) >= 8 and any(char.isdigit() for char in senha) and any(char.isalpha() for char in senha):
        return True
    else:
        return False

def retorno():
    retorno=input('\nGostaria de voltar a escolha de tópicos? (S/N)').upper()
    global topicos
    if retorno in ('S','SIM'):
        print('\nREDIRECIONANDO...\n')
        return topicos
    else:
        print('\n\nOK, Volte sempre ao BrainForms :D')
      

def exibir_respostas(respostas):
    print("\n\nAqui estar o histórico das suas respostas:")
    for resposta in respostas:
        escolhaQ, questao, RESPOSTA, acertou, resposta_apos_dica, acertou_apos_dica = resposta
        print(f"\n{questao}")
        print(f"\nRESPOSTA original: {RESPOSTA} - {'Correto' if acertou else 'Incorreto'}")
        if resposta_apos_dica:
            print(f"RESPOSTA após dica: {resposta_apos_dica} - {'Correto' if acertou_apos_dica else 'Incorreto'}")

print('Seja Muito Bem Vindo ao BrainForms!!\n')

# Armazena as respostas em uma matriz
respostas = []

while True:
    entrada = input('Você deseja fazer verificação de login ou cadastro?\nL=login\nC=cadastro\n\nDigite: ').upper()

    if entrada in ('L', 'LOGIN'):
        print('\nVamos iniciar seu login\n')
        emailL = input('Insira seu e-mail: ')

        if validar_email(emailL):
            print('\nE-mail válido! Podemos prosseguir!\n')
            senhaL = input('Insira sua senha (A senha deve ter pelo menos 8 caracteres, incluindo números e letras): ')

            if validar_senha(senhaL):
                print('\nSenha válida! Acesso liberado!\n')
                break
            else:
                print('\nA senha não atende aos critérios mínimos de segurança! Tente novamente.\nREDIRECIONANDO AO MENU INICIAL...\n')

        else:
            print('\nE-mail inválido!\nREDIRECIONANDO AO MENU INICIAL...\n')

    elif entrada in ('C', 'CADASTRO'):
        print('\nVamos iniciar seu cadastro\n')
        nomeC = input('Digite seu nome: ')
        emailC = input('\nDigite seu e-mail: ')

        if validar_email(emailC):
            print('\nE-mail válido! Podemos prosseguir!\n')
            senhaC = input('Crie sua senha (a senha deve ter pelo menos 8 caracteres, incluindo números e letras): ')

            if validar_senha(senhaC):
                confirmar_senhaC = input('Confirme sua senha: ')

                if confirmar_senhaC == senhaC:
                    print('\nSenha confirmada! Cadastro realizado com sucesso!\n')
                    break
                else:
                    print('\nAs senhas não coincidem! REDIRECIONANDO AO MENU INICIAL...\n')

            else:
                print('\nA senha não atende aos critérios mínimos de segurança! Tente novamente.\nREDIRECIONANDO AO MENU INICIAL...\n')

        else:
            print('\nE-mail inválido! REDIRECIONANDO AO MENU INICIAL...\n')

    else:
        print('\nEscolha inválida! REDIRECIONANDO AO MENU INICIAL...\n')

print('\nAcesso liberado para Tela Inicial\n')

while True:
    topicos = input('Gostaria de acessar o tópico de Questões ou Cálculo de Fórmulas?\nQ=Questões\nC=Cálculos de Fórmulas\n\nEscolha:').upper()
    if topicos in ('Q', 'QUESTÕES'):
        escolhaQ = input('''\nEscolha qual questão gostaria de fazer:\n
                         Digite "1" para questão de Análise Combinatória (Matemática)
                         Digite "2" para questão de Porcentagem (Matemática)
                         Digite "3" para questão de Cálculo de Velocidade (Física)
                         Digite "4" para questão de Cálculo de Altura (Física)\n
                         Insira qual questão deseja:''')

        match escolhaQ:
            
            case '1':
                questao = ('''\nQUESTÃO 01:\nUm técnico de um time de voleibol possui a sua disposição 15 jogadores que podem jogar em qualquer posição.
                De quantas maneiras ele poderá escalar seu time de 6 jogadores?
                (A) 4.450 maneiras
                (B) 5.210 maneiras
                (C) 4.500 maneiras
                (D) 5.005 maneiras
                (E) 5.610 maneiras''')
                print(questao)

                RESPOSTA = input('\nInsira a letra que representa sua RESPOSTA: "A", "B", "C", "D" ou "E": ').upper()

                acertou = RESPOSTA in ('D', '5.005')
                
                # Inicializa as variáveis para evitar NameError
                resposta_apos_dica = None
                acertou_apos_dica = None

                if acertou:
                    print('\nRESPOSTA certa. PARABÉNS!')
                else:
                    print('\nOps, não foi dessa vez, parece que sua RESPOSTA está incorreta.')
                    dica = input("\nDeseja receber uma dica? (S/N): ").upper()

                    if dica == 'S':
                        print('\nDica: Para calcular o número de maneiras de escalar o time, use a fórmula de combinação (C(n, k)), onde n é o número de jogadores disponíveis e k é o número de jogadores que o técnico deseja escalar.')

                        resposta_apos_dica = input('\nInsira a letra que representa sua RESPOSTA: "A", "B", "C", "D" ou "E": ').upper()

                        acertou_apos_dica = resposta_apos_dica in ('D', '5.005')

                        if acertou_apos_dica:
                            print('\nDessa vez você acertou. PARABÉNS!')
                        else:
                            print('\nDesculpe, sua RESPOSTA está incorreta novamente. A RESPOSTA correta é D) 5.005 maneiras.')
                    else:
                        print('\nA RESPOSTA correta seria D) 5.005 maneiras.')

                respostas.append([escolhaQ, questao, RESPOSTA, acertou, resposta_apos_dica, acertou_apos_dica])
                
                if not retorno():
                    break
        
        
            case '2':
                    questao = ('''\nQUESTÃO 02:\nUm boleto deveria ser pago no dia 10 de setembro, porém nesta data o devedor não possuía o dinheiro para o pagamento.')
                    Pagou o boleto somente no dia 20 de setembro, 10 dias após o vencimento
                    Ao efetuar o pagamento foi cobrado multa de 2% sobre o valor do boleto e R$ 5,40 por dia de atraso
                    Se o valor do boleto era de R$ 320,00 o valor pago no dia 20 com multa e juros foi de:
                    (A) R$ 378,80.
                    (B) R$ 380,40.
                    (C) R$ 382,20.
                    (D) R$ 386,60.
                    (E) R$ 392,40.''')
                    print(questao)

                    RESPOSTA = input('\nInsira a letra que representa sua RESPOSTA: "A", "B", "C", "D" ou "E": ').upper()

                    acertou = RESPOSTA in ('B' ,'380.40')
                    
                    # Inicializa as variáveis para evitar NameError
                    resposta_apos_dica = None
                    acertou_apos_dica = None

                    if acertou:
                        print('\nRESPOSTA certa. PARABÉNS!')
                    else:
                        print('\nOps, não foi dessa vez, parece que sua RESPOSTA está incorreta.')
                        dica = input("\nDeseja receber uma dica? (S/N): ").upper()

                        if dica == 'S':
                            print('\n\nDica: Para calcular o valor pago com multa e juros, primeiro calcule a multa de 2% sobre o valor do boleto e depois some os R$ 5,40 por cada dia de atraso.')

                            resposta_apos_dica = input('\nInsira a letra que representa sua RESPOSTA: "A", "B", "C", "D" ou "E": ').upper()

                            acertou_apos_dica = resposta_apos_dica in ('B' ,'380.40')

                            if acertou_apos_dica:
                                print('\nDessa vez você acertou. PARABÉNS!')
                            else:
                                print('\nDesculpe, sua RESPOSTA está incorreta novamente. A resposta correta é B) R$ 380,40.')
                        else:
                            print('\nA RESPOSTA correta seria B) R$ 380,40.')

                    respostas.append([escolhaQ, questao, RESPOSTA, acertou, resposta_apos_dica, acertou_apos_dica])
                    
                    if not retorno():
                        break
               
                
            case '3':
                questao = ('''\nQUESTÃO 03 (FÍSICA):\nUm objeto de 2 kg está inicialmente em repouso. Se uma força constante de 10 N é aplicada sobre ele, qual será sua velocidade (em m/s) após 5 segundos?\n')
                (A) 1 m/s
                (B) 5 m/s
                (C) 10 m/s
                (D) 25 m/s
                (E) 50 m/s''')
                print(questao)

                RESPOSTA = input('\nInsira a letra que representa sua RESPOSTA: "A", "B", "C", "D" ou "E": ').upper()

                acertou = RESPOSTA in ('C','10', '10 m/s')
                
                # Inicializa as variáveis para evitar NameError
                resposta_apos_dica = None
                acertou_apos_dica = None

                if acertou:
                    print('\nRESPOSTA certa. PARABÉNS!')
                else:
                    print('\nOps, não foi dessa vez, parece que sua RESPOSTA está incorreta.')
                    dica = input("\nDeseja receber uma dica? (S/N): ").upper()

                    if dica == 'S':
                        print('\nDica: Use a segunda Lei de Newton: F=ma para encontrar a aceleração e logo em seguida, use a fórmula de velocidade v=at para achar a resposta certa.')

                        resposta_apos_dica = input('\nInsira a letra que representa sua RESPOSTA: "A", "B", "C", "D" ou "E": ').upper()

                        acertou_apos_dica = resposta_apos_dica in ('C','10', '10 m/s')

                        if acertou_apos_dica:
                            print('\nDessa vez você acertou. PARABÉNS!')
                        else:
                            print('\nDesculpe, sua RESPOSTA está incorreta novamente. A resposta correta é a Letra (C) 10 m/s ')

                    else:
                        print('\nA RESPOSTA correta seria (C) 10 m/s ')


                respostas.append([escolhaQ, questao, RESPOSTA, acertou, resposta_apos_dica, acertou_apos_dica])
                
                if not retorno():
                    break
               
                
            case '4':
                    questao =  ('''\nQUESTÃO 04 (FÍSICA):\nUm objeto é lançado verticalmente para cima a partir do solo com uma velocidade inicial de 20 m/s.\nConsiderando a aceleraçao devido a gravidade g= 9,8m/s²\nQual será aproximadamente a altura máxima alcançada por esse objeto?\n')
                    (A) 10 m
                    (B) 20 m
                    (C) 25 m
                    (D) 40 m
                    (E) 50 m''')
                    print(questao)

                    RESPOSTA = input('\nInsira a letra que representa sua RESPOSTA: "A", "B", "C", "D" ou "E": ').upper()

                    acertou = RESPOSTA in ('B', '20', '20 m')
                    
                    # Inicializa as variáveis para evitar NameError
                    resposta_apos_dica = None
                    acertou_apos_dica = None

                    if acertou:
                        print('\nRESPOSTA certa. PARABÉNS!')
                    else:
                        print('\nOps, não foi dessa vez, parece que sua RESPOSTA está incorreta.')
                        dica = input("\nDeseja receber uma dica? (S/N): ").upper()

                        if dica == 'S':
                            print('\nDica: Use a formula movimento vertical no caso nessa questão seria, Hmax (altura maxima)= Vi² (Velocidade inicial) / 2.g (gravidade)')

                            resposta_apos_dica = input('\nInsira a letra que representa sua RESPOSTA: "A", "B", "C", "D" ou "E": ').upper()
                            
                            acertou_apos_dica = resposta_apos_dica in ('B', '20', '20 m')
                            
                            if acertou_apos_dica:
                                print('\nDessa vez você acertou. PARABÉNS!')
                            else:
                                print('\nDesculpe, sua RESPOSTA está incorreta novamente. A resposta correta é a Letra (B) 20m ')
                        else:
                            print('\nA RESPOSTA correta seria (B) 20m.')

                    respostas.append([escolhaQ, questao, RESPOSTA, acertou, resposta_apos_dica, acertou_apos_dica])
                    
                    if not retorno():
                        break

    
    
    elif topicos in ('C','CÁLCULOS'):
        escolhaC= input('\nEscolha qual Cálculo de Formúla gostaria de executar:\n\nDigite "1" Equação 2° grau (Matemática)\nDigite "2" Cálculos Geométricos (Matemática)\nDigite "3" Conversão de Celsius e Fahrenheit (Física)\nDigite "4" Cálculo da Velocidade Média (Física)\nDigite "5" Cálculo de Média Aritimética\nDigite "6" Calculo da Média Ponderada\nInsira qual cálculo deseja:')

        match escolhaC:
            case '1':
                print('\nUma Equação do Segundo Grau é escrita na forma padrão: ax^2 + bx + c = 0\nOnde: "a" é o coeficiente do termo quadrático (não pode ser igual a zero).\n"b" é o coeficiente do termo linear.\n"c" é o termo constante.\nSuas fórmulas são Delta = (b^2 - 4ac) e x = -b ± √(b² – 4ac)/2a\nA Equação do Segundo Grau serve para encontrar as raízes ou soluções de uma equação polinomial de segundo grau (x1) e (x2)')
                print('\nCÁLCULO 01:\nCalculando as raízes de uma equação de 2º grau\n')
                a = float(input('Entre com o valor de a: '))
                b = float(input('Entre com o valor de b: '))
                c = float(input('Entre com o valor de c: '))

                delta = (b**2 - 4*a*c)
                x1 = (-b + delta**(1/2)) / (2*a)
                x2 = (-b - delta**(1/2)) / (2*a)

                print(f'''\nValor de x1: {x1}
                Valor de x2: {x2}')
                \nResolução passo a passo:
                1: Calcule o valor de Delta usando a fórmula D = (b^2 - 4ac)
                D = ({b}^2 - 4*{a}*{c}) = {delta}\n
                2: Use a fórmula de Bhaskara x = -b ± √(b² – 4ac)/2a para calcular as raízes:
                x1 = (-{b} + √{delta}) / (2*{a})')
                x2 = (-{b} - √{delta}) / (2*{a})\n
                3: Substitua os valores de "Delta", "a" e "b" nas fórmulas e calcule x1 e x2.\n
                4: As raízes calculadas são os valores de x1({x1}) e x2({x2}).\n''')

                retorno()


            case '2':
                print('\nEm cálculos geométricos são encontradas medidas de uma figura geométrica, desde de sua área, perímetro e até volume')
                print('\nCÁLCULO 02:\nCálculando Fórmulas Geométricas\n')

                print('Área e Perímetro do círculos:\n')
                r = float (input ("Defina o valor do raio do círculo:"))
                Area = float (3.144444*r**2)
                print ("\nA área do círculo é:" , Area)
                print('\nResolução passo a passo:\n')
                print(f'1: Multiplique o valor de π(3,1444...) pelo valor do raio ao quadrado {r}^2\n2: O valor da área desse círculo será 3,1444*{r}^2= {Area}')

                Perimetro = float (2*3.1444444444*r)
                print('\nO perímetro do Círculo é:', Perimetro)
                print('\nResolução passo a passo:\n')
                print(f'1: Multiplique o valor de π(3,1444...) por 2\n2: Em seguida multiplique esse resultado ({3.1444*2}) pelo valor do raio({r})\n3: O valor do perímetro desse círculo será 3,1444*2*{r}= {Perimetro}')


                print('\nÁrea e Volume da esfera:')
                re = float (input('Defina o valor do raio da esfera:'))
                AreaE = float (4*3.14444*re**2)
                print ("\nA área da esfera é:" , AreaE)
                print('\nResolução passo a passo:\n')
                print(f'1: Multiplique o valor de π(3,1444...) por 4\n2: Em seguida multiplique esse resultado {3.1444*4} pelo valor do raio{re} ao quadrado\n3: O valor da área dessa esfera será 3,1444*4*{r}^2= {AreaE} ')

                VolumeE = float ((4*3.14444*re**3)/3)
                print ("\nO volume da esfera é:" , VolumeE)
                print('\nResolução passo a passo:\n')
                print(f'1: Multiplique o valor de π(3,1444...) por 4\n2: Em seguida multiplique esse resultado {3.1444*4} pelo valor do raio{re} ao cubo\n3: Após isso divida tudo por 3 {3.1444*4*re**3}/3\n4: O valor do volume dessa esfera será (3,1444*4*{r}^3)/3= {VolumeE} ')

                retorno()

            case '3':
                print('\nCelsius e Fahrenheit são medidas de temperaturas que possuem o mesmo objetivo, mas são indicadas por números diferentes, assim sendo necessário fazer suas conversões')
                print('\nCÁLCULO 03:\nCalculando Celsius e Fahrenheit\n')
                print('Celsius para Fahrenheit:\n')
                c = float (input ("Defina o valor de Celsius:\n"))
                Far = float (1.8*c+32)
                print ("O valor convertido em Fahrenheit é:" , Far)

                print('\nResolução passo a passo:\n')
                print(f'\n1: Multiplique o valor de celsius"{c}" por 1,8 ({c}*1,8).\n2: Some esse resultado "{c*1.8}" com 32:\n3: O resultado final da conversão será 1.8*{c}+32= {Far} Fahrenheit')

                print ("\nFahrenheit para Celsius:\n")

                f = float (input ("Defina o valor de Fahrenheit:"))
                Cel = float ((f-32)/1.8)
                print ("\nO valor covertido para Celsius é:" , Cel)

                print('\nResolução passo a passo:\n')
                print(f'\n1: Subtraia o valor de Fahrenheit"{f}" por 32 ({f}-32).\n2: Divida esse resultado "{f-32}" por 1,8:\n3: O resultado final da conversão será ({f}-32)/1,8= {Cel} Celsius')

                retorno()

            case '4':
                print('\nO cálculo da velocidade média é uma maneira de determinar a taxa média de mudança de posição de um objeto ao longo do tempo.\nPara calculá-la você pode usar a seguinte fórmula: Velocidade Média (V) = Variação da Posição / Intervalo de Tempo\nOnde: Velocidade Média (V) é a velocidade média do objeto.\nVariação na Posição (ΔS) é a diferença entre a posição final e a posição inicial do objeto.\nIntervalo de Tempo (Δt) é a diferença entre o tempo final e o tempo inicial.')
                print('\nCÁLCULO 04:\nCalculando a velocidade média')

                variação_de_espaço=float(input('\nInsira o valor da Variação da Posição em metros: '))

                variação_de_tempo=float(input('\nInsira o valor do Intervalo de Tempo em segundos: '))


                velocidade_media=(variação_de_espaço)/(variação_de_tempo)
                print(f'\nA Velocidade Média desse objeto é de: {velocidade_media}m/s')
                print(f'Em Km/h esse objeto estaria em uma velocidade de: {velocidade_media*3.6}KM/H')

                print('\nResolução passo a passo:\n')
                print(f'1: Para encontar a Velocidade Média basta dividir a Variação da posição({variação_de_espaço}) pelo Intervalo de Tempo({variação_de_tempo})')
                print(f'2: Para transformar a velocidade média m/s em KM/H, basta apenas multiplicar o valor da Velocidade Média em m/s {velocidade_media} por 3,6 que dará o resultado de {velocidade_media*3.6} KM/H.\n')

                retorno()
                
            
            case '5':
                print('\nA média aritmética é considerada uma medida de tendência central e é muito utilizada no cotidiano.\nSurge do resultado da divisão do somatório dos números dados pela quantidade de números somados')
                print('\nCÁLCULO 04:\nCalculando a Média Aritmética')
                
                soma = 0
                numero = int(input('\nQuantos valores você deseja inserir para calcular a média? \n'))

                for i in range(1, numero + 1):
                    valor = float(input(f'Insira o valor {i}: '))
                    soma += valor

                media = soma / numero
                
                print(f'O valor da Média é: {media}')

                print('\nResolução passo a passo:\n')
                print('Para calcular a média aritmética é necessrário somar todos os valores e\ndividir pela quantidade total de valores.\nDesse modo, temos:')
                print(f'A soma é dos seus valores inseridos é igual a: {soma}')
                print(f'A quantidade de valores é: {numero}')
                print(f'Logo sua média aritmética é igual a: {media}\n')
                
                retorno()
            
            case '6':
                print('\nA média Ponderada é a média que leva em consideração o peso atribuído a cada um dos valores dos quais queremos calcular a média.\nQuanto maior o peso de determinado valor, maior será o impacto dele na média, tornando esses valores mais relevantes.')
                ('\nCÁLCULO 06:\nCalculando a Média Pobderada')

                soma_produtos = 0
                soma_pesos = 0

                numero = int(input("Quantos valores que você deseja inserir? "))

                for i in range(1, numero + 1):

                    valor = float(input(f'Insira o valor {i}: '))
                    peso = float(input(f'Insira o peso para o valor {i}: '))
                    soma_produtos += valor * peso
                    soma_pesos += peso

                media_ponderada = soma_produtos / soma_pesos

                print('\nResolução passo a passo:\n')
                print('\nPara calcular a media ponderada é necessesario multiplicar o valor dos pesos com o valor colocardo pelo usuario exemplo 80 com peso 4 = 80*4\nDesse modo temos:')
                print(f'A soma dos valores (considerando já a multiplicação pelos pesos) é igual a: {soma_produtos}')
                print(f'A soma dos pesos é igual a: {soma_pesos}')
                print(f'A média ponderada é {media_ponderada}\n')

                retorno()
                

    else:
        print('Entrada inválida! Tente novamente.')
            
# Exibe todas as respostas no final
exibir_respostas(respostas)
