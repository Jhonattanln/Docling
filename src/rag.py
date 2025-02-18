########################### Langchain ###########################
import os
from langchain_openai import AzureChatOpenAI

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

# Exemplo de uso
response = client.invoke("Tell me a joke")
print(response)
