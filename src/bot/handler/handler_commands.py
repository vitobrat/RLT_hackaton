from aiogram import types, Router, html
from aiogram.filters import Command

router = Router()


@router.message(Command("start"))
async def start_command(message: types.Message) -> None:
    """Handler of command /start; print some start information

    Attributes:
        message: obj to get user information or send something to user
    """
    await message.answer(
        f"Добро пожаловать, <b>{html.quote(message.from_user.full_name)}</b>!\n"
        f"Данный бот создан для предоставления списка релевантных поставщиков.\n"
        f"Отправьте номер процедуры в правильном формате."
    )
    print(message.from_user.id, message.from_user.full_name)
