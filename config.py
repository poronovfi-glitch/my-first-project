"""
Configuration module for AI Assistant Bot.
Loads and validates settings from environment variables.
"""

import os
import json
import logging
from pathlib import Path
from typing import Dict, List, Optional
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Base paths
BASE_DIR = Path(__file__).parent.absolute()
DATA_DIR = BASE_DIR / "data"
CONFIG_DIR = BASE_DIR / "config"
LOGS_DIR = DATA_DIR

# Ensure directories exist
DATA_DIR.mkdir(exist_ok=True)
CONFIG_DIR.mkdir(exist_ok=True)
LOGS_DIR.mkdir(exist_ok=True)


# =============================================================================
# TELEGRAM CONFIGURATION
# =============================================================================

class TelegramConfig:
    """Telegram bot configuration."""

    BOT_TOKEN: str = os.getenv("TELEGRAM_BOT_TOKEN", "")
    ADMIN_ID: int = int(os.getenv("TELEGRAM_ADMIN_ID", "0"))

    # Parse allowed user IDs
    _allowed_ids = os.getenv("ALLOWED_USER_IDS", "")
    ALLOWED_USER_IDS: List[int] = (
        [int(uid.strip()) for uid in _allowed_ids.split(",") if uid.strip()]
        if _allowed_ids else []
    )

    @classmethod
    def validate(cls) -> bool:
        """Validate Telegram configuration."""
        if not cls.BOT_TOKEN:
            raise ValueError("TELEGRAM_BOT_TOKEN is not set")
        if not cls.ADMIN_ID:
            raise ValueError("TELEGRAM_ADMIN_ID is not set")
        return True


# =============================================================================
# LLM CONFIGURATION
# =============================================================================

class LLMConfig:
    """LLM providers configuration."""

    # OpenAI (primary)
    OPENAI_API_KEY: str = os.getenv("OPENAI_API_KEY", "")
    OPENAI_MODEL: str = os.getenv("OPENAI_MODEL", "gpt-4o-mini")

    # Anthropic Claude (fallback)
    ANTHROPIC_API_KEY: str = os.getenv("ANTHROPIC_API_KEY", "")
    ANTHROPIC_MODEL: str = os.getenv("ANTHROPIC_MODEL", "claude-3-5-sonnet-20241022")

    @classmethod
    def validate(cls) -> bool:
        """Validate LLM configuration."""
        if not cls.OPENAI_API_KEY:
            raise ValueError("OPENAI_API_KEY is not set")
        return True


# =============================================================================
# BUDGET & USAGE TRACKING
# =============================================================================

class BudgetConfig:
    """Budget and usage tracking configuration."""

    # Parse user budgets
    _budgets_str = os.getenv("USER_BUDGETS", "{}")
    USER_BUDGETS: Dict[int, float] = {}

    try:
        _budgets = json.loads(_budgets_str)
        USER_BUDGETS = {int(k): float(v) for k, v in _budgets.items()}
    except (json.JSONDecodeError, ValueError) as e:
        logging.warning(f"Failed to parse USER_BUDGETS: {e}")

    BUDGET_PERIOD: str = os.getenv("BUDGET_PERIOD", "monthly")
    BUDGET_WARNING_THRESHOLD: int = int(os.getenv("BUDGET_WARNING_THRESHOLD", "80"))


# =============================================================================
# CALENDAR CONFIGURATION
# =============================================================================

class CalendarConfig:
    """Calendar providers configuration."""

    PROVIDER: str = os.getenv("CALENDAR_PROVIDER", "local")

    # Apple Calendar (CalDAV)
    APPLE_URL: str = os.getenv("APPLE_CALENDAR_URL", "")
    APPLE_USERNAME: str = os.getenv("APPLE_CALENDAR_USERNAME", "")
    APPLE_PASSWORD: str = os.getenv("APPLE_CALENDAR_PASSWORD", "")

    # Google Calendar
    GOOGLE_CREDENTIALS_FILE: Path = CONFIG_DIR / os.getenv(
        "GOOGLE_CALENDAR_CREDENTIALS_FILE", "google_credentials.json"
    )
    GOOGLE_TOKEN_FILE: Path = DATA_DIR / os.getenv(
        "GOOGLE_CALENDAR_TOKEN_FILE", "google_token.json"
    )

    # Microsoft Outlook
    MICROSOFT_TENANT_ID: str = os.getenv("MICROSOFT_TENANT_ID", "")
    MICROSOFT_CLIENT_ID: str = os.getenv("MICROSOFT_CLIENT_ID", "")
    MICROSOFT_CLIENT_SECRET: str = os.getenv("MICROSOFT_CLIENT_SECRET", "")

    # Universal CalDAV
    CALDAV_URL: str = os.getenv("CALDAV_URL", "")
    CALDAV_USERNAME: str = os.getenv("CALDAV_USERNAME", "")
    CALDAV_PASSWORD: str = os.getenv("CALDAV_PASSWORD", "")


# =============================================================================
# CONTACTS CONFIGURATION
# =============================================================================

class ContactsConfig:
    """Contacts providers configuration."""

    PROVIDER: str = os.getenv("CONTACTS_PROVIDER", "local")

    # Apple Contacts (CardDAV)
    APPLE_URL: str = os.getenv("APPLE_CONTACTS_URL", "")
    APPLE_USERNAME: str = os.getenv("APPLE_CONTACTS_USERNAME", "")
    APPLE_PASSWORD: str = os.getenv("APPLE_CONTACTS_PASSWORD", "")

    # Google Contacts
    GOOGLE_CREDENTIALS_FILE: Path = CONFIG_DIR / os.getenv(
        "GOOGLE_CONTACTS_CREDENTIALS_FILE", "google_credentials.json"
    )
    GOOGLE_TOKEN_FILE: Path = DATA_DIR / os.getenv(
        "GOOGLE_CONTACTS_TOKEN_FILE", "google_contacts_token.json"
    )


# =============================================================================
# DATABASE & SECURITY
# =============================================================================

class DatabaseConfig:
    """Database and security configuration."""

    DATABASE_PATH: Path = DATA_DIR / os.getenv("DATABASE_PATH", "bot.db")
    ENCRYPTION_KEY: Optional[str] = os.getenv("ENCRYPTION_KEY") or None

    # Rate limiting
    RATE_LIMIT_REQUESTS: int = int(os.getenv("RATE_LIMIT_REQUESTS", "30"))
    RATE_LIMIT_PERIOD: int = int(os.getenv("RATE_LIMIT_PERIOD", "60"))


# =============================================================================
# MEMORY & CONTEXT
# =============================================================================

class MemoryConfig:
    """Memory and context configuration."""

    MAX_CONTEXT_MESSAGES: int = int(os.getenv("MAX_CONTEXT_MESSAGES", "50"))
    MAX_CONTEXT_TOKENS: int = int(os.getenv("MAX_CONTEXT_TOKENS", "8000"))
    ENABLE_LONG_TERM_MEMORY: bool = os.getenv("ENABLE_LONG_TERM_MEMORY", "true").lower() == "true"


# =============================================================================
# PLUGINS
# =============================================================================

class PluginsConfig:
    """Plugins configuration."""

    _enabled = os.getenv("ENABLED_PLUGINS", "calendar,contacts,excel,memory")
    ENABLED_PLUGINS: List[str] = [p.strip() for p in _enabled.split(",") if p.strip()]

    CUSTOM_PLUGINS_DIR: Path = BASE_DIR / os.getenv("CUSTOM_PLUGINS_DIR", "bot/plugins")


# =============================================================================
# LOGGING
# =============================================================================

class LoggingConfig:
    """Logging configuration."""

    LOG_LEVEL: str = os.getenv("LOG_LEVEL", "INFO")
    LOG_FILE: Path = LOGS_DIR / os.getenv("LOG_FILE", "bot.log")
    LOG_MAX_SIZE: int = int(os.getenv("LOG_MAX_SIZE", "10")) * 1024 * 1024  # MB to bytes
    LOG_BACKUP_COUNT: int = int(os.getenv("LOG_BACKUP_COUNT", "5"))


# =============================================================================
# FEATURE FLAGS
# =============================================================================

class FeatureFlags:
    """Feature flags configuration."""

    ENABLE_STREAMING: bool = os.getenv("ENABLE_STREAMING", "true").lower() == "true"
    ENABLE_IMAGE_ANALYSIS: bool = os.getenv("ENABLE_IMAGE_ANALYSIS", "false").lower() == "true"
    ENABLE_VOICE_RECOGNITION: bool = os.getenv("ENABLE_VOICE_RECOGNITION", "false").lower() == "true"
    ENABLE_PDF_PROCESSING: bool = os.getenv("ENABLE_PDF_PROCESSING", "false").lower() == "true"


# =============================================================================
# ADVANCED
# =============================================================================

class AdvancedConfig:
    """Advanced configuration."""

    DEFAULT_TIMEZONE: str = os.getenv("DEFAULT_TIMEZONE", "Europe/Moscow")
    DEFAULT_LANGUAGE: str = os.getenv("DEFAULT_LANGUAGE", "ru")
    DEBUG: bool = os.getenv("DEBUG", "false").lower() == "true"


# =============================================================================
# CONFIG VALIDATION
# =============================================================================

def validate_config() -> bool:
    """
    Validate all required configuration settings.

    Returns:
        bool: True if configuration is valid

    Raises:
        ValueError: If required settings are missing or invalid
    """
    try:
        TelegramConfig.validate()
        LLMConfig.validate()
        return True
    except ValueError as e:
        logging.error(f"Configuration validation failed: {e}")
        raise


# =============================================================================
# EXPORT ALL CONFIGS
# =============================================================================

__all__ = [
    "TelegramConfig",
    "LLMConfig",
    "BudgetConfig",
    "CalendarConfig",
    "ContactsConfig",
    "DatabaseConfig",
    "MemoryConfig",
    "PluginsConfig",
    "LoggingConfig",
    "FeatureFlags",
    "AdvancedConfig",
    "validate_config",
    "BASE_DIR",
    "DATA_DIR",
    "CONFIG_DIR",
    "LOGS_DIR",
]
