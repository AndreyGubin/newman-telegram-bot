from aiogram.types import CallbackQuery, Chat, Message
import logging
import os
from aiogram import executor, Bot, Dispatcher
import json

os.environ['TOKEN'] = 'токен_бота'
bot = Bot(token=os.getenv('TOKEN'))
dp = Dispatcher(bot)
logging.basicConfig(level=logging.INFO, filename='report.log', filemode='a')

# запуск бота командой python3 bot.py
@dp.message_handler(commands=['postman'])
async def start_bot(message: Message):
# output.json - путь к отчету newman
    with open('output.json', 'r') as report_file:
        data = json.load(report_file)
        run = data.get("run")
        stats = run.get("stats")
        assertions = stats.get("assertions")
        total = assertions.get("total")
        failed = assertions.get("failed")
#result = (f'Запущено тестов: {total}, Из них провалено: {failed}')
    await message.answer(f'Запущено тестов: {total}, Из них провалено: {failed}')

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
