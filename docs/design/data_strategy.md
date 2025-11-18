# Data Strategy: Storing Conversations

This document outlines the strategy for storing and utilizing conversation data.

### Should We Save Conversations?

Yes. Saving all user prompts, CUI responses, and tool interactions is critical for the application's functionality and future development.

### How to Store

- Conversations will be stored in a dedicated `conversation_history` table in the database.
- Each entry will be linked to a `session_id`, `project_id`, and `user_id`.
- The schema will differentiate between user messages, assistant responses, and tool calls/results, storing structured data (like function arguments) in JSON fields.

### How to Use the Data

1.  **Session History:** To allow users to view their past conversations and resume their work.
2.  **AI Context:** To provide the CUI Orchestrator with the necessary "memory" for new sessions. Before starting a task, the relevant historical context is loaded, ensuring continuity and intelligent responses.
3.  **Debugging and Auditing:** To provide a clear, auditable trail for developers to diagnose issues with agent performance or CUI logic.
4.  **Fine-Tuning Data:** The collected data creates a valuable, high-quality dataset that can be used in the future to fine-tune a custom Gemini model for Glimmer, improving performance and efficiency.
