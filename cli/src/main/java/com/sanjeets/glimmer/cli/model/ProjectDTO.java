package com.sanjeets.glimmer.cli.model;

import java.time.LocalDateTime;
import java.util.UUID;
import lombok.Data;

@Data
public class ProjectDTO {
    private UUID projectId;
    private String projectName;
    private UUID ownerId;
    private LocalDateTime createdAt;
    private LocalDateTime updatedAt;
}
