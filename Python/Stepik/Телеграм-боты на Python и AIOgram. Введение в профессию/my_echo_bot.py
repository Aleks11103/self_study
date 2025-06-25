#  Простой эхо бот
from aiogram import Bot, Dispatcher
from aiogram.filters import Command
from aiogram.types import Message
from tg_bot_token import BOT_TOKEN


#  Создание объектов бота и диспетчера
bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()


#  Хендлер комманды '/start'
@dp.message(Command(commands=['start']))
async def process_start_command(message: Message):
    await message.answer('Привет!\nМеня зовут эхо-бот!\nЗаходи, если скучно!')


#  Хендлер комманды '/help'
@dp.message(Command(commands=['help']))
async def process_help_command(message: Message):
    await message.answer('Напиши сообщение и получи его же в ответ')


#  Хендлер любых текстовых сообщений кроме комманд '/start' и '/help'
@dp.message()
async def send_echo(message: Message):
    await message.reply(text=message.text)


if __name__ == '__main__':
    dp.run_polling(bot)
# dp.run_polling(bot)
