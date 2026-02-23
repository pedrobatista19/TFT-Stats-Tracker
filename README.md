# ♟️ TFT STATS TRACKER

Um script em Python desenvolvido para consumir a API oficial da Riot Games, analisar o histórico de partidas de Teamfight Tactics (TFT) de um jogador e exportar um relatório detalhado no formato `.csv`.

Atualmente, o script está configurado para filtrar e analisar estatísticas de partidas do modo **Duplas (Double Up)**.

## ✨ Funcionalidades

- **Busca de Conta:** Converte o Riot ID (Nickname + Tag) no `PUUID` do jogador.
- **Histórico Automático:** Resgata o ID das últimas 100 partidas jogadas.
- **Filtro Inteligente:** Isola apenas as partidas do modo Duplas (`queue_id = 1160`) até atingir uma meta de 30 partidas analisadas.
- **Extração de Dados:** Coleta a colocação final e o dano total causado aos jogadores.
- **Cálculo de Médias:** Gera automaticamente a média de colocação e de dano do jogador nas partidas analisadas.
- **Exportação:** Salva os dados processados em uma planilha Excel (`meu_historico_tft.csv`).

## 🛠️ Tecnologias Utilizadas

- **Python 3**
- **Pandas** (para manipulação de dados e exportação do CSV)
- **Requests** (para realizar as requisições HTTP na API da Riot)
- **Python-dotenv** (para ocultar e proteger a chave da API)

## ⚙️ Pré-requisitos

Antes de começar, você precisará ter instalado em sua máquina:
- [Python](https://www.python.org/downloads/)
- O gerenciador de pacotes `pip`
- Uma Chave de Desenvolvedor da Riot Games (pegue a sua no [Riot Developer Portal](https://developer.riotgames.com/)).

## 🚀 Como executar o projeto

**1. Clone o repositório**
```bash
git clone [https://github.com/SEU_USUARIO/SEU_REPOSITORIO.git](https://github.com/SEU_USUARIO/SEU_REPOSITORIO.git)
cd SEU_REPOSITORIO

**2. Instale as dependências
pip install -r requirements.txt
