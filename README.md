# ChatBot - Programa Python

        ───████████───
        ──▐▀▀▀▀▀▀▀▀▌──
        ─▐▐  ▀  ▀  ▌▌─
        ──▐──▄▄▄▄──▌──
        ──▐  █▄▄█  ▌──


Este é um chatbot desenvolvido em Python usando as seguintes bibliotecas:

- `urllib3`: Para realizar requisições HTTP.
- `pygame`: Para o uso da biblioteca `gtts` (Google Text-to-Speech) para converter texto em áudio.
- `random`: Para gerar nomes de arquivos aleatórios.
- `string`: Para definir a string de caracteres permitidos para os nomes de arquivos.
- `gTTS`: Bilioteca para conversão de texto em voz.
- `datetime`: Para obter a data e hora atual.
- `dotenv`: Para carregar variáveis de ambiente.
- `langchain_ollama`: Para integração com o modelo Ollama.
- `rich.console` e `rich.markdown`: Para melhorar a exibição dos outputs.
- `os`: Para manipulação do sistema operacional.

## Funcionalidades

1. **Interface de Chat**: Um menu que solicita ao usuário um prompt para enviar sua pergunta ou interromper o chat com 'x'.
2. **Requisição ao Chat**: O prompt é enviado ao modelo Ollama usando a biblioteca `langchain_ollama`.
3. **Feedback ao Usuário**: A resposta do modelo é exibida no console, mostrando também a conversa até então.
4. **Suporte para Tradução de Texto em Áudio**: O bot usa `gtts` para converter a resposta em áudio e `pygame.mixer` para o áudio ser reproduzido.
5. **Histórico das Conversas**: As conversas são registradas no arquivo `history_<data>.txt`.
6. **Integração com Variáveis de Ambiente**: Configurado para ler as URLs e modelos do Ollama de um arquivo `.env`.

## Como Rodar o Programa

1. **Configurações**:
   - Crie um arquivo `.env` na raiz do projeto com as seguintes variáveis:
     ```
     OLLAMA_URL=your_ollama_url
     OLLAMA_MODEL=your_model_name
     ```
2. **Instalação das Dependências**: Use o comando `pip install -r requirements.txt` para instalar todas as bibliotecas necessárias.
3. **Execução**: Execute o script com o comando: `python chat.py`.
