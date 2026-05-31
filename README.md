# 🚀 Mission Control AI - Sistema Inteligente de Monitoramento Espacial

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.x-blue?style=for-the-badge&logo=python&logoColor=white" alt="Python Version">
  <img src="https://img.shields.io/badge/FIAP-Global%20Solution-red?style=for-the-badge" alt="FIAP GS">
  <img src="https://img.shields.io/badge/Status-Conclu%C3%ADdo-brightgreen?style=for-the-badge" alt="Status">
</p>

## 📋 Informações do Projeto
* **Nome da Missão:** Missão Vesania | Extração de Lithium
* **Equipe:** Equipe Astroneer
* **Instituição:** FIAP (Faculdade de Informática e Administração Paulista)
* **Sala:** 1CCPO

### 👥 Integrantes
* **Temitope Kuku da Silva Ogunbanjo** — RM 573772
* **Gabrieli de Lima Pettena de Oliveira** — RM 569799

---

## 🛰️ Sobre o Projeto
O **Mission Control AI** é uma solução em Python desenvolvida para a Global Solution, simulando o sistema de monitoramento central de uma missão espacial experimental em Vesania. O programa analisa múltiplos fatores críticos de suporte e infraestrutura para classificar o nível de risco de cada ciclo de operação, gerando relatórios de tendência e alertas automáticos com base em regras lógicas predefinidas.

---

## ⚙️ Como o Código Funciona (Arquitetura Lógica)

O core do sistema baseia-se no conceito de **estruturas de dados estáticas correlacionadas**. O motor do programa foi otimizado para evitar desperdício de memória e garantir consistência na leitura das seguintes métricas:
1. Temperatura Interna (ºC)
2. Comunicação com a Base (%)
3. Sistema de Energia / Bateria (%)
4. Suporte de Oxigênio (%)
5. Estabilidade Operacional (%)

---

### 🧠 Logica de Indexação Síncrona via `enumerate()`
A principal inteligência de mapeamento do código funciona através de **listas padronizadas que acessam valores conforme o índice (`index`) gerado pela função `enumerate()`**. 

Quando a matriz multidimensional `dados_missao` é iterada ciclo a ciclo:
1. O laço interno utiliza o `enumerate(ciclo)` para extrair simultaneamente a telemetria (o valor numérico bruto) e a sua posição exata na lista.
2. Esse **índice de posição** atua como uma chave universal. Ele é repassado para as funções analíticas para acessar de forma síncrona as listas de metadados correspondentes nas variáveis globais (como `variaveis`, `mensagens_recomendacoes` e `areas_monitoradas`).

*Exemplo prático:* Se o `enumerate` estiver no `index = 2`, o sistema sabe automaticamente que o valor numérico refere-se à variável `BATERIA`, buscará as diretrizes de tratamento específicas de bateria, e selecionará as recomendações do índice `2` da matriz de alertas, garantindo que o acoplamento de dados seja limpo, modular e sem necessidade de estruturas complexas ou bibliotecas externas.

---

## 🖥️ Estrutura do Relatório Gerado
Ao final da execução, o terminal exibe um log detalhado composto por duas seções principais:
1. **Mapeamento por Ciclo:** Apresentação formatada das telemetrias de cada período, acompanhada do diagnóstico textual individual de cada subsistema e recomendações randômicas de mitigação de falhas.
2. **Relatório Final Consolidado:** Apresentação de médias aritméticas das variáveis, identificação exata do ciclo mais perigoso, cálculo da pontuação de risco acumulada por área (determinando qual foi o setor mais afetado na missão), tendência estatística (Melhorar, Piorar ou Se Manter Estável) e uma mensagem conclusiva contextualizada com o estado geral da operação.

---

## 🛠️ Como Executar a simulação

1. Clone este repositório ou baixe o arquivo fonte.
2. Certifique-se de que o arquivo está localizado na estrutura correta recomendada (`mission-control-ai/mission_control.py`).
3. Abra o seu terminal na pasta do projeto e execute o comando:
   ```bash
   python mission_control.py
