import os
import pandas as pd
import requests #biblioteca para chamar as infos da web
from dotenv import load_dotenv

print("--- ETAPA 1: ACESSANDO A API ---")
load_dotenv() # Carrega os arquivos do .env

chave_api = os.getenv("RIOT_API_KEY") # Chama a chave_do_api do .env


#  ***!!!***  Local para alterar o nome e a tag do usuário
nickname = "pedrobatista"
tag = "777"
#  ***!!!***


# URL corrigida para puxar as variáveis e não expor a chave
url_puuid = f"https://americas.api.riotgames.com/riot/account/v1/accounts/by-riot-id/{nickname}/{tag}"

# Mostra o 'crachá' de entrada pra API
senha_entrada = { 
    "X-Riot-Token": chave_api
}
# Pega o url_PUUID usando o crachá para API
resposta = requests.get(url_puuid, headers=senha_entrada)

dados = resposta.json() # Traduz a resposta de json para um dict em python
print(dados)

#--------------------------------------------------------------

print("--- ETAPA 2: BUSCANDO OS IDs DAS PARTIDAS ---")

meu_puuid = dados["puuid"] # Puxando só o PUUID das respostas anteriores

# 'matches' = histórico | 'ids' = pegar apenas os IDs das partidas | '?count=100' = pegar os últimos x games | Da pra mudar o número pra pegar mais partidas do histórico
url_partidas = f"https://americas.api.riotgames.com/tft/match/v1/matches/by-puuid/{meu_puuid}/ids?count=100"

# Guarda os IDs das últimas x partidas jogadas, nesse caso
resposta_partidas = requests.get(url_partidas, headers=senha_entrada)

# Tradução json --> python
lista_partidas = resposta_partidas.json()

# len = lenght ou comprimento
print(f"Minhas últimas {len(lista_partidas)} partidas no TFT foram:")
print(lista_partidas)

#--------------------------------------------------------------

print(f"\n--- ETAPA 3: PEGANDO AS INFOs DAS {len(lista_partidas)} PARTIDAS ---")

# Inserindo uma tabela em branco
dados_tabela = []

meta_de_partidas = 30
partidas_salvas = 0

# Procura em cada partida da lista de IDs
for partida_id in lista_partidas:
    
    if partidas_salvas == meta_de_partidas:
        # Checa se o número de partidas foi hitado
        break

        # 1. Busca os dados de uma partida específica, usando o ID dela
    url = f"https://americas.api.riotgames.com/tft/match/v1/matches/{partida_id}"
    resposta = requests.get(url, headers=senha_entrada)
    dados = resposta.json()
    
    tipo_partida = dados["info"]["queue_id"]

    # Se não for duplas, pula pra próxima partida ----> | 1100 == Ranked | 1160 == Duplas |
    if tipo_partida != 1160:
        continue

    # 2. Chama a lista dos 8 jogadores
    jogadores = dados["info"]["participants"]
    
    # 3. Procura nos jogadores o PUUID == meu_PUUID e caso igual puxa as infos da partida específica
    for jogador in jogadores:
          if jogador["puuid"] == meu_puuid:
            colocacao = jogador["placement"]
            dano = jogador["total_damage_to_players"]
            
            # Cria a "linha" na planilha com os dados
            linha = {
                "ID_Partida": partida_id,
                "Colocação": colocacao,
                "Dano_Causado": dano
            }
            
            # Inserimos a linha na nossa tabela em branco
            dados_tabela.append(linha)

            partidas_salvas+= 1
            
            # 4. Mostra o Resultado e termina a busca nessa partida
            print(f"Partida {partida_id} | Fiquei em {colocacao}º lugar (Dano causado: {dano})")
            break

#--------------------------------------------------------------

print("\n--- ETAPA 4: GERANDO O ARQUIVO EXCEL(CSV) ---")

# Transforma a lista de python em pandas
tabela_final = pd.DataFrame(dados_tabela)

media_colocacao = tabela_final["Colocação"].mean()
media_dano_causado = tabela_final["Dano_Causado"].mean()


# len(tabela_final) serve para descobrir o número da última linha vazia
tabela_final.loc[len(tabela_final)] = {
    #Cria a linha de Média no arquivo .csv
    "ID_Partida": "MÉDIA TOTAL", 
    "Colocação": round(media_colocacao, 1), # round() arredonda para 2 casas decimais
    "Dano_Causado": round(media_dano_causado, 0) # Arredonda sem casas decimais
}

# Exporta a tabela para um arquivo .csv na mesma pasta do seu projeto | "Index" retira a numeração automática que o pandas faz na planilha | "sep" muda o separador pra ";"
tabela_final.to_csv("meu_historico_tft.csv", index=False, sep=";", encoding ="utf-8-sig", decimal =',')
print("O arquivo 'meu_historico_tft.csv' foi gerado.")