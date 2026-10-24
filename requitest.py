import asyncio
from aiogram import Bot, Dispatcher, types, Router, F
from aiogram.filters import Command
from aiogram.types import Message
import aiohttp
import ssl

user_router = Router()

async def get_product(product_id):
    url = f"https://fakestoreapi.com/products/{product_id}"

    ssl_context = ssl.create_default_context()
    ssl_context.check_hostname = False
    ssl_context.verify_mode = ssl.CERT_NONE

    async with aiohttp.ClientSession() as session:
        async with session.get(url, ssl=ssl_context) as resp:
            if resp.status == 404:
                return None
            
            data = await resp.json()
            return data

@user_router.message(Command("start"))
async def start(message: Message):
    await message.answer("Привет, введи команду: /product ID")

@user_router.message(Command("product"))
async def get_product_cmd(message: Message):
    parts = message.text.strip().split()

    if len(parts) != 2:
        await message.answer("")
        return
    
    product_id = parts[1]
    if not product_id.isdigit():
        await message.answer("")
        return
    
    await message.answer(f"Ищу товар с id: {product_id}")

    try:
        product = await get_product(int(product_id))
    except Exception as e:
        await message.answer(f"ошибка {e}")
        return
    
    if product is None:
        await message.answer("нет такого")
        return
    
    title = product.get("title", "Без названия")
    price = product.get("price", "?")
    desc = product.get("description", "описание")
    category = product.get("category", "???")

    text = (
        f"{title}\n"
        f"Категория: {category}\n"
        f"Цена: {price}\n"
        f"{desc}"
    )

    await message.answer(text)