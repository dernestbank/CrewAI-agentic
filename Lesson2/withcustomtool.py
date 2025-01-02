#Object is to use locall LLM for agentic building with crewai

import os
from crewai import Crew, Agent, Task, LLM, Process
# from withcustomtool import calculate #import the custom tool
#load the openai api key
from dotenv import load_dotenv

os.environ["OPENAI_API_KEY"] = "sk-proj-1111" #just as a placeholder


#initialize the local LLama model via ollama first before running the code
llm = LLM(model="ollama/mistral:latest")


print("## Welcome to the Math Whiz")
math_input = input("What is your math equation: ")



from langchain_community.tools import tool


@tool("Calculate")
def calculate(equation):
    """ Useful for solving math equations """

    return eval(equation)



# Configure the agents for local LLM
# maths agent
math_agent = Agent(
    role="Math Magician",
    goal="You are able to evaluate any math expression",
    backstory="YOU ARE A MATH WHIZ.",
    verbose=True,
    tools=[calculate],
    llm=llm
)
# writer agent
writer = Agent(
    role="Writer",
    goal="Craft compelling explanations based from results of math equations.",
    backstory="""You are a renowned Content Strategist, known for your insightful and engaging articles.  
    You transform complex concepts into compelling narratives.
    """,
    verbose=True,
    llm=llm
)


# Create tasks
# Task 1: Evaluate the math expression
task1 = Task(
    description=f"{math_input}",
    expected_output="Give full details in bullet points.",
    agent=math_agent
)
# Task 2: Write an explanation based on the result
task2 = Task(
    description="""using the insights provided, explain in great detail how the equation and result 
    were formed.""",
    expected_output="""Explain in great detail and save in markdown.  Do no add the triple tick marks at the 
                    beginning or end of the file.  Also don't say what type it is in the first line.""",
    output_file="markdown/math.md",
    agent=writer
)

# Create a crew with the agents and tasks
# The crew will execute the tasks sequentially
crew = Crew(
    agents=[math_agent, writer],
    tasks=[task1, task2],
    process=Process.sequential,
    verbose=True
)

result = crew.kickoff()

print(result)



