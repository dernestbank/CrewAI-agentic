#Object is to use locall LLM for agentic building with crewai

import os
from crewai import Crew, Agent, Task, LLM
from langchain_openai import  ChatOpenAI

#load the openai api key
from dotenv import load_dotenv

os.environ["OPENAI_API_KEY"] = "sk-proj-1111" #just as a placeholder

# llm = ChatOpenAI(
#     model="phi3:3.8b",
#     base_url="http://localhost:11434/v1"
# )

#initialize the local LLama model via ollama first before running the code
llm = LLM(model="ollama/mistral:latest")

info_agent = Agent(
    role="Information Agent",
    goal="Give compelling information about a certain topic",
    backstory="""
        You love to know information.  People love and hate you for it.  You win most of the
        quizzes at your local pub.
    """,
    llm=llm
)

task1 = Task(
    description="Tell me all about the box jellyfish.",
    expected_output="Give me a quick summary and then also give me 7 bullet points describing it.",
    agent=info_agent
)

crew = Crew(
    agents=[info_agent],
    tasks=[task1],
    verbose=True
)

result = crew.kickoff()

print("############")
print(result)
