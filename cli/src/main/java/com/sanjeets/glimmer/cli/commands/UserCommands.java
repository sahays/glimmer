package com.sanjeets.glimmer.cli.commands;

import com.sanjeets.glimmer.cli.client.GlimmerApiClient;
import com.sanjeets.glimmer.cli.model.CreateUserDTO;
import com.sanjeets.glimmer.cli.model.UserDTO;
import java.util.List;
import lombok.RequiredArgsConstructor;
import org.springframework.stereotype.Component;
import picocli.CommandLine;
import picocli.CommandLine.Command;
import picocli.CommandLine.Option;

@Component
@Command(name = "users", description = "Manage users", mixinStandardHelpOptions = true)
@RequiredArgsConstructor
public class UserCommands {

    private final GlimmerApiClient apiClient;

    @Command(name = "list", description = "List all users")
    public void list() {
        try {
            List<UserDTO> users = apiClient.listUsers();
            if (users.isEmpty()) {
                System.out.println("No users found.");
                return;
            }
            System.out.printf("%-36s %-30s %-20s %-15s%n", "ID", "Email", "Name", "Google ID");
            System.out.println("-".repeat(105));
            for (UserDTO u : users) {
                System.out.printf("%-36s %-30s %-20s %-15s%n",
                    u.getUserId(), u.getEmail(),
                    u.getFullName() != null ? u.getFullName() : "",
                    u.getGoogleId());
            }
        } catch (Exception e) {
            System.err.println("Error fetching users: " + e.getMessage());
        }
    }

    @Command(name = "create", description = "Create a new user")
    public void create(
        @Option(names = "--email", required = true, description = "Email address") String email,
        @Option(names = "--google-id", required = true, description = "Google ID") String googleId,
        @Option(names = "--full-name", description = "Full Name") String fullName,
        @Option(names = "--picture-url", description = "Picture URL") String pictureUrl
    ) {
        try {
            CreateUserDTO dto = new CreateUserDTO();
            dto.setEmail(email);
            dto.setGoogleId(googleId);
            dto.setFullName(fullName);
            dto.setPictureUrl(pictureUrl);

            UserDTO user = apiClient.createUser(dto);
            System.out.println("User created successfully: " + user.getUserId());
        } catch (Exception e) {
            System.err.println("Error creating user: " + e.getMessage());
        }
    }
}
