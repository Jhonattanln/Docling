########################### Langchain ###########################
import os
from dotenv import load_dotenv
from langchain_openai import AzureChatOpenAI
from langchain_openai import OpenAIEmbeddings
from langchain_chroma import Chroma
from langchain_docling.loader import DoclingLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_core.prompts import PromptTemplate

load_dotenv()

endpoint = os.getenv("ENDPOINT_URL")
deployment = os.getenv("DEPLOYMENT_NAME")
subscription_key = os.getenv("AZURE_OPENAI_API_KEY")

# Inicializar o cliente do Serviço OpenAI do Azure com autenticação baseada em chave
client = AzureChatOpenAI(
    azure_deployment=deployment,
    api_key=subscription_key, # type: ignore
    api_version="2024-05-01-preview",
    azure_endpoint=endpoint
)

# Load a PDF document
load = DoclingLoader('2311.04727v2.pdf')

data = load.load()

# Split o pdf
rc_splitter = RecursiveCharacterTextSplitter(
    chunk_size=1000, # número de caracteres por chunk
    chunk_overlap=200, # número de caracteres de sobreposição
    separators=["\n", "\n\n"] # separadores de chunk
)

docs = rc_splitter.split_documents(data)

# Embedding dos chunks
embed_function = OpenAIEmbeddings(api_key=subscription_key, model='text-embedding-3-small')

vectorstore = Chroma(
    collection_name="docs",
    embedding_function=embed_function,
    persist_directory='data/rag'
)

retriever = vectorstore.as_retriever(
    search_type = 'similarity',
    search_kwargs = {'k': 5}
)

# Query
query = """
Answer the following question using the context provided:

Context:
{context}

Question:
{question}

Answer:
"""

prompt_template = PromptTemplate([("human", query)])

rag_chain = ({'context': retriever, 'question': RunnablePassthrough()}
            | prompt_template
            | client)

response = rag_chain.invoke('What is the conclusion of the paper?')
print(response.content)

