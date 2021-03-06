from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor

#from config import TOKEN, CHANNEL_ID
from config import garrip91_TOKEN, CHANNEL_ID

import json

import asyncio



#bot = Bot(token=TOKEN)
bot = Bot(token=garrip91_TOKEN)
dp = Dispatcher(bot)

path = 'from_r/DATA.json'


'''
@dp.message_handler(commands=['start'])
async def process_start_command(message: types.Message):
    #await message.reply("Привет!\nНапиши мне что-нибудь!")
    #await bot.send_message(CHANNEL_ID, F"Ваш бот отправил в Ваш канал команду - [{message.text}]")
    with open(path, 'r', encoding='utf-8') as f:
        data = json.loads(f.read())
        n = 0
        for i in data:
            for k, v in i.items():
                if k == 'url':
                    #await bot.send_message(CHANNEL_ID, F"{v}")
                    await bot.send_message(CHANNEL_ID, F"{v}")
                    await asyncio.sleep(3)
            n += 1
    print(n)
'''    
async def SendMessageToChannel():
    bot = Bot(token=garrip91_TOKEN)
    await bot.send_message(CHANNEL_ID, F"Ваш бот отправил в Ваш канал какую-то команду!")        

@dp.message_handler(commands=['help'])
async def process_help_command(message: types.Message):
    await message.reply("Напиши мне что-нибудь и я отправлю этот текст тебе в ответ!")

'''
# @dp.message_handler()
# async def echo_message(msg: types.Message):
    # await bot.send_message(msg.from_user.id, msg.text)
@dp.message_handler(commands=['msg'])
async def echo_message(msg: types.Message):
    #await bot.send_message(CHANNEL_ID, msg.text)
    await bot.send_message(CHANNEL_ID, F"Ваш бот отправил в наш канал команду - [{msg.text}]")
'''    

'''
if __name__ == '__main__':
    executor.start_polling(dp)
'''
if __name__ == '__main__':
    asyncio.run(SendMessageToChannel())