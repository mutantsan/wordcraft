import asyncio
import logging
import inspect

from aiogram import Bot, Dispatcher
from aiogram.types import BotCommand
from aiogram.contrib.fsm_storage.memory import MemoryStorage


import app.config as conf
import app.handlers as handlers
import app.middleware as middleware

logger = logging.getLogger(__name__)


async def set_commands(bot: Bot):
    """Register BOT commands that will be accessible via dropdown menu in telegram"""
    await bot.set_my_commands(
        [
            BotCommand(command="/start", description="Почнімо."),
            BotCommand(command="/drink", description="Випити водички."),
            BotCommand(command="/stats", description="Статистика."),
            BotCommand(command="/settings", description="Налаштування."),
            BotCommand(command="/cancel", description="Скасувати дію."),
        ]
    )


async def main():
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(name)s - %(message)s",
    )
    logger.info("Starting wordcraft bot")

    bot = Bot(token=conf.get_bot_token())
    dp = Dispatcher(bot, storage=MemoryStorage())

    # Register handlers
    for handler in handlers.get_handlers():
        if len(inspect.getfullargspec(handler).args) == 2:
            handler(dp, "")  # type: ignore
        else:
            handler(dp)  # type: ignore

    # Setup Middlewares
    dp.middleware.setup(middleware.RegisterMiddleware())

    # Setup BOT commands
    await set_commands(bot)

    await dp.skip_updates()
    await dp.start_polling()


if __name__ == "__main__":
    asyncio.run(main())
