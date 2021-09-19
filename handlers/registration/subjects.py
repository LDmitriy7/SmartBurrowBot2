from aiogram import types
from aiogram.dispatcher import FSMContext

import api
import keyboards as kb
import models
import states
from config.subjects import ALL_SUBJECTS
from loader import dp
from utils import StorageProxy

main_state = states.Registration.subjects
SUBJECTS_CATEGORY = 'subjects_category'
SUBJECTS_PAGE = 'subjects_page'


@dp.callback_query_handler(button=kb.SubjectsSearch.MANUALLY, state=main_state)
async def show_subjects_by_category(query: types.CallbackQuery):
    await query.message.answer('Категории предметов:', reply_markup=kb.SubjectsCategories())


@dp.callback_query_handler(button=kb.SubjectsCategories.BUTTONS, state=main_state)
async def show_subjects_in_category(query: types.CallbackQuery, state: FSMContext):
    async with StorageProxy(models.Profile) as profile:
        reply_markup = kb.SubjectsInCategory(query.data, 0, profile.subjects)

    await state.update_data({SUBJECTS_CATEGORY: query.data, SUBJECTS_PAGE: 0})
    await query.message.edit_text('Предметы категории:', reply_markup=reply_markup)


@dp.callback_query_handler(button=kb.SubjectsInCategory.BACK_TO_CATEGORIES, state=main_state)
async def go_back_to_subjects_categories(query: types.CallbackQuery):
    await query.message.edit_text('Категории предметов:', reply_markup=kb.SubjectsCategories())


@dp.callback_query_handler(button=kb.SubjectsInCategory.NEXT_PAGE, state=main_state)
async def turn_subjects_page(query: types.CallbackQuery, button: dict, state: FSMContext):
    storage_data = await state.get_data()
    subjects_page: int = int(button['page_num'])

    async with StorageProxy(models.Profile) as profile:
        reply_markup = kb.SubjectsInCategory(
            category=storage_data[SUBJECTS_CATEGORY],
            page=subjects_page,
            marked_subjects=profile.subjects,
        )

    await state.update_data({SUBJECTS_PAGE: subjects_page})
    await query.message.edit_text('Предметы категории:', reply_markup=reply_markup)


@dp.callback_query_handler(text=ALL_SUBJECTS, state=main_state)
async def process_subject(query: types.CallbackQuery, state: FSMContext):
    storage_data = await state.get_data()

    async with StorageProxy(models.Profile) as profile:
        if query.data in profile.subjects:
            profile.subjects.remove(query.data)
        else:
            profile.subjects.append(query.data)

    async with StorageProxy(models.Profile) as profile:
        reply_markup = kb.SubjectsInCategory(
            category=storage_data[SUBJECTS_CATEGORY],
            page=storage_data[SUBJECTS_PAGE],
            marked_subjects=profile.subjects,
        )

    await query.message.edit_reply_markup(reply_markup)


@dp.message_handler(text=kb.SaveBack.RESET, state=main_state)
async def reset_subjects(msg: types.Message):
    async with StorageProxy(models.Profile) as profile:
        profile.subjects = []

    await msg.answer('Вы сбросили все выбранные предметы')


@dp.message_handler(text=kb.SaveBack.SAVE, state=main_state)
async def save_subjects(_msg: types.Message):
    await states.Registration.next()
    await api.answer_for_state()


@dp.message_handler(state=main_state)
async def process_subject(msg: types.Message):
    if msg.via_bot != await dp.bot.me:
        await msg.answer('Ошибка, отправь предмет, используя поиск')
        return

    async with StorageProxy(models.Profile) as profile:
        if msg.text in profile.subjects:
            profile.subjects.remove(msg.text)
            await msg.answer('Предмет удален')
        else:
            profile.subjects.append(msg.text)
            await msg.answer('Предмет добавлен')
