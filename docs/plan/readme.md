# Glimmer Development Plan & Tasks

This document outlines the development plan for Glimmer, broken down into epics, stories, and tasks. This will serve as
our TODO list, with the goal of creating small, feature-complete commits.

---

### Epic 1: Project Foundation & Setup

_Goal: Establish a robust and scalable monorepo structure with all necessary boilerplate for the backend, frontend, and
CLI._

**Story: Initial Project Scaffolding**

- [x] Task: Set up the monorepo directory structure (`api/`, `web/`, `cli/`).
- [x] Task: Initialize the Python backend project (FastAPI) in `api/`.
- [x] Task: Define frontend tech stack spec (Next.js, TypeScript, Tailwind, shadcn/ui, lucide-react, Zustand, TanStack Query, React Hook Form, Zod).
- [x] Task: Initialize the Next.js frontend project in `web/` using the defined tech stack.
- [x] Task: Initialize the Python CLI project (Typer) in `cli/`.
- [x] Task: Add basic configuration for linters and formatters (e.g., Ruff, Prettier) with pre-commit hooks.
- [x] Task: Create a root `README.md` explaining the project structure and setup instructions.

**Story: Formal Project Documentation**

- [x] Task: Create `docs/design/tech_stack.md` detailing the full tech stack (backend, frontend, and tooling).
- [x] Task: Update `docs/design/architecture.md` with the expanded pipeline and Worker architecture.
- [x] Task: Create `docs/design/principles.md` outlining the core development philosophies.
- [x] Task: Create `docs/TESTING_STRATEGY.md` outlining the pyramid approach (Unit, Integration, E2E).

**Story: Database & Expanded Core Models**

- [x] Task: Set up database solution using Postgres with SQLAlchemy ORM.
- [x] Task: Define initial database models for `Project`, `User`, and `ConversationHistory`.
- [x] Task: Define models for Pre-Production Buckets: `Character`, `Screenplay`, `Prompt`, `Audio`, `Video`, `Music`.
- [x] Task: Define model for the Production Bucket: `Assembly` (timeline/sequence data).
- [x] Task: Define model for Post-Production: `RenderJob` (to track export progress and final output).
- [x] Task: Implement initial database migration scripts (e.g., using Alembic).

**Story: Containerization & Deployment Scripts**

- [ ] Task: Create `Dockerfile` for the FastAPI backend (`api/`).
- [ ] Task: Create `Dockerfile` for the React frontend (`web/`).
- [ ] Task: Create `docker-compose.yml` for local development (api, web, postgres, memorystore/redis).
- [ ] Task: Write deployment scripts for Cloud Run with clear environment separation (e.g., `.env.dev`, `.env.prod`).
- [ ] Task: Document the local setup and production deployment process.

**Story: Testing Framework Setup**

- [ ] Task: Set up `pytest` for the backend, including utilities for managing a test database.
- [ ] Task: Set up `Vitest` and `React Testing Library` for frontend component and integration tests.
- [ ] Task: Set up `Playwright` for critical-path E2E tests.

**Story: API Security & Configuration**

- [ ] Task: Configure CORS middleware in FastAPI to allow requests from the frontend origin.
- [ ] Task: Implement IP-based rate limiting for API endpoints, with stricter limits on AI-related routes.
- [ ] Task: Add a basic honeypot field to user input forms as a simple bot detection measure.

**Story: Cloud Integration & Asset Storage**

- [ ] Task: Set up a Google Cloud Storage (GCS) bucket for asset storage.
- [ ] Task (Backend): Implement an API endpoint to generate GCS pre-signed URLs for secure file uploads.
- [ ] Task (Frontend): Implement client-side logic to fetch pre-signed URLs and upload files directly to GCS.
- [ ] Task (Database): Update asset models (`Audio`, `Video`, etc.) to store a GCS object key instead of file data.

---

### Epic 2: Core AI Agent Framework

_Goal: Build the backend infrastructure for the CUI, including the main orchestrator and a full suite of specialist
agents._

**Story: CUI Orchestrator & Agent Invocation**

- [ ] Task: Implement the main CUI endpoint in the FastAPI backend (e.g., via WebSocket).
- [ ] Task: Develop the core logic for receiving user prompts and calling the Gemini API (the Orchestrator).
- [ ] Task: Implement the function calling/tool use mechanism to delegate tasks to agent modules.
- [ ] Task: Implement the logic for saving all conversation history to the database.

**Story: Prompt Management & AI Observability**

- [ ] Task: Design and implement a file-based Prompt Registry to decouple prompts from code.
- [ ] Task: Implement structured logging across the entire CUI request lifecycle.
- [ ] Task: Create a mocking service/module for the Gemini API to enable robust integration testing.

**Story: Creative Agents (Pre-Production)**

- [ ] Task: Implement `CharacterAgent` for character sheet and concept art generation.
- [ ] Task: Implement `ScreenplayAgent` for screenplay blueprinting and scene writing.
- [ ] Task: Implement `AudioAgent` for generating voice-overs or simple sound effects.
- [ ] Task: Implement `MusicAgent` for generating mood-based background music.
- [ ] Task: Implement `VideoAgent` for generating short video clips or storyboards.
- [ ] Task: Write unit tests for agent data parsing and validation logic (using mocked AI responses).
- [ ] Task: Register all new agent tools with the CUI Orchestrator.

---

### Epic 3: Web Frontend - The Creative Studio

_Goal: Develop the user-facing web application, including the conversational interface and the asset management views._

**Story: User Authentication & Project Dashboard**

- [ ] Task: Set up Google OAuth 2.0 credentials in Google Cloud Console for local development (using `localhost`).

- [ ] Task (Backend): Implement the Google OAuth callback endpoint, token validation, and JWT session creation.

- [ ] Task (Frontend): Implement the "Login with Google" button and the client-side authentication flow.

- [ ] Task: Create a project dashboard to view, create, and delete projects.

- [ ] Task: Write E2E test for the complete user sign-up and project creation flow.

**Story: The Conversational UI (Session View)**

- [ ] Task: Build the main chat interface component in React.
- [ ] Task: Implement the WebSocket connection to the backend CUI endpoint.
- [ ] Task: Implement rendering for assistant messages, user messages, and tool interaction statuses.
- [ ] Task: Implement UI for displaying all generated asset types (text, images, audio, video).
- [ ] Task: Write integration tests for the chat component's state management.

**Story: The Asset Buckets (GUI View)**

- [ ] Task: Create a GUI view for the `Character` Bucket.
- [ ] Task: Create a GUI view for the `Screenplay` Bucket.
- [ ] Task: Create a GUI view for the `Prompt` Bucket.
- [ ] Task: Create GUI views for `Audio`, `Video`, and `Music` Buckets, including media players.
- [ ] Task: Implement basic CRUD functionality for all assets directly from the GUI.
- [ ] Task: Write component tests for the main Bucket UI components.

---

### Epic 4: Production - The Assembly Room

_Goal: Build the functionality to combine pre-production assets into a coherent sequence or timeline._

**Story: Assembly Agent (Backend)**

- [ ] Task: Create the `AssemblyAgent` module in the backend.
- [ ] Task: Develop logic for the agent to create a draft assembly by sequencing assets based on the screenplay.
- [ ] Task: Implement the API endpoints for the GUI to manage assemblies (CRUD operations).
- [ ] Task: Write integration tests for the assembly API endpoints.

**Story: Assembly Editor (Frontend)**

- [ ] Task: Design and build the Assembly view, a timeline-based editor.
- [ ] Task: Implement drag-and-drop functionality to add/reorder assets from the buckets onto the timeline.
- [ ] Task: Implement logic to save the state of the assembly back to the server.

---

### Epic 5: Post-Production & Export

_Goal: Provide tools to render the final product and export it for use in external applications._

**Story: Post-Production Service (Backend)**

- [ ] Task: Design and document the dedicated Worker architecture for background rendering jobs.
- [ ] Task: Create the `PostProductionAgent` to handle export jobs.
- [ ] Task: Integrate a backend video processing library (e.g., FFMPEG).
- [ ] Task: Implement the logic to take an `Assembly` model and render it into an MP4 video file (executed by the
      Worker).
- [ ] Task: Implement a job queue (using Redis) to communicate between the API and the Worker.
- [ ] Task: Implement API endpoints to start an export job and check its status.
- [ ] Task: Write integration tests for the API-to-Worker job queue mechanism.

**Story: Export & Render Management (Frontend)**

- [ ] Task: Implement a "Render" button in the Assembly view.
- [ ] Task: Create a GUI view to see the list of `RenderJobs`, their status (pending, rendering, complete, failed), and
      a link to download the final video.
