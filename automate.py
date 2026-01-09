from crewai import Agent, Task, Crew

def run_lead_research(company_name):
    # 1. The Researcher Agent
    researcher = Agent(
        role='Business Analyst',
        goal=f'Find the core services and main contact person for {company_name}',
        backstory='You are an expert at B2B market research.',
        llm='gemini-1.5-flash' # Using your Gemini model
    )

    # 2. The Task
    task = Task(
        description=f'Search the web for {company_name} and summarize their lead potential.',
        agent=researcher,
        expected_output="A summary of the company and a contact email if possible."
    )

    # 3. The Crew
    crew = Crew(agents=[researcher], tasks=[task])
    return crew.kickoff()
