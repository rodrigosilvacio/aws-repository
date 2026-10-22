# Tech Challenge AWS Repository

Repositório contendo projetos de análise de dados e previsão de séries temporais, além de scripts de automação para serviços AWS.

## O que este projeto faz

Este repositório contém dois principais componentes:

1. **Análise de Exportação de Vinhos Brasileiros**: Análise exploratória e visualização de dados de exportação de vinhos do Brasil, incluindo tratamento de dados, análise descritiva e visualizações gráficas.

2. **Previsão do IBOVESPA (Tech Challenge Fase 2)**: Modelos preditivos para prever o fechamento diário da pontuação do IBOVESPA utilizando séries temporais. O projeto implementa e compara diversos modelos de previsão.

3. **Scripts AWS**: Scripts utilitários para interação com serviços AWS como S3 e EC2.

## Principais Funcionalidades

### Análise de Exportação de Vinhos
- Leitura e tratamento de dados históricos de exportação (arquivo `ExpVinho.csv`)
- Conversão de dados de formato wide para long
- Análise dos últimos 15 anos de dados
- Agrupamento e resumo por país de destino
- Visualização com gráficos de barras (valores exportados em USD)

### Previsão do IBOVESPA
- Implementação de múltiplos modelos de séries temporais:
  - **Naive e Seasonal Naive**: Modelos base para comparação
  - **ARIMA e Auto ARIMA**: Modelos autorregressivos integrados de média móvel
  - **SARIMA**: ARIMA com componentes sazonais (semanal, mensal e anual)
  - **Prophet**: Modelo do Facebook com suporte a sazonalidade e eventos especiais
- Tratamento de feriados brasileiros que afetam a bolsa
- Consideração do impacto da COVID-19 (março/2020 a junho/2021)
- Métricas de avaliação: WMAPE, MAPE, MAE, MSE
- Previsão de até 90 dias futuros
- Otimização de hiperparâmetros via Grid Search

### Scripts AWS
- Listagem de buckets S3
- Criação de instâncias EC2

## Stack Tecnológica

- **Python 3**
- **Pandas** - Manipulação e análise de dados
- **NumPy** - Computação numérica
- **Matplotlib** - Visualização de dados
- **Seaborn** - Visualização estatística
- **Scikit-learn** - Métricas de avaliação
- **Statsmodels** - Modelagem estatística e séries temporais
- **Statsforecast** - Modelos de previsão (Naive, AutoARIMA, ARIMA)
- **Prophet** - Modelo de previsão do Facebook
- **Boto3** - SDK AWS para Python
- **Google Colab** - Ambiente de execução dos notebooks

## Como Instalar e Executar

### Pré-requisitos
- Python 3.x instalado
- Pip para gerenciamento de pacotes
- Conta AWS configurada (para scripts AWS)

### Instalação das dependências

```bash
pip install pandas numpy matplotlib seaborn scikit-learn statsmodels statsforecast prophet boto3
```

### Executando os Notebooks

Os notebooks Jupyter podem ser executados diretamente no Google Colab:

1. **Tech_Challenge_Python.ipynb**: Análise de exportação de vinhos
   - Requer o arquivo `ExpVinho.csv` no mesmo diretório

2. **Tech_Challenge_Fase_2_Grupo_7.ipynb**: Previsão do IBOVESPA
   - Requer o arquivo `dados_historicos_Ibovespa_2015_a_2025.csv`

### Executando os Scripts AWS

**Listagem de buckets S3:**
```bash
python list-bucket.py
```

**Criação de instância EC2:**
```bash
./cria-instancia.sh
```

## Estrutura de Pastas

```
/
├── README.md                              # Este arquivo
├── Tech_Challenge_Python.ipynb            # Notebook de análise de exportação de vinhos
├── Tech_Challenge_Fase_2_Grupo_7.ipynb    # Notebook de previsão do IBOVESPA
├── list-bucket.py                         # Script para listar buckets S3
└── cria-instancia.sh                      # Script para criar instância EC2
```

## Variáveis de Ambiente Necessárias

Para os scripts AWS, as seguintes credenciais devem estar configuradas:

- `AWS_ACCESS_KEY_ID`
- `AWS_SECRET_ACCESS_KEY`
- `AWS_DEFAULT_REGION`

Alternativamente, configure as credenciais via AWS CLI:
```bash
aws configure
```

## Arquivos de Dados Necessários

- `ExpVinho.csv` - Dados históricos de exportação de vinhos brasileiros
- `dados_historicos_Ibovespa_2015_a_2025.csv` - Série histórica do IBOVESPA (2015-2025)
