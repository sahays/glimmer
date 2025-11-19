package com.sanjeets.glimmer.cli.model;

import java.util.UUID;
import lombok.Data;

@Data
public class CreateProjectDTO {
    private String projectName;
    private UUID ownerId;
}
