from aiogram import Bot, Dispatcher
from aiogram.utils import executor

bot = Bot('6232185603:AAGQKI1GWh5WnAApRZEDWfQlehOQbaj1V-Q')
dp = Dispatcher(bot)

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)

