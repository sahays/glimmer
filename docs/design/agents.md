# Agent Implementation

This document describes the technical implementation of Agents in the Glimmer platform.

### The Two-Layer AI Model

1.  **CUI Orchestrator:** The primary, user-facing Gemini model.
    - Its role is to understand user intent and select the appropriate tool (Agent) to call.
    - It uses Gemini's **Function Calling** feature to delegate tasks.

2.  **Specialist Agents:** Backend modules that execute specific tasks.
    - These are not chatbots; they are functions (e.g., Python code) that are called by the backend.
    - Each Agent contains a highly specialized, detailed prompt for its specific task.
    - It makes its own, independent call to the Gemini API to generate its creative output.

### Invocation Flow

1.  User sends a prompt to the CUI.
2.  The CUI Orchestrator matches the intent to a registered tool and returns a `tool_calls` object.
3.  The backend receives this object and executes the corresponding Agent function.
4.  The Agent function builds its specialized prompt, calls the Gemini API, parses the result, and may interact with the database.
5.  The Agent returns its result to the backend.
6.  The backend sends the result back to the CUI Orchestrator, which then formulates a natural language response for the user.
