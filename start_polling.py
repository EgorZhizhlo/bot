from aiogram import executor

from commands.main import registrate_main
from commands.shop_commands import registrate_shop
from commands.services.fortnite import registrate_fortnite

from create_bot import dp

registrate_fortnite(dp)
registrate_shop(dp)
registrate_main(dp)

executor.start_polling(dp, skip_updates=True)
