

# Ollama Agent Lab

Agente conversacional local construído com Python e Ollama.

## O que faz
- Mantém histórico de conversa (contexto entre mensagens)
- System prompt configurável para definir comportamento
- Modelo e configurações via arquivo .env

## Tecnologias
- Python 3.11
- Ollama (llama3.2)
- python-dotenv

## Como rodar

1. Instale o Ollama em ollama.com e baixe o modelo:
ollama pull llama3.2

2. Clone o repositório:
git clone https://github.com/Jhonattaw/ollama-agent-lab

3. Crie o ambiente virtual e instale as dependências:
py -3.11 -m venv venv
venv\Scripts\activate
pip install ollama python-dotenv

4. Crie o arquivo .env na raiz:
OLLAMA_MODEL=llama3.2

5. Rode o agente:
python src/agent.py

## O que aprendi
- Como funciona o loop de conversa com LLMs
- Gerenciamento de histórico de mensagens
- Uso de system prompt para controlar comportamento do modelo
- Integração Python + Ollama via API local