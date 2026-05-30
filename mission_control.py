import math #Utilizado para arredondar valores
import random #É usado somente para acessar mensagens aleatórias | Diferenciando cada iteração do código

largura_terminal = 80
#Essa variável é usada para printar linhas no terminal (==========) = ("=" * largura_terminal)

dados_missao = [
    [35, 18, 91, 8, 63],
    [52, 45, 13, 88, 36],
    [17, 74, 29, 95, 5],
    [41, 57, 81, 22, 69],
    [25, 10, 38, 60, 99],
    [29, 62, 58, 84, 73]
]

variaveis = ["TEMPERATURA", "COMUNICAÇÃO", "BATERIA", "OXIGÊNIO", "ESTABILIDADE"]
#Lista com as variáveis na ordem correta | Usada para converter index's em variável

classificacoes = ["PIORAR", "MELHORAR", "SE MANTER ESTÁVEL"]
#Classificações de tendência da missão

pontuacoes = [0, 1, 2]
#Quanto vale cada tipo de classificação (Normal | Atenção | Crítico)

areas_monitoradas = [
    "Temperatura interna",
    "Comunicação com a base",
    "Sistema de energia",
    "Suporte de oxigênio",
    "Estabilidade operacional"
]

mensagens_recomendacoes = [
    #A lista possuí diveras mensagens para cada variável
    [
        "Ajuste os módulos de controle térmico para evitar superaquecimento.",
        "Reduza atividades não essenciais até que a temperatura retorne aos níveis seguros.",
        "Verifique os sistemas de refrigeração da base e substitua componentes."
    ],
    [
        "Realinhe as antenas de comunicação para melhorar a transmissão.",
        "Execute uma varredura nos repetidores de sinal instalados.",
        "Priorize o envio de informações críticas enquanto a conexão permanece instável."
    ],
    [
        "Amplie a geração de energia utilizando painéis solares.",
        "Desative equipamentos secundários para preservar a carga.",
        "Inspecione cabos e baterias em busca de falhas."
    ],
    [
        "Verifique os geradores de oxigênio e garanta o fornecimento.",
        "Reduza deslocamentos desnecessários até normalizar.",
        "Realize manutenção preventiva nos tanques e filtros."
    ],
    [
        "Revise os protocolos para reduzir riscos na extração.",
        "Distribua melhor as tarefas entre os módulos para evitar sobrecarga.",
        "Execute diagnósticos completos nos sistemas críticos."
    ]
]

mensagens_classificacao = [
    #Diversidade de mensagens de classificação
    [
        "Os níveis de risco aumentaram desde o início da operação em Vesania.",
        "Sensores registraram crescimento contínuo dos riscos operacionais.",
        "A equipe Astroneer identificou uma piora nos indicadores da missão.",
        "O ambiente de Vesania apresentou aumento de instabilidade."
    ],
    [
        "Os riscos da missão diminuíram desde o ciclo inicial.",
        "Os indicadores apontam redução gradual dos riscos em Vesania.",
        "A equipe Astroneer conseguiu estabilizar parte das ameaças.",
        "Os sistemas registram melhora consistente nas condições operacionais.",
    ],
    [
        "Os níveis de risco permaneceram semelhantes aos observados no início.",
        "Não foram detectadas variações significativas nos indicadores de risco.",
        "As condições da missão permanecem estáveis.",
        "Os sistemas registram comportamento consistente dos riscos."
    ]
]

nome = "Missão Vesania | Extração de Lithium"
equipe = "Equipe Astroneer"

#Nome e equipe baseado no jogo astroneer (Exploração espacial)
#Vesania = Um planeta do jogo que realmente possuí o minério Lithium

#Função geral para realizar a GS
def simular_missao():
    resultados = []

    for ciclo in dados_missao:
        pontuacao = 0 #Soma da pontuação do ciclo
        dados_variaveis = [] #Lista com : classificação | pontuação e valor de cada variável

        for index, variavel in enumerate(ciclo):
            variavel_atual = variaveis[index]
            classificacao = analisar_variavel(variavel_atual, variavel)
            dados_variaveis.append([classificacao[0], classificacao[1], variavel])
            pontuacao += classificacao[1]

        classificacao_ciclo_atual = classificar_ciclo(pontuacao) #Pega a classificação do ciclo em geral
        recomendacoes_por_variavel = identificar_recomendacao_por_linha(dados_variaveis) #Retorna uma lista com todas as recomendações das variáveis em ordem
        areas_mais_afetadas = identificar_areas_criticas(dados_variaveis) #Identifica as áreas mais afetas (pode ser mais de uma caso tenham valor igual)

        resultado = [pontuacao, classificacao_ciclo_atual, dados_variaveis, recomendacoes_por_variavel,areas_mais_afetadas] #Dados do atual ciclo convertido em lista
        resultados.append(resultado) #Coloca a lista na lista de dados dos ciclos

    analises = definir_clasificacoes(resultados)  #Retona as tendências e mensagens de cada variável
    tendencias = analises[0]
    mensagens_ciclos = analises[1]
    estatisticas = calcular_estatisticas_ciclos(resultados) #Diversas estátiscas úteis para o print ordem das variáveis:
    # [Medias, Ciclo_mais_critico, Maior_pontuação_risco, risco_medio, ciclos_criticos, ciclos_estaveis, ciclos_atencao, pontuação acumulada, total de pontuações, area mais afetada e classificação final]
    
    tendencia_missao = calcular_tendencia(resultados) #Usa a tendência da primeira e da última para calcular a da missão

    print_header()

    for i in range(len(dados_missao)):
        ciclo_atual = resultados[i]
        print(f"CICLO {i + 1}")
        print("-" * largura_terminal)
        print(f"Temperatura: {ciclo_atual[2][0][2]:.2f} ºC | {ciclo_atual[2][0][0].upper()} | {ciclo_atual[3][0]}")
        print(f"Comunicação: {ciclo_atual[2][1][2]:.2f} % | {ciclo_atual[2][1][0].upper()} | {ciclo_atual[3][1]}")
        print(f"Bateria: {ciclo_atual[2][2][2]:.2f} % | {ciclo_atual[2][2][0].upper()} | {ciclo_atual[3][2]}")
        print(f"Oxigênio: {ciclo_atual[2][3][2]:.2f} % | {ciclo_atual[2][3][0].upper()} | {ciclo_atual[3][3]}")
        print(f"Estabilidade: {ciclo_atual[2][4][2]:.2f} % | {ciclo_atual[2][4][0].upper()} | {ciclo_atual[3][4]}")
        print()
        print(f"Pontuação de risco do ciclo: {ciclo_atual[0]}")
        print(f"Classificação do ciclo: {ciclo_atual[1]}")
        print(f"Status do ciclo: {mensagens_ciclos[i]}")
        print()

    print("=" * largura_terminal)
    print("RELATÓRIO FINAL DA MISSÃO")
    print("=" * largura_terminal)
    print(f"Missão : {nome}")
    print(f"Equipe : {equipe}")
    print()
    print(f"Quantidade de ciclos analisados : {len(dados_missao)}")
    print()
    print(f"Média de temperatura: {estatisticas[0][0]:.2f} ºC")
    print(f"Média de comunicação: {estatisticas[0][1]:.2f} %")
    print(f"Média de bateria: {estatisticas[0][2]:.2f} %")
    print(f"Média de oxigênio: {estatisticas[0][3]:.2f} %")
    print(f"Média de estabilidade: {estatisticas[0][4]:.2f} %")
    print()
    print(f"Ciclo mais crítico : {estatisticas[1]}")
    print(f"Maior pontuação de risco : {estatisticas[2]}")
    print(f"Risco médio da missão : {estatisticas[3]:.2f}")
    print(f"Quantidade de ciclos críticos : {estatisticas[4][0]}")
    print(f"Quantidade de ciclos estáveis : {estatisticas[4][1]}")
    print(f"Quantidade de ciclos atenção : {estatisticas[4][2]}")
    print()
    print("Tendência da missão:")
    if tendencia_missao == "PIORAR":
        print("A missão apresentou tendência de piora.")
    elif tendencia_missao == "MELHORAR":
        print("A missão apresentou tendência de melhora.")
    else:
        print("A missão permaneceu estável em relação ao início.")
    print()
    print("Pontuação acumulada por área:")
    print(f"{areas_monitoradas[0]} : {estatisticas[5][0]} pontos")
    print(f"{areas_monitoradas[1]} : {estatisticas[5][1]} pontos")
    print(f"{areas_monitoradas[2]} : {estatisticas[5][2]} pontos")
    print(f"{areas_monitoradas[3]} : {estatisticas[5][3]} pontos")
    print(f"{areas_monitoradas[4]} : {estatisticas[5][4]} pontos")
    print()
    print(f"Pontuação total : {estatisticas[6]}")
    print()
    print("Área mais afetada:")
    print(f"{estatisticas[7]}")
    print()
    print("Classificação final da missão:")
    print(f"{estatisticas[8]}")
    print()
    print("Conclusão:")
    if estatisticas[8] == "MISSÃO CRÍTICA":
        print("ALERTA VERMELHO: Instabilidade severa detectada no núcleo de Vesania. Riscos críticos de sobrecarga na extração de Lithium. Ative imediatamente os protocolos de evacuação emergencial e contenção dos módulos Astroneer!")
    elif estatisticas[8] == "MISSÃO EM ATENÇÃO":
        print("NOTIFICAÇÃO OPERACIONAL: Parâmetros atmosféricos e estruturais oscilando além da margem ideal. Recomenda-se cautela no manejo dos geradores e manutenção preventiva nos filtros antes que o próximo ciclo de mineração seja iniciado.")
    else:
        print("STATUS RECURSOS: Operação nominal estável. Os sistemas de suporte de vida e extração seguem em perfeita harmonia com o ambiente de Vesania. Prossiga com o cronograma padrão de exploração, pioneiro.")


#Função que pega a variável (strin) e o Valor (Número) e retorna sua classificação
def analisar_variavel(variavel, valor):
    result = ""
    variavel_maiuscula = variavel.upper() #Normaliza

    #Cada variável possuí uma função dentro da função
    #Isso permite chamar só a função analisar_variavel ao invés de criar uma para cada variável
    def temperatura(value):
        if value < 18: return "Atenção"
        if 18 <= value <= 30: return "Normal"
        if 30 < value <= 35: return "Atenção"
        if value > 35: return "Crítico"

    def comunicacao(value):
        if value < 30: return "Crítico"
        if 30 <= value <= 59: return "Atenção"
        if value >= 60: return "Normal"

    def bateria(value):
        if value < 20: return "Crítico"
        if 20 <= value <= 49: return "Atenção"
        if value >= 50: return "Normal"

    def oxigenio(value):
        if value < 80: return "Crítico"
        if 80 <= value <= 89: return "Atenção"
        if value >= 90: return "Normal"

    def estabilidade(value):
        if value < 40: return "Crítico"
        if 40 <= value <= 69: return "Atenção"
        if value >= 70: return "Normal"


    #Calculando resultado conforme a variável
    if variavel_maiuscula == "TEMPERATURA":
        result = temperatura(valor)
    elif variavel_maiuscula == "COMUNICAÇÃO":
        result = comunicacao(valor)
    elif variavel_maiuscula == "BATERIA":
        result = bateria(valor)
    elif variavel_maiuscula == "OXIGÊNIO":
        result = oxigenio(valor)
    elif variavel_maiuscula == "ESTABILIDADE":
        result = estabilidade(valor)

    #Cálculo de pontuação conforme a ordem da lista pontuacoes
    pontuacao = 0
    if result.upper() == "NORMAL":
        pontuacao = pontuacoes[0]
    elif result.upper() == "ATENÇÃO":
        pontuacao = pontuacoes[1]
    elif result.upper() == "CRÍTICO":
        pontuacao = pontuacoes[2]

    #Retorna tanto o resultado quanto a pontuação
    return [result, pontuacao]

#Função simples para classificar o ciclo em estável | atenção | Crítico
def classificar_ciclo(pontuacao):
    if 0 <= pontuacao <= 2:
        return "MISSÃO ESTÁVEL"
    elif 3 <= pontuacao <= 5:
        return "MISSÃO EM ATENÇÃO"
    elif 6 <= pontuacao <= 10:
        return "MISSÃO CRÍTICA"
    return ""

#Função que defini a tendência de um ciclo com base no anterior
def definir_clasificacoes(ciclos):
    mensagens = []
    tendencias = []

    for i, v in enumerate(ciclos):
        recomendacao = 2
        ciclo_anterior = ciclos[i - 1]

        if i != 0 and ciclo_anterior:
            if v[0] > ciclo_anterior[0]:
                recomendacao = 0
            elif v[0] < ciclo_anterior[0]:
                recomendacao = 1

        lista_mensagens = mensagens_classificacao[recomendacao]
        mensagem = lista_mensagens[random.randint(0, len(lista_mensagens) - 1)]
        tendencias.append(classificacoes[recomendacao])
        mensagens.append(mensagem)

    #Retorna tanto a tendência quanto uma mensagem aleatória
    return [tendencias, mensagens]


#Pega a mensagem aleatória de recomendação que aparece no print depois da classificação
def identificar_recomendacao_por_linha(dados):
    recomendacoes = []
    for index, variavel in enumerate(dados):
        mensagens_variavel = mensagens_recomendacoes[index]
        recomendacoes.append(mensagens_variavel[random.randint(0, len(mensagens_variavel) - 1)])
    return recomendacoes


#Identifica a àrea mais afetada
def identificar_areas_criticas(dados):
    maior = 0
    resultado = []
    areas_mais_afetadas = []

    for index, variavel in enumerate(dados):
        if variavel[1] > maior:
            maior = variavel[1]

    for index, variavel in enumerate(dados):
        if variavel[1] == maior:
            resultado.append(index)

    for index in resultado:
        areas_mais_afetadas.append(variaveis[index])

    return areas_mais_afetadas


#Essa função calcula diversas estátiscas de todos os ciclos
#Colocamos ela aqui para não poluir muito a função principal
def calcular_estatisticas_ciclos(ciclos):
    ciclo_mais_critico = ""
    medias = [0.0, 0.0, 0.0, 0.0, 0.0]
    area_mais_afetada = ""
    maior_area = -1

    ciclos_estaveis = 0
    ciclos_atencao = 0
    ciclos_criticos = 0

    maior_pontuacao_risco = -1
    risco_total = 0

    pontuacao_acumulada = [0, 0, 0, 0, 0]

    for index, ciclo in enumerate(ciclos):
        risco_ciclo = ciclo[0]
        risco_total += risco_ciclo

        if risco_ciclo > maior_pontuacao_risco:
            maior_pontuacao_risco = risco_ciclo
            ciclo_mais_critico = f"Ciclo {index + 1}"

        if ciclo[1] == "MISSÃO ESTÁVEL":
            ciclos_estaveis += 1
        elif ciclo[1] == "MISSÃO EM ATENÇÃO":
            ciclos_atencao += 1
        elif ciclo[1] == "MISSÃO CRÍTICA":
            ciclos_criticos += 1

        for index_dados, dados in enumerate(ciclo[2]):
            pontuacao_acumulada[index_dados] += dados[1]
            medias[index_dados] += dados[2]

    for i in range(len(medias)):
        medias[i] /= len(ciclos)

    for index_area, valor_area in enumerate(pontuacao_acumulada):
        if valor_area > maior_area:
            maior_area = valor_area
            area_mais_afetada = areas_monitoradas[index_area]

    risco_medio = risco_total / len(ciclos)
    classificacao_final = classificar_ciclo(math.ceil(risco_medio))

    #Esse return tem a ordem correta que serve de base na função principal
    return [
        medias, ciclo_mais_critico, maior_pontuacao_risco, risco_medio,
        [ciclos_criticos, ciclos_estaveis, ciclos_atencao],
        pontuacao_acumulada, sum(pontuacao_acumulada), area_mais_afetada, classificacao_final
    ]

#Calcula a tendência com base no primeiro e ultimo ciclo
def calcular_tendencia(ciclos):
    primeiro_risco = ciclos[0][0]
    ultimo_risco = ciclos[-1][0] #[-1] pega o ultimo | mesma coisa de (len(x) - 1)

    if ultimo_risco > primeiro_risco: return "PIORAR"
    if ultimo_risco < primeiro_risco: return "MELHORAR"
    return "SE MANTER ESTÁVEL"

def print_header():
    print("=" * largura_terminal)
    print("MISSION CONTROL AI")
    print("=" * largura_terminal)
    print(f"Missão : {nome}")
    print(f"Equipe : {equipe}")
    print(f"Quantidade de ciclos analisados : {len(dados_missao)}")
    print("=" * largura_terminal)
    print()

#Função que chama a simulação
simular_missao()