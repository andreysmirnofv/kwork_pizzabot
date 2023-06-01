from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
from aiogram.dispatcher.filters import Text
import os

from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

bot = Bot(token=os.getenv('TOKEN'))
dp = Dispatcher(bot)

answer = dict()

urlkb = InlineKeyboardMarkup(row_width=2)
urlButton = InlineKeyboardButton(text="Ссылка", url='https://youtube.com')
urlButton2 = InlineKeyboardButton(text="Вторая ссылка", url="https://google.com")
x = [InlineKeyboardButton(text="Третия ссылка", url="https://google.com"),
     InlineKeyboardButton(text="Четвертая ссылка", url="https://google.com"),
     InlineKeyboardButton(text="Пятая ссылка", url="https://google.com")]
urlkb.add(urlButton, urlButton2).row(*x).insert(InlineKeyboardButton(text="шестая ссылка", url="https://google.com"))


@dp.message_handler(commands=["Ссылки"])
async def url_command(message: types.Message):
    await message.answer('Ссылочки', reply_markup=urlkb)


inkb = InlineKeyboardMarkup(row_width=1).add(InlineKeyboardButton(text='like', callback_data='like_1'),
                                             InlineKeyboardButton(text="He like", callback_data="like_-1"))


@dp.message_handler(command='test')
async def test_cpmmands(message: types.Message):
    await message.reply('like', reply_markup=inkb)


@dp.callback_query_handler(Text(startswith='like_'))
async def www_call(callback: types.Message):
    result = int(callback.text.split('_')[1])
    if f'{callback.from_user.id not in answer}':
        answer[f'{callback.from_user.id}'] = result
        await callback.answer('Вы проголосавали')
    else:
        await callback.answer('Вы уже проголосавали', show_alert=True)


executor.start_polling(dp, skip_updates=True)
