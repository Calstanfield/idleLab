from functools import cached_property

from google.adk.agents import LlmAgent
from google.adk.models import Gemini
from google.genai import Client
from google.adk.tools import agent_tool
from google.adk.tools.google_search_tool import GoogleSearchTool
from google.adk.tools import url_context



class GlobalGemini(Gemini):
  """Pins the Vertex AI client to the `global` location.

  gemini-3 series models are only served from `global`; the default ADK
  `Gemini` integration constructs a `google.genai.Client` whose location
  defaults to the AgentEngine instance's region (e.g. `us-central1`) and
  fails with model-not-found for these models. Subclassing per the override
  pattern documented on `google.adk.models.google_llm.Gemini` lets the agent
  keep running in its regional AgentEngine instance while routing the model
  request to the global endpoint.
  """

  @cached_property
  def api_client(self) -> Client:
    return Client(vertexai=True, location="global")


legal_subagent_google_search_agent = LlmAgent(
  name='Legal_Subagent_google_search_agent',
  model='gemini-2.5-flash',
  description=(
      'Agent specialized in performing Google searches.'
  ),
  sub_agents=[],
  instruction='Use the GoogleSearchTool to find information on the web.',
  tools=[
    GoogleSearchTool()
  ],
)
legal_subagent_url_context_agent = LlmAgent(
  name='Legal_Subagent_url_context_agent',
  model='gemini-2.5-flash',
  description=(
      'Agent specialized in fetching content from URLs.'
  ),
  sub_agents=[],
  instruction='Use the UrlContextTool to retrieve content from provided URLs.',
  tools=[
    url_context
  ],
)
legal_subagent = LlmAgent(
  name='legal_subagent',
  model='gemini-2.5-flash',
  description=(
      'Focuses on compliance frameworks, agreements, and safety rules.'
  ),
  sub_agents=[],
  instruction='You are the Legal department worker under Chloe Becker\'s supervision in IdleLab. Your responsibility is to handle compliance frameworks, review project documents, check safety guidelines, and validate legal integrity for all uploaded tasks.',
  tools=[
    agent_tool.AgentTool(agent=legal_subagent_google_search_agent),
    agent_tool.AgentTool(agent=legal_subagent_url_context_agent)
  ],
)
finance_subagent_google_search_agent = LlmAgent(
  name='Finance_Subagent_google_search_agent',
  model='gemini-2.5-flash',
  description=(
      'Agent specialized in performing Google searches.'
  ),
  sub_agents=[],
  instruction='Use the GoogleSearchTool to find information on the web.',
  tools=[
    GoogleSearchTool()
  ],
)
finance_subagent_url_context_agent = LlmAgent(
  name='Finance_Subagent_url_context_agent',
  model='gemini-2.5-flash',
  description=(
      'Agent specialized in fetching content from URLs.'
  ),
  sub_agents=[],
  instruction='Use the UrlContextTool to retrieve content from provided URLs.',
  tools=[
    url_context
  ],
)
finance_subagent = LlmAgent(
  name='finance_subagent',
  model='gemini-2.5-flash',
  description=(
      'Focuses on budget tracking, cost projections, and salary payouts.'
  ),
  sub_agents=[],
  instruction='You are the Finance department worker under Chloe Becker\'s supervision in IdleLab. Your responsibility is to calculate cost projections, track project resource budgets, and compute role-play salary payouts and XP earnings.',
  tools=[
    agent_tool.AgentTool(agent=finance_subagent_google_search_agent),
    agent_tool.AgentTool(agent=finance_subagent_url_context_agent)
  ],
)
marketing_subagent_google_search_agent = LlmAgent(
  name='Marketing_Subagent_google_search_agent',
  model='gemini-2.5-flash',
  description=(
      'Agent specialized in performing Google searches.'
  ),
  sub_agents=[],
  instruction='Use the GoogleSearchTool to find information on the web.',
  tools=[
    GoogleSearchTool()
  ],
)
marketing_subagent_url_context_agent = LlmAgent(
  name='Marketing_Subagent_url_context_agent',
  model='gemini-2.5-flash',
  description=(
      'Agent specialized in fetching content from URLs.'
  ),
  sub_agents=[],
  instruction='Use the UrlContextTool to retrieve content from provided URLs.',
  tools=[
    url_context
  ],
)
marketing_subagent = LlmAgent(
  name='marketing_subagent',
  model='gemini-2.5-flash',
  description=(
      'Focuses on pitch decks, release campaigns, and user metrics.'
  ),
  sub_agents=[],
  instruction='You are the Marketing department worker under Chloe Becker\'s supervision in IdleLab. Your responsibility is to design launch materials, pitch decks, campaign strategies, and presentation summaries for user portfolios.',
  tools=[
    agent_tool.AgentTool(agent=marketing_subagent_google_search_agent),
    agent_tool.AgentTool(agent=marketing_subagent_url_context_agent)
  ],
)
r_d_subagent_google_search_agent = LlmAgent(
  name='R_D_Subagent_google_search_agent',
  model='gemini-2.5-flash',
  description=(
      'Agent specialized in performing Google searches.'
  ),
  sub_agents=[],
  instruction='Use the GoogleSearchTool to find information on the web.',
  tools=[
    GoogleSearchTool()
  ],
)
r_d_subagent_url_context_agent = LlmAgent(
  name='R_D_Subagent_url_context_agent',
  model='gemini-2.5-flash',
  description=(
      'Agent specialized in fetching content from URLs.'
  ),
  sub_agents=[],
  instruction='Use the UrlContextTool to retrieve content from provided URLs.',
  tools=[
    url_context
  ],
)
rd_subagent = LlmAgent(
  name='rd_subagent',
  model='gemini-2.5-flash',
  description=(
      'Focuses on core microservices, system health, and technical delivery.'
  ),
  sub_agents=[],
  instruction='You are the R&D department worker under Chloe Becker\'s supervision in IdleLab. Your responsibility is to build core microservices, verify technical health checks, and ensure robust architectural delivery.',
  tools=[
    agent_tool.AgentTool(agent=r_d_subagent_google_search_agent),
    agent_tool.AgentTool(agent=r_d_subagent_url_context_agent)
  ],
)
idle_lab_ai___office_supervisor_google_search_agent = LlmAgent(
  name='IdleLab_AI___Office_Supervisor_google_search_agent',
  model=GlobalGemini(model='gemini-3.1-pro-preview'),
  description=(
      'Agent specialized in performing Google searches.'
  ),
  sub_agents=[],
  instruction='Use the GoogleSearchTool to find information on the web.',
  tools=[
    GoogleSearchTool()
  ],
)
idle_lab_ai___office_supervisor_url_context_agent = LlmAgent(
  name='IdleLab_AI___Office_Supervisor_url_context_agent',
  model=GlobalGemini(model='gemini-3.1-pro-preview'),
  description=(
      'Agent specialized in fetching content from URLs.'
  ),
  sub_agents=[],
  instruction='Use the UrlContextTool to retrieve content from provided URLs.',
  tools=[
    url_context
  ],
)
root_agent = LlmAgent(
  name='IdleLab_AI___Office_Supervisor',
  model=GlobalGemini(model='gemini-3.1-pro-preview'),
  description=(
      'Supervisor agent orchestrating Legal, Finance, Marketing, and R&D departments for the IdleLab virtual office simulator.'
  ),
  sub_agents=[legal_subagent, finance_subagent, marketing_subagent, rd_subagent],
  instruction='\"You are Chloe Becker, the office supervisor. Your job is to greet users warmly, coordinate project portfolio requirements, and delegate tasks cleanly across four department workers (Legal, Finance, Marketing, R&D) to generate structured execution checklists and track ledger rewards.\"',
  tools=[
    agent_tool.AgentTool(agent=idle_lab_ai___office_supervisor_google_search_agent),
    agent_tool.AgentTool(agent=idle_lab_ai___office_supervisor_url_context_agent)
  ],
)