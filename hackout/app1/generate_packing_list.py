
import os
from langchain.chat_models import ChatOpenAI
from langchain import agents
from langchain_experimental.agents.agent_toolkits import create_csv_agent
from langchain.agents.agent_types import AgentType
def generate_packing_list():
    os.environ["OPENAI_API_KEY"] = "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"
    csv_file_path = r'C:\Users\kshas\OneDrive\Documents\Django_projects\hackout\app1\Book21.csv'
    agent = create_csv_agent(
        ChatOpenAI(temperature=1),
        csv_file_path,
        verbose = True,
        agent_type=AgentType.OPENAI_FUNCTIONS,
    )
    output = agent.run("Give me a packing list when I am going to Abu Dhabi in Winter.")
    return output