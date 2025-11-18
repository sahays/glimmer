# Glimmer Development Principles

This document outlines the core philosophies and principles that guide the development of the Glimmer project. Adhering to these principles will ensure we build a high-quality, maintainable, and scalable application.

## Preamble: Foundational Software Engineering Principles

All code contributed to the Glimmer project should be written with the following foundational principles in mind. The goal is to create a codebase that is easy to understand, modify, and extend, thereby minimizing regressions when adding new features or making changes.

- **SOLID:** Follow the five SOLID principles of object-oriented design to create understandable, maintainable, and flexible software.
- **KISS (Keep It Simple, Stupid):** Strive for simplicity. Avoid unnecessary complexity and favor the simplest solution that effectively solves the problem.
- **DRY (Don't Repeat Yourself):** Avoid duplicating code. Abstract and reuse common logic and components to make the codebase easier to maintain and less prone to bugs.

---

### 1. Agent-First for Creation, GUI for Management

This is the core product philosophy. The initial, creative act of generation should be a fluid, conversational experience. The organization, refinement, and management of those creations are best handled through a powerful and intuitive graphical interface.

- **CUI (Conversational UI):** Used for all primary asset generation (e.g., writing scenes, creating characters, generating music). The goal is to make creation feel like a collaboration, not a task.
- **GUI (Graphical UI):** Used for everything else (e.g., browsing assets, editing details, assembling timelines, managing projects). The goal is to provide clarity, control, and a comprehensive overview.

### 2. Monorepo for Cohesion

All Glimmer code—backend, frontend, and CLI—lives in a single repository.

- **Benefits:** This approach simplifies dependency management, encourages code sharing, and ensures a consistent development experience across the entire project. It makes cross-cutting changes (e.g., updating an API contract and the frontend that consumes it) much easier to manage in a single atomic commit.

### 3. Stateless, Scalable Backend Services

The backend API should be designed to be stateless.

- **Why:** A stateless architecture is fundamental to scalability, especially in a serverless environment like Cloud Run. Each incoming request should be able to be handled by any available container instance. All persistent state must be stored in the database (Postgres) or a dedicated cache (Redis).

### 4. Secure and Performant by Design

Security and performance are not afterthoughts; they are architectural requirements.

- **Asset Handling:** We use **pre-signed URLs** for all file uploads. This ensures that large files are sent directly to cloud storage, bypassing our backend. This is more secure, highly scalable, and keeps our API responsive.
- **Asynchronous Tasks:** Heavy, long-running jobs like video rendering are handled by a **dedicated worker architecture**. This decouples the main API from intensive tasks, ensuring the user-facing application remains fast and reliable.

### 5. Pragmatic and Efficient Testing

We follow the "Testing Pyramid" model to ensure maximum confidence with the minimum maintenance overhead.

- **Unit Tests (Base):** The majority of our tests. They are fast, isolated, and verify individual functions and components.
- **Integration Tests (Middle):** Test the interaction between different parts of our system (e.g., API endpoint to database).
- **End-to-End (E2E) Tests (Peak):** A small number of high-value tests that simulate critical user journeys through the entire application.

### 6. Automate Everything That Can Be Automated

We leverage tooling to automate routine tasks, freeing up developers to focus on building features.

- **Code Quality:** **Pre-commit hooks** automatically lint and format all code before it is committed. This enforces a consistent style and catches simple errors before they ever enter the codebase.
- **Dependencies:** We maintain clear `requirements.txt` and `package.json` files to ensure that development and production environments are consistent and reproducible.
