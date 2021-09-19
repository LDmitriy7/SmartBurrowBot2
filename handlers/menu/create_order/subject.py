from aiogram import types
from aiogram.dispatcher import FSMContext

import api
import keyboards as kb
import models
import states
from config.subjects import ALL_SUBJECTS
from loader import dp
from utils import StorageProxy

main_state = states.CreateOrder.subject
SUBJECTS_CATEGORY = 'subjects_category'


@dp.message_handler(state=main_state)
async def process_subject(msg: types.Message):
    if msg.via_bot != await dp.bot.me:
        await msg.answer('Ошибка, отправь предмет, используя поиск')
        return

    async with StorageProxy(models.Order) as order:
        order.subject = msg.text

    await states.CreateOrder.next()
    await api.answer_for_state()


@dp.callback_query_handler(button=kb.SubjectsSearch.MANUALLY, state=main_state)
async def show_subjects_by_category(query: types.CallbackQuery):
    await query.message.answer('Категории предметов:', reply_markup=kb.SubjectsCategories())


@dp.callback_query_handler(button=kb.SubjectsCategories.BUTTONS, state=main_state)
async def show_subjects_in_category(query: types.CallbackQuery, state: FSMContext):
    await state.update_data({SUBJECTS_CATEGORY: query.data})
    reply_markup = kb.SubjectsInCategory(query.data, 0)
    await query.message.edit_text('Предметы категории:', reply_markup=reply_markup)


@dp.callback_query_handler(button=kb.SubjectsInCategory.BACK_TO_CATEGORIES, state=main_state)
async def go_back_to_subjects_categories(query: types.CallbackQuery):
    await query.message.edit_text('Категории предметов:', reply_markup=kb.SubjectsCategories())


@dp.callback_query_handler(button=kb.SubjectsInCategory.NEXT_PAGE, state=main_state)
async def turn_subjects_page(query: types.CallbackQuery, button: dict, state: FSMContext):
    storage_data = await state.get_data()
    reply_markup = kb.SubjectsInCategory(storage_data[SUBJECTS_CATEGORY], int(button['page_num']))
    await query.message.edit_text('Предметы категории:', reply_markup=reply_markup)


@dp.callback_query_handler(text=ALL_SUBJECTS, state=main_state)
async def process_subject(query: types.CallbackQuery):
    async with StorageProxy(models.Order) as order:
        order.subject = query.data

    await states.CreateOrder.next()
    await api.answer_for_state()
