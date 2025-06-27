#  Простой эхо бот
from aiogram import Bot, Dispatcher, F
from aiogram.filters import Command
from aiogram.types import Message, ContentType
from tg_bot_token import BOT_TOKEN


#  Создание объектов бота и диспетчера
bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()


#  Хендлер комманды '/start'
# @dp.message(Command(commands=['start']))
async def process_start_command(message: Message):
    await message.answer('Привет!\nМеня зовут эхо-бот!\nЗаходи, если скучно!')


#  Хендлер комманды '/help'
# @dp.message(Command(commands=['help']))
async def process_help_command(message: Message):
    await message.answer('Напиши сообщение и получи его же в ответ')


#  Хендлер для обработки фото
async def send_photo_echo(message: Message):
    await message.reply_photo(message.photo[0].file_id)


#  Хендлер для обработки аудиофайлов
async def send_audio_echo(message: Message):
    await message.reply_audio(message.audio.file_id)


#  Хендлер для обработки видео
async def send_video_echo(message: Message):
    await message.reply_video(message.video.file_id)


#  Хендлер для обработки стикеров
async def send_sticker_echo(message: Message):
    await message.reply_sticker(message.sticker)


#  Хендлер для обработки гифок
async def send_animation_echo(message: Message):
    await message.reply_animation(message.animation)


#  Хендлер для обработки документов
async def send_document_echo(message: Message):
    await message.reply_document(message.document.file_id)


#  Хендлер для обработки голосовых сообщений
async def send_voice_echo(message: Message):
    await message.reply_voice(message.voice.file_id)


#  Хендлер любых текстовых сообщений
# @dp.message()
async def send_echo(message: Message):
    await message.answer(message.text)


# Регистрируем хэндлеры
dp.message.register(process_start_command, Command(commands='start'))
dp.message.register(process_help_command, Command(commands='help'))
dp.message.register(send_photo_echo, F.content_type == ContentType.PHOTO)
dp.message.register(send_audio_echo, F.content_type == ContentType.AUDIO)
dp.message.register(send_video_echo, F.content_type == ContentType.VIDEO)
dp.message.register(send_sticker_echo, F.content_type == ContentType.STICKER)
dp.message.register(
    send_animation_echo,
    F.content_type == ContentType.ANIMATION
)
dp.message.register(send_document_echo, F.content_type == ContentType.DOCUMENT)
dp.message.register(send_voice_echo, F.content_type == ContentType.VOICE)
dp.message.register(send_echo)


if __name__ == '__main__':
    dp.run_polling(bot)
# dp.run_polling(bot)
