import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain.agents import AgentExecutor, create_react_agent
from langchain_community.agent_toolkits.load_tools import load_tools
from langchain.chains import LLMMathChain

# Carregar variáveis de ambiente
load_dotenv()

endpoint = os.getenv("ENDPOINT_URL")
deployment = os.getenv("DEPLOYMENT_NAME")
subscription_key = os.getenv("AZURE_OPENAI_API_KEY")

# Inicializar o cliente do Serviço OpenAI do Azure
client = ChatOpenAI(
    deployment_name=deployment,
    api_key=subscription_key,
    api_version="2024-05-01-preview",
    azure_endpoint=endpoint
)

tools = load_tools(["llm-math"], llm=client, )
agent = create_react_agent(llm=client, tools=tools, prompt="What is the square root of 101?")
messages = agent.invoke({"question": [("human", "What is the square root of 101?")]})
print(messages)

