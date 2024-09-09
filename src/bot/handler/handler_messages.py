from aiogram import types, F, Router
from src.model.main import Category

router = Router()
category = Category()
output_format = "Категория №1:\n" "{0}\n" "Категория №2:\n" "{1}"


@router.message(F.text)
async def print_text(message: types.Message):
    try:
        code = category.from_pn_to_str(message.text).split("_")
    except ValueError:
        await message.answer("Неправильный формат запроса!")
        return
    first_category = category.get_first_category(code[0], code[1])
    exist = []
    first_category_output = ""
    for i, supplier in enumerate(first_category):
        first_category_output += f"Приоритет: {i + 1}, Поставщик:{supplier}\n"
        exist.append(supplier)
    second_category = category.get_second_category(code[0], code[1])
    second_category_output = ""
    i = 1
    for supplier in second_category:
        if not (supplier in exist):
            second_category_output += f"Приоритет: {i}, Поставщик:{supplier}\n"
            i += 1
    await message.answer(
        output_format.format(first_category_output, second_category_output)
    )
