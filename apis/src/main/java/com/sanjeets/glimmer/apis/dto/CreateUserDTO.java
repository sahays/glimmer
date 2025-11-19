package com.sanjeets.glimmer.apis.dto;

import jakarta.validation.constraints.Email;
import jakarta.validation.constraints.NotBlank;
import lombok.Data;

@Data
public class CreateUserDTO {
    @NotBlank
    @Email
    private String email;

    @NotBlank
    private String googleId;

    private String fullName;
    private String pictureUrl;
}
