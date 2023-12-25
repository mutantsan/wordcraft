from aiogram import Dispatcher, types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text, IDFilter

import app.utils as utils


def register_handlers_common(dp: Dispatcher, admin_id: int):
    dp.register_message_handler(cmd_start, commands="start", state="*")
    dp.register_message_handler(cmd_cancel, commands="cancel", state="*")
    dp.register_message_handler(
        cmd_cancel, Text(equals="стоп", ignore_case=True), state="*"
    )


async def cmd_start(message: types.Message, state: FSMContext):
    await state.finish()

    user: types.User = message.from_user

    await message.answer(f"""Вітаю, {user}! Почнімо.""")


async def cmd_cancel(message: types.Message, state: FSMContext):
    await state.finish()
    await message.answer("Дія скасована.", reply_markup=types.ReplyKeyboardRemove())  # type: ignore
