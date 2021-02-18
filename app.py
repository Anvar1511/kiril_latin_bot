# from aiogram import executor, Bot
# from loader import dp
# import middlewares, filters, handlers
# from utils.notify_admins import on_startup_notify
#
# async def on_startup(dispatcher):
#     # Уведомляет про запуск
#     await on_startup_notify(dispatcher)
#
#
# if __name__ == '__main__':
#     executor.start_polling(dp, on_startup=on_startup)
from aiogram import Bot

bot = Bot(token="1039659888:AAGAzdArAUlCQ5l68DKeE2N89Yt8FCNcjhI")

bo