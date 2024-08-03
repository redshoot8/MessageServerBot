import datetime
import aiohttp

from aiogram import Router
from aiogram.types import Message, ReplyKeyboardMarkup, KeyboardButton
from aiogram.filters import Command

from config import settings

router = Router()

info_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text='/info')],
    ],
    resize_keyboard=True
)

message_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text='/read')],
    ],
    resize_keyboard=True
)


@router.message(Command('start'))
async def start_handler(msg: Message):
    """Start message handler"""
    await msg.answer('Привет! Я бот для отправки и просмотра сообщений', reply_markup=info_keyboard)


@router.message(Command('info'))
async def info_handler(msg: Message):
    """Info message handler"""
    await msg.answer(
        'Чтобы прочитать сообщения следует использовать команду /read'
        'Чтобы отправить сообщение следует использовать команду /send {сообщение} без фигурных скобок',
        reply_markup=message_keyboard
    )


@router.message(Command('read'))
async def read_handler(msg: Message):
    """Read message handler"""
    async with aiohttp.ClientSession() as session:
        async with session.get(f'{settings.API_URL}/messages/') as resp:
            if resp.status == 200:
                messages = await resp.json()
                response = '\n'.join([f"**{message['author']}**: {message['content']}" for message in messages['data']])
                if response != '':
                    await msg.answer(response, reply_markup=message_keyboard)
                else:
                    await msg.answer('Сообщений не найдено', reply_markup=message_keyboard)
            else:
                await msg.answer('Ошибка при попытке просмотра сообщений', reply_markup=message_keyboard)


@router.message(Command('send'))
async def send_handler(msg: Message):
    """Send message handler"""
    new_message = {
        'author': msg.from_user.full_name,
        'content': msg.text[len('/send '):],
        'created_at': str(datetime.datetime.now(datetime.UTC))
    }
    async with aiohttp.ClientSession() as session:
        async with session.post(f"{settings.API_URL}/messages/", json=new_message) as resp:
            if resp.status == 200:
                await msg.answer('Сообщение отправлено', reply_markup=message_keyboard)
            else:
                await msg.answer('Ошибка при отправке сообщения', reply_markup=message_keyboard)
