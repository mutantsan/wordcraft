from __future__ import annotations

import os
import logging

from app.exceptions import BotConfigError
from app.const import BOT_TOKEN


logger = logging.getLogger(__name__)


def get_bot_token() -> str:
    """Get a bot token. Register a bot with @BotFather (https://t.me/BotFather)
    to access a token"""
    token: str | None = os.environ.get(BOT_TOKEN)

    if not token:
        raise BotConfigError("Set a bot token to proceed!")

    return token
