# Glimmer Architecture: Sessions, Agents, and Buckets

This document outlines the high-level architecture for Glimmer, a hybrid system combining a Conversational UI (CUI) with a traditional Graphical UI (GUI).

### 1. The Session: The Creative Conversation
- The primary user interaction for creative tasks is a **Session**, a goal-oriented conversation powered by the CUI.
- Sessions are contextual. They load relevant data from the "Buckets" (e.g., characters, plot points) to inform the conversation.
- The CUI acts as an **Orchestrator**, understanding user intent and delegating tasks to specialized Agents.

### 2. The Agents: The Specialist Tools
- **Agents** are modular, backend components that perform specific, complex tasks (e.g., character creation, scriptwriting).
- They are invoked by the CUI Orchestrator via Gemini's **Function Calling** mechanism.
- Each Agent has its own highly-tuned prompts and logic, allowing for focused and high-quality output. This makes the system scalable and easy to maintain.

### 3. The Buckets: The Asset Library
- All generated content (characters, scripts, images) is stored in **Buckets**, which are essentially organized sections of the project's database.
- The Buckets are managed through a traditional **GUI**. This interface allows users to view, edit, and manage their assets directly.
- This hybrid approach provides the best of both worlds: a guided, conversational experience for creation (Sessions) and a powerful, visual interface for management (Buckets).
