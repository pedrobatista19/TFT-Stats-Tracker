# ♟️ TFT STATS TRACKER

Um script em Python desenvolvido para consumir a API oficial da Riot Games, analisar o histórico de partidas de Teamfight Tactics (TFT) de um jogador e exportar um relatório detalhado no formato `.csv`.

Atualmente, o script está configurado para analisar estatísticas de partidas do modo **Duplas Dinâmicas (Double Up)**.

## Funcionalidades

- **Busca de Conta:** Converte o Riot ID (Nickname + Tag) no `PUUID` do jogador.
- **Histórico Automático:** Resgata o ID das últimas 100 partidas jogadas.
- **Filtro Inteligente:** Isola apenas as partidas do modo Duplas Dinâmicas até atingir uma meta de 30 partidas analisadas.
- **Extração de Dados:** Coleta a colocação final e o dano total causado aos jogadores.
- **Cálculo de Médias:** Gera automaticamente a média de colocação e de dano do jogador nas partidas analisadas.
- **Exportação:** Salva os dados processados em uma planilha Excel (`meu_historico_tft.csv`).

## Tecnologias Utilizadas

- **Python 3**
- **Pandas** (para manipulação de dados e exportação do CSV)
- **Requests** (para requisitar as informações na API da Riot)
- **Python-dotenv** (para ocultar e proteger a chave da API)

## Pré-requisitos

Antes de executar, você precisará ter instalado em sua máquina:
- [Python](https://www.python.org/downloads/)
- O gerenciador de pacotes `pip`
- Uma Chave de Desenvolvedor da Riot Games (pegue a sua no [Riot Developer Portal](https://developer.riotgames.com/)).

## Como executar o projeto

**1. Clone o repositório**
```bash
git clone [https://github.com/SEU_USUARIO/SEU_REPOSITORIO.git](https://github.com/SEU_USUARIO/SEU_REPOSITORIO.git)
cd SEU_REPOSITORIO

```
**2. Instale as dependências**
```bash
pip install -r requirements.txt
```
**3. Configure as Variáveis do Ambiente**
```bash
RIOT_API_KEY=RGAPI-sua-chave-aqui-12345
```
**4. Ajuste os dados do jogador**
```bash
nickname = "seu_apelido"
tag = "BR1"
```

**5. Rode o Script**
```bash
python main.py
```

## Estrutura do Arquivo de Saída
Após a execução, um arquivo chamado meu_historico_tft.csv será gerado na mesma pasta, contendo:

- ID_Partida

- Colocação

- Dano_Causado

- Uma linha final com a MÉDIA TOTAL das estatísticas obtidas.
