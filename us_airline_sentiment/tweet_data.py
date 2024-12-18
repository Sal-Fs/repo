import csv
import logging

logging.basicConfig(level=logging.INFO, filename="logs.log", filemode="w", 
                    format="%(asctime)s; Line:%(lineno)s; %(levelname)s: %(message)s",
                    datefmt="%d-%b-%Y %H:%M")

def load_data(filepath):
    data = []  # Lista para armazenar os tweets como dicionários

    try:
        logging.info("Iniciando a leitura do arquivo: %s", filepath)
        assert filepath.strip() != "", "O filepath não pode ser uma string vazia."
        
        with open(filepath, mode="r", encoding="utf-8") as csvfile:
            reader = csv.DictReader(csvfile)  # Lê o CSV como uma lista de dicionários
           
          # Verificar se o arquivo contém cabeçalhos esperados
            assert set(reader.fieldnames) >= {
                "tweet_id",
                "airline_sentiment",
                "airline",
                "tweet_created",
                "retweet_count",
                "text"
            }, f"Os cabeçalhos do arquivo CSV não estão corretos. Esperados: tweet_id, airline_sentiment, airline, tweet_created, retweet_count, text. Obtido: {reader.fieldnames}"
          
          # Itera sobre as linhas do arquivo
            for row in reader:
                try:

                    # Garantir que todos os valores necessários estejam presentes antes de converter
                    assert "tweet_id" in row, "Campo 'tweet_id' está ausente na linha."
                    assert "airline_sentiment" in row, "Campo 'airline_sentiment' está ausente na linha."
                    assert "airline" in row, "Campo 'airline' está ausente na linha."
                    assert "tweet_created" in row, "Campo 'tweet_created' está ausente na linha."
                    assert "retweet_count" in row, "Campo 'retweet_count' está ausente na linha."
                    assert "text" in row, "Campo 'text' está ausente na linha."

                    # Cria o dicionário
                    tweets_dict = {
                        "tweet_id": int(row["tweet_id"]),
                        "airline_sentiment": row["airline_sentiment"],
                        "airline": row["airline"],
                        "tweet_created": row["tweet_created"],
                        "retweet_count": int(row["retweet_count"]),
                        "text": row["text"],
                    }
                    data.append(tweets_dict)
                except ValueError as e:
                    # Trata erros de conversão
                    logging.error("Erro ao processar linha: %s - Erro: %s", row, e)

        logging.info("Leitura do arquivo concluída com sucesso: %s", filepath)
    
    except FileNotFoundError as e:
        logging.error("Arquivo não encontrado: %s - Erro: %s", filepath, e)
        pass
    
    except Exception as e:
        logging.error("Erro inesperado ao ler o arquivo: %s - Erro: %s", filepath, e)
        pass
      
    # Garantir que a lista de dados não está vazia
    assert data, "Nenhum dado foi carregado do arquivo. Verifique o conteúdo do CSV."
    
    return data
