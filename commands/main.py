from aiogram import Dispatcher, types
from aiogram.types import InputFile
from markups import main_markup as m
import os

from create_bot import bot
from commands.shop_commands import ShopClass


async def start(message: types.Message):
    await bot.send_photo(
        message.chat.id,
        photo=InputFile(os.path.abspath('files/menu_logo.png')),
        reply_markup=m.menu_markup,
        caption=f"""🖐Привет, <b>{message.chat.first_name}</b>.\nГлавное меню бота <b>Hayan Shop</b>!\n"""
    )
    await ShopClass.shop_menu.set()


def registrate_main(dp: Dispatcher):
    dp.register_message_handler(start, commands=['menu', 'start'])
