# Workflow: Screenplay Development

This document outlines the workflow for writing a screenplay, focusing on how it handles the interdependence of plot and character.

### The "Catch-22" Solution

The `ScreenplayAgent` is designed to handle characters dynamically.
- **Placeholder Recognition:** It identifies any capitalized name before dialogue as a character.
- **Automatic Linking:** If the character exists in the "Character Bucket," it links to their profile to inform their dialogue.
- **In-Session Creation:** If the character is new, the CUI pauses the session and prompts the user to quickly define them. This allows for a "write-first, detail-later" creative process.

### Writing Workflow

1.  **Initiation:** The user starts a "New Screenplay" session.

2.  **Structural Blueprint:** Based on the user's story idea, the `ScreenplayAgent` first proposes a high-level structural blueprint (e.g., a 3-act structure, a scene list). This ensures the story has a solid foundation before diving into details.

3.  **Scene-by-Scene Generation:** The user directs the agent to write the script scene by scene. The agent generates action descriptions and dialogue, using the profiles of known characters to keep their voice consistent.

4.  **Dialogue & Pacing Workshop:** The user refines the generated script via conversational commands. They can ask the agent to make dialogue more impactful, adjust the pacing of a scene to fit a specific duration, or add action beats.

5.  **Finalization:** Once the script is complete, the `ScreenplayAgent` saves it to the "Screenplay Bucket" as a structured data object, ready for the Storyboard Agent.
