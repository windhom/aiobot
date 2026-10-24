import asyncio
from aiogram import Bot, Dispatcher, types, F
from aiogram.types import Message
from testbot import router, notifier

bot = Bot(token="8995433663:AAEUEunzOu3Xt5U3TMlIcYzDyhwYpHD8yGw")
dp = Dispatcher()

async def main():
    dp.include_router(router)
    asyncio.create_task(notifier(bot))
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())