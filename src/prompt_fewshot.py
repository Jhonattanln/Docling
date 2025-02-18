########################### Langchain ###########################
import os
from langchain_openai import AzureChatOpenAI # type: ignore
from langchain_core.prompts import PromptTemplate, FewShotPromptTemplate # typr: ignore

endpoint = os.getenv("ENDPOINT_URL", "https://oai-cvm358.openai.azure.com/")
deployment = os.getenv("DEPLOYMENT_NAME", "gpt-4o-mini")
subscription_key = os.getenv("AZURE_OPENAI_API_KEY", "15b50eb85377452b841989f625b8f577")

# Inicializar o cliente do Serviço OpenAI do Azure com autenticação baseada em chave
client = AzureChatOpenAI(
    deployment_name=deployment,
    api_key=subscription_key,
    api_version="2024-05-01-preview",
    azure_endpoint=endpoint)

examples = [{
    'question': 'How many DataCamp courses has Jack completed?',
    'answer': '36'},
    {
    'question': 'How much XP does Jack have on DataCamp?',
    'answer': '284,320XP'},
    {'question': 'What technology does Jack learn about most on DataCamp?',
    'answer': 'Python'}
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