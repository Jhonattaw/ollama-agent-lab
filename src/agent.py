import ollama
import os
from dotenv import load_dotenv

load_dotenv()

model = os.getenv("OLLAMA_MODEL", "llama3.2")
historico = [
    {
        "role": "system",
        "content": "Você é um assistente prestativo. Responda sempre em português brasileiro, de forma clara e objetiva."
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