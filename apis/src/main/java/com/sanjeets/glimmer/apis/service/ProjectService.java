package com.sanjeets.glimmer.apis.service;

import com.sanjeets.glimmer.apis.dto.CreateProjectDTO;
import com.sanjeets.glimmer.apis.dto.ProjectDTO;
import com.sanjeets.glimmer.apis.exception.ResourceNotFoundException;
import com.sanjeets.glimmer.apis.model.Project;
import com.sanjeets.glimmer.apis.model.User;
import com.sanjeets.glimmer.apis.repository.ProjectRepository;
import com.sanjeets.glimmer.apis.repository.UserRepository;
import java.util.List;
import java.util.UUID;
import java.util.stream.Collectors;
import lombok.RequiredArgsConstructor;
import org.springframework.stereotype.Service;
import org.springframework.transaction.annotation.Transactional;

@Service
@RequiredArgsConstructor
public class ProjectService {

    private final ProjectRepository projectRepository;
    private final UserRepository userRepository;

    @Transactional(readOnly = true)
    public List<ProjectDTO> getAllProjects(UUID ownerId) {
        List<Project> projects;
        if (ownerId != null) {
            projects = projectRepository.findByOwner_UserId(ownerId);
        } else {
            projects = projectRepository.findAll();
        }
        return projects.stream().map(this::convertToDTO).collect(Collectors.toList());
    }

    @Transactional(readOnly = true)
    public ProjectDTO getProjectById(UUID id) {
        Project project = projectRepository.findById(id)
            .orElseThrow(() -> new ResourceNotFoundException("Project not found with id " + id));
        return convertToDTO(project);
    }

    @Transactional
    public ProjectDTO createProject(CreateProjectDTO createDTO) {
        User owner = userRepository.findById(createDTO.getOwnerId())
            .orElseThrow(() -> new ResourceNotFoundException("User not found with id " + createDTO.getOwnerId()));

        Project project = new Project();
        project.setProjectName(createDTO.getProjectName());
        project.setOwner(owner);

        Project savedProject = projectRepository.save(project);
        return convertToDTO(savedProject);
    }

    @Transactional
    public void deleteProject(UUID id) {
        if (!projectRepository.existsById(id)) {
            throw new ResourceNotFoundException("Project not found with id " + id);
        }
        projectRepository.deleteById(id);
    }

    private ProjectDTO convertToDTO(Project project) {
        ProjectDTO dto = new ProjectDTO();
        dto.setProjectId(project.getProjectId());
        dto.setProjectName(project.getProjectName());
        dto.setOwnerId(project.getOwner().getUserId());
        dto.setCreatedAt(project.getCreatedAt());
        dto.setUpdatedAt(project.getUpdatedAt());
        return dto;
    }
}
