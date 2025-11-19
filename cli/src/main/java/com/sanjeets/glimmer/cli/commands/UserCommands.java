package com.sanjeets.glimmer.cli.commands;

import com.sanjeets.glimmer.cli.client.GlimmerApiClient;
import com.sanjeets.glimmer.cli.model.CreateUserDTO;
import com.sanjeets.glimmer.cli.model.UserDTO;
import java.util.List;
import lombok.RequiredArgsConstructor;
import org.springframework.shell.standard.ShellComponent;
import org.springframework.shell.standard.ShellMethod;
import org.springframework.shell.standard.ShellOption;
import org.springframework.shell.table.ArrayTableModel;
import org.springframework.shell.table.BorderStyle;
import org.springframework.shell.table.TableBuilder;
import org.springframework.shell.table.TableModel;

@ShellComponent
@RequiredArgsConstructor
public class UserCommands {

    private final GlimmerApiClient apiClient;

    @ShellMethod(key = "users list", value = "List all users")
    public void listUsers() {
        try {
            List<UserDTO> users = apiClient.listUsers();
            if (users.isEmpty()) {
                System.out.println("No users found.");
                return;
            }

            Object[][] data = new Object[users.size() + 1][4];
            data[0] = new Object[]{"ID", "Email", "Name", "Google ID"};

            for (int i = 0; i < users.size(); i++) {
                UserDTO u = users.get(i);
                data[i + 1] = new Object[]{
                    u.getUserId(),
                    u.getEmail(),
                    u.getFullName(),
                    u.getGoogleId()
                };
            }

            TableModel model = new ArrayTableModel(data);
            TableBuilder tableBuilder = new TableBuilder(model);
            tableBuilder.addFullBorder(BorderStyle.fancy_light);
            System.out.println(tableBuilder.build().render(80));

        } catch (Exception e) {
            System.err.println("Error fetching users: " + e.getMessage());
        }
    }

    @ShellMethod(key = "users create", value = "Create a new user")
    public void createUser(
        @ShellOption(help = "Email address") String email,
        @ShellOption(help = "Google ID") String googleId,
        @ShellOption(help = "Full Name", defaultValue = ShellOption.NULL) String fullName,
        @ShellOption(help = "Picture URL", defaultValue = ShellOption.NULL) String pictureUrl
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
