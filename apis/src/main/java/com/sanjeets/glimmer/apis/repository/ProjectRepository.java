package com.sanjeets.glimmer.apis.repository;

import com.sanjeets.glimmer.apis.model.Project;
import java.util.List;
import java.util.UUID;
import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.stereotype.Repository;

@Repository
public interface ProjectRepository extends JpaRepository<Project, UUID> {
    List<Project> findByOwner_UserId(UUID ownerId);
}
