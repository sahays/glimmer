# api/app/models.py

import datetime

from sqlalchemy import (
    JSON,
    Column,
    DateTime,
    ForeignKey,
    Integer,
    String,
)
from sqlalchemy.orm import declarative_base, relationship

Base = declarative_base()


class User(Base):
    __tablename__ = "users"

    user_id = Column(Integer, primary_key=True, index=True)
    google_id = Column(String, unique=True, index=True, nullable=False)
    email = Column(String, unique=True, index=True, nullable=False)
    full_name = Column(String, nullable=True)
    picture_url = Column(String, nullable=True)
    created_at = Column(DateTime, default=datetime.datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.datetime.utcnow, onupdate=datetime.datetime.utcnow)

    projects = relationship("Project", back_populates="owner")
    conversation_history = relationship("ConversationHistory", back_populates="user")


class Project(Base):
    __tablename__ = "projects"

    project_id = Column(Integer, primary_key=True, index=True)
    project_name = Column(String, index=True, nullable=False)
    owner_id = Column(Integer, ForeignKey("users.user_id"), nullable=False)
    created_at = Column(DateTime, default=datetime.datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.datetime.utcnow, onupdate=datetime.datetime.utcnow)

    owner = relationship("User", back_populates="projects")
    conversation_history = relationship("ConversationHistory", back_populates="project")
    # Buckets relationships
    characters = relationship("Character", back_populates="project")
    screenplays = relationship("Screenplay", back_populates="project")
    prompts = relationship("Prompt", back_populates="project")
    audios = relationship("Audio", back_populates="project")
    music = relationship("Music", back_populates="project")
    videos = relationship("Video", back_populates="project")
    assemblies = relationship("Assembly", back_populates="project")


class ConversationHistory(Base):
    __tablename__ = "conversation_history"

    history_id = Column(Integer, primary_key=True, index=True)
    session_id = Column(String, index=True, nullable=False)
    user_id = Column(Integer, ForeignKey("users.user_id"), nullable=False)
    project_id = Column(Integer, ForeignKey("projects.project_id"), nullable=False)
    message_content = Column(JSON, nullable=False)
    created_at = Column(DateTime, default=datetime.datetime.utcnow)

    user = relationship("User", back_populates="conversation_history")
    project = relationship("Project", back_populates="conversation_history")


# --- Pre-Production Buckets (Assets) ---


class Character(Base):
    __tablename__ = "characters"

    character_id = Column(Integer, primary_key=True, index=True)
    project_id = Column(Integer, ForeignKey("projects.project_id"), nullable=False)
    created_by_id = Column(Integer, ForeignKey("users.user_id"), nullable=True)
    character_name = Column(String, nullable=False)
    character_description = Column(String, nullable=True)  # Biography / Physical description
    attributes = Column(JSON, nullable=True)  # Flexible JSON for stats, traits, etc.
    concept_image_url = Column(String, nullable=True)  # URL to generated concept art
    created_at = Column(DateTime, default=datetime.datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.datetime.utcnow, onupdate=datetime.datetime.utcnow)

    project = relationship("Project", back_populates="characters")
    creator = relationship("User")


class Screenplay(Base):
    __tablename__ = "screenplays"

    screenplay_id = Column(Integer, primary_key=True, index=True)
    project_id = Column(Integer, ForeignKey("projects.project_id"), nullable=False)
    created_by_id = Column(Integer, ForeignKey("users.user_id"), nullable=True)
    title = Column(String, nullable=False)
    scene_content = Column(JSON, nullable=True)  # Structured representation (scenes, dialogue)
    raw_text = Column(String, nullable=True)  # Flat text representation
    created_at = Column(DateTime, default=datetime.datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.datetime.utcnow, onupdate=datetime.datetime.utcnow)

    project = relationship("Project", back_populates="screenplays")
    creator = relationship("User")


class Prompt(Base):
    __tablename__ = "prompts"

    prompt_id = Column(Integer, primary_key=True, index=True)
    project_id = Column(Integer, ForeignKey("projects.project_id"), nullable=False)
    created_by_id = Column(Integer, ForeignKey("users.user_id"), nullable=True)
    prompt_name = Column(String, nullable=True)  # Optional label for the prompt
    prompt_text = Column(String, nullable=False)  # The actual text prompt
    agent_type = Column(String, nullable=False)  # e.g., "character", "music"
    created_at = Column(DateTime, default=datetime.datetime.utcnow)

    project = relationship("Project", back_populates="prompts")
    creator = relationship("User")


class Audio(Base):
    __tablename__ = "audios"

    audio_id = Column(Integer, primary_key=True, index=True)
    project_id = Column(Integer, ForeignKey("projects.project_id"), nullable=False)
    created_by_id = Column(Integer, ForeignKey("users.user_id"), nullable=True)
    audio_name = Column(String, nullable=False)
    file_url = Column(String, nullable=False)  # GCS Object Key or URL
    duration_seconds = Column(Integer, nullable=True)
    audio_type = Column(String, default="sfx")  # "voiceover" or "sfx"
    created_at = Column(DateTime, default=datetime.datetime.utcnow)

    project = relationship("Project", back_populates="audios")
    creator = relationship("User")


class Music(Base):
    __tablename__ = "music"

    music_id = Column(Integer, primary_key=True, index=True)
    project_id = Column(Integer, ForeignKey("projects.project_id"), nullable=False)
    created_by_id = Column(Integer, ForeignKey("users.user_id"), nullable=True)
    music_name = Column(String, nullable=False)
    file_url = Column(String, nullable=False)
    duration_seconds = Column(Integer, nullable=True)
    mood = Column(String, nullable=True)
    created_at = Column(DateTime, default=datetime.datetime.utcnow)

    project = relationship("Project", back_populates="music")
    creator = relationship("User")


class Video(Base):
    __tablename__ = "videos"

    video_id = Column(Integer, primary_key=True, index=True)
    project_id = Column(Integer, ForeignKey("projects.project_id"), nullable=False)
    created_by_id = Column(Integer, ForeignKey("users.user_id"), nullable=True)
    video_name = Column(String, nullable=False)
    file_url = Column(String, nullable=False)
    duration_seconds = Column(Integer, nullable=True)
    created_at = Column(DateTime, default=datetime.datetime.utcnow)

    project = relationship("Project", back_populates="videos")
    creator = relationship("User")


# --- Production Bucket (Assembly) ---


class Assembly(Base):
    __tablename__ = "assemblies"

    assembly_id = Column(Integer, primary_key=True, index=True)
    project_id = Column(Integer, ForeignKey("projects.project_id"), nullable=False)
    created_by_id = Column(Integer, ForeignKey("users.user_id"), nullable=True)
    assembly_name = Column(String, nullable=False)
    timeline_data = Column(JSON, nullable=False)  # The sequence of assets on the timeline
    created_at = Column(DateTime, default=datetime.datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.datetime.utcnow, onupdate=datetime.datetime.utcnow)

    project = relationship("Project", back_populates="assemblies")
    creator = relationship("User")
    render_jobs = relationship("RenderJob", back_populates="assembly")


# --- Post-Production (Export) ---


class RenderJob(Base):
    __tablename__ = "render_jobs"

    job_id = Column(Integer, primary_key=True, index=True)
    assembly_id = Column(Integer, ForeignKey("assemblies.assembly_id"), nullable=False)
    job_status = Column(String, default="pending")  # pending, processing, completed, failed
    output_url = Column(String, nullable=True)  # Final video URL
    error_message = Column(String, nullable=True)
    created_at = Column(DateTime, default=datetime.datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.datetime.utcnow, onupdate=datetime.datetime.utcnow)

    assembly = relationship("Assembly", back_populates="render_jobs")
