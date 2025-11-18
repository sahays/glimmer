# Glimmer System Architecture

This document provides a comprehensive overview of the Glimmer system architecture. It covers the high-level monorepo structure, the core user interaction patterns, the end-to-end data pipeline, and the backend architecture for handling asynchronous tasks.

---

## 1. Monorepo Structure

Glimmer is a monorepo that houses three distinct applications, ensuring a centralized and manageable codebase:

- **`/api`**: The core backend built with **FastAPI (Python)**. It manages business logic, AI agent orchestration, database interactions, and serves the primary API.
- **`/web`**: The frontend application built with **Next.js (TypeScript)**. This is the main user interface for the Glimmer creative studio.
- **`/cli`**: A command-line interface built with **Typer (Python)**. It provides utility scripts and direct access to backend services for development and administration.

---

## 2. The Hybrid UI Pattern: CUI + GUI

Glimmer's core design philosophy is a hybrid of a Conversational UI (CUI) for creation and a Graphical UI (GUI) for management.

### The Session: The Creative Conversation (CUI)

- The primary user interaction for creative tasks is a **Session**, a goal-oriented conversation within the CUI.
- The CUI acts as an **Orchestrator**, understanding user intent and delegating tasks to specialized backend Agents.
- This allows for a fluid, natural language-driven workflow for generating assets like characters, screenplay scenes, or music concepts.

### The Buckets: The Asset Library (GUI)

- All generated content is stored in **Buckets**, which are organized sections of the project's database (e.g., the `characters` table is the "Character Bucket").
- The Buckets are managed through a traditional **GUI**. This interface allows users to visually browse, edit, organize, and manage their assets.
- This hybrid approach provides the best of both worlds: a guided, conversational experience for creation and a powerful, visual interface for management.

---

## 3. The End-to-End Data Pipeline

The architecture is designed to support a full production workflow, from raw ideas to a final rendered video.

![Data Pipeline Flow](https://i.imgur.com/example.png) <!-- Placeholder for a real diagram -->

**a. Pre-Production (Asset Generation)**

- **Flow:** `Session (CUI) -> Agent -> Bucket (Database)`
- Users interact with the CUI to invoke **Agents** (e.g., `CharacterAgent`, `ScreenplayAgent`).
- Agents are modular, backend components that use Gemini's Function Calling to perform specific, complex tasks.
- The output of an Agent is a structured asset, which is saved into its corresponding **Pre-Production Bucket** (e.g., `characters`, `screenplays`, `music`).

**b. Production (Assembly)**

- **Flow:** `Buckets -> Assembly Editor (GUI) -> Assembly Model (Database)`
- Users move from the CUI to the GUI to work in the **Assembly Editor**.
- This is a timeline-based interface where they can sequence the assets from their Pre-Production Buckets.
- The state of this timeline is saved as an **Assembly**, which is a model that references the various assets and their arrangement.

**c. Post-Production (Rendering)**

- **Flow:** `Assembly -> Post-Production Job -> Rendered Video`
- From the Assembly Editor, a user can trigger a **Render Job**.
- This job takes the `Assembly` data and uses a backend service to render it into a final video format (e.g., MP4).
- The output is stored in a final "Render" bucket, ready for download and use in external tools.

---

## 4. Backend Worker Architecture

To handle long-running, computationally intensive tasks like video rendering without blocking the main API, we use a dedicated **Worker** architecture.

- **API Server:** The main FastAPI application's role is to be responsive. When a render job is requested, it does **not** perform the render itself. Instead, its only job is to add a new task to a **Job Queue** (e.g., using Redis).
- **Job Queue:** A message broker (like Redis) that acts as an intermediary between the API server and the Workers.
- **Worker(s):** These are completely separate processes, running independently from the API server. They constantly listen for new jobs on the queue. When a job appears, a Worker picks it up and performs the heavy lifting (e.g., running an FFMPEG process to render the video).
- **Benefits:** This decoupling is critical for scalability and reliability. The API remains fast and available, and we can scale the number of Workers independently based on the rendering workload.
