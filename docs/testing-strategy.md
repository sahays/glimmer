# Glimmer Testing Strategy

This document outlines the official testing strategy for the Glimmer project. Our goal is to build a robust and reliable application while keeping the test suite fast, effective, and easy to maintain. To achieve this, we are adopting the **Testing Pyramid** model.

---

## The Testing Pyramid

The Testing Pyramid is a model for structuring a test suite that emphasizes a healthy balance between different types of tests. It is composed of three layers:

- **Unit Tests (Base):** The largest number of tests.
- **Integration Tests (Middle):** A smaller, more focused set of tests.
- **End-to-End (E2E) Tests (Peak):** The fewest number of tests, reserved for critical user paths.

![Testing Pyramid](https://martinfowler.com/bliki/images/testPyramid/test-pyramid.png)
_(Image credit: Martin Fowler)_

---

### 1. Unit Tests (~70% of Tests)

- **What they are:** Small, focused tests that verify a single, isolated piece of functionality (e.g., one function, one React component).
- **Key Characteristics:**
  - **Isolation:** All external dependencies (databases, APIs, other services) are **mocked**. The unit under test is completely isolated from the rest of the system.
  - **Speed:** They run extremely fast, often in milliseconds. The entire unit test suite should complete in seconds.
- **Our Implementation:**
  - **Backend (`api/`, `cli/`):** We will use `pytest`. We will create mock objects to simulate database responses and external API calls (like the Gemini API).
  - **Frontend (`web/`):** We will use `Vitest` and `React Testing Library`. Components will be rendered in isolation, and any data fetching or state management dependencies will be mocked.
- **Purpose:** To form the foundation of our test suite, ensuring that the core logic of each individual part of the application is correct.

### 2. Integration Tests (~20% of Tests)

- **What they are:** Tests that verify the interaction between two or more components of our system.
- **Key Characteristics:**
  - **Partial Integration:** They do not test the entire application stack. Instead, they focus on specific integration points.
  - **Real Dependencies (where appropriate):** These tests will often interact with a real, containerized test database to ensure that our API logic and database queries work correctly together. External services (like the Gemini API) will still be mocked to keep tests deterministic and fast.
- **Our Implementation:**
  - **Backend (`api/`):** We will use `pytest` to make live HTTP requests to our API endpoints and assert that the correct data is created, retrieved, or updated in a dedicated test database (running in Docker).
  - **Frontend (`web/`):** We will test how multiple components work together. For example, we will test a form component's integration with our state management library (`Zustand`) to ensure that state is updated correctly when the form is submitted.
- **Purpose:** To catch errors at the boundaries between our system's components (e.g., API layer, database layer, UI state layer).

### 3. End-to-End (E2E) Tests (~10% of Tests)

- **What they are:** High-level tests that simulate a complete user journey through the application, from the UI to the database and back.
- **Key Characteristics:**
  - **Full Stack:** They run against a fully deployed version of the application (locally in Docker or in a staging environment).
  - **Browser Automation:** They use a tool to control a real web browser, performing actions like clicking buttons, filling out forms, and navigating between pages.
  - **Brittle and Slow:** E2E tests are the most expensive to write, run, and maintain.
- **Our Implementation:**
  - We will use **Playwright** to write a small, carefully selected suite of E2E tests.
  - These tests will only cover the most critical "happy path" user flows, such as:
    1.  User signs up and creates a new project.
    2.  User successfully generates a character via the CUI.
    3.  User can see the generated character in the GUI bucket view.
- **Purpose:** To provide a final layer of confidence that the core, critical workflows of the application are functioning correctly from a user's perspective. We will **not** aim for high E2E test coverage, as this leads to a slow and unmaintainable test suite.
