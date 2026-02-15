"""
Configuration management for PHAIT.

Handles paths for database, encryption keys, and AI models.
"""

import os
from pathlib import Path
from typing import Optional


class Config:
    """Configuration for PHAIT system."""

    def __init__(self, base_dir: Optional[Path] = None) -> None:
        """
        Initialize configuration.

        Args:
            base_dir: Base directory for PHAIT data. Defaults to ~/.phait
        """
        if base_dir is None:
            base_dir = Path.home() / ".phait"

        self.base_dir = base_dir
        self.data_dir = base_dir / "data"
        self.backup_dir = base_dir / "backups"
        self.attachments_dir = base_dir / "attachments"
        self.models_dir = base_dir / "models"

        # Database paths
        self.db_path = self.data_dir / "medical_vault.db"
        self.key_path = self.data_dir / "master.key"

        # AI model paths
        self.ai_model_path = self.models_dir / "model.gguf"

        # Encryption settings
        self.encryption_algorithm = "AES-256-GCM"
        self.key_derivation_iterations = 100000

        # Performance settings
        self.sos_generation_timeout_seconds = 5
        self.sos_regeneration_timeout_seconds = 10
        self.search_timeout_seconds = 2
        self.export_timeout_seconds = 30

        # Supported languages for SOS summaries
        self.supported_languages = ["en", "es", "fr", "de", "zh"]

    def ensure_directories(self) -> None:
        """Create all required directories if they don't exist."""
        for directory in [
            self.base_dir,
            self.data_dir,
            self.backup_dir,
            self.attachments_dir,
            self.models_dir,
        ]:
            directory.mkdir(parents=True, exist_ok=True)

    def get_attachment_path(self, attachment_id: str) -> Path:
        """
        Get the file path for an attachment.

        Args:
            attachment_id: Unique identifier for the attachment

        Returns:
            Path to the attachment file
        """
        return self.attachments_dir / f"{attachment_id}.enc"

    def get_backup_path(self, backup_name: str) -> Path:
        """
        Get the file path for a backup.

        Args:
            backup_name: Name of the backup file

        Returns:
            Path to the backup file
        """
        return self.backup_dir / backup_name


# Global default configuration instance
default_config = Config()
