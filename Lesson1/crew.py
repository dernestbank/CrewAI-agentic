from crewai import Crew, Process
from agents import researcher_agent,blog_writer,notes_writer,mindmap_generator,Quality_assurance
from tools import Yt_searchTool,Yt_ChannelTool

# Create a crew with the agents and tools

crew = Crew(
    agents=[researcher_agent,blog_writer,notes_writer],
    tools=[Yt_searchTool,Yt_ChannelTool],
    verbose=True,
    process = Process.sequential, # or Process.parallel sequential is defulated
    memory = True, # set to True to enable memory
    memory_size = 1000, #unit is in words
    cache = True, # set to True to enable cache
    max_rpm = 100, # maximum requests per minute
    share_crew = True, # set to True to share the crew with other agents
)

# crew_output = crew.kickoff('Machine learning vrs AI')
inputs = {'topic': 'Machine learning vrs AI'}

crew_output = crew.kickoff(inputs)

# Accessing the crew output
print(f"Raw Output: {crew_output.raw}")
if crew_output.json_dict:
    print(f"JSON Output: {json.dumps(crew_output.json_dict, indent=2)}")
if crew_output.pydantic:
    print(f"Pydantic Output: {crew_output.pydantic}")
print(f"Tasks Output: {crew_output.tasks_output}")
print(f"Token Usage: {crew_output.token_usage}")