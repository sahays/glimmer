package com.sanjeets.glimmer.cli.commands;

import com.sanjeets.glimmer.cli.client.GlimmerApiClient;
import com.sanjeets.glimmer.cli.model.CreateProjectDTO;
import com.sanjeets.glimmer.cli.model.ProjectDTO;
import java.util.List;
import java.util.UUID;
import lombok.RequiredArgsConstructor;
import org.springframework.shell.standard.ShellComponent;
import org.springframework.shell.standard.ShellMethod;
import org.springframework.shell.standard.ShellOption;
import org.springframework.shell.table.ArrayTableModel;
import org.springframework.shell.table.BorderStyle;
import org.springframework.shell.table.TableBuilder;
import org.springframework.shell.table.TableModel;

@ShellComponent
@RequiredArgsConstructor
public class ProjectCommands {

    private final GlimmerApiClient apiClient;

    @ShellMethod(key = "projects list", value = "List all projects")
    public void listProjects(
        @ShellOption(help = "Filter by Owner ID", defaultValue = ShellOption.NULL) UUID ownerId
    ) {
        try {
            List<ProjectDTO> projects = apiClient.listProjects(ownerId);
            if (projects.isEmpty()) {
                System.out.println("No projects found.");
                return;
            }

            Object[][] data = new Object[projects.size() + 1][3];
            data[0] = new Object[]{"ID", "Name", "Owner ID"};

            for (int i = 0; i < projects.size(); i++) {
                ProjectDTO p = projects.get(i);
                data[i + 1] = new Object[]{
                    p.getProjectId(),
                    p.getProjectName(),
                    p.getOwnerId()
                };
            }

            TableModel model = new ArrayTableModel(data);
            TableBuilder tableBuilder = new TableBuilder(model);
            tableBuilder.addFullBorder(BorderStyle.fancy_light);
            System.out.println(tableBuilder.build().render(80));

        } catch (Exception e) {
            System.err.println("Error fetching projects: " + e.getMessage());
        }
    }

    @ShellMethod(key = "projects create", value = "Create a new project")
    public void createProject(
        @ShellOption(help = "Project Name") String name,
        @ShellOption(help = "Owner User ID") UUID ownerId
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
