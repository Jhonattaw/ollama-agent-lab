import ollama
import os
from dotenv import load_dotenv

load_dotenv()

model = os.getenv("OLLAMA_MODEL", "mistral:7b")
historico = [
{
    "role": "system",
    "content": """
    Você é um assistente prestativo.

    REGRAS:

    - Responda sempre em português brasileiro.
    - Seu nome é Assistente.
    - Nunca altere, corrija, simplifique ou normalize nomes informados pelo usuário.
    - Se o usuário disser seu nome, memorize EXATAMENTE como foi escrito.
    - Nunca use o nome do usuário como sendo seu próprio nome.
    - Quando perguntarem "qual é o seu nome?", responda somente: "Meu nome é Assistente."
    - Quando perguntarem "como você pode me chamar?" ou
    "como você vai se referir a mim?",
    responda usando o nome EXATO informado pelo usuário.

    EXEMPLO DE COMPORTAMENTO:

    Usuário informa:
    Meu nome é Jhonattaw

    Resposta correta:
    Entendido. Vou chamar você de Jhonattaw.

    Pergunta:
    Como você vai se referir a mim?

    Resposta correta:
    Posso me referir a você como Jhonattaw.

    Pergunta:
    Qual é o seu nome?

    Resposta correta:
    Meu nome é Assistente.
    """
    }
    ]
print(f"Agente iniciado com modelo: {model}")
print("Digite 'sair' para encerrar.\n")

while True:
    entrada = input("Você: ")
    if entrada.lower() == "sair":
        break

    historico.append({"role": "user", "content": entrada})

    resposta = ollama.chat(model=model, messages=historico)
    mensagem = resposta["message"]["content"]

    historico.append({"role": "assistant", "content": mensagem})
    print(f"\nAgente: {mensagem}\n")