from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
from aiogram.types import Message
import asyncio


bot = Bot(token='7558583844:AAGGE3cmcqtXjM-wYpqXjrry-nwB0waQFrY')
dp = Dispatcher()

@dp.message_handler()
async def all_massages(message):
    print("Введите команду /start, чтобы начать общение.")

@dp.message_handler()
async def start_command(commands= ['start']):
    print("Привет! Я бот помогающий твоему здоровью.")


if __name__ == '__main__':
    executor.start_polling(dp, start_command = True)