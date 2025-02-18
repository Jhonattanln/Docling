########################### Langchain ###########################
import os
from langchain_openai import AzureChatOpenAI # type: ignore
from langchain_core.prompts import PromptTemplate # typr: ignore

endpoint = os.getenv("ENDPOINT_URL", "https://oai-cvm358.openai.azure.com/")
deployment = os.getenv("DEPLOYMENT_NAME", "gpt-4o-mini")
subscription_key = os.getenv("AZURE_OPENAI_API_KEY", "15b50eb85377452b841989f625b8f577")

# Inicializar o cliente do Serviço OpenAI do Azure com autenticação baseada em chave
client = AzureChatOpenAI(
    deployment_name=deployment,
    api_key=subscription_key,
    api_version="2024-05-01-preview",
    azure_endpoint=endpoint
)
template = "You are a quantitative finance analyst, answar the following question: {question}" 
prompt_template = PromptTemplate(template=template, input_variables=["question"])

# Invocar o modelo de linguagem com a pergunta
llm_chain = prompt_template | client
response = llm_chain.invoke({'question': 'What is a stock option?'})

print(response)
