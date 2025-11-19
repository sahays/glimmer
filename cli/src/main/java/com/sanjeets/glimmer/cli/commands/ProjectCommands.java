package com.sanjeets.glimmer.cli.commands;

import com.sanjeets.glimmer.cli.client.GlimmerApiClient;
import com.sanjeets.glimmer.cli.model.CreateProjectDTO;
import com.sanjeets.glimmer.cli.model.ProjectDTO;
import java.util.List;
import java.util.UUID;
import lombok.RequiredArgsConstructor;
import org.springframework.stereotype.Component;
import picocli.CommandLine.Command;
import picocli.CommandLine.Option;

@Component
@Command(name = "projects", description = "Manage projects", mixinStandardHelpOptions = true)
@RequiredArgsConstructor
public class ProjectCommands {

    private final GlimmerApiClient apiClient;

    @Command(name = "list", description = "List all projects")
    public void list(
        @Option(names = "--owner-id", description = "Filter by Owner ID") UUID ownerId
    ) {
        try {
            List<ProjectDTO> projects = apiClient.listProjects(ownerId);
            if (projects.isEmpty()) {
                System.out.println("No projects found.");
                return;
            }
            System.out.printf("%-36s %-30s %-36s%n", "ID", "Name", "Owner ID");
            System.out.println("-".repeat(105));
            for (ProjectDTO p : projects) {
                System.out.printf("%-36s %-30s %-36s%n",
                    p.getProjectId(), p.getProjectName(), p.getOwnerId());
            }
        } catch (Exception e) {
            System.err.println("Error fetching projects: " + e.getMessage());
        }
    }

    @Command(name = "create", description = "Create a new project")
    public void create(
        @Option(names = "--name", required = true, description = "Project Name") String name,
        @Option(names = "--owner-id", required = true, description = "Owner User ID") UUID ownerId
    ) {
        try {
            CreateProjectDTO dto = new CreateProjectDTO();
            dto.setProjectName(name);
            dto.setOwnerId(ownerId);

            ProjectDTO project = apiClient.createProject(dto);
            System.out.println("Project created successfully: " + project.getProjectId());
        } catch (Exception e) {
            System.err.println("Error creating project: " + e.getMessage());
        }
    }
}
