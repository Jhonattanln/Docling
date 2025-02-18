########################### Langchain ###########################
#from openai import AzureOpenAI
from langchain_openai import AzureOpenAI
import os  
import base64
from openai import AzureOpenAI  
from azure.identity import DefaultAzureCredential, get_bearer_token_provider  
        
endpoint = os.getenv("ENDPOINT_URL", "https://jhona-m7aj9hc3-swedencentral.openai.azure.com/")  
deployment = os.getenv("DEPLOYMENT_NAME", "gpt-35-turbo")  
      
# Inicializar o cliente do Serviço OpenAI do Azure com autenticação do Entra ID
token_provider = get_bearer_token_provider(  
    DefaultAzureCredential(),  
    "https://cognitiveservices.azure.com/.default"  
)  
  
client = AzureOpenAI(  
    azure_endpoint=endpoint,  
    azure_ad_token_provider=token_provider,  
    api_version="2024-05-01-preview",  
)  

llm = AzureOpenAI(
    deployment_name = 'gpt-35-turbo',
)
llm.invoke("Tell me a joke")
print(llm)