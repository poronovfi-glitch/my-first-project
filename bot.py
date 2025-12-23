#!/usr/bin/env python3
"""
AI Assistant Telegram Bot - Main Entry Point

Персональный ИИ-ассистент с функциями:
- Управление календарём (Apple/Google/Microsoft/Local)
- Работа с контактами
- Анализ Excel файлов
- Долговременная память
- Бюджет-трекинг

Author: Claude Code
License: MIT
"""

import sys
import logging
from pathlib import Path

# Add project root to Python path
sys.path.insert(0, str(Path(__file__).parent))

from config import (
    validate_config,
    LoggingConfig,
    TelegramConfig,
    LLMConfig,
    AdvancedConfig,
)


def setup_logging():
    """
    Configure logging for the application.
    Uses both console and file handlers.
    """
    # Create formatter
    log_format = "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
    formatter = logging.Formatter(log_format)

    # Console handler
    console_handler = logging.StreamHandler(sys.stdout)
    console_handler.setFormatter(formatter)

    # File handler (with rotation)
    from logging.handlers import RotatingFileHandler
    file_handler = RotatingFileHandler(
        LoggingConfig.LOG_FILE,
        maxBytes=LoggingConfig.LOG_MAX_SIZE,
        backupCount=LoggingConfig.LOG_BACKUP_COUNT,
        encoding="utf-8",
    )
    file_handler.setFormatter(formatter)

    # Root logger configuration
    root_logger = logging.getLogger()
    root_logger.setLevel(LoggingConfig.LOG_LEVEL)
    root_logger.addHandler(console_handler)
    root_logger.addHandler(file_handler)

    # Reduce noise from libraries
    logging.getLogger("httpx").setLevel(logging.WARNING)
    logging.getLogger("httpcore").setLevel(logging.WARNING)
    logging.getLogger("telegram").setLevel(logging.WARNING)
    logging.getLogger("urllib3").setLevel(logging.WARNING)

    return logging.getLogger(__name__)


def print_banner():
    """Print application banner."""
    banner = """
    ╔══════════════════════════════════════════════════════════╗
    ║                                                          ║
    ║           🤖 AI Assistant Telegram Bot                   ║
    ║                                                          ║
    ║  Персональный интеллектуальный помощник                 ║
    ║  • Календарь  • Контакты  • Excel  • Память             ║
    ║                                                          ║
    ╚══════════════════════════════════════════════════════════╝
    """
    print(banner)


def print_config_info(logger: logging.Logger):
    """Print configuration information at startup."""
    logger.info("=" * 60)
    logger.info("CONFIGURATION")
    logger.info("=" * 60)
    logger.info(f"Bot Token: {TelegramConfig.BOT_TOKEN[:10]}...")
    logger.info(f"Admin ID: {TelegramConfig.ADMIN_ID}")
    logger.info(f"Allowed Users: {len(TelegramConfig.ALLOWED_USER_IDS)} users")
    logger.info(f"OpenAI Model: {LLMConfig.OPENAI_MODEL}")
    logger.info(f"Language: {AdvancedConfig.DEFAULT_LANGUAGE}")
    logger.info(f"Timezone: {AdvancedConfig.DEFAULT_TIMEZONE}")
    logger.info(f"Debug Mode: {AdvancedConfig.DEBUG}")
    logger.info("=" * 60)


async def main():
    """
    Main application entry point.
    Initializes bot, database, and starts polling.
    """
    # Setup logging
    logger = setup_logging()

    # Print banner
    print_banner()

    try:
        # Validate configuration
        logger.info("Validating configuration...")
        validate_config()
        logger.info("✅ Configuration valid")

        # Print config info
        print_config_info(logger)

        # TODO: Initialize database
        logger.info("Initializing database...")
        # from bot.database import init_database
        # await init_database()
        logger.warning("⚠️  Database initialization not implemented yet")

        # TODO: Initialize bot
        logger.info("Initializing Telegram bot...")
        # from bot.telegram_bot import TelegramBot
        # bot = TelegramBot()
        # await bot.start()
        logger.warning("⚠️  Bot initialization not implemented yet")

        logger.info("=" * 60)
        logger.info("🚀 Bot is ready and running!")
        logger.info("Press Ctrl+C to stop")
        logger.info("=" * 60)

        # Keep the bot running
        # await bot.idle()

        # Temporary: Just keep running
        import asyncio
        logger.info("Temporary: Sleeping indefinitely (bot not implemented yet)")
        await asyncio.Event().wait()

    except KeyboardInterrupt:
        logger.info("Received Ctrl+C, shutting down gracefully...")
    except Exception as e:
        logger.error(f"Fatal error: {e}", exc_info=True)
        sys.exit(1)
    finally:
        logger.info("Bot stopped")


if __name__ == "__main__":
    """
    Run the bot using asyncio.
    """
    try:
        import asyncio
        asyncio.run(main())
    except KeyboardInterrupt:
        print("\n👋 Goodbye!")
        sys.exit(0)
