# Glimmer Tech Stack

This document provides a comprehensive overview of the technologies, frameworks, and libraries used across the Glimmer monorepo. The primary goal of this stack is to enable high developer velocity, maintainability, and a robust, scalable architecture.

---

## Backend (`api/`)

The backend is a Python-based application responsible for AI agent orchestration, business logic, and data persistence.

- **Framework:** **FastAPI**
  - **Why:** For its high performance, asynchronous support, and automatic data validation and documentation powered by Pydantic.
- **Language:** **Python 3.14+**
  - **Why:** A modern, widely-supported language with a rich ecosystem for AI and web development.
- **Database ORM:** **SQLAlchemy**
  - **Why:** A powerful and flexible ORM that provides a robust abstraction layer for interacting with our relational database.
- **Database Migrations:** **Alembic**
  - **Why:** The standard, powerful migration tool for SQLAlchemy, allowing for version-controlled database schema changes.

---

## Frontend (`web/`)

The frontend is a modern web application built for a rich, interactive user experience.

- **Framework:** **Next.js**
  - **Why:** A full-stack React framework that provides a robust foundation with server-side rendering, a file-based router, and API routes, enabling both performance and scalability.
- **Language:** **TypeScript**
  - **Why:** For strict type safety, which improves code quality, maintainability, and developer experience.
- **Styling:** **Tailwind CSS**
  - **Why:** A utility-first CSS framework that enables rapid UI development and ensures a consistent, scalable design system.
- **UI Components:** **shadcn/ui**
  - **Why:** A collection of beautifully designed, accessible, and unstyled components that can be easily customized and composed.
- **Icons:** **Lucide React**
  - **Why:** A clean, consistent, and highly customizable icon library.
- **State Management:** **Zustand**
  - **Why:** A lightweight and unopinionated state management solution that is simple to use and scales effectively without excessive boilerplate.
- **Server State & Data Fetching:** **TanStack Query (React Query)**
  - **Why:** The industry standard for managing server state, simplifying data fetching, caching, and synchronization.
- **HTTP Client:** **axios**
  - **Why:** A reliable and easy-to-use promise-based HTTP client for making requests to the backend API.
- **Form Management:** **React Hook Form**
  - **Why:** For building performant and flexible forms with a hook-based API that minimizes re-renders.
- **Form Validation:** **Zod**
  - **Why:** A TypeScript-first schema declaration library for robust, type-safe validation of forms and data structures.

---

## Command-Line Interface (`cli/`)

The CLI provides a set of tools for developers and power users to interact with the Glimmer backend directly.

- **Framework:** **Typer**
  - **Why:** For its simplicity, ease of use, and powerful features for building robust command-line applications, built on top of Click.
- **Rich Terminal Output:** **Rich**
  - **Why:** A library for beautiful formatting in the terminal, making the CLI output more readable and user-friendly.

---

## Monorepo Tooling & Standards

These tools are used at the root level of the project to ensure code quality and consistency across all applications.

- **Code Formatter (Python):** **Ruff Format**
  - **Why:** An extremely fast and comprehensive formatter that ensures a consistent code style.
- **Linter (Python):** **Ruff**
  - **Why:** An all-in-one, high-performance linter that can replace dozens of older tools, providing fast and effective code quality checks.
- **Code Formatter (Frontend):** **Prettier**
  - **Why:** An opinionated code formatter that enforces a consistent style across all frontend code (TS, TSX, CSS, JSON, etc.).
- **Automated Git Hooks:** **pre-commit**
  - **Why:** A framework for managing and maintaining multi-language pre-commit hooks, which automates the process of running linters and formatters before commits are made.
