#Aluna: LUISA COTINHO DE MELO
#Curso: Analise e Desenvolvimento de Sistemas

import random
from time import sleep

#criar um jogo - objetivo não morrer by tiros

print('=' * 25)
print('      ZOMBIE DICE   ')
print('=' * 25)

#JOGADORES
num_joga = int(input('Digite o número de jogadores [Minimo 2]: '))
if num_joga < 2:
    num_joga = int(input(('Número de jogadores inválido, digite novamente: [minimo 2]')))
#imprimi n vezes para número de jogadores
armazena_jogadores = []
for i in range(num_joga):
    nome = input(f'Digite o nome do jogador {i + 1}:')
    armazena_jogadores.append(nome)
#Imprimi o nome do jogadores
print('JOGADORES:', ', ' .join(armazena_jogadores).upper())
    
print('=' * 15)

#DADOS
dados_verdes = 'CPCTPC'

dados_amarelos = 'TPCTPC'

dados_vermelhos = 'TPTCPT'

#13 dados
dados = [
    dados_amarelos, dados_amarelos, dados_amarelos, dados_amarelos,
    dados_verdes,dados_verdes,dados_verdes,dados_verdes,dados_verdes,dados_verdes,
    dados_vermelhos, dados_vermelhos, dados_vermelhos
]

print('Iniciando o jogo...')
sleep(2)
print('Seus dados:')

#para armazenar os dados sorteados
jogadores = 0
dadosSorteados = []
tiros = 0
cerebro = 0
passos = 0


#dados aleatorios
while True:
    #aqui ok
    print(f'Turno do jogador {armazena_jogadores[jogadores]}')
    sleep(0.5)
    print('Você inicializa com 3 vidas...')
    sleep(1)
    print('=' * 15)
    #roda 3 dados
    for i in range(0, 3):
        #roda as 12 faces
        numSorteado = random.randint(0, 12)
        sorteados = dados[numSorteado]

        if sorteados == 'CPCTPC':
            corDado = '\033[32mVerde\033[m'
        elif sorteados == 'TPCTPC':
            corDado = '\033[33mAmarelo\033[m'
        else:
            corDado = '\033[31mVermelho\033[m'
        print(f'Dado Sorteado: {corDado}')

        #incluir um dado
        dadosSorteados.append(sorteados) 


    #itens dos dados:

    print('=' * 15)
    print('As faces sorteadas foram:')
    score_cerebro = []
    score_tiros = []
    for sorteados in dadosSorteados:
        #roda até 6
        faceDado = random.randint(0, 5)

        #condições dos dados - itens // adicionando as pontuações
        if sorteados[faceDado] == 'C':
            print("\033[32mCerebro\033[m")
            cerebro += 1
            score_cerebro.append(cerebro)
        elif sorteados[faceDado] == 'T':
            print('\033[31mTiro\033[m')
            tiros += 1
            score_tiros.append(tiros)
        else:
            print('Passos')
            passos += 1 
    print('=' * 15)

    #score do jogador atual
    print('Score Atual:')
    print(f'Cerebros: {cerebro}')
    print(f'Tiros {tiros}')

    #Caso queira jogar novamente
    continuarJogo = input('AVISO: Você deseja continuar jogando dados? [S/N]'.upper())

    if continuarJogo == 'n':  
        jogadores += 1
        dadosSorteados = []
        tiros = 0
        cerebros = 0
        passos = 0
        if jogadores == len(armazena_jogadores):
            print('Finalizando prototipo do jogo...')
            sleep(0.5)
            print('Bye Bye')
            break
    #Resposta positiva, deve voltar do inicio...como?
    else:
        print('Iniciando mais uma rodada do turno atual...')
        score_cerebro = [cerebro]
        score_tiros = [tiros]
        sleep(0.5)
        dadosSorteados = []
    
