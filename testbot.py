import asyncio
from aiogram import Bot, Dispatcher, types, Router, F
from aiogram.filters.command import Command
from aiogram.types import Message

router = Router()

subscribers = set()

async def notifier(bot: Bot):
    while True:
        if subscribers:
            for user_id in list(subscribers):
                try:
                    await bot.send_message(user_id, "сообщение")
                except Exception:
                    pass

        await asyncio.sleep(10)

@router.message(Command("start"))
async def start(message: Message):
    await message.answer(
        "привет\n"
        "комманды\n"
        "/subscribe\n"
        "/unsubscribe\n"
        "/subscribers\n"
    )


@router.message(Command("subscribe"))
async def subscribe(message: Message):
    user_id = message.from_user.id

    subscribers.add(user_id)

    await message.answer("вы подписались")

@router.message(Command("unsubscribe"))
async def subscribe(message: Message):
    user_id = message.from_user.id

    subscribers.discard(user_id)

    await message.answer("вы отписались")

@router.message(Command("subscribers"))
async def subscribers_cmd(message: Message):
    if not subscribers:
        await message.answer("пока никого нет")
        return
    
    text = "подписчики:\n"
    for uid in subscribers:
        text += f"{uid}\n"

    await message.answer(text)