########################### Langchain ###########################
import os
from dotenv import load_dotenv # type: ignore
from langchain_openai import AzureChatOpenAI # type: ignore
from langchain_core.prompts import PromptTemplate, FewShotPromptTemplate # type: ignore


load_dotenv()

endpoint = os.getenv("ENDPOINT_URL")
deployment = os.getenv("DEPLOYMENT_NAME")
subscription_key = os.getenv("AZURE_OPENAI_API_KEY")

# Inicializar o cliente do Serviço OpenAI do Azure com autenticação baseada em chave
client = AzureChatOpenAI(
    deployment_name=deployment,
    api_key=subscription_key,
    api_version="2024-05-01-preview",
    azure_endpoint=endpoint)

examples = [
    {
    'question': 'How many DataCamp courses has Jack completed?',
    'answer': '36'
    },
    {
    'question': 'How much XP does Jack have on DataCamp?',
    'answer': '284,320XP'
    },
    {
    'question': 'What technology does Jack learn about most on DataCamp?',
    'answer': 'Python'
    }
]

exemple_prompt = PromptTemplate.from_template('Question: {question}\n{answer}')

# Few-shot prompt template
prompt_template = FewShotPromptTemplate(
    examples=examples,
    example_prompt=exemple_prompt,
    suffix="Question: {input}",
    input_variables=["input"],
)
prompt = prompt_template.invoke({'input': 'How many DataCamp courses has Jack completed?'})
print(prompt.text)