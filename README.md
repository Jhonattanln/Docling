# Docling Examples

Este repositório contém exemplos práticos de uso do Docling em conjunto com LangChain para processamento de documentos e geração de respostas utilizando Large Language Models (LLMs).

## Estrutura do Projeto

```
src/
└── examples/
    ├── ai_agents.py         - Exemplo de uso de agentes AI
    ├── prompt_fewshot.py    - Demonstração de few-shot prompting
    ├── prompt_template.py   - Uso de templates de prompt
    ├── rag.py              - Implementação de RAG (Retrieval Augmented Generation)
    └── sequential_chains.py - Exemplos de cadeias sequenciais
```

## Exemplos Disponíveis

### 1. RAG (Retrieval Augmented Generation)
Demonstração de como implementar um sistema RAG usando Docling para processamento de documentos e Milvus como vector store.

### 2. Prompt Templates
Exemplos de como criar e utilizar templates de prompt para interações consistentes com LLMs.

### 3. Few-Shot Prompting
Implementação de few-shot learning com exemplos para melhorar a precisão das respostas.

### 4. Sequential Chains
Exemplo de como criar cadeias sequenciais de processamento usando LangChain.

### 5. AI Agents
Demonstração de como utilizar agentes AI para tarefas específicas.

## Pré-requisitos

- Python 3.12.3
- Docling
- LangChain
- Azure OpenAI API Key

## Configuração

1. Clone o repositório
2. Crie um arquivo `.env` com suas credenciais:
```
ENDPOINT_URL=seu_endpoint
DEPLOYMENT_NAME=seu_deployment
AZURE_OPENAI_API_KEY=sua_chave
```
3. Instale as dependências:
```bash
pip install -r requirements.txt
```

## Recursos Adicionais

- [Documentação Docling](https://github.com/DS4SD/docling)
- [Documentação LangChain](https://python.langchain.com/docs/get_started/introduction.html)