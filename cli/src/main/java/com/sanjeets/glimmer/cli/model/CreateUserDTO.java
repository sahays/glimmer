package com.sanjeets.glimmer.cli.model;

import lombok.Data;

@Data
public class CreateUserDTO {
    private String email;
    private String googleId;
    private String fullName;
    private String pictureUrl;
}
