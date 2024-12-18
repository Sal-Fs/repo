import logging
from us_airline_sentiment import *

logging.basicConfig(level=logging.INFO, filename="logs.log", filemode="w", 
                    format="%(asctime)s; Line:%(lineno)s; %(levelname)s: %(message)s",
                    datefmt="%d-%b-%Y %H:%M")

def main():
    try:
        while True:
            # Menu de opções para o usuário
            print("Escolha uma das opções abaixo:")
            print("1. Listar todas as companhias aéreas")
            print("2. Identificar a companhia com mais tweets negativos")
            print("3. Calcular o número total de tweets por companhia")
            print("4. Filtrar tweets por companhia")
            print("5. Identificar o dia com mais tweets")
            print("6. Contar número de tweets por mês ou ano")
            print("7. Sair")

            opcao = input("Digite o número da opção: ")

            if opcao == "1":
                listar_companhias(tweets_dict)
            elif opcao == "2":
                companhia_com_mais_tweets_negativos(tweets_dict)
            elif opcao == "3":
                total_tweets_por_companhia(tweets_dict)
            elif opcao == "4":
                tweets_especificos_por_companhia(tweets_dict)
            elif opcao == "5":
                dia_com_mais_tweets(tweets_dict)
            elif opcao == "6":
                contar_numero_tweets(tweets_dict)
            elif opcao == "7":
                print("Programa fechado")
                break
            else:
                print("Opção inválida. Tente novamente.")

    except Exception as e:
        logging.error(f"Erro inesperado: {e}")

if __name__ == "__main__":
    main()
