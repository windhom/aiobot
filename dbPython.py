import asyncio
from aiogram import Bot, Dispatcher, types, Router,F
from aiogram.types import Message
from aiogram.filters.command import Command
import aiosqlite

router = Router()

db_name = "bot_base.sql"

async def init_db():
    async with aiosqlite.connect(db_name) as db:
        await db.execute("""
            CREATE TABLE IF NOT EXISTS users(
                         id INTEGER PRIMARY KEY,
                         full_name TEXT,
                         age INTEGER 
                         )
                        """)
        await db.commit()

async def add_user(full_name, age):
    async with aiosqlite.connect(db_name) as db:
        await db.execute("INSERT INTO users (full_name, age) VALUES(?, ?)", (full_name, age))
        await db.commit()

async def get_users():
    async with aiosqlite.connect(db_name) as db:
        cursor = await db.execute("SELECT full_name, age FROM users")
        result = await cursor.fetchall()
        return result
    
@router.message(Command("start"))
async def start(message: Message):
    await init_db()
    await message.answer("привет!\nпропишите команду: /reg AGE")

@router.message(Command("reg"))
async def reg(message: Message):
    parts = message.text.strip().split()

    if len(parts) != 2 or not parts[1].isdigit():
        await message.answer("введите команду нормально")
        return
    
    await add_user(message.from_user.full_name, int(parts[1]))
    
    await message.answer("добавлен")

@router.message(Command("users"))
async def users(message: Message):
    users = await get_users()

    if not users:
        await message.answer("нет пользователей")
        return
    
    text = "пользователи\n"
    for full_name, age in users:
        text += f"{full_name} - {age}\n"

    await message.answer(text)