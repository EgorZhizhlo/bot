from aiogram import Dispatcher, types
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.types import InputMedia, InputFile
from aiogram.dispatcher import FSMContext
import os

from markups import main_markup as main_m
from markups import shop_markup as shop_m

from create_bot import bot


class ShopClass(StatesGroup):
    shop_menu = State()
    choose_shop = State()
    h_back_to_menu = State()


async def shop_menu(callback_query: types.CallbackQuery):
    match callback_query.data:
        case "shop":
            await bot.answer_callback_query(callback_query.id)
            await callback_query.message.edit_media(
                InputMedia(media=InputFile(os.path.abspath('files/shop_logo.png')),
                           caption='💡Выберите доступный игру или сервис: '),
                reply_markup=shop_m.shop_markup
            )
            await ShopClass.choose_shop.set()
        case "help":
            await bot.answer_callback_query(callback_query.id)
            await callback_query.message.edit_media(
                InputMedia(media=InputFile(os.path.abspath('files/shop_logo.png')),
                           caption=f"🌟Дорогой <b>{callback_query.message.chat.first_name}</b>."
                                   "\nКонтакт поддержки: <b>@skainer_234</b>."),
                reply_markup=main_m.back_markup
            )
            await ShopClass.h_back_to_menu.set()


async def choose_shop(callback_query: types.CallbackQuery, state: FSMContext):
    match callback_query.data:
        case "fortnite":
            await bot.answer_callback_query(callback_query.id)
            await callback_query.message.edit_media(
                InputMedia(media=InputFile(os.path.abspath('files/fortnite.png')),
                           caption='Выберите товар для Fortnite: '),
                reply_markup=shop_m.fortnite_markup
            )
            await state.finish()
            from commands.services.fortnite import FortniteClass
            await FortniteClass.choose_vb.set()
        case "gta":
            await bot.answer_callback_query(callback_query.id)
            await callback_query.message.edit_media(
                InputMedia(media=InputFile(os.path.abspath('files/fortnite.png')),
                           caption='Выберите товар для GTA: ')
            )
            await state.finish()
        case "discordN":
            await bot.answer_callback_query(callback_query.id)
            await callback_query.message.edit_media(
                InputMedia(media=InputFile(os.path.abspath('files/fortnite.png')),
                           caption='Выберите товар для Discord Nitro: ')
            )
            await state.finish()
        case "xbox":
            await bot.answer_callback_query(callback_query.id)
            await callback_query.message.edit_media(
                InputMedia(media=InputFile(os.path.abspath('files/fortnite.png')),
                           caption='Выберите товар для Xbox: ')
            )
            await state.finish()
        case "exitlag":
            await bot.answer_callback_query(callback_query.id)
            await callback_query.message.edit_media(
                InputMedia(media=InputFile(os.path.abspath('files/fortnite.png')),
                           caption='Выберите товар для ExitLag: ')
            )
            await state.finish()
        case "faceit":
            await bot.answer_callback_query(callback_query.id)
            await callback_query.message.edit_media(
                InputMedia(media=InputFile(os.path.abspath('files/fortnite.png')),
                           caption='Выберите товар для Faceit: ')
            )
            await state.finish()
        case "twitch":
            await bot.answer_callback_query(callback_query.id)
            await callback_query.message.edit_media(
                InputMedia(media=InputFile(os.path.abspath('files/fortnite.png')),
                           caption='Выберите товар для Twitch: ')
            )
            await state.finish()
        case "playstation":
            await bot.answer_callback_query(callback_query.id)
            await callback_query.message.edit_media(
                InputMedia(media=InputFile(os.path.abspath('files/fortnite.png')),
                           caption='Выберите товар для Playstation: ')
            )
            await state.finish()
        case "back_shop":
            await bot.answer_callback_query(callback_query.id)
            await callback_query.message.edit_media(
                InputMedia(media=InputFile(os.path.abspath('files/menu_logo.png')),
                           caption=f"""🖐Привет, <b>{callback_query.message.chat.first_name}</b>.\nГлавное меню бота <b>Hayan Shop</b>!\n"""
                           ), reply_markup=main_m.menu_markup)
            await ShopClass.shop_menu.set()


async def h_back_to_menu(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    await callback_query.message.edit_media(
        InputMedia(media=InputFile(os.path.abspath('files/menu_logo.png')),
                   caption=f"""🖐Привет, <b>{callback_query.message.chat.first_name}</b>.\nГлавное меню бота <b>Hayan Shop</b>!\n"""
                   ), reply_markup=main_m.menu_markup)

    await ShopClass.shop_menu.set()


def registrate_shop(dp: Dispatcher):
    dp.register_callback_query_handler(shop_menu, state=ShopClass.shop_menu)
    dp.register_callback_query_handler(choose_shop, state=ShopClass.choose_shop)
    dp.register_callback_query_handler(h_back_to_menu, state=ShopClass.h_back_to_menu)
