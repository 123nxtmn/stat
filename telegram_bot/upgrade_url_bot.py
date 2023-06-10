from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import ReplyKeyboardRemove, ReplyKeyboardMarkup, KeyboardButton
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

# InlineKeyboardMarkup пригодится для инициализации инлайн-кнопок, а InlineKeyboardButton — для их создания.

# Нам понадобится класс ReplyKeyboardMarkup — для начала импортируем его и дополнительные необходимые классы:
# Bot - определяет на какие команды пользователя и как он будет отвечать
# Dispatcher позволяет отслеживать обновления.
# Executor запускает бота и выполняет функции, которые следует выполнить.
# Модуль types позволит нам использовать базовые классы для аннотирования, то есть восприятия сообщений.
# Например, мы будем использовать types.Message, позволяющий работать с приёмом текстовых сообщений пользователя.

API_TOKEN = '6104600204:AAHUxHufnD3FNLz8oDFPLWRkMYpI3xAJptQ'

bot = Bot(API_TOKEN)
dp = Dispatcher(bot)

urlkb = InlineKeyboardMarkup(row_width=1)
urlButton = InlineKeyboardButton(text='Перейти в блог Skillbox', url='https://skillbox.ru/media/code/')
urlButton2 = InlineKeyboardButton(text='Перейти к курсам Skillbox', url='https://skillbox.ru/code/')
urlkb.add(urlButton, urlButton2)


@dp.message_handler(commands='ссылки')
async def url_command(message: types.Message):
    await message.answer('Полезные ссылки:', reply_markup=urlkb)



