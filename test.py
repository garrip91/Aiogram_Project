from config import TOKEN, CHANNEL_NAME

import requests



requests.get('https://api.telegram.org/bot{}/sendMessage'.format(TOKEN), params=dict(
   chat_id=CHANNEL_NAME,
   #text='ДАННОЕ СООБЩЕНИЕ ОТПРАВЛЕНО В КАНАЛ С ИСПОЛЬЗОВАНИЕМ ЯП "Python"! ДОБРО ПОЖАЛОВАТЬ В НАШ КАНАЛ!!! ;-)'
   text='Такссс.... Ещё одна проверочка и приступаем к следующему этапу!'
))