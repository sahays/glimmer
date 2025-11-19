package com.sanjeets.glimmer.cli.client;

import com.sanjeets.glimmer.cli.model.CreateProjectDTO;
import com.sanjeets.glimmer.cli.model.CreateUserDTO;
import com.sanjeets.glimmer.cli.model.ProjectDTO;
import com.sanjeets.glimmer.cli.model.UserDTO;
import java.util.List;
import java.util.UUID;
import lombok.RequiredArgsConstructor;
import org.springframework.core.ParameterizedTypeReference;
import org.springframework.http.MediaType;
import org.springframework.stereotype.Service;
import org.springframework.web.client.RestClient;

@Service
@RequiredArgsConstructor
public class GlimmerApiClient {

    private final RestClient restClient;

    // --- Users ---

    public List<UserDTO> listUsers() {
        return restClient.get()
                .uri("/users")
                .retrieve()
                .body(new ParameterizedTypeReference<>() {});
    }

    public UserDTO createUser(CreateUserDTO dto) {
        return restClient.post()
                .uri("/users")
                .contentType(MediaType.APPLICATION_JSON)
                .body(dto)
                .retrieve()
                .body(UserDTO.class);
    }

    // --- Projects ---

    public List<ProjectDTO> listProjects(UUID ownerId) {
        String uri = "/projects";
        if (ownerId != null) {
            uri += "?ownerId=" + ownerId;
        }
        return restClient.get()
                .uri(uri)
                .retrieve()
                .body(new ParameterizedTypeReference<>() {});
    }

    public ProjectDTO createProject(CreateProjectDTO dto) {
        return restClient.post()
                .uri("/projects")
                .contentType(MediaType.APPLICATION_JSON)
                .body(dto)
                .retrieve()
                .body(ProjectDTO.class);
    }
}
