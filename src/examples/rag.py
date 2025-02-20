########################### Langchain ###########################
import os
from dotenv import load_dotenv
from langchain_openai import AzureChatOpenAI
from langchain_community.document_loaders import PyPDFLoader
from langchain_docling.loader import DoclingLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter

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
    chunk_size=500,
    chunk_overlap=200,
    separators=["\n", "\n\n"]
)
docs = rc_splitter.split_documents(data)
print(docs[0])
