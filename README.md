# Glimmer

Glimmer is a creative studio powered by generative AI. It uses a hybrid Conversational UI (CUI) and Graphical UI (GUI) to facilitate the creation of complex media projects, from screenplays to final video productions.

## Project Structure

This project is a monorepo containing three distinct applications:

- `api/`: The core backend written in Python with FastAPI. It handles the AI agent orchestration, database interactions, and serves the primary API for the web frontend.

- `web/`: The frontend application built with Next.js. This is the main user interface for interacting with the Glimmer studio.

- `cli/`: A command-line interface written in Python with Typer. It provides utility scripts and direct access to backend services for power users and developers.

## Design & Documentation

This project is guided by a set of core design and planning documents. For a deeper understanding of the project's architecture, principles, and tech stack, please refer to the following:

- [**Architecture Overview**](./docs/design/architecture.md): A high-level look at the system's structure and data flow.

- [**Development Principles**](./docs/design/principles.md): The core philosophies that guide our development process.

- [**Tech Stack**](./docs/design/tech_stack.md): A complete list of the technologies and libraries used in the project.

- [**Testing Strategy**](./docs/testing-strategy.md): Our approach to ensuring code quality and reliability.

## Prerequisites

Before you begin, ensure you have the following installed:

- **Python 3.14+**: It is recommended to manage Python versions with a tool like `pyenv`.
- **Node.js 20.x+**: It is recommended to manage Node versions with a tool like `nvm`.
- **Git**: For version control.
- **(macOS)** **Homebrew**: For installing dependencies like the latest Python version.

## Development Setup

Follow these steps to get your local development environment set up and running.

### 1. Clone the Repository

```bash
git clone <repository-url>
cd glimmer
```

### 2. Set Up Backend & CLI Environments

The `api` and `cli` projects each have their own Python virtual environment.

```bash
# Set up the API backend
cd api
python3.14 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
cd ..

# Set up the CLI
cd cli
python3.14 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
cd ..
```

### 3. Set Up Frontend Environment

The `web` project uses NPM for package management.

```bash
# Set up the web frontend
cd web
npm install
cd ..
```

### 4. Install Pre-Commit Hooks

This project uses pre-commit hooks to automatically format and lint code before each commit. This is a crucial one-time setup step.

```bash
# From the project root, activate one of the Python environments
cd api
source .venv/bin/activate

# Install the hooks from the root directory
cd ..
pre-commit install
```

### 5. Running the Applications

- **To run the API server:**

  ```bash
  cd api
  source .venv/bin/activate
  uvicorn main:app --reload
  ```

  The API will be available at `http://127.0.0.1:8000`.

- **To run the Web frontend:**

  ```bash
  cd web
  npm run dev
  ```

  The web application will be available at `http://localhost:3000`.

- **To use the CLI:**
  ```bash
  cd cli
  source .venv/bin/activate
  python main.py --help
  ```
