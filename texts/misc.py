import config

cancelled = 'Отменено'
not_implemented = 'Не реализовано'

welcome = f"""
<b>Как пользоваться меню:</b>
🔸 Чтобы <b>добавить задание</b>, нажми 📝 <b>Создать заказ</b> 📝
🔸 Чтобы открыть <b>персональную защищенную сделку</b> с исполнителем, выбери пункт 🔐 <b>Личный заказ</b> 🔐
🔸 Чтобы просматривать <b>опубликованные задания</b> и управлять ими, нажми 🗂 <b>Мои заказы</b> 🗂
🔸 Чтобы <b>вывести заработанные деньги</b> или <b>пополнить счет</b> для заказа услуг, нажми 💳 <b>Баланс</b> 💳
🔸 Чтобы предложить идею для улучшения работы сервиса или сообщить о баге и получить финансовое вознаграждение, \
нажми кнопку 💡 <b>Предложить идею</b> 💡
🔸 Чтобы найти ответы на вопросы о работе сервиса, нажми на кнопку 🧾 <b>Инструкция</b> 🧾
🔸 Чтобы <b>выполнять задания и зарабатывать деньги</b>, выбери меню исполнителя и зарегистрируйся

🛎 По любым вопросам, включая рекламу на канале и сотрудничество в другом формате, \
пишите администрации {config.Users.OWNER_USERNAME} 🦦
"""

guide = f"""
<a href="{config.ArticleUrls.ABOUT_PROJECT}"><b>О проекте</b></a>

<a href="{config.ArticleUrls.PROJECT_RULES}"><b>Правила проекта</b></a>

<a href="{config.ArticleUrls.CLIENT_MENU_GUIDE}"><b>Как использовать "Меню заказчика"</b></a>

<a href="{config.ArticleUrls.WORKER_MENU_GUIDE}"><b>Как использовать "Меню исполнителя"</b></a>

<a href="{config.ArticleUrls.FAQ}"><b>Часто задаваемые вопросы</b></a>

<a href="{config.Users.OWNER_URL}"><b>Связаться с администратором</b></a>
"""

ref_program_info = f"""
<b>Рекомендуйте Умную нору</b> в соцсетях: \
<b>Заказчикам</b> и <b>Помощникам</b>, за это <b>получайте</b> дополнительный заработок в размере \
<b>{config.RefProgram.PERCENT}% от комиссии с каждого заказа</b>

<b>Твоя уникальная ссылка</b>: 
{{ref_link}}

<b>Твоя статистика:</b>
• Кол-во рефералов: {{refs_count}}
• Общий доход: {{ref_income}} грн.
"""

create_order = """
Чтобы <b>опубликовать задание</b> и <b>найти исполнителя</b>, следуй простым шагам и подсказкам. \
Это займет не больше пары минут:
"""

ask_work_type = 'Выбери тип работы из списка'

ask_subject = """
А теперь <b>выбери название предмета</b>. Можно сделать это <b>вручную</b>, \
либо <b>ввести пару первых букв</b> в поле для ввода текста, нажав на кнопку "Поиск по словам"'
"""

ask_until_date = 'Теперь укажи <b>сроки выполнения</b> заказа - выбери дату из календаря'

ask_description = 'Как можно подробнее <b>опиши проект</b> в специальном поле, укажи время выполнения проекта.'

description_len_must_be = f"""
Ошибка, описание должно быть от {config.Order.MIN_DESCRIPTION_LEN} до {config.Order.MAX_DESCRIPTION_LEN} символов
"""

ask_price = """
<b>Укажи цену</b>, которую которую готов заплатить за выполнение задания - введи ее в специальном поле в гривнах
"""

ask_note = """
Добавь <b>заметку</b> в поле - это информация исключительно для тебя - она не видна исполнителям и другим пользователям
"""

ask_files = """
А теперь <b>отправь все необходимые материалы</b> для выполнения проекта.
Когда загрузятся все необходимые файлы, нажми кнопку "Готово". \
Внимание: <b>прикрепляй файлы по одному</b>, иначе часть из них может не загрузиться.
Если прикрепил не те файлы или по любой другой причине хочешь начать процесс заново, нажми кнопку "Сбросить"
"""

ask_to_confirm_order = """
Нажми кнопку <b>"Отправить проект"</b> и он будет опубликован в ленте. \
Вскоре ты начнешь получать заявки от исполнителей.
"""

ask_to_confirm_personal_order = 'Теперь ты можешь <b>проверить проект</b> и <b>отправить исполнителю</b>'

ask_to_save_personal_order = 'Нажми <b>отправить проект</b>, чтобы <b>сохранить результат</b>'

balance_info = """
Здесь ты можешь просматривать свой баланс на сервисе, пополнять его или выводить деньги.

<b>Твой баланс</b>: {amount} грн.
"""

worker_menu_info = """
Здесь ты можешь <b>зарабатывать</b> за выполнение заданий.
Для этого <b>выбери понравившийся проект</b> из списка и подай заявку на его выполнение.  
"""

ask_to_register = 'Перед началом работы пройди регистрацию'

ask_phone_number = """
Отправь номер телефона, нажав на кнопку, или введи его самостоятельно (12 цифр, начиная с 3)
"""

ask_email = 'Теперь e-mail'

ask_biography = """
<b>Расскажите о себе</b>. Напишите тут о своем образовании, опыте, расскажите про сильные стороны, \
чтобы заказчикам захотелось выбрать исполнителем именно вас
"""

ask_works = """
<b>Отправь примеры своих работ</b> (только фото/скриншоты). \
Загружай файлы по одному, иначе они могут не сохраниться.
Когда закончишь, нажми "сохранить", чтобы сохранить данные или "сбросить", чтобы отредактировать
"""

ask_subjects = """
Теперь <b>выбери предметы</b>, если хочешь получать задания по определенным специализациям.
Можно сделать это <b>вручную</b> либо <b>ввести пару первых букв</b> в поле для ввода текста, \
нажав на кнопку "Поиск по словам".
<b>Кнопка "Сбросить" обнулит все выбранные предметы</b>
"""

ask_nickname = 'Осталось придумать ник'

ask_deposit_amount = 'На сколько гривен ты хочешь пополнить баланс?'

ask_to_pay = """
Оплати заявку по ссылке и нажми "Подтвердить оплату"
"""

deposit_info = """
Мы зачислим средства на твой счет после автоматической проверки
"""

ask_withdrawal_amount = 'Сколько гривен ты хочешь вывести?'

ask_withdrawal_card_num = 'Отправь номер карты 💳'

after_withdrawal = 'Средства будут зачислены в течение часа'

ask_withdrawal_confirmation = 'Вывести {amount} грн. на карту {card_num}?'

new_withdrawal = '<b>Поступил новый запрос на вывод средств</b>. Смотри в /withdrawals'

check_subscription_error = f"""
Чтобы работать с ботом, сначала подпишись на {config.Channel.USERNAME} - \
тут будут публиковаться твои проекты и задания, которые ты можешь брать для выполнения.
"""

ask_search_orders_option = 'Выбери тип заказов для отображения'
