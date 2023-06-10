from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import ReplyKeyboardRemove, ReplyKeyboardMarkup, KeyboardButton

# Нам понадобится класс ReplyKeyboardMarkup — для начала импортируем его и дополнительные необходимые классы:
# Bot - определяет на какие команды пользователя и как он будет отвечать
# Dispatcher позволяет отслеживать обновления.
# Executor запускает бота и выполняет функции, которые следует выполнить.
# Модуль types позволит нам использовать базовые классы для аннотирования, то есть восприятия сообщений.
# Например, мы будем использовать types.Message, позволяющий работать с приёмом текстовых сообщений пользователя.

API_TOKEN = '6104600204:AAHUxHufnD3FNLz8oDFPLWRkMYpI3xAJptQ'
# Импортировали токен бота, к которому мы подключаемся

bot = Bot(API_TOKEN)
dp = Dispatcher(bot)
# Импортировал в переменную bot объект API_token с нашим ключом, тем самым инициализировал подключение
# Если их не инициализировать, то подключения не будет - точнее будет ошибка


@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    kb = [
        [
            types.KeyboardButton(text="/ссылки"),
            types.KeyboardButton(text="А это?")
        ],
    ]
    keyboard = types.ReplyKeyboardMarkup(keyboard=kb)

    await message.reply("Привет!\n Я бот testy morsel\n Отправь мне любое сообщение, а я отвечу.",
                        reply_markup=keyboard)
# Создали функцию send_welcome в которю передаём два параметра, приветственное сообщение и сообщение, которым
# нам будет отвечать наш бот, в message.reply мы передаём наше сообщение
# Явно указываем в декораторе, на какую команду реагируем с помощью @dp.message_handler(commands=['start'])


@dp.message_handler()
async def echo(message: types.Message):
    await message.answer(message.text)
# Создаём новое событие, которое запускается в ответ на любой текст, введённый пользователем.
# Создаём функцию с простой задачей — отправить обратно тот же текст, что ввёл пользователь.

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
# Метод start_polling опрашивает сервер, проверяя на нём обновления. Если они есть, то они приходят в Telegram.


# ReplyKeybordRemove и ReplyKeyboardMarkup позволяют создавать и удалять клавиатуру,
# а класс KeyboardButton используется для добавления кнопок.


# Сначала создадим в нашем первом декораторе список kb, который будет хранить кнопки.
# Кнопка в aiogram создаётся с помощью types.KeyboardButton(text=" "),
# где в параметре text мы передаём отображаемое название кнопки
# После этого необходимо создать клавиатуру и рассказать ей про наши кнопки.
# Делается это с помощью метода types.ReplyKeyboardMarkup(keyboard=list),
# где вместо list записывается название списка с кнопками — в нашем случае это список kb.


# Теперь остаётся показать клавиатуру в Telegram-чате.
# Для этого добавляем в ответ строку reply_markup=keyboard,
# которая отображает клавиатуру после команды /start.
# Теперь при запуске бота мы видим, что в чате появились обе кнопки из списка kb

