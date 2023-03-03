from aiogram import Bot,Dispatcher,executor,types
import python_weather
import Locales
import asyncio
import os

# bot init
bot = Bot(token="5633606088:AAHIbk7F8nQFA-ZWYBebACyAStWjE9_E92U")
dp = Dispatcher(bot)
client = python_weather.Client(format=python_weather.IMPERIAL)

@dp.message_handler()
async def echo(message: types.Message):
    weather = await client.get(message.text)
    celsius = (weather.current.temperature - 32) * 5 / 9
    print(str(round(celsius)))

    resp_msg = message.text+"\n"
    resp_msg += f"Текущая температура:{round(celsius)}С\n"

    await message.answer(resp_msg)

# run long-polling
if __name__=="__main__":
    executor.start_polling(dp,skip_updates=True)
  #  await client.close()