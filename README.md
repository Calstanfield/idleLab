 **IdleLab© — Autonomous 3D Agentic Spatial Virtual Office Workspace** 

**Developed by:** Benz-Carlton 

**Contact:** benzcarltonheinz@gmail.com  

**Test Link:** [idleLab AI Studio](https://idlelab-benzcarlton.ai.studio/)

**Creation Date:** August 6th 2026 

**IdleLab** is an interactive, spatial 3D WebGL virtual office workspace powered by an autonomous multi-agent cloud architecture. Driven by **Gemini 3.5 Flash**, the `@google/genai` TypeScript SDK, and **Google Cloud Firestore**, IdleLab transforms distributed remote work into a dynamic, real-time collaboration ecosystem where autonomous AI colleagues handle document orchestration, meeting facilitation, code governance, and workplace wellness.

---

## 🏛️ Systemic Agentic Cloud Logic & Architecture

IdleLab is engineered with an enterprise-grade cloud-native multi-agent architecture combining real-time bidirectional WebSocket synchronization, server-side Gemini orchestration, and Google Cloud Firestore persistence.

```mermaid
graph TD
    %% Core Entities
    Client[("💻 IdleLab Client (React / WebGL)")]
    Express["⚙️ Express Backend (Port 3000)"]
    WSS["🔌 WebSocket Sync Server"]
    Gemini["🧠 Gemini 3.5 API (@google/genai)"]
    Firestore[("🗄️ Google Cloud Firestore")]
    Agents["🤖 Multi-Agent Router (TaskGov, TechFix, etc.)"]

    %% Connections - Client to Server
    Client -- "REST API (Tasks, Docs, Votes)" --> Express
    Client -- "Real-Time Avatar/Room Sync" <--> WSS
    
    %% Connections - Server to Services
    Express -- "Dispatch Commands" --> Agents
    Express -- "Persist Agent Memory & State" --> Firestore
    WSS -- "Broadcast Agent Actions" --> Client
    
    %% Connections - Agent to LLM
    Agents -- "Prompt & Context Payload" --> Gemini
    Gemini -- "Structured JSON Schema / Sub-Agent Execution" --> Agents

    %% Subgraphs for Organization
    subgraph "Frontend Layer"
        Client
    end

    subgraph "Backend Infrastructure"
        Express
        WSS
        Agents
    end

    subgraph "External Cloud Services"
        Gemini
        Firestore
    end
```

### 1. Cloud Agent Control Bus (`/api/agent-command`)
- **Centralized Dispatching:** External clients, automated CI/CD webhooks, or workspace users dispatch structured actions (`NAVIGATE_TO_DESK`, `PROJECT_DISPLAY`, `START_MEETING`, `SUMMARIZE_DOCUMENT`, `CONDUCT_VOTE`, `SET_MOOD_AUDIO`, `EXECUTE_SUB_AGENT`).
- **Google Cloud Firestore Persistence:** Every agent interaction, tool invocation, and decision path is logged to the `agent_memory` collection via `logAgentActivity`, preserving context across sessions.
- **WebSocket Broadcast (`CLOUD_AGENT_COMMAND`):** Synchronizes agent actions across all connected 3D spatial clients in real time.

---

## 🤖 Chloe Becker — Primary Executive AI Agent & Orchestrator

Located at the **B1 Executive Data Center & Theater**, **Chloe Becker** is an autonomous AI colleague equipped with contextual awareness, real-time spatial head tracking, and a specialized fleet of 5 sub-agents:

### The 5 Specialized Sub-Agents:
1. **🛡️ TaskGov (Task Governance & Accountability Lead):**
   - Validates sprint milestones and predicts roadmap delivery dates.
   - Generates automated, itemized rubric grading criteria with XP and salary token rewards.
2. **🤝 CultureMatch (Workplace Culture & Team Alignment Specialist):**
   - Resolves cross-functional jargon, slang, and cultural misunderstandings using the *Define → Search → Discuss* framework.
   - Enforces psychological safety and team harmony metrics.
3. **⚡ TechFix (Technical Architecture & Diagnostics Supervisor):**
   - Monitors live client/server telemetry and diagnostic logs.
   - Automatically formats bug reports and generates structured debug payloads for Gemini.
4. **🧘 WisdomWell (Executive Strategic Wisdom & Health Coach):**
   - Tracks screen time and triggers ergonomic hydration / Pomodoro breaks every 30 minutes.
   - Provides strategic executive decision coaching and burn-out prevention.
   - Operates a non-intrusive hydration reminder engine with customizable intervals (default 5-minute alerts) directly configurable in Settings.
5. **⚙️ WorkspaceAutomator (Workflow Execution Specialist):**
   - Extracts actionable tasks from transcripts and meeting discussions.
   - Synchronizes shared team checklists and generates concise end-of-meeting summaries.

### Spatial Awareness & Voice Synthesis:
- **Proximity Gaze Engine:** Uses vector arithmetic to calculate yaw/pitch relative to the player, maintaining Pixar-style eye contact and blinking.
- **Neural TTS:** Powered by **ElevenLabs Multilingual v2** (`EXAVITQu4vr4xnSDxMaL`) with instant fallback to the Web Speech API.


---

## 💼 Claire Wang — 2F Executive Boardroom Facilitator

Situated in the **2nd Floor Executive Boardroom**, **Claire Wang** directs formal organizational governance:
- **8K Screen Stream Interception:** Analyzes live presenter slide decks and meeting transcripts.
- **Participant Alignment Scorecard (0–100):** Evaluates presentation clarity and partnership suitability.
- **Consensus Voting Pipeline:** Orchestrates real-time board member ballots (Approve, Revise, Reject) and records official meeting minutes.

---

## 🚀 Multiworkspace Tab & Integration Suite

The **AgentFlow Multiworkspace Modal** is the central productivity hub:
- **6 Persona Categories:** Instant configuration for *Remote Work*, *Academic Research*, *Content Creation*, *Forum Moderation*, *Small Business*, and *Live Streaming*.
- **Cross-Session Document Analysis:** Attach markdown, PDF, or text files for instant AI document ingestion and contextual querying.
- **Live System Telemetry:** Inspect sub-agent execution logs, tool invocations, and token latency.
- **Interactive Task Checklist:** Add, complete, and delete sprint goals with automatic local storage and cloud persistence.
- **Gamified Level & XP Progression:** Earn experience points, salary credits, and achievement badges for passing automated Chloe grading rubrics.

---

## 🎮 3D Spatial Environment & Physical Mechanics

- **Basement B1:** Chloe Becker's AI Data Center, 8-Server Rack Cluster, and Championship Tennis Court (with Dolly Bot, Fireball Smashes, Topspin physics, and Wall Scoreboards).
- **1st Floor (Main Floor):** Open-plan developer workstations, Barista Coffee Robot, Ping Pong table arena, and Whiteboard brainstorm area.
- **2nd Floor:** Executive Boardroom with Claire Wang, 12-seat conference table, presentation projectors, and voting terminals.
- **3rd Floor:** Sunlight Study Cafe, rooftop glass garden, ambient study soundscapes, and relaxing focus stations.
- **Kinematic Rule Enforcement:**
  - Avatar ping pong paddle is strictly restricted to the 1st Floor table zone.
  - Avatar tennis racquet and swing animations are strictly restricted to the B1 Tennis Court.

---
## 🛠️ Devpost "Setme" Quickstart Instructions

**Step 1: Repository Setup and Required Assets**
* Clone the repository locally:
  ```bash
  git clone [https://github.com/Calstanfield/idleLab.git](https://github.com/Calstanfield/idleLab.git)
  cd idleLab
**Ensure you have downloaded and placed the following required architecture archives and orchestrators directly inside your working directory:**

- idlelab (Autonomous 3D Agentic Spatial Virtual Office Workspace).zip: Contains the full spatial frontend and backend workspace assets.
- multiagent-workspace_terraform_code_2026-08-23T09_48_59Z.zip: Houses the infrastructure-as-code files to spin up the cloud network.
- agentic.py: The autonomous core orchestration script that runs multi-agent reasoning, decision loops, and tool execution routines.

**Step 2: Provisioning Multi-Agent Architecture on Google Cloud Console**
- Log in to the Google Cloud Console, create a new dedicated project, and enable billing.
- Enable core APIs including Cloud Run, Artifact Registry, and Vertex AI.
- Unzip multiagent-workspace_terraform_code_2026-08-23T09_48_59Z.zip and run your Terraform GCP deployment pipeline to provision the cloud infrastructure and routing meshes.
- Configure IAM roles and service accounts to allow secure container communication across Cloud Run instances.

**Step 3: Wiring the Simulator to the Cloud (agentic.py)** 
- Open agentic.py and configure the environment bindings to point your local simulation or container instance to your deployed GCP project endpoints.
- Establish the Autonomous Office Mesh (AOM) communication layer so that 3D physical coordinates, agent states, and event telemetry synchronize between local execution and cloud workers.
- Pass your active Gemini API credentials into the runtime environment to power the Governed Agent Topology (GAT) security and fallback layers.

**Step 4: Environment Variables Configuration**
- Create a .env file in your root workspace directory with the following configuration keys:
  ```Code snippet
   GEMINI_API_KEY=your_google_ai_studio_api_key
   GCP_PROJECT_ID=your_gcp_project_id
   PORT=8080
   CLOUD_RUN_ENDPOINT=your_cloud_run_service_url

**Step 5: Running, Testing, and Deploying**
- Install local project dependencies:
  ```Bash
   npm install
- Spin up the app locally to test spatial mechanics and agent responses:
  ```Bash
   npm run start
- Build and deploy your containers to production on Google Cloud Run:
  ```Bash
     npm run build


## 🗺️ Guided Tour for Judges & Reviewers

**Controls & Navigation:**
* 1. If you feel stuck, use your mouse to click in any direction to smoothly move your avatar around the office.
* 2. Click and drag your mouse to rotate and adjust your camera view, just like Roblox.
* 3. Use the navigation toolbar to click the left and right panels, just like in Figma.
* 4. Press E on any floor to instantly hop on a scooter for a fast joy ride across the map.
* 5. Avatar Customization: Click on settings inside the navigation tool to customize your avatar's appearance to your liking.
* 6. 💡 To test Claire Wang as your collaborative assistant, go to the 2nd floor (2F) and wave at or approach her.
* 7. 🎾 Tennis Court Tip: When playing at the tennis court on Floor B1, press the **Spacebar** if you want to smash the ball!

**Floor Tour:**

**Floor B1: Agentic Suite**
  * Explore the server rack cluster and task center. 
 
**Floor 1: Entry Hub**
  * The starting zone where you spawn directly into the virtual workspace upon login.

**Floor 2: Meeting Room & Claire Wang**
  *💡 Meet Claire Wang from the second floor. Approach or wave at her to initialize presentation streams, view participant alignment scores, conduct executive votes, and cast live camera feeds or external tabs onto office monitors.

**Floor 3: Cafeteria**
  * A scenic lounge for online coffee chats  
