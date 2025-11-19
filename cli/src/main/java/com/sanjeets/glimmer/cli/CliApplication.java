package com.sanjeets.glimmer.cli;

import com.sanjeets.glimmer.cli.commands.GlimmerCliCommand;
import org.springframework.boot.CommandLineRunner;
import org.springframework.boot.ExitCodeGenerator;
import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import picocli.CommandLine;
import picocli.CommandLine.IFactory;

@SpringBootApplication
public class CliApplication implements CommandLineRunner, ExitCodeGenerator {

    private final IFactory factory;
    private final GlimmerCliCommand glimmerCliCommand;
    private int exitCode;

    public CliApplication(IFactory factory, GlimmerCliCommand glimmerCliCommand) {
        this.factory = factory;
        this.glimmerCliCommand = glimmerCliCommand;
    }

    public static void main(String[] args) {
        System.exit(SpringApplication.exit(SpringApplication.run(CliApplication.class, args)));
    }

    @Override
    public void run(String... args) {
        exitCode = new CommandLine(glimmerCliCommand, factory).execute(args);
    }

    @Override
    public int getExitCode() {
        return exitCode;
    }
}
