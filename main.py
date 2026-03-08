import os
from dotenv import load_dotenv
from crewai import Crew, Process
from agents import researcher, analyst, writer
from tasks import research_task, analysis_task, writing_task
 
load_dotenv()
 
# ─────────────────────────────────────────────
# Assemble the crew
# ─────────────────────────────────────────────
crew = Crew(
    agents=[researcher, analyst, writer],
    tasks=[research_task, analysis_task, writing_task],
    process=Process.sequential,  # Tasks run one after another in order
    verbose=True,                # Print full agent logs
)
 
# ─────────────────────────────────────────────
# Get company from user and launch
# ─────────────────────────────────────────────
if __name__ == '__main__':
    company = input('Enter company name for analysis: ')
 
    print(f'\n Starting BI Report Crew for: {company}\n')
    print('─' * 60)
 
    # kickoff() starts all agents in sequence
    result = crew.kickoff(inputs={'company': company})
 
    print('\n' + '─' * 60)
    print(' Report generation complete!')
    print(' Report saved to: output/report.md')
    print('\n── FINAL OUTPUT ──')
    print(result)
