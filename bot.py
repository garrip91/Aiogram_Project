from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor

from config import TOKEN, CHANNEL_ID


bot = Bot(token=TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def process_start_command(message: types.Message):
    await message.reply("Привет!\nНапиши мне что-нибудь!")


@dp.message_handler(commands=['help'])
async def process_help_command(message: types.Message):
    await message.reply("Напиши мне что-нибудь и я отправлю этот текст тебе в ответ!")


# @dp.message_handler()
# async def echo_message(msg: types.Message):
    # await bot.send_message(msg.from_user.id, msg.text)
@dp.message_handler(commands=['msg'])
async def echo_message(msg: types.Message):
    #await bot.send_message(CHANNEL_ID, msg.text)
    await bot.send_message(CHANNEL_ID, F"Ваш бот отправил в наш канал команду - [{msg.text}]")
    


if __name__ == '__main__':
    executor.start_polling(dp)
    
    
    
#await bot.send_message(chat_id=channel_id, text='123')