# Glimmer

Glimmer is a creative studio powered by generative AI. It uses a hybrid Conversational UI (CUI) and Graphical UI (GUI) to facilitate the creation of complex media projects, from screenplays to final video productions.

## Project Structure

This project is a monorepo containing three distinct applications:

- `apis/`: The core backend written in **Java (Spring Boot)**. It handles the AI agent orchestration, database interactions, and serves the primary API for the web frontend.

- `web/`: The frontend application built with **Next.js**. This is the main user interface for interacting with the Glimmer studio.

- `cli/`: A command-line interface written in **Java (Picocli)**. It provides utility scripts and direct access to backend services for power users and developers.

## Design & Documentation

This project is guided by a set of core design and planning documents. For a deeper understanding of the project's architecture, principles, and tech stack, please refer to the following:

- [**Architecture Overview**](./docs/design/architecture.md): A high-level look at the system's structure and data flow.

- [**Development Principles**](./docs/design/principles.md): The core philosophies that guide our development process.

- [**Tech Stack**](./docs/design/tech_stack.md): A complete list of the technologies and libraries used in the project.

- [**Testing Strategy**](./docs/testing-strategy.md): Our approach to ensuring code quality and reliability.

## Prerequisites

Before you begin, ensure you have the following installed:

- **Java 21+**: JDK 21 is required for the backend and CLI. Recommended distribution: [Eclipse Temurin](https://adoptium.net/).
- **Node.js 20.x+**: Required for the frontend. Manage with `nvm` if possible.
- **Git**: For version control.
- **PostgreSQL**: A local running instance (or Docker container).

## Development Setup

Follow these steps to get your local development environment set up and running.

### 1. Clone the Repository

```bash
git clone <repository-url>
cd glimmer
```

### 2. Configure Environment

Create a `.env` file in the project root with your database credentials:

```properties
DATABASE_URL=jdbc:postgresql://localhost:5432/glimmer
DB_HOST=localhost
DB_PORT=5432
DB_NAME=glimmer
DB_USERNAME=postgres
DB_PASSWORD=your_password
```

### 3. Run the Backend API

Use the helper script to start the backend (this automatically loads your `.env` variables):

```bash
./scripts/start_apis.sh
```

The API will be available at `http://localhost:8000`.

### 4. Run the CLI

You can build and run the CLI using the helper script:

```bash
./scripts/run_cli.sh --help
# Example: ./scripts/run_cli.sh users list
```

### 5. Run the Web Frontend

```bash
cd web
npm install
npm run dev
```

The web application will be available at `http://localhost:3000`.

### Database Reset

If you need to reset the database (clean and re-migrate), use:

```bash
./scripts/fix_db_migration.sh
```

## Pre-Commit Hooks

To ensure code quality, install the pre-commit hooks:

```bash
brew install pre-commit # macOS
pre-commit install
```
