from aiogram import Dispatcher, types
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.types import InputMedia, InputFile, InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.dispatcher import FSMContext
import os

from markups import shop_markup as shop_m
from markups import main_markup as m

from create_bot import bot


class FortniteClass(StatesGroup):
    choose_vb = State()
    pay_vb = State()
    check_pay_vb = State()
    back_to_menu = State()


async def choose_vb(callback_query: types.CallbackQuery, state: FSMContext):
    match callback_query.data:
        case "1000vb":
            await bot.answer_callback_query(callback_query.id)
            await callback_query.message.edit_media(
                InputMedia(media=InputFile(os.path.abspath('files/shop_logo.png')),
                           caption='Выбран товар: 1000 В-баксов'),
                reply_markup=shop_m.pay_markup
            )
            async with state.proxy() as date:
                date['vb_col'] = 1000
            await FortniteClass.next()
        case "2800vb":
            await bot.answer_callback_query(callback_query.id)
            await callback_query.message.edit_media(
                InputMedia(media=InputFile(os.path.abspath('files/shop_logo.png')),
                           caption='Выбран товар: 2800 В-баксов'),
                reply_markup=shop_m.pay_markup
            )
            async with state.proxy() as date:
                date['vb_col'] = 2800
            await FortniteClass.next()
        case "5000vb":
            await bot.answer_callback_query(callback_query.id)
            await callback_query.message.edit_media(
                InputMedia(media=InputFile(os.path.abspath('files/shop_logo.png')),
                           caption='Выбран товар: 5000 В-баксов'),
                reply_markup=shop_m.pay_markup
            )
            async with state.proxy() as date:
                date['vb_col'] = 5000
            await FortniteClass.next()
        case "13500vb":
            await bot.answer_callback_query(callback_query.id)
            await callback_query.message.edit_media(
                InputMedia(media=InputFile(os.path.abspath('files/shop_logo.png')),
                           caption='Выбран товар: 13500 В-баксов'),
                reply_markup=shop_m.pay_markup
            )
            async with state.proxy() as date:
                date['vb_col'] = 13500
            await FortniteClass.next()
        case "back_fort":
            await bot.answer_callback_query(callback_query.id)
            await callback_query.message.edit_media(
                InputMedia(media=InputFile(os.path.abspath('files/shop_logo.png')),
                           caption='💡Выберите доступный игру или сервис: '),
                reply_markup=shop_m.shop_markup
            )
            await state.finish()
            from commands.shop_commands import ShopClass
            await ShopClass.choose_shop.set()


async def pay_vb(callback_query: types.CallbackQuery, state: FSMContext):
    match callback_query.data:
        case "pay":
            pay_b = InlineKeyboardButton('Оплата',
                                         url="https://aaio.io/")
            check_pay_b = InlineKeyboardButton('Проверка оплаты', callback_data='check_pay')

            back_prod_b = InlineKeyboardButton('Назад🔙', callback_data='back_pay_prod_menu')
            pay_markup = InlineKeyboardMarkup(row_width=2).add(
                *[pay_b, check_pay_b, back_prod_b])
            await bot.answer_callback_query(callback_query.id)
            await callback_query.message.edit_media(
                InputMedia(media=InputFile(os.path.abspath('files/shop_logo.png')),
                           caption=f"Ссылка для оплаты создана.\n"
                                   f"{(await state.get_data())['vb_col']}\n"
                                   f"Для перехода воспользуйтесь кнопкой: <b>Оплата</b>.\n"
                                   f"Для проверки платежа воспользуйтесь кнопкой: <b>Проверка оплаты</b>"),
                reply_markup=pay_markup
            )
            await FortniteClass.next()
        case "back_to_prod":
            await bot.answer_callback_query(callback_query.id)
            await callback_query.message.edit_media(
                InputMedia(media=InputFile(os.path.abspath('files/fortnite.png')),
                           caption='Выберите товар для Fortnite: '),
                reply_markup=shop_m.fortnite_markup
            )
            await state.finish()
            await FortniteClass.choose_vb.set()


async def check_pay_vb(callback_query: types.CallbackQuery, state: FSMContext):
    match callback_query.data:
        case "check_pay":
            await bot.answer_callback_query(callback_query.id)
            await callback_query.message.edit_media(
                InputMedia(media=InputFile(os.path.abspath('files/shop_logo.png')),
                           caption=f"<b>ОПЛАТА ПРОШЛА УСПЕШНО</b>\n"
                                   f"Скоро с вами свяжется администратор <b>Hayan Shop</b>.\n"
                                   f"@{callback_query.message.chat.username}"
                           ),
                reply_markup=shop_m.back_menu_markup
            )
            await FortniteClass.next()
        case "back_pay_prod_menu":
            await bot.answer_callback_query(callback_query.id)
            await callback_query.message.edit_media(
                InputMedia(media=InputFile(os.path.abspath('files/fortnite.png')),
                           caption='Выберите товар для Fortnite: '),
                reply_markup=shop_m.fortnite_markup
            )
            await state.finish()
            await FortniteClass.choose_vb.set()


async def back_to_menu(callback_query: types.CallbackQuery, state: FSMContext):
    match callback_query.data:
        case "back_a_menu_b":
            await bot.answer_callback_query(callback_query.id)
            await callback_query.message.edit_media(
                InputMedia(media=InputFile(os.path.abspath('files/menu_logo.png')),
                           caption=f"🖐Привет, <b>{callback_query.message.chat.first_name}</b>.\n"
                                   f"Главное меню бота <b>Hayan Shop</b>!\n"),
                reply_markup=m.menu_markup
            )
            await state.finish()
            from commands.shop_commands import ShopClass
            await ShopClass.shop_menu.set()


def registrate_fortnite(dp: Dispatcher):
    dp.register_callback_query_handler(choose_vb, state=FortniteClass.choose_vb)
    dp.register_callback_query_handler(pay_vb, state=FortniteClass.pay_vb)
    dp.register_callback_query_handler(check_pay_vb, state=FortniteClass.check_pay_vb)
    dp.register_callback_query_handler(back_to_menu, state=FortniteClass.back_to_menu)
