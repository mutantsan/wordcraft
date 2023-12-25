from __future__ import annotations

from typing import Callable

from aiogram import Dispatcher

from app.handlers.common import register_handlers_common


def get_handlers() -> (
    list[Callable[[Dispatcher], None] | Callable[[Dispatcher, int], None]]
):
    return [
        register_handlers_common,
    ]
