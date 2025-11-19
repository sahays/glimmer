package com.sanjeets.glimmer.apis.dto;

import java.time.LocalDateTime;
import java.util.UUID;
import lombok.Data;

@Data
public class UserDTO {
    private UUID userId;
    private String googleId;
    private String email;
    private String fullName;
    private String pictureUrl;
    private LocalDateTime createdAt;
    private LocalDateTime updatedAt;
}
