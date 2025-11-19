package com.sanjeets.glimmer.apis.service;

import com.sanjeets.glimmer.apis.dto.CreateUserDTO;
import com.sanjeets.glimmer.apis.dto.UserDTO;
import com.sanjeets.glimmer.apis.exception.ResourceNotFoundException;
import com.sanjeets.glimmer.apis.model.User;
import com.sanjeets.glimmer.apis.repository.UserRepository;
import java.util.List;
import java.util.UUID;
import java.util.stream.Collectors;
import lombok.RequiredArgsConstructor;
import org.springframework.stereotype.Service;
import org.springframework.transaction.annotation.Transactional;

@Service
@RequiredArgsConstructor
public class UserService {

    private final UserRepository userRepository;

    @Transactional(readOnly = true)
    public List<UserDTO> getAllUsers() {
        return userRepository.findAll().stream()
            .map(this::convertToDTO)
            .collect(Collectors.toList());
    }

    @Transactional(readOnly = true)
    public UserDTO getUserById(UUID id) {
        User user = userRepository.findById(id)
            .orElseThrow(() -> new ResourceNotFoundException("User not found with id " + id));
        return convertToDTO(user);
    }

    @Transactional
    public UserDTO createUser(CreateUserDTO createDTO) {
        // Check if exists
        if (userRepository.findByEmail(createDTO.getEmail()).isPresent()) {
            throw new IllegalArgumentException("Email already registered");
        }

        User user = new User();
        user.setEmail(createDTO.getEmail());
        user.setGoogleId(createDTO.getGoogleId());
        user.setFullName(createDTO.getFullName());
        user.setPictureUrl(createDTO.getPictureUrl());

        User savedUser = userRepository.save(user);
        return convertToDTO(savedUser);
    }

    private UserDTO convertToDTO(User user) {
        UserDTO dto = new UserDTO();
        dto.setUserId(user.getUserId());
        dto.setGoogleId(user.getGoogleId());
        dto.setEmail(user.getEmail());
        dto.setFullName(user.getFullName());
        dto.setPictureUrl(user.getPictureUrl());
        dto.setCreatedAt(user.getCreatedAt());
        dto.setUpdatedAt(user.getUpdatedAt());
        return dto;
    }
}
