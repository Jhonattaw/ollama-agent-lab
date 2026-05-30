

        Ollama Agent Lab
        Agente conversacional local construído com Python e Ollama.
        Projeto criado para estudo prático de agentes conversacionais, memória de conversa, prompting e comportamento de LLMs.
        Roda 100% offline, sem API paga e sem internet. Nenhuma informação sai da máquina.
        O que faz

        * Mantém histórico de conversa (contexto entre mensagens)
        * Comportamento definido por system prompt com regras explícitas
        * Few-shot prompting para controlar respostas do modelo
        * Respostas sempre em português brasileiro
        * Modelo e configurações definidas via arquivo `.env`
        Tecnologias

        * Python 3.11
        * Ollama
        * Mistral 7B
        * python-dotenv
        Lições aprendidas
        O primeiro modelo escolhido nem sempre é o melhor para o problema.
        Comecei utilizando Llama 3.2 e encontrei algumas alucinações factuais: o modelo atribuiu a criação do Python à Microsoft e inventou uma origem baseada em pizza italiana.
        Ao migrar para Mistral 7B, a precisão factual melhorou, mas surgiu outro comportamento interessante: o modelo normalizava nomes incomuns, chamando "Jhonattaw" de "Johnathan".
        A solução foi estruturar melhor o system prompt, definindo:

        * identidade explícita
        * regras de comportamento
        * exemplos de resposta esperada (few-shot prompting)
        Após os ajustes, o agente passou a respeitar corretamente o contexto conversacional e o nome informado.
        Projetos com IA exigem exatamente isso:
        testar → observar comportamento → ajustar → testar novamente
        Como rodar
        1. Instale o Ollama
        Baixe em:
        https://ollama.com
        Baixe o modelo:

        ```bash
        ollama pull mistral:7b

        ```

        2. Clone o repositório

        ```bash
        git clone https://github.com/Jhonattaw/ollama-agent-lab
        cd ollama-agent-lab

        ```

        3. Crie o ambiente virtual
        Windows:

        ```bash
        py -3.11 -m venv venv
        venv\Scripts\activate

        ```

        4. Instale as dependências

        ```bash
        pip install ollama python-dotenv

        ```

        5. Configure o arquivo `.env`
        Crie um arquivo `.env` na raiz:

        ```env
        OLLAMA_MODEL=mistral:7b

        ```

        6. Execute o agente

        ```bash
        python src/agent.py

        ```

        Exemplo de uso

        ```txt
        Você: O que é a linguagem de programação Python e quem criou?

    Agente: Python é uma linguagem de alto nível criada por Guido van 
    Rossum em 1989...

    Você: Meu nome é Jhonattaw. Pode me chamar assim.

    Agente: Entendido. Vou chamar você de Jhonattaw.

    Você: Qual linguagem você explicou anteriormente?

    Agente: A linguagem discutida anteriormente foi Python.

    Você: Qual é o seu nome?

    Agente: Meu nome é Assistente.

        ```

        Próximos projetos

        * Integração com APIs externas para busca em tempo real
        * Sistema RAG com base de conhecimento em documentos próprios
        * Evolução da arquitetura de agentes e experimentos com contexto/memória