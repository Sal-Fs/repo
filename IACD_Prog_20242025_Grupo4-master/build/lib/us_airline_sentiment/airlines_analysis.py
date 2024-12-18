import logging

logging.basicConfig(level=logging.INFO, filename="logs.log", filemode="w", 
                    format="%(asctime)s; Line:%(lineno)s; %(levelname)s: %(message)s",
                    datefmt="%d-%b-%Y %H:%M")

#Listar todas as companhias aéreas mencionadas no dataset

def listar_companhias(tweets_dict):
    logging.info("A compilar lista de companhias no dataset.")
    try:
        companhias = set()  # Usar um conjunto para evitar duplicatas

        for tweet in tweets_dict:
            companhia = tweet.get("airline", "")
            if companhia:
                companhias.add(companhia)

        logging.info(f"Companhias encontradas: {companhias}")
        return list(companhias)

    except Exception as e:
        logging.error(f"Erro ao listar companhias: {e}")
        return []

#Identificar a companhia com mais tweets negativos

def companhia_com_mais_tweets_negativos(tweets_dict):
    logging.info("A apurar companhia com mais tweets negativos.")
    try:
        sentimentos_por_companhia = {}

        for tweet in tweets_dict:
            companhia = tweet.get("airline", "")
            sentimento = tweet.get("airline_sentiment", "")

            if companhia and sentimento == "negative":
                sentimentos_por_companhia[companhia] = sentimentos_por_companhia.get(companhia, 0) + 1

        if sentimentos_por_companhia:
            companhia_negativa = max(sentimentos_por_companhia, key=sentimentos_por_companhia.get)
            max_negativos = sentimentos_por_companhia[companhia_negativa]
            logging.info(f"Companhia com mais tweets negativos: {companhia_negativa} com {max_negativos} tweets negativos")
            return companhia_negativa, max_negativos
        else:
            logging.warning("Nenhuma companhia com tweets negativos encontrada.")
            return None, 0

    except Exception as e:
        logging.error(f"Erro ao identificar companhia com mais tweets negativos: {e}")
        return None, 0

#Calcular o número total de tweets por companhia

def total_tweets_por_companhia(tweets_dict):
    logging.info("A calcular tweets por companhia.")
    try:
        total_companhia = {}

        for tweet in tweets_dict:
            companhia = tweet.get("airline", "")
            if companhia:
                total_companhia[companhia] = total_companhia.get(companhia, 0) + 1

        logging.info(f"Total de tweets por companhia: {total_companhia}")
        return total_companhia

    except Exception as e:
        logging.error(f"Erro ao calcular o total de tweets por companhia: {e}")
        return {}


#Filtrar os tweets de uma companhia específica e mostrar seus detalhes

def tweets_especificos_por_companhia(tweets_dict):
    try:
        comp = input("Digite a companhia que deseja ter informações: ").strip()
        dict_da_companhia = []

        logging.info(f"A pesquisar tweets da companhia {comp}.")
        for tweet in tweets_dict:
            if tweet.get("airline", "").lower() == comp.lower():
                dict_da_companhia.append(tweet)

        if dict_da_companhia:
            logging.info(f"Tweets encontrados para a companhia {comp}: {len(dict_da_companhia)}")
        else:
            logging.warning(f"Nenhum tweet encontrado para a companhia {comp}.")

        return dict_da_companhia

    except Exception as e:
        logging.error(f"Erro ao filtrar tweets por companhia: {e}")
        return []
