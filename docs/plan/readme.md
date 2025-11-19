# Glimmer Development Plan & Tasks

This document outlines the development plan for Glimmer, broken down into epics, stories, and tasks. This will serve as
our TODO list, with the goal of creating small, feature-complete commits.

---

### Epic 1: Backend Migration to Java Spring Boot

_Goal: Replace the Python FastAPI backend with a scalable, robust Java Spring Boot 3 application (Java 21)._

**Story: Project Scaffolding & Setup**

- [x] Task: Initialize a new Spring Boot project in `apis/` (Java 21, Maven, Spring Web, JPA, PostgreSQL, Flyway, Validation).
- [x] Task: Configure Maven build scripts and dependencies.
- [ ] Task: Configure Docker Compose to include the new Java backend service.
- [ ] Task: Set up code formatting (Spotless with Google Java Format).

**Story: Domain Migration**

- [x] Task: Port User, Project, and ConversationHistory entities to JPA (`@Entity`).
- [ ] Task: Port Pre-Production Bucket entities (`Character`, `Screenplay`, etc.) to JPA.
- [ ] Task: Port Production/Post-Production entities (`Assembly`, `RenderJob`) to JPA.
- [x] Task: Create Flyway migration scripts to replicate the current schema.

**Story: API Implementation**

- [x] Task: Implement `UserController` and `ProjectController` (REST API parity with Python).
- [x] Task: Implement Service layer logic for Users and Projects.
- [x] Task: Configure Exception Handling (GlobalExceptionHandler).

---

### Epic 2: CLI Migration to Java

_Goal: Rewrite the CLI tool in Java to maintain a single-language backend ecosystem._

**Story: Java CLI Setup**

- [ ] Task: Initialize a new module or project for the CLI (e.g., using Spring Shell or Picocli).
- [ ] Task: Implement the `projects` command group (list, create) in Java.
- [ ] Task: Implement the `users` command group in Java.
- [ ] Task: Set up a build task to produce an executable JAR or native binary.

---

### Epic 3: Web Frontend - The Creative Studio

_Goal: Develop the user-facing web application. (Frontend remains TypeScript/Next.js)._

**Story: User Authentication & Project Dashboard**

- [x] Task (Legacy Backend): Implement CRUD API endpoints for `Users` and `Projects`.
- [x] Task (Legacy CLI): Implement `projects` command group via API.
- [ ] Task (Java Backend): Re-verify Frontend integration with new Java API.
- [ ] Task: Set up Google OAuth 2.0 credentials.
- [ ] Task (Frontend): Implement "Login with Google".
- [ ] Task (Frontend): Create project dashboard.

---

### Epic 4: Core AI Agent Framework (Java)

_Goal: Build the backend infrastructure for the CUI using Java and Spring AI/LangChain4j._

**Story: CUI Orchestrator & Agent Invocation**

- [ ] Task: Implement the main CUI endpoint in Spring Boot (WebSocket/SSE).
- [ ] Task: Develop the core Orchestrator service using Java AI libraries.
- [ ] Task: Implement Function Calling mechanism in Java.

**Story: Creative Agents**

- [ ] Task: Implement specialized Agent services in Java (Character, Screenplay, Audio, etc.).

---

### Epic 5: Production & Export

_Goal: Build assembly and export functionality._

**Story: Assembly & Export**

- [ ] Task: Implement Assembly logic in Java.
- [ ] Task: Integrate video processing (FFMPEG) via Java ProcessBuilder or wrapper library (e.g., Jave2).
- [ ] Task: Implement Job Queue for rendering (using Spring Boot + Redis/RabbitMQ).

---

### [Deprecated] Python Assets

_The `api/` and `cli/` (Python) directories are now deprecated and will be removed once the Java migration is complete._
