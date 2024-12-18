import logging

logging.basicConfig(level=logging.INFO, filename="logs.log", filemode="w", 
                    format="%(asctime)s; Line:%(lineno)s; %(levelname)s: %(message)s",
                    datefmt="%d-%b-%Y %H:%M")

#Contar o n~umero de tweets por sentimento

def numero_de_tweets_por_sentimento(tweets_dict):
    logging.info("A contar tweets por sentimento.")
    try:
        # Inicializar contadores
        tweets_negativos = 0
        tweets_neutros = 0
        tweets_positivos = 0
    
        # Iterar sobre os tweets
        for tweet in tweets_dict:
            sentimento = tweet.get("airline_sentiment", "").lower()
            if sentimento == "negative":
                tweets_negativos += 1
            elif sentimento == "neutral":
                tweets_neutros += 1
            elif sentimento == "positive":
                tweets_positivos += 1
            else:
                logging.warning(f"Sentimento desconhecido no tweet: {tweet}")

        # Exibir resultados
        logging.info(f"Contagem concluída: Negativos={tweets_negativos}, Neutros={tweets_neutros}, Positivos={tweets_positivos}")
        print(f"Número de tweets negativos: {tweets_negativos}")
        print(f"Número de tweets neutros: {tweets_neutros}")
        print(f"Número de tweets positivos: {tweets_positivos}")

        # Retornar os resultados como um dicionário
        return {
            "negativos": tweets_negativos,
            "neutros": tweets_neutros,
            "positivos": tweets_positivos,
        }
    
    except Exception as e:
        logging.error(f"Erro ao contar tweets: {e}")
        return {
            "negativos": 0,
            "neutros": 0,
            "positivos": 0,
        }

        
#Calcular percentagem de cada tipo de sentimento por companhia áerea

def sentimento_por_companhia_percentagem(tweets_dict):
    logging.info("A calcular porcentagem de tweets por companhia.")
    try:
        # Inicializar estruturas para armazenar os dados
        total_por_companhia = {}
        sentimentos_por_companhia = {}
    
        # Processar os tweets
        for tweet in tweets_dict:
            companhia = tweet.get("airline", "")
            sentimento = tweet.get("airline_sentiment", "")

            if not companhia or not sentimento:  # Ignorar tweets inválidos
                logging.warning(f"Tweet ignorado (linha inválida): {tweet}")
                continue

            # Inicializar contadores para a companhia, se necessário
            if companhia not in total_por_companhia:
                total_por_companhia[companhia] = 0
                sentimentos_por_companhia[companhia] = {'negative': 0, 'neutral': 0, 'positive': 0}

            # Incrementar contadores
            total_por_companhia[companhia] += 1
            if sentimento in sentimentos_por_companhia[companhia]:
                sentimentos_por_companhia[companhia][sentimento] += 1

        # Calcular e exibir porcentagens
        resultado_percentagens = {}
        for companhia in total_por_companhia:
            total = total_por_companhia[companhia]
            sentimentos = sentimentos_por_companhia[companhia]

            percent_negativo = (sentimentos['negative'] / total) * 100
            percent_neutro = (sentimentos['neutral'] / total) * 100
            percent_positivo = (sentimentos['positive'] / total) * 100

            resultado_percentagens[companhia] = {
                "negative": percent_negativo,
                "neutral": percent_neutro,
                "positive": percent_positivo,
            }

            logging.info(
                f"Companhia {companhia}: Negativos={percent_negativo:.2f}%, "
                f"Neutros={percent_neutro:.2f}%, Positivos={percent_positivo:.2f}%"
            )
            print(f"Sentimentos da companhia {companhia}:")
            print(f" - Negativos: {percent_negativo:.2f}%")
            print(f" - Neutros: {percent_neutro:.2f}%")
            print(f" - Positivos: {percent_positivo:.2f}%")

        return resultado_percentagens

    except Exception as e:
        logging.error(f"Erro ao calcular porcentagem de tweets por companhia: {e}")
        return {}

        
# Identificar a companhia aérea com o maior número de tweets positivos

def companhia_com_maior_numero_positivo(tweets_dict):
    logging.info("A calcular companhia com maior número de tweets positivos.")
    try:
        # Inicializar dicionário para armazenar os sentimentos por companhia
        sentimentos_por_companhia = {}

        # Processar os tweets
        for tweet in tweets_dict:
            companhia = tweet.get("airline", "")
            sentimento = tweet.get("airline_sentiment", "")

            if not companhia or not sentimento:
                logging.warning(f"Tweet ignorado (linha inválida): {tweet}")
                continue

            # Inicializar contadores para a companhia, se necessário
            if companhia not in sentimentos_por_companhia:
                sentimentos_por_companhia[companhia] = {"negative": 0, "neutral": 0, "positive": 0}

            # Incrementar o sentimento positivo
            if sentimento == "positive":
                sentimentos_por_companhia[companhia]["positive"] += 1

        # Encontrar a companhia com o maior número de tweets positivos
        companhia_positiva = max(
            sentimentos_por_companhia.items(),
            key=lambda item: item[1]["positive"],
        )

        logging.info(
            f"Companhia com maior número de tweets positivos: {companhia_positiva[0]} "
            f"com {companhia_positiva[1]['positive']} tweets positivos."
        )
        return companhia_positiva[0]

    except Exception as e:
        logging.error(f"Erro ao identificar companhia com maior número de tweets positivos: {e}")
        return None


#Analisar o número médio de retweets por tipo de sentimento.

def media_retweets_sentimento(tweets_dict):
    logging.info("A calcular média de retweets por tipo de sentimento.")
    try:
        # Dicionário para armazenar retweets por tipo de sentimento
        retweets_sentimento = {"positive": [], "negative": [], "neutral": []}

        # Iterar pelos tweets e organizar os retweets por tipo de sentimento
        for tweet in tweets_dict:
            sentimento = tweet.get("airline_sentiment", "").lower()
            retweets = tweet.get("retweet_count", 0)

            if sentimento in retweets_sentimento:
                retweets_sentimento[sentimento].append(retweets)

        # Calcular a média de retweets para cada sentimento
        average_retweets = {
            sentimento: (sum(retweets) / len(retweets) if retweets else 0)
            for sentimento, retweets in retweets_sentimento.items()
        }

        logging.info(f"Média de retweets por sentimento: {average_retweets}")
        return average_retweets

    except Exception as e:
        logging.error(f"Erro ao calcular média de retweets por sentimento: {e}")
        return {}
