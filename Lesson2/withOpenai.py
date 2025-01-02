import os
from crewai import Crew, Agent, Task
from langchain_openai import LLM

#load the openai api key
from dotenv import load_dotenv
load_dotenv()

#set ebvironment variables  
os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")
os.environ['OPENAI_MODEL_NAME'] = os.getenv("OPENAI_MODEL_NAME")

# Create an agent
agent1 = Agent(
    role="blog_researcher",
    goal="Give compelling information about a certain topic",
    backstory="""You love to know information.  People love and hate you for it.  You win most of the
        quizzes at your local pub.""",
        llm = LLM(model="ollama/mistral:latest")
        
)

# Create a task
task1 = Task(
    description="Tell me all about the blue-ringed octopus.",
    expected_output="Give me a quick summary and then also give me 7 bullet points describing it.",
    agent=agent1,
)

# Create a crew
crew = Crew(
    agents=[agent1],
    tasks=[task1],
    verbose=True,
)

# Kickoff the crew
crew.kickoff()  # Returns the result of the task    
# Expected output: Give me a quick summary and then also give me 7 bullet points describing it. 