# Previsão de Consumo de Energia Fotovoltaica com Métodos de Séries Temporais

## 📋 Sobre o Projeto

Este projeto de pesquisa (TCC/IC) investiga e compara diferentes métodos de previsão de séries temporais aplicados ao consumo de energia de instalações fotovoltaicas. O objetivo é identificar qual abordagem oferece melhor acurácia para prever o consumo mensal de energia em 5 instalações solares.

### Motivação

Com o crescimento da geração distribuída de energia solar, torna-se essencial desenvolver modelos precisos de previsão de consumo para:
- Planejamento energético eficiente
- Otimização de custos operacionais
- Melhoria na gestão de contratos de fornecimento
- Suporte à tomada de decisão em investimentos

## 🎯 Objetivos

1. **Comparar modelos estatísticos clássicos** (SARIMA) com **modelos modernos** (Prophet)
2. **Avaliar métodos ensemble** que combinam diferentes abordagens
3. **Identificar o melhor método** para cada instalação analisada
4. **Gerar resultados reproduzíveis** para publicação acadêmica

## 📊 Dataset

### Dados Analisados
- **Período**: Junho/2019 a Dezembro/2024
- **Frequência**: Mensal
- **Instalações**: 5 unidades consumidoras (UC)
- **Variável**: Consumo de energia (kWh)

### Instalações Estudadas
| ID (UC)      | Nome           | Características                    |
|-------------|----------------|------------------------------------|
| 3001084033  | Instalação 1   | Consumo alto e estável            |
| 3001449459  | Instalação 2   | Consumo médio com variações       |
| 3003858507  | Instalação 3   | Consumo variável                  |
| 3011373971  | Instalação 4   | Consumo baixo com zeros (~9%)     |
| 3011504476  | Instalação 5   | Consumo médio-alto                |

## 🔬 Metodologia

### 1. Modelos Implementados

#### SARIMA (Seasonal ARIMA)
- **Descrição**: Modelo estatístico clássico para séries temporais com sazonalidade
- **Parâmetros testados**:
  - p, d, q ∈ [0, 10] × [0, 1] × [0, 10]
  - P, D, Q ∈ [0, 10] × [0, 1] × [0, 10]
  - s = 12 (sazonalidade mensal)
- **Total de combinações**: 58.564 por instalação
- **Localização**: `SARIMA/SARIMA_[UC].ipynb`

#### Prophet (Facebook Prophet)
- **Descrição**: Modelo moderno baseado em decomposição aditiva de tendências e sazonalidades
- **Parâmetros testados**:
  - yearly_seasonality ∈ [0, 12]
  - growth = 'flat'
- **Localização**: `Prophet/prophet.ipynb`

#### Métodos Ensemble
Combinam SARIMA e Prophet usando diferentes estratégias:

1. **Simple Voting**: Média simples das previsões
2. **Weighted Voting**: Média ponderada por desempenho (RMSE inverso)
3. **Bagging**: Bootstrap aggregating com regressão Ridge
4. **Random Forest**: Árvores de decisão com features de séries temporais

**Localização**: `Ensemble/Ensemble.ipynb`

### 2. Pipeline de Processamento

```
Dados Brutos (Excel + CSV)
    ↓
Preprocessamento
    ↓ - Combinação de fontes
    ↓ - Resolução de duplicatas
    ↓ - Reamostragem mensal
    ↓
Divisão Treino/Teste (índice 23)
    ↓
Grid Search (SARIMA e Prophet)
    ↓
Seleção de Melhores Modelos (baseado em RMSE)
    ↓
Ensemble Methods
    ↓
Análise Comparativa
    ↓
Resultados Finais + Visualizações
```

### 3. Métricas de Avaliação

| Métrica | Descrição | Observações |
|---------|-----------|-------------|
| **RMSE** | Raiz do Erro Quadrático Médio | **Métrica principal** - robusta para valores zero |
| **MAE** | Erro Absoluto Médio | Interpretação direta em kWh |
| **MAPE** | Erro Percentual Absoluto Médio | Problemático com consumos zero |
| **WMAPE** | MAPE Ponderado | MAPE com pesos por amostra |

**⚠️ Importante**: MAPE pode ser infinito quando há consumos zero. Por isso, **RMSE é a métrica primária** para seleção de modelos.

## 🚀 Como Executar

### Pré-requisitos

```bash
pip install pandas numpy matplotlib statsmodels prophet scikit-learn openpyxl
```

### Workflow Completo

#### 1. Grid Search SARIMA (por instalação)
```python
# Abrir SARIMA/SARIMA_[UC].ipynb
# Definir INSTALLATION_ID no topo do notebook
# Executar todas as células
# Saída: sarima_results_[UC].csv
```

**Nota**: O grid search é resumível - pode ser interrompido e continuará de onde parou.

#### 2. Grid Search Prophet (todas as instalações)
```python
# Abrir Prophet/prophet.ipynb
# Executar todas as células
# Saída: prophet_results_[UC].csv para cada instalação
```

#### 3. Análise Ensemble
```python
# Abrir Ensemble/Ensemble.ipynb
# Executar todas as células
# Saída: ensemble_results.csv + gráficos PNG
```

#### 4. Análise Final e Exportação
```python
# Abrir Analise/analise.ipynb
# Executar todas as células
# Saída: Múltiplos CSVs para tabelas LaTeX
```

## 📈 Resultados

### Estrutura de Saída

#### Arquivos CSV Gerados
- `sarima_results_[UC].csv`: Resultados completos do grid search SARIMA
- `prophet_results_[UC].csv`: Resultados completos do grid search Prophet
- `ensemble_results.csv`: Resultados de todos os métodos ensemble
- `best_sarima_results.csv`: Melhores parâmetros SARIMA por instalação
- `best_prophet_results.csv`: Melhores parâmetros Prophet por instalação
- `best_ensemble_results.csv`: Melhor método ensemble por instalação
- `model_comparison.csv`: Comparação lado a lado de todos os modelos
- `latex_*.csv`: Tabelas formatadas para LaTeX

#### Visualizações Geradas
- `dados_consumo_originais.png`: Série temporal original de todas as instalações
- `comparacao_todas_instalacoes_ensemble.png`: Comparação abrangente de métodos
- `visao_geral_metodos_ensemble.png`: Performance média por método
- `mape_melhores_modelos_por_instalacao.png`: MAPE dos melhores modelos
- `todas_metricas_melhores_modelos.png`: Comparação multi-métrica
- `comparacao_ensemble_instalação_[1-5].png`: Comparações individuais

### Interpretação dos Resultados

**Exemplo de saída típica**:
```
Installation: 3001084033
Best SARIMA: (9,1,9)x(1,0,1,12) - RMSE: 656.87
Best Prophet: yearly_seasonality=12 - RMSE: 929.10
Best Ensemble: Weighted_Voting - RMSE: 580.39
→ Ensemble melhora 11.6% em relação ao melhor modelo individual
```

## 📁 Estrutura do Repositório

```
IC-Gasto-Fotovoltaico/
│
├── SARIMA/                    # Grid search SARIMA por instalação
│   ├── SARIMA_3001084033.ipynb
│   ├── SARIMA_3001449459.ipynb
│   ├── SARIMA_3003858507.ipynb
│   ├── SARIMA_3011373971.ipynb
│   └── SARIMA_3011504476.ipynb
│
├── Prophet/                   # Grid search Prophet
│   └── prophet.ipynb
│
├── Ensemble/                  # Métodos ensemble
│   ├── Ensemble.ipynb         # Implementação principal
│   └── tutorial.ipynb         # Tutorial explicativo
│
├── Analise/                   # Análise de resultados
│   └── analise.ipynb          # Extração e comparação
│
├── Augmentation/              # [Experimental] Técnicas de aumento de dados
├── Interpolation/             # [Experimental] Métodos de interpolação
├── Normalization/             # [Experimental] Normalização
├── Normal/                    # Versões baseline dos modelos
├── Model-Saving/              # Utilidades de persistência
│
└── README.md                  # Este arquivo
```

## 🔧 Detalhes Técnicos

### Preprocessamento de Dados

1. **Combinação de fontes**: Excel (histórico 2019-2023) + CSV (forecast 2023-2025)
2. **Tratamento de duplicatas**: Prioriza dados CSV sobre Excel para datas sobrepostas
3. **Reamostragem**: Converte dados irregulares para frequência mensal (MS - Month Start)
4. **Filtro temporal**: Remove dados após 2025-01-01

### Divisão Treino/Teste

- **Ponto de corte**: Índice 23 do dataset (consistente em todos os modelos)
- **Treino**: Primeiros 23 meses
- **Teste**: Restante da série (`half = data.iloc[23:]`)

### Features para Ensemble

Os métodos ensemble (Bagging, Random Forest) utilizam:
- **Lags**: 1-12 meses
- **Estatísticas móveis**: janelas de 3, 6, 12 meses
- **Features temporais**: mês, trimestre, ano, índice temporal
- **Diferenças sazonais**: 1 mês e 12 meses
- **Previsões base**: SARIMA e Prophet como features

### Tratamento de Valores Zero

Algumas instalações têm períodos com consumo zero, o que afeta:
- **MAPE**: Pode resultar em divisão por zero → infinito
- **Prophet**: Requer valores positivos → remove zeros antes do fit

**Solução**: RMSE como métrica principal + preprocessamento específico para Prophet

## 📊 Insights da Pesquisa

### Descobertas Principais

1. **Ensemble supera modelos individuais**: Em 60% das instalações, métodos ensemble apresentaram melhor performance
2. **RMSE vs MAPE**: Instalações com consumos zero invalidam MAPE como métrica confiável
3. **Weighted Voting é robusto**: Combina simplicidade com bom desempenho
4. **Random Forest captura não-linearidades**: Melhor para instalações com padrões complexos

### Recomendações por Perfil

| Perfil da Instalação | Método Recomendado | Justificativa |
|---------------------|-------------------|---------------|
| Consumo estável e alto | SARIMA | Padrões lineares bem definidos |
| Consumo variável | Random Forest | Captura variações não-lineares |
| Consumo com zeros | Weighted Voting | Robusto a valores extremos |
| Dados limitados | Simple Voting | Simples e generaliza bem |

## 🤝 Contribuindo

Este é um projeto de pesquisa acadêmica. Sugestões e melhorias são bem-vindas:

1. Fork o repositório
2. Crie uma branch para sua feature (`git checkout -b feature/NovaAnalise`)
3. Commit suas mudanças (`git commit -m 'Adiciona nova análise X'`)
4. Push para a branch (`git push origin feature/NovaAnalise`)
5. Abra um Pull Request

## 📝 Licença

Este projeto é desenvolvido para fins acadêmicos e de pesquisa.

## 👥 Autores

Projeto desenvolvido como parte do Trabalho de Conclusão de Curso (TCC) / Iniciação Científica (IC).

## 📚 Referências

- Box, G. E. P., & Jenkins, G. M. (1976). Time Series Analysis: Forecasting and Control
- Taylor, S. J., & Letham, B. (2018). Forecasting at Scale. The American Statistician
- Hyndman, R. J., & Athanasopoulos, G. (2021). Forecasting: Principles and Practice

## 🔍 Trabalhos Futuros

- [ ] Incorporar variáveis exógenas (temperatura, irradiância solar)
- [ ] Testar modelos de deep learning (LSTM, Transformer)
- [ ] Expandir análise para mais instalações
- [ ] Implementar previsão em tempo real
- [ ] Desenvolver dashboard interativo para visualização

---

**Última atualização**: Dezembro 2024
