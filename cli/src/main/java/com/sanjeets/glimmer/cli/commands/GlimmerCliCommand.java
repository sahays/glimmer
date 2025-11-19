package com.sanjeets.glimmer.cli.commands;

import org.springframework.stereotype.Component;
import picocli.CommandLine.Command;

@Component
@Command(name = "glimmer",
    description = "Glimmer Creative Studio CLI",
    subcommands = {UserCommands.class, ProjectCommands.class},
    mixinStandardHelpOptions = true)
public class GlimmerCliCommand {
    // Main entry command, subcommands handle the logic
}
