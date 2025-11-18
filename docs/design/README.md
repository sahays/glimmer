# Glimmer Design Documentation

This directory contains the core design and architectural documents for the Glimmer platform. These documents outline the conceptual framework, agent implementation, and key user workflows.

### Core Concepts

- [**Architecture**](./architecture.md)
  - An overview of the "Sessions, Agents, and Buckets" model, which combines a Conversational UI (CUI) with a traditional GUI for asset management.

- [**Agent Implementation**](./agents.md)
  - Describes the technical details of how Agents are developed and invoked using a two-layer AI model and Gemini's Function Calling feature.

- [**Data Strategy**](./data_strategy.md)
  - Explains the importance of storing conversation history for session context, debugging, and future model fine-tuning.

### User Workflows

- [**Character Development Workflow**](./character_workflow.md)
  - Details the step-by-step conversational process for creating a new character, from an initial seed to a final, visually-realized asset.

- [**Screenplay Development Workflow**](./screenplay_workflow.md)
  - Outlines the process for writing a script, including the dynamic "catch-22" solution for handling character creation on-the-fly.
