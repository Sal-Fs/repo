import logging

logging.basicConfig(level=logging.INFO, filename="logs.log", filemode="w", 
                    format="%(asctime)s; Line:%(lineno)s; %(levelname)s: %(message)s",
                    datefmt="%d-%b-%Y %H:%M")

#Identificar o dia com mais tweets

def dia_com_mais_tweets(tweets_dict):
    logging.info("A calcular o dia com mais tweets.")
    try:
        dias = {}

        # Itera pelos tweets e conta os tweets por dia
        for tweet in tweets_dict:
            dia = tweet.get("tweet_created", "").split()[0]

            if not dia:
                logging.warning(f"Tweet ignorado por não ter data válida: {tweet}")
                continue

            if dia not in dias:
                dias[dia] = 1
            else:
                dias[dia] += 1

        # Identifica o dia com mais tweets
        maior_valor = max(dias.values())
        dia_mais_tweets = [dia for dia, count in dias.items() if count == maior_valor][0]

        logging.info(f"O dia com mais tweets foi {dia_mais_tweets} com {maior_valor} tweets.")
        return dia_mais_tweets, maior_valor

    except Exception as e:
        logging.error(f"Erro ao identificar o dia com mais tweets: {e}")
        return None, 0


#Contar quantos tweets foram feitos num determinado mês ou ano

def contar_numero_tweets(tweets_dict):
    try:
        # Solicitar ao usuário se deseja contar por mês ou ano
        dado1 = input('Digite se deseja contar os tweets de um ano ou um mês: ').strip().lower()

        if dado1 == 'mês':
            dado2 = input('Digite o mês (formato MM) que deseja saber quantos tweets existiram: ').strip()

            logging.info(f'A calcular os tweets no mês de {dado2}.')
            contagem_mes = 0

            # Itera sobre os tweets e conta os que pertencem ao mês especificado
            for tweet in tweets_dict:
                try:
                    dia = tweet['tweet_created'].split()[0].split('-')[1]
                    if dia == dado2:
                        contagem_mes += 1
                except KeyError:
                    logging.warning(f"Tweet sem data válida: {tweet}")
                    continue

            logging.info(f'No mês {dado2} houveram {contagem_mes} tweets.')
            print(f'No mês {dado2} houveram {contagem_mes} tweets.')

        elif dado1 == 'ano':
            dado3 = input('Digite o ano (formato YYYY) que deseja saber quantos tweets existiram: ').strip()

            logging.info(f'A calcular os tweets no ano de {dado3}.')
            contagem_ano = 0

            # Itera sobre os tweets e conta os que pertencem ao ano especificado
            for tweet in tweets_dict:
                try:
                    ano = tweet['tweet_created'].split()[0].split('-')[0]
                    if ano == dado3:
                        contagem_ano += 1
                except KeyError:
                    logging.warning(f"Tweet sem data válida: {tweet}")
                    continue

            logging.info(f'No ano {dado3} houveram {contagem_ano} tweets.')
            print(f'No ano {dado3} houveram {contagem_ano} tweets.')

        else:
            logging.warning("Entrada inválida. Digite 'mês' ou 'ano'.")
            print("Opção inválida. Por favor, escolha 'mês' ou 'ano'.")

    except Exception as e:
        logging.error(f"Erro ao contar número de tweets: {e}")
        print("Erro ao processar a solicitação.")

