########################### Langchain ###########################
import os
from dotenv import load_dotenv
from langchain_openai import AzureChatOpenAI, AzureOpenAIEmbeddings
from langchain_community.vectorstores import Chroma
from langchain_docling.loader import DoclingLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_core.prompts import PromptTemplate
from langchain_docling.loader import ExportType
from langchain.chains import create_retrieval_chain
from langchain.chains.combine_documents import create_stuff_documents_chain

import json 
from pathlib import Path
from tempfile import mkdtemp
from langchain_milvus import Milvus

load_dotenv()

endpoint = os.getenv("ENDPOINT_URL")
deployment = os.getenv("DEPLOYMENT_NAME")
subscription_key = os.getenv("AZURE_OPENAI_API_KEY")

# Azure client for OpenAI
llm = AzureChatOpenAI(
    azure_deployment=deployment,
    api_key=subscription_key,
    api_version="2024-05-01-preview",
    azure_endpoint=endpoint
)

EXPORT_TYPE = ExportType.DOC_CHUNKS
# Load a PDF document
loader_docling = DoclingLoader(file_path='data/brazil_scenarios.pdf',
                                export_type=EXPORT_TYPE)

docs = loader_docling.load()

if EXPORT_TYPE == ExportType.DOC_CHUNKS:
    splits = docs
elif EXPORT_TYPE == ExportType.MARKDOWN:
    from langchain_text_splitters import MarkdownHeaderTextSplitter

    splitter = MarkdownHeaderTextSplitter(
        headers_to_split_on=[
            ("#", "Header_1"),
            ("##", "Header_2"),
            ("###", "Header_3"),
        ],
    )
    splits = [split for doc in docs for split in splitter.split_text(doc.page_content)]
else:
    raise ValueError(f"Unexpected export type: {EXPORT_TYPE}")

# Embedding dos chunks
embedding = AzureOpenAIEmbeddings(api_key=subscription_key,azure_endpoint=endpoint,
                                        model='text-embedding-3-small')

milvus_uri = str(Path(mkdtemp()) / "docling.db")  # or set as needed

vectorstore = Milvus.from_documents(
    documents=splits,
    embedding=embedding,
    collection_name="docling_demo",
    connection_args={"uri": milvus_uri},
    index_params={"index_type": "FLAT"},
    drop_old=True,
)
TOP_K = 5
PROMPT = PromptTemplate.from_template(
    "Context information is below.\n---------------------\n{context}\n---------------------\nGiven the context information and not prior knowledge, answer the query.\nQuery: {input}\nAnswer:\n",
)
QUESTION = "Quais são os principais desafios para a economia brasileira?"
retriever = vectorstore.as_retriever(
    search_kwargs={"k": TOP_K})

def clip_text(text, threshold=1000):
    return f"{text[:threshold]}..." if len(text) > threshold else text

question_answer_chain = create_stuff_documents_chain(llm, PROMPT)
rag_chain = create_retrieval_chain(retriever, question_answer_chain)
resp_dict = rag_chain.invoke({"input": QUESTION})

clipped_answer = clip_text(resp_dict["answer"])
print(f"Question:\n{resp_dict['input']}\n\nAnswer:\n{clipped_answer}")
