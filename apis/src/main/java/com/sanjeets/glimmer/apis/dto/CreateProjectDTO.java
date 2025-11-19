package com.sanjeets.glimmer.apis.dto;

import jakarta.validation.constraints.NotBlank;
import jakarta.validation.constraints.NotNull;
import java.util.UUID;
import lombok.Data;

@Data
public class CreateProjectDTO {
    @NotBlank
    private String projectName;

    @NotNull
    private UUID ownerId;
}
