import os

from langchain.agents import initialize_agent, AgentType, create_react_agent
from langchain_community.llms.huggingface_hub import HuggingFaceHub
from langchain_core.tools import Tool
from langchain_core.prompts import PromptTemplate

"""
All requests to the LLM require some form of a key.
Other sensitive data has also been hidden through environment variables.
"""

"""
We will create an agent that can deduce the length of a word or the cube of a number.
The agent will decide on one process or another by matching a given task with the description of its tools.

https://python.langchain.com/docs/modules/agents/
"""

# Set the HUGGINGFACEHUB_API_TOKEN environment variable
os.environ['HUGGINGFACEHUB_API_TOKEN'] = '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'


# define llm
llm = HuggingFaceHub(
    repo_id="google/flan-t5-xxl",
    model_kwargs={"temprature":0.0 , "max_length":200}
)

"""
The two functions below will serve as tools for the agent. 
In other words, they are processes that the agent can choose from to complete a given task.
However, the agent won't know which tool to use if they aren't described well. 
"""
def get_word_length(word) -> int:
    # TODO: you are honest agent and you need to find the length of a word.
    """
    Find the length of a word.

    Parameters:
    - word (str): The input word.

    Returns:
    - int: Length of the word.
    """
    return len(word)

def get_cube_of_number(number) -> int:
    # TODO: You are a honest agent and  you need to calculate the cube of a number.
    """
    Calculates the cube of given number.

    Parameters:
    - number (int): The input number.

    Returns:
    - int: cube of number.
    """
    
    return number**3

"""
Here, we are defining the tools that the agent will have access to. 
"""
# TODO: finish defining the second tool that the agent will have access to (get_word_length)
tools = [
    Tool.from_function(
        func=get_word_length,
        name="get_word_length",
        description="Calculates the length of a word",
    ),
    Tool.from_function(
        func=get_cube_of_number,
        name="get_cube_of_number",
        description="Finds the cube of a number",
    ),
]

"""
We can now create the agent! No need to edit the code below.
We are using the initialize_agent function, providing it with the tools and llm defined above.  

We've defined the agent type as ZERO_SHOT_REACT_DESCRIPTION. 
This is the most general type of agent. It determines which tool to use solely based on the tool descriptions.

By setting verbose=True, we can see what the agent is thinking/doing in the console. 

Finally, by setting return_intermediate_steps=True, we can access the intermediate steps of the agent.
This is useful for debugging and writing tests.
"""
# agent_executor = initialize_agent(
#     tools=tools,
#     llm=llm,
#     agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
#     verbose=True,
#     return_intermediate_steps=True,
# )

# Create a ReAct agent without specifying agent_type

agent_executor = initialize_agent(
    tools=tools,
    llm=llm,
    agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
    verbose=True,
    return_intermediate_steps=True,
    max_iterations = 3,
    handle_parsing_errors=True
)
