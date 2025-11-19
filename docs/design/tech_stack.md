# Glimmer Tech Stack

This document provides a comprehensive overview of the technologies, frameworks, and libraries used across the Glimmer monorepo. The primary goal of this stack is to enable high developer velocity, maintainability, and a robust, scalable architecture suitable for enterprise development.

---

## Backend (`apis/`)

The backend is a pure Java application responsible for AI agent orchestration, business logic, and data persistence.

- **Framework:** **Spring Boot 3.x**
  - **Why:** The industry standard for building production-grade applications with dependency injection and robust ecosystem support.
- **Language:** **Java 21**
  - **Why:** The latest LTS release, offering features like Virtual Threads (Project Loom) for high-concurrency AI orchestration.
- **Build Tool:** **Maven**
  - **Why:** The stable, industry-standard build automation tool for Java projects.
- **Database ORM:** **Hibernate / JPA**
  - **Why:** The standard for Java object-relational mapping.
- **Database Migrations:** **Flyway**
  - **Why:** Robust version control for database schemas.
- **AI Integration:** **Spring AI** or **LangChain4j**
  - **Why:** To interface with Gemini and other LLMs directly from the Java backend, replacing Python scripts.

---

## Frontend (`web/`)

The frontend is a modern web application built for a rich, interactive user experience.

- **Framework:** **Next.js** (React)
- **Language:** **TypeScript**
- **Styling:** **Tailwind CSS**
- **UI Components:** **shadcn/ui**
- **State Management:** **Zustand** & **TanStack Query**

---

## Command-Line Interface (`cli/`)

The CLI is a Java-based tool for developers and power users.

- **Framework:** **Spring Shell** or **Picocli**
  - **Why:** powerful frameworks for building CLI applications in the Java ecosystem.
- **Distribution:** **JBang** or **GraalVM Native Image**
  - **Why:** To provide a single-binary or easy-to-run experience without requiring complex setup.

---

## Monorepo Tooling & Standards

- **Code Formatter (Java):** **Spotless (Google Java Format)**
- **Code Formatter (Frontend):** **Prettier**
- **Containerization:** **Docker** (Multi-stage builds for Java)
