from aiogram import Bot, Dispatcher
from aiogram.filters import Command
from aiogram.types import Message
from tg_bot_token import BOT_TOKEN


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


#  Хендлер любых сообщений, кроме объявленных ранее
@dp.message()
async def send_echo(message: Message):
    try:
        await message.send_copy(chat_id=message.chat.id)
    except TypeError:
        await message.reply('Данный тип апдейтов не поддерживается '
                            'методом send_copy')


if __name__ == '__main__':
    dp.run_polling(bot)
