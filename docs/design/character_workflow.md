# Workflow: Character Development

This document outlines the user workflow for creating a new character.

1.  **Initiation:** The user starts a "New Character" session either from the GUI or contextually during another session (like screenwriting).

2.  **The Seed:** The CUI prompts the user for a simple, high-level description of the character.

3.  **First Draft:** The `CharacterAgent` is invoked. It generates a preliminary character sheet including an archetype, appearance, personality traits, and a suggested backstory.

4.  **Iterative Refinement:** The user refines the character through conversation. They can ask for changes to personality, motivation, or other details. The Agent updates the character sheet with each request.

5.  **Visual Generation:** Once the textual description is finalized, the CUI prompts the user to generate concept art. The `CharacterAgent` uses the full character sheet as a detailed prompt for an image generation model, creating several visual options.

6.  **Finalization:** The user selects a final concept image. The CUI confirms the session is complete and the `CharacterAgent` saves the final, complete character sheet (text and image) to the project's "Character Bucket". The character can optionally be made shareable across other projects.
