from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

shop_b = InlineKeyboardButton('Магазин🛒', callback_data='shop')
freq_quest_b = InlineKeyboardButton('Частые вопросы❓', callback_data='freq_quest')
profile_b = InlineKeyboardButton('Профиль👤', callback_data='profile')
guar_b = InlineKeyboardButton('Гарантии✅', callback_data='guar')
rev_b = InlineKeyboardButton('Отзывы🌟', callback_data='rev')
help_b = InlineKeyboardButton('Поддержка🤝', callback_data='help')
menu_markup = InlineKeyboardMarkup(row_width=2).add(*[shop_b, freq_quest_b, profile_b, guar_b, rev_b, help_b])

back_to_menu_b = InlineKeyboardButton('Назад🔙', callback_data='back_to_menu_b')
back_markup = InlineKeyboardMarkup(row_width=2).add(back_to_menu_b)
