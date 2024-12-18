import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

def process_sentiments(df):
    # Filtrar as colunas relevantes
    relevant_columns = df[['airline', 'airline_sentiment']]
    
    # Contar sentimentos por companhia aérea
    sentiment_counts = relevant_columns.groupby(['airline', 'airline_sentiment']).size().unstack(fill_value=0)
    
    return sentiment_counts

def plot_sentiments(sentiment_counts):
    # Configurar os dados para o gráfico
    airlines = sentiment_counts.index
    sentiments = sentiment_counts.columns
    x = np.arange(len(airlines))  # Localização das companhias no eixo x
    width = 0.25  # Largura das barras
    
    # Criar as barras
    fig, ax = plt.subplots(figsize=(12, 6))
    colors = ['#d62d20', '#0057e7', '#008744']  # Cores para sentimentos (positivo, negativo, neutro)
    
    for i, sentiment in enumerate(sentiments):
        ax.bar(x + i * width, sentiment_counts[sentiment], width, label=sentiment.capitalize(), color=colors[i])
    
    # Adicionar detalhes ao gráfico
    ax.set_xlabel('Companhias Aéreas', fontsize=12)
    ax.set_ylabel('Número de Tweets', fontsize=12)
    ax.set_title('Distribuição de Sentimentos por Companhia Aérea', fontsize=14)
    ax.set_xticks(x + width)
    ax.set_xticklabels(airlines, rotation=45, ha='right', fontsize=10)
    ax.legend(title="Sentimentos")
    
    # Exibir o gráfico
    plt.tight_layout()
    plt.show()

# Carregar o dataframe a partir do arquivo CSV
tweets_df = pd.read_csv("Tweets.csv")  # Altere para o caminho correto
sentiment_counts = process_sentiments(tweets_df)
