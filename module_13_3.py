from aiogram import Bot, Dispatcher, types, Router
from aiogram.filters import Command
from aiogram.types import Message
import asyncio

router = Router()


bot = Bot(token='7558583844:AAGGE3cmcqtXjM-wYpqXjrry-nwB0waQFrY')

@router.message(Command("start"))
async def start_command(message: Message):
    await message.answer("Привет! Я бот помогающий твоему здоровью.")

@router.message()
async def echo_handler(message: Message) -> None:
    await message.answer('Введите команду /start, чтобы начать общение.')

async def main():
    dp = Dispatcher() 

    dp.include_router(router)
    try:
        await dp.start_polling(bot)  
    except Exception as e: 
        print(e)

    finally:
        await bot.session.close()


if __name__ == '__main__':
    print('start')
    asyncio.run(main())