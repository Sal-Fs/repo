import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def process_tweets_by_hour(df):
    # Converter datas para o formato apropriado
    df['tweet_created'] = pd.to_datetime(df['tweet_created'], errors='coerce')
    
    # Retirar a data e hora do tweet
    df['hour'] = df['tweet_created'].dt.hour
    
    # Contagem dos tweets realizados em determinada hora
    hourly_tweet_counts = df.groupby(['hour']).size()
    
    # Garantir que todas as horas sejam representadas, mesmo as sem tweets
    hourly_tweet_counts = hourly_tweet_counts.reindex(range(24), fill_value=0)
    
    return hourly_tweet_counts

def plot_heatmap(hourly_counts):
    # Reestruturar os dados para o formato necessário para o heatmap
    data = hourly_counts.values.reshape(1, -1)  # 1 linha, 24 colunas (horas)
    hours = list(range(24))  # 24 horas
    
    # Usar o seaborn para criar o heatmap
    plt.figure(figsize=(12, 4))
    sns.heatmap(data, annot=True, fmt="d", cmap="coolwarm", cbar=True, xticklabels=hours, yticklabels=["Tweets"])
    
    plt.title("Número de Tweets por Hora", fontsize=14)
    plt.xlabel("Hora do Dia", fontsize=12)
    plt.ylabel("", fontsize=12)
    plt.tight_layout()
    plt.show()

# Carregar o dataframe a partir do arquivo CSV
tweets_df = pd.read_csv("Tweets.csv")
# Processar e contar os tweets por hora
hourly_tweet_counts = process_tweets_by_hour(tweets_df)
