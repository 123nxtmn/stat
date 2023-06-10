from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import ReplyKeyboardRemove, ReplyKeyboardMarkup, KeyboardButton
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

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


urlkb = InlineKeyboardMarkup(row_width=2)
urlButton = InlineKeyboardButton(text='Перейти в ВК Карины', url='https://vk.com/magicunicat')
urlButton2 = InlineKeyboardButton(text='Перейти в ВК Павла', url='https://vk.com/pavel_dolgih')
urlButton3 = InlineKeyboardButton(text='Перейти в ВК Ивана', url='https://vk.com/karamnovivan')
urlButton4 = InlineKeyboardButton(text='Перейти в ВК Макса', url='https://vk.com/maks.bro_official_page')
urlkb.add(urlButton, urlButton2, urlButton3, urlButton4)


@dp.message_handler(commands='ссылки')
async def url_command(message: types.Message):
   await message.answer('Полезные ссылки:', reply_markup=urlkb)

# Создали функцию send_welcome передаём два параметра, приветственное сообщение и сообщение, которым
# нам будет отвечать наш бот, в message.reply мы передаём наше сообщение
# Явно указываем в декораторе, на какую команду реагируем с помощью @dp.message_handler(commands=['start'])


@dp.message_handler()
async def echo(message: types.Message):
    await message.answer(message.text)
# Создаём новое событие, которое запускается в ответ на любой текст, введённый пользователем.
# Создаём функцию с простой задачей — отправить обратно тот же текст, что ввёл пользователь.

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)

