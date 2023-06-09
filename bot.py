from aiogram.utils import executor
from create_bot import dp
from database import sqlite_db
from handlers import client, admin, other


async def on_startup(_):
    print('Бот вышел в онлайн')
    sqlite_db.start()

client.register_handlers_client(dp)
other.register_handler_other(dp)
admin.register_handlers_admin(dp)


executor.start_polling(dp, skip_updates=True, on_startup=on_startup)
