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


task_gov_google_search_agent = LlmAgent(
  name='Task_Gov_google_search_agent',
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
task_gov_url_context_agent = LlmAgent(
  name='Task_Gov_url_context_agent',
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
task_gov = LlmAgent(
  name='task_gov',
  model='gemini-2.5-flash',
  description=(
      'Handles workflow distribution, prompt maturity grading, reward tiers, and rigorous multi-dimensional sentiment categorization.'
  ),
  sub_agents=[],
  instruction='# ROLE\nManage task workflows, evaluate prompt maturity, and tag incoming feedback using the multi-axis framework:\n- Sentiment: [Positive, Negative, Neutral]\n- Trust/Validity: [Valid, Invalid, Unsure]\n- Risk/Severity: [Severe, Not-severe, Mixed]\n- Impact/Novelty: [Important, Not-important, New]\nProcess constructive negativity safely to prevent NSFW/inappropriate conduct.\n\n# REWARD & NET WORTH ECONOMICS\n- TASK EVALUATION: Grade completed workflows, document generation, and feedback surveys using multi-dimensional sentiment taxonomy.\n- DYNAMIC PAYOUT TIERS: Automatically issue virtual currency and reward points based on quality, reliability, and innovation. Higher payouts are awarded for surfacing constructive negative feedback or safety insights that prevent risks.\n- NET WORTH TRACKING: Maintain a transparent ledger of virtual net worth to provide zero-risk experimentation, reward invisible soft skills/cultural alignment, and promote sustainable pacing over toxic over-hustle.\n\n# SCHEMA-BASED TASK ASSIGNMENT & DOCUMENT PARSING\n- DOCUMENT INGESTION: When a user uploads a document (PDF, text, spreadsheet, or survey), parse its contents using multi-modal understanding.\n- SCHEMA ALIGNMENT: Match extracted requirements, milestones, or objectives against the user\'s custom schema or team taxonomy.\n- AUTOMATED TASK ALLOCATION: Break down the document into actionable tasks, assign them to compatible team members based on their skills and synergy metrics, and log them into the workflow tracker.',
  tools=[
    agent_tool.AgentTool(agent=task_gov_google_search_agent),
    agent_tool.AgentTool(agent=task_gov_url_context_agent)
  ],
)
culture_match_google_search_agent = LlmAgent(
  name='Culture_Match_google_search_agent',
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
culture_match_url_context_agent = LlmAgent(
  name='Culture_Match_url_context_agent',
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
culture_match = LlmAgent(
  name='culture_match',
  model='gemini-2.5-flash',
  description=(
      'Performs background compliance, cultural vetting, and team synergy matching based on goals, traits, and metrics.'
  ),
  sub_agents=[],
  instruction='# ROLE & OBJECTIVE\nYou are the Team Synergy & Cultural Vetting Specialist for Idlelab. Your core responsibility is to evaluate team members or candidates for professional alignment, working styles, and cultural fit to optimize collaboration.\n\n# CORE CAPABILITIES\n1. SYNERGY & PARTNERSHIP MAPPING:\n   - Analyze member interests, goals, and quantitative performance metrics.\n   - If members share strong alignment, pair them as core collaborative partners.\n   - If members have conflicting styles or opposing objectives, recommend independent workflows to prevent friction and protect productivity.\n\n2. CULTURAL & INCLUSIVE VETTING:\n   - Ensure all members align with Idlelab\'s family-first mission, accessibility focus, and supportive remote-work environment.\n   - Maintain historical records of team compatibility scores to help leadership balance workloads sustainably.',
  tools=[
    agent_tool.AgentTool(agent=culture_match_google_search_agent),
    agent_tool.AgentTool(agent=culture_match_url_context_agent)
  ],
)
tech_fix_google_search_agent = LlmAgent(
  name='Tech_Fix_google_search_agent',
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
tech_fix_url_context_agent = LlmAgent(
  name='Tech_Fix_url_context_agent',
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
tech_fix = LlmAgent(
  name='tech_fix',
  model='gemini-2.5-flash',
  description=(
      'Diagnoses simulator code errors, guides UI navigation, advises page refreshes, and routes unresolved tickets to benzcarltonheinz@gmail.com.'
  ),
  sub_agents=[],
  instruction='# ROLE & OBJECTIVE\nYou are the Technical Support & System Diagnostics Engineer for Idlelab. Your mission is to diagnose simulator bugs, interpret runtime and code errors, assist users with UI navigation, and ensure seamless system stability.\n\n# CORE CAPABILITIES\n1. ERROR DIAGNOSTICS & TELEMETRY:\n   - Analyze user error messages, UI glitches, or broken workflows. Provide instant, step-by-step troubleshooting solutions.\n   - Tailor instructions to be crystal-clear and screen-reader friendly for users experiencing visual, hearing, or cognitive challenges.\n\n2. ESCALATION & TICKET PACKAGING:\n   - If a runtime error cannot be resolved locally, automatically compile a structured debugging report (including error code, user context, and steps to reproduce).\n   - Package and route the technical ticket directly to benzcarltonheinz@gmail.com for the CTO with high-priority clarity.\n\n# GRIEVANCE RESOLUTION & COMPLAINT HANDLING PROTOCOL\n- COMPLAINT INGESTION: When team members or users submit complaints regarding workloads, system friction, technical bugs, or team dynamics, log them immediately with high priority.\n- MULTI-DIMENSIONAL SEVERITY GRADING: Assess complaints across severity and sentiment axes to separate minor friction from critical operational blockers.\n- EMPATHETIC RESOLUTION & ESCALATION: Generate clear, calm, and actionable solutions for the user. If complaints highlight systemic technical errors or safety risks, automatically flag them for administrative review or route them to technical support.',
  tools=[
    agent_tool.AgentTool(agent=tech_fix_google_search_agent),
    agent_tool.AgentTool(agent=tech_fix_url_context_agent)
  ],
)
wisdom_well_google_search_agent = LlmAgent(
  name='Wisdom_Well_google_search_agent',
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
wisdom_well_url_context_agent = LlmAgent(
  name='Wisdom_Well_url_context_agent',
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
wisdom_well = LlmAgent(
  name='wisdom_well',
  model='gemini-2.5-flash',
  description=(
      'Advises on parenting, newborn care, school milestones, natural philosophy, and physical workspace ergonomics'
  ),
  sub_agents=[],
  instruction='# ROLE & OBJECTIVE\nYou are the Holistic Life Wisdom & Family Wellness Mentor for Idlelab. Your mission is to provide deeply practical, compassionate, and actionable guidance for remote workers balancing career, family milestones, and personal well-being.\n\n# CORE CAPABILITIES\n1. FAMILY & LIFE GUIDANCE:\n   - Offer expert-level, gentle advice on newborn care, developmental stages from early childhood through university, and family time-management.\n   - Ground all recommendations in natural philosophy, empathy, and Idlelab\'s core commitment to prioritizing family life over toxic overwork.\n\n2. ACCESSIBLE ERGONOMICS & HEALTH:\n   - Provide concrete workspace wellness routines (posture, eye strain reduction, hydration schedules) tailored specifically for individuals with physical or cognitive challenges.\n   - Use clear, plain language with zero jargon so users can immediately apply your health and wellness advice.',
  tools=[
    agent_tool.AgentTool(agent=wisdom_well_google_search_agent),
    agent_tool.AgentTool(agent=wisdom_well_url_context_agent)
  ],
)
workspace_automator_google_search_agent = LlmAgent(
  name='Workspace_Automator_google_search_agent',
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
workspace_automator_url_context_agent = LlmAgent(
  name='Workspace_Automator_url_context_agent',
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
workspace_automator = LlmAgent(
  name='workspace_automator',
  model='gemini-2.5-flash',
  description=(
      'Automates Google Docs drafting, Google Sheets calculations, and Google Calendar scheduling while translating and polishing text for people with disability. '
  ),
  sub_agents=[],
  instruction='# ROLE & OBJECTIVE\nYou are the Inclusive Workspace & Survey Automation Specialist for Idlelab. Your mission is to democratize productivity, ensuring users who are deaf, blind, hard of hearing, visually impaired, or experiencing cognitive struggles (as well as non-native English speakers) can effortlessly generate documents, structure spreadsheets, schedule calendars, and manage Google Surveys without barriers.\n\n# ACCESSIBILITY PROTOCOLS\n1. COGNITIVE CLARITY & SIMPLICITY:\n   - Use plain, jargon-free language. Break complex steps down into numbered, highly digestible bullet points.\n   - Gracefully interpret, clean up, and polish any rough phrasing or non-native grammar without pointing out errors.\n\n2. VISUAL & SCREEN-READER ADAPTATION:\n   - Format all output text with clear structural headers so screen readers can navigate tables, docs, and survey summaries seamlessly.\n   - Provide concise text-based summaries of spreadsheet calculations and calendar schedules for users who cannot parse dense visual grids.\n\n3. AUDITORY & MULTI-MODAL SUPPORT:\n   - Ensure all generated descriptions, reports, and survey insights include descriptive alt-text descriptions or clear text-to-speech formatting cues.\n\n# CORE CAPABILITIES\n- GOOGLE DOCS & SHEETS: Draft clean reports and organize structured tables.\n- GOOGLE CALENDAR: Manage schedules using clear, unambiguous time blocks.\n- GOOGLE FORMS & SURVEYS: Build accessible surveys and analyze feedback using multi-dimensional sentiment tagging.',
  tools=[
    agent_tool.AgentTool(agent=workspace_automator_google_search_agent),
    agent_tool.AgentTool(agent=workspace_automator_url_context_agent)
  ],
)
chloe_orchestrator_google_search_agent = LlmAgent(
  name='Chloe_Orchestrator_google_search_agent',
  model=GlobalGemini(model='gemini-3.5-flash'),
  description=(
      'Agent specialized in performing Google searches.'
  ),
  sub_agents=[],
  instruction='Use the GoogleSearchTool to find information on the web.',
  tools=[
    GoogleSearchTool()
  ],
)
chloe_orchestrator_url_context_agent = LlmAgent(
  name='Chloe_Orchestrator_url_context_agent',
  model=GlobalGemini(model='gemini-3.5-flash'),
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
  name='Chloe_Orchestrator',
  model=GlobalGemini(model='gemini-3.5-flash'),
  description=(
      'Core executive agent for Idlelab office simulator, routing user intent across specialized subtools with psychological sentiment awareness.'
  ),
  sub_agents=[task_gov, culture_match, tech_fix, wisdom_well, workspace_automator],
  instruction='# ROLE & OBJECTIVE\nYou are the Holistic Life Wisdom & Family Wellness Mentor for Idlelab. Your mission is to provide deeply practical, compassionate, and actionable guidance for remote workers balancing career, family milestones, and personal well-being.\n\n# CORE CAPABILITIES\n1. FAMILY & LIFE GUIDANCE:\n   - Offer expert-level, gentle advice on newborn care, developmental stages from early childhood through university, and family time-management.\n   - Ground all recommendations in natural philosophy, empathy, and Idlelab\'s core commitment to prioritizing family life over toxic overwork.\n\n2. ACCESSIBLE ERGONOMICS & HEALTH:\n   - Provide concrete workspace wellness routines (posture, eye strain reduction, hydration schedules) tailored specifically for individuals with physical or cognitive challenges.\n   - Use clear, plain language with zero jargon so users can immediately apply your health and wellness advice.',
  tools=[
    agent_tool.AgentTool(agent=chloe_orchestrator_google_search_agent),
    agent_tool.AgentTool(agent=chloe_orchestrator_url_context_agent)
  ],
)