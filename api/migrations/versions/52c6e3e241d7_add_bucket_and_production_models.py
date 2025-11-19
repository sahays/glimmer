"""Add bucket and production models

Revision ID: 52c6e3e241d7
Revises: 2e8d4dbcdca8
Create Date: 2025-11-19 10:52:00.614923

"""

from typing import Sequence, Union

import sqlalchemy as sa
from alembic import op
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision: str = "52c6e3e241d7"
down_revision: Union[str, None] = "2e8d4dbcdca8"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # 1. Update Users Table
    # Add user_id
    op.add_column("users", sa.Column("user_id", sa.Integer(), nullable=False))

    # Drop old FKs pointing to users.id (from projects and conversation_history)
    op.drop_constraint("projects_owner_id_fkey", "projects", type_="foreignkey")
    op.drop_constraint("conversation_history_user_id_fkey", "conversation_history", type_="foreignkey")

    # Drop old PK on users.id and create new PK on users.user_id
    # Note: In Postgres, dropping the PK usually drops the index, but we should be explicit if needed.
    op.drop_constraint("users_pkey", "users", type_="primary")
    op.create_primary_key("users_pkey", "users", ["user_id"])

    # Clean up old id column
    op.drop_index("ix_users_id", table_name="users")
    op.drop_column("users", "id")

    # Create index on new PK (optional if PK already creates it, but good for consistency with model definition)
    op.create_index(op.f("ix_users_user_id"), "users", ["user_id"], unique=False)

    # 2. Update Projects Table
    # Add new columns
    op.add_column("projects", sa.Column("project_id", sa.Integer(), nullable=False))
    op.add_column("projects", sa.Column("project_name", sa.String(), nullable=False))

    # Drop old FK pointing to projects.id
    op.drop_constraint("conversation_history_project_id_fkey", "conversation_history", type_="foreignkey")

    # Swap PK
    op.drop_constraint("projects_pkey", "projects", type_="primary")
    op.create_primary_key("projects_pkey", "projects", ["project_id"])

    # Clean up old columns
    op.drop_index("ix_projects_id", table_name="projects")
    op.drop_index("ix_projects_name", table_name="projects")
    op.drop_column("projects", "name")
    op.drop_column("projects", "id")

    # Create new indexes
    op.create_index(op.f("ix_projects_project_id"), "projects", ["project_id"], unique=False)
    op.create_index(op.f("ix_projects_project_name"), "projects", ["project_name"], unique=False)

    # Re-create FK to users.user_id (Now safe because users.user_id is PK)
    op.create_foreign_key(None, "projects", "users", ["owner_id"], ["user_id"])

    # 3. Update Conversation History Table
    op.add_column("conversation_history", sa.Column("history_id", sa.Integer(), nullable=False))
    op.add_column("conversation_history", sa.Column("message_content", sa.JSON(), nullable=False))

    # Swap PK
    op.drop_constraint("conversation_history_pkey", "conversation_history", type_="primary")
    op.create_primary_key("conversation_history_pkey", "conversation_history", ["history_id"])

    # Clean up old columns
    op.drop_index("ix_conversation_history_id", table_name="conversation_history")
    op.drop_column("conversation_history", "id")
    op.drop_column("conversation_history", "content")

    # Create new index
    op.create_index(op.f("ix_conversation_history_history_id"), "conversation_history", ["history_id"], unique=False)

    # Re-create FKs
    op.create_foreign_key(None, "conversation_history", "users", ["user_id"], ["user_id"])
    op.create_foreign_key(None, "conversation_history", "projects", ["project_id"], ["project_id"])

    # 4. Create New Tables
    op.create_table(
        "assemblies",
        sa.Column("assembly_id", sa.Integer(), nullable=False),
        sa.Column("project_id", sa.Integer(), nullable=False),
        sa.Column("created_by_id", sa.Integer(), nullable=True),
        sa.Column("assembly_name", sa.String(), nullable=False),
        sa.Column("timeline_data", sa.JSON(), nullable=False),
        sa.Column("created_at", sa.DateTime(), nullable=True),
        sa.Column("updated_at", sa.DateTime(), nullable=True),
        sa.ForeignKeyConstraint(
            ["created_by_id"],
            ["users.user_id"],
        ),
        sa.ForeignKeyConstraint(
            ["project_id"],
            ["projects.project_id"],
        ),
        sa.PrimaryKeyConstraint("assembly_id"),
    )
    op.create_index(op.f("ix_assemblies_assembly_id"), "assemblies", ["assembly_id"], unique=False)

    op.create_table(
        "audios",
        sa.Column("audio_id", sa.Integer(), nullable=False),
        sa.Column("project_id", sa.Integer(), nullable=False),
        sa.Column("created_by_id", sa.Integer(), nullable=True),
        sa.Column("audio_name", sa.String(), nullable=False),
        sa.Column("file_url", sa.String(), nullable=False),
        sa.Column("duration_seconds", sa.Integer(), nullable=True),
        sa.Column("audio_type", sa.String(), nullable=True),
        sa.Column("created_at", sa.DateTime(), nullable=True),
        sa.ForeignKeyConstraint(
            ["created_by_id"],
            ["users.user_id"],
        ),
        sa.ForeignKeyConstraint(
            ["project_id"],
            ["projects.project_id"],
        ),
        sa.PrimaryKeyConstraint("audio_id"),
    )
    op.create_index(op.f("ix_audios_audio_id"), "audios", ["audio_id"], unique=False)

    op.create_table(
        "characters",
        sa.Column("character_id", sa.Integer(), nullable=False),
        sa.Column("project_id", sa.Integer(), nullable=False),
        sa.Column("created_by_id", sa.Integer(), nullable=True),
        sa.Column("character_name", sa.String(), nullable=False),
        sa.Column("character_description", sa.String(), nullable=True),
        sa.Column("attributes", sa.JSON(), nullable=True),
        sa.Column("concept_image_url", sa.String(), nullable=True),
        sa.Column("created_at", sa.DateTime(), nullable=True),
        sa.Column("updated_at", sa.DateTime(), nullable=True),
        sa.ForeignKeyConstraint(
            ["created_by_id"],
            ["users.user_id"],
        ),
        sa.ForeignKeyConstraint(
            ["project_id"],
            ["projects.project_id"],
        ),
        sa.PrimaryKeyConstraint("character_id"),
    )
    op.create_index(op.f("ix_characters_character_id"), "characters", ["character_id"], unique=False)

    op.create_table(
        "music",
        sa.Column("music_id", sa.Integer(), nullable=False),
        sa.Column("project_id", sa.Integer(), nullable=False),
        sa.Column("created_by_id", sa.Integer(), nullable=True),
        sa.Column("music_name", sa.String(), nullable=False),
        sa.Column("file_url", sa.String(), nullable=False),
        sa.Column("duration_seconds", sa.Integer(), nullable=True),
        sa.Column("mood", sa.String(), nullable=True),
        sa.Column("created_at", sa.DateTime(), nullable=True),
        sa.ForeignKeyConstraint(
            ["created_by_id"],
            ["users.user_id"],
        ),
        sa.ForeignKeyConstraint(
            ["project_id"],
            ["projects.project_id"],
        ),
        sa.PrimaryKeyConstraint("music_id"),
    )
    op.create_index(op.f("ix_music_music_id"), "music", ["music_id"], unique=False)

    op.create_table(
        "prompts",
        sa.Column("prompt_id", sa.Integer(), nullable=False),
        sa.Column("project_id", sa.Integer(), nullable=False),
        sa.Column("created_by_id", sa.Integer(), nullable=True),
        sa.Column("prompt_name", sa.String(), nullable=True),
        sa.Column("prompt_text", sa.String(), nullable=False),
        sa.Column("agent_type", sa.String(), nullable=False),
        sa.Column("created_at", sa.DateTime(), nullable=True),
        sa.ForeignKeyConstraint(
            ["created_by_id"],
            ["users.user_id"],
        ),
        sa.ForeignKeyConstraint(
            ["project_id"],
            ["projects.project_id"],
        ),
        sa.PrimaryKeyConstraint("prompt_id"),
    )
    op.create_index(op.f("ix_prompts_prompt_id"), "prompts", ["prompt_id"], unique=False)

    op.create_table(
        "screenplays",
        sa.Column("screenplay_id", sa.Integer(), nullable=False),
        sa.Column("project_id", sa.Integer(), nullable=False),
        sa.Column("created_by_id", sa.Integer(), nullable=True),
        sa.Column("title", sa.String(), nullable=False),
        sa.Column("scene_content", sa.JSON(), nullable=True),
        sa.Column("raw_text", sa.String(), nullable=True),
        sa.Column("created_at", sa.DateTime(), nullable=True),
        sa.Column("updated_at", sa.DateTime(), nullable=True),
        sa.ForeignKeyConstraint(
            ["created_by_id"],
            ["users.user_id"],
        ),
        sa.ForeignKeyConstraint(
            ["project_id"],
            ["projects.project_id"],
        ),
        sa.PrimaryKeyConstraint("screenplay_id"),
    )
    op.create_index(op.f("ix_screenplays_screenplay_id"), "screenplays", ["screenplay_id"], unique=False)

    op.create_table(
        "videos",
        sa.Column("video_id", sa.Integer(), nullable=False),
        sa.Column("project_id", sa.Integer(), nullable=False),
        sa.Column("created_by_id", sa.Integer(), nullable=True),
        sa.Column("video_name", sa.String(), nullable=False),
        sa.Column("file_url", sa.String(), nullable=False),
        sa.Column("duration_seconds", sa.Integer(), nullable=True),
        sa.Column("created_at", sa.DateTime(), nullable=True),
        sa.ForeignKeyConstraint(
            ["created_by_id"],
            ["users.user_id"],
        ),
        sa.ForeignKeyConstraint(
            ["project_id"],
            ["projects.project_id"],
        ),
        sa.PrimaryKeyConstraint("video_id"),
    )
    op.create_index(op.f("ix_videos_video_id"), "videos", ["video_id"], unique=False)

    op.create_table(
        "render_jobs",
        sa.Column("job_id", sa.Integer(), nullable=False),
        sa.Column("assembly_id", sa.Integer(), nullable=False),
        sa.Column("job_status", sa.String(), nullable=True),
        sa.Column("output_url", sa.String(), nullable=True),
        sa.Column("error_message", sa.String(), nullable=True),
        sa.Column("created_at", sa.DateTime(), nullable=True),
        sa.Column("updated_at", sa.DateTime(), nullable=True),
        sa.ForeignKeyConstraint(
            ["assembly_id"],
            ["assemblies.assembly_id"],
        ),
        sa.PrimaryKeyConstraint("job_id"),
    )
    op.create_index(op.f("ix_render_jobs_job_id"), "render_jobs", ["job_id"], unique=False)


def downgrade() -> None:
    # 1. Drop New Tables
    op.drop_index(op.f("ix_render_jobs_job_id"), table_name="render_jobs")
    op.drop_table("render_jobs")
    op.drop_index(op.f("ix_videos_video_id"), table_name="videos")
    op.drop_table("videos")
    op.drop_index(op.f("ix_screenplays_screenplay_id"), table_name="screenplays")
    op.drop_table("screenplays")
    op.drop_index(op.f("ix_prompts_prompt_id"), table_name="prompts")
    op.drop_table("prompts")
    op.drop_index(op.f("ix_music_music_id"), table_name="music")
    op.drop_table("music")
    op.drop_index(op.f("ix_characters_character_id"), table_name="characters")
    op.drop_table("characters")
    op.drop_index(op.f("ix_audios_audio_id"), table_name="audios")
    op.drop_table("audios")
    op.drop_index(op.f("ix_assemblies_assembly_id"), table_name="assemblies")
    op.drop_table("assemblies")

    # 2. Restore Conversation History
    op.add_column(
        "conversation_history",
        sa.Column("content", postgresql.JSON(astext_type=sa.Text()), autoincrement=False, nullable=False),
    )
    op.add_column("conversation_history", sa.Column("id", sa.INTEGER(), autoincrement=True, nullable=False))

    op.drop_constraint("conversation_history_pkey", "conversation_history", type_="primary")
    op.create_primary_key("conversation_history_pkey", "conversation_history", ["id"])

    op.drop_constraint(None, "conversation_history", type_="foreignkey")
    op.drop_constraint(None, "conversation_history", type_="foreignkey")
    op.create_foreign_key(
        "conversation_history_project_id_fkey", "conversation_history", "projects", ["project_id"], ["id"]
    )
    op.create_foreign_key("conversation_history_user_id_fkey", "conversation_history", "users", ["user_id"], ["id"])

    op.drop_index(op.f("ix_conversation_history_history_id"), table_name="conversation_history")
    op.create_index("ix_conversation_history_id", "conversation_history", ["id"], unique=False)
    op.drop_column("conversation_history", "message_content")
    op.drop_column("conversation_history", "history_id")

    # 3. Restore Projects
    op.add_column(
        "projects",
        sa.Column(
            "id",
            sa.INTEGER(),
            server_default=sa.text("nextval('projects_id_seq'::regclass)"),
            autoincrement=True,
            nullable=False,
        ),
    )
    op.add_column("projects", sa.Column("name", sa.VARCHAR(), autoincrement=False, nullable=False))

    op.drop_constraint("projects_pkey", "projects", type_="primary")
    op.create_primary_key("projects_pkey", "projects", ["id"])

    op.drop_constraint(None, "projects", type_="foreignkey")
    op.create_foreign_key("projects_owner_id_fkey", "projects", "users", ["owner_id"], ["id"])

    op.drop_index(op.f("ix_projects_project_name"), table_name="projects")
    op.drop_index(op.f("ix_projects_project_id"), table_name="projects")
    op.create_index("ix_projects_name", "projects", ["name"], unique=False)
    op.create_index("ix_projects_id", "projects", ["id"], unique=False)
    op.drop_column("projects", "project_name")
    op.drop_column("projects", "project_id")

    # 4. Restore Users
    op.add_column(
        "users",
        sa.Column(
            "id",
            sa.INTEGER(),
            server_default=sa.text("nextval('users_id_seq'::regclass)"),
            autoincrement=True,
            nullable=False,
        ),
    )

    op.drop_constraint("users_pkey", "users", type_="primary")
    op.create_primary_key("users_pkey", "users", ["id"])

    op.drop_index(op.f("ix_users_user_id"), table_name="users")
    op.create_index("ix_users_id", "users", ["id"], unique=False)
    op.drop_column("users", "user_id")
