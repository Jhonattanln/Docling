########################### Langchain ###########################
import os
from dotenv import load_dotenv
from langchain_openai import AzureChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

endpoint = os.getenv("ENDPOINT_URL")
deployment = os.getenv("DEPLOYMENT_NAME")
subscription_key = os.getenv("AZURE_OPENAI_API_KEY")

# Inicializar o cliente do Serviço OpenAI do Azure com autenticação baseada em chave
client = AzureChatOpenAI(
    deployment_name=deployment, # type: ignore
    api_key=subscription_key,
    api_version="2024-05-01-preview",
    azure_endpoint=endpoint
)
# Cadeira de pesquisa sequencial
destination_prompt = PromptTemplate(input_variables=["destination"],
                                    template="I am planning a trip to {destination}. Can you suggest some activities to do there?")
activities_prompt = PromptTemplate(input_variables=["activities"],
                                   template="I only have one day, so can you create an itinerary from your top three activities: {activities}.")

seq_chain = ({"activities": destination_prompt | client | StrOutputParser()}    
             | activities_prompt    | client    | StrOutputParser()) # Pergunta de destino -> Atividades -> Itinerário

# Invocar a cadeia sequencial com o destino
response = seq_chain.invoke({"destination": "Paris"})
print(response)

