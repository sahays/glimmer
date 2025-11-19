CREATE TABLE users (
    user_id UUID PRIMARY KEY,
    google_id VARCHAR(255) NOT NULL UNIQUE,
    email VARCHAR(255) NOT NULL UNIQUE,
    full_name VARCHAR(255),
    picture_url VARCHAR(255),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE projects (
    project_id UUID PRIMARY KEY,
    project_name VARCHAR(255) NOT NULL,
    owner_id UUID NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    CONSTRAINT fk_projects_owner FOREIGN KEY (owner_id) REFERENCES users(user_id)
);

CREATE TABLE conversation_history (
    history_id UUID PRIMARY KEY,
    session_id VARCHAR(255) NOT NULL,
    user_id UUID NOT NULL,
    project_id UUID NOT NULL,
    message_content TEXT NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    CONSTRAINT fk_ch_user FOREIGN KEY (user_id) REFERENCES users(user_id),
    CONSTRAINT fk_ch_project FOREIGN KEY (project_id) REFERENCES projects(project_id)
);

-- Pre-Production Buckets

CREATE TABLE characters (
    character_id UUID PRIMARY KEY,
    project_id UUID NOT NULL,
    created_by_id UUID,
    character_name VARCHAR(255) NOT NULL,
    character_description TEXT,
    attributes TEXT, -- JSON stored as text
    concept_image_url VARCHAR(255),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    CONSTRAINT fk_characters_project FOREIGN KEY (project_id) REFERENCES projects(project_id),
    CONSTRAINT fk_characters_creator FOREIGN KEY (created_by_id) REFERENCES users(user_id)
);

CREATE TABLE screenplays (
    screenplay_id UUID PRIMARY KEY,
    project_id UUID NOT NULL,
    created_by_id UUID,
    title VARCHAR(255) NOT NULL,
    scene_content TEXT, -- JSON
    raw_text TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    CONSTRAINT fk_screenplays_project FOREIGN KEY (project_id) REFERENCES projects(project_id),
    CONSTRAINT fk_screenplays_creator FOREIGN KEY (created_by_id) REFERENCES users(user_id)
);

CREATE TABLE prompts (
    prompt_id UUID PRIMARY KEY,
    project_id UUID NOT NULL,
    created_by_id UUID,
    prompt_name VARCHAR(255),
    prompt_text TEXT NOT NULL,
    agent_type VARCHAR(255) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    CONSTRAINT fk_prompts_project FOREIGN KEY (project_id) REFERENCES projects(project_id),
    CONSTRAINT fk_prompts_creator FOREIGN KEY (created_by_id) REFERENCES users(user_id)
);

CREATE TABLE audios (
    audio_id UUID PRIMARY KEY,
    project_id UUID NOT NULL,
    created_by_id UUID,
    audio_name VARCHAR(255) NOT NULL,
    file_url VARCHAR(255) NOT NULL,
    duration_seconds INTEGER,
    audio_type VARCHAR(255) DEFAULT 'sfx',
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    CONSTRAINT fk_audios_project FOREIGN KEY (project_id) REFERENCES projects(project_id),
    CONSTRAINT fk_audios_creator FOREIGN KEY (created_by_id) REFERENCES users(user_id)
);

CREATE TABLE music (
    music_id UUID PRIMARY KEY,
    project_id UUID NOT NULL,
    created_by_id UUID,
    music_name VARCHAR(255) NOT NULL,
    file_url VARCHAR(255) NOT NULL,
    duration_seconds INTEGER,
    mood VARCHAR(255),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    CONSTRAINT fk_music_project FOREIGN KEY (project_id) REFERENCES projects(project_id),
    CONSTRAINT fk_music_creator FOREIGN KEY (created_by_id) REFERENCES users(user_id)
);

CREATE TABLE videos (
    video_id UUID PRIMARY KEY,
    project_id UUID NOT NULL,
    created_by_id UUID,
    video_name VARCHAR(255) NOT NULL,
    file_url VARCHAR(255) NOT NULL,
    duration_seconds INTEGER,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    CONSTRAINT fk_videos_project FOREIGN KEY (project_id) REFERENCES projects(project_id),
    CONSTRAINT fk_videos_creator FOREIGN KEY (created_by_id) REFERENCES users(user_id)
);

-- Production & Post-Production

CREATE TABLE assemblies (
    assembly_id UUID PRIMARY KEY,
    project_id UUID NOT NULL,
    created_by_id UUID,
    assembly_name VARCHAR(255) NOT NULL,
    timeline_data TEXT NOT NULL, -- JSON
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    CONSTRAINT fk_assemblies_project FOREIGN KEY (project_id) REFERENCES projects(project_id),
    CONSTRAINT fk_assemblies_creator FOREIGN KEY (created_by_id) REFERENCES users(user_id)
);

CREATE TABLE render_jobs (
    job_id UUID PRIMARY KEY,
    assembly_id UUID NOT NULL,
    job_status VARCHAR(255) DEFAULT 'pending',
    output_url VARCHAR(255),
    error_message TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    CONSTRAINT fk_jobs_assembly FOREIGN KEY (assembly_id) REFERENCES assemblies(assembly_id)
);
