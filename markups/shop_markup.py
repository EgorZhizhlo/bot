from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

fortnite_b = InlineKeyboardButton('Fortnite🔥', callback_data='fortnite')
gta_b = InlineKeyboardButton('GTA🎮', callback_data='gta')
discordN_b = InlineKeyboardButton('Discord Nitro👾', callback_data='discordN')
xbox_b = InlineKeyboardButton('Xbox🟢', callback_data='xbox')
exitlag_b = InlineKeyboardButton('ExitLag💖', callback_data='exitlag')
faceit_b = InlineKeyboardButton('Faceit🌟', callback_data='faceit')
twitch_b = InlineKeyboardButton('Twitch💜', callback_data='twitch')
playstation_b = InlineKeyboardButton('Playstation🕹️', callback_data='playstation')
back_shop_b = InlineKeyboardButton('Назад🔙', callback_data='back_shop')
shop_markup = InlineKeyboardMarkup(row_width=2).add(
    *[fortnite_b, gta_b, discordN_b, xbox_b, exitlag_b, faceit_b, twitch_b, playstation_b, back_shop_b])

vb1000_b = InlineKeyboardButton('1000 В-баксов🔥', callback_data='1000vb')
vb2800_b = InlineKeyboardButton('2800 В-баксов🔥', callback_data='2800vb')
vb5000_b = InlineKeyboardButton('5000 В-баксов🔥', callback_data='5000vb')
vb13500_b = InlineKeyboardButton('13500 В-баксов🔥', callback_data='13500vb')
back_fort_b = InlineKeyboardButton('Назад🔙', callback_data='back_fort')
fortnite_markup = InlineKeyboardMarkup(row_width=2).add(
    *[vb1000_b, vb2800_b, vb5000_b, vb13500_b, back_fort_b])

pay_b = InlineKeyboardButton('Оплатить✅', callback_data='pay')
back_prod_b = InlineKeyboardButton('Назад🔙', callback_data='back_to_prod')
pay_markup = InlineKeyboardMarkup(row_width=2).add(
    *[pay_b, back_prod_b])


back_a_menu_b = InlineKeyboardButton('Назад🔙', callback_data='back_a_menu_b')
back_menu_markup = InlineKeyboardMarkup(row_width=2).add(
    *[back_a_menu_b])
