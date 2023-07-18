from aiogram import Bot, Dispatcher
from aiogram.filters import CommandStart
from aiogram.types import (ReplyKeyboardMarkup, KeyboardButton,
                           KeyboardButtonPollType, Message)
from aiogram.utils.keyboard import ReplyKeyboardBuilder
from aiogram.types.web_app_info import WebAppInfo


API_TOKEN = '6206897348:AAENqclh-o1SObNCLJV69uJCTL5VUVOgjUc'

bot: Bot = Bot(API_TOKEN)
dp: Dispatcher = Dispatcher()

# Инициализируем билдер
kb_builder: ReplyKeyboardBuilder = ReplyKeyboardBuilder()

# Создаем кнопки
contact_btn: KeyboardButton = KeyboardButton(text='Отправить телефон',
                                             request_contact=True)

geo_btn: KeyboardButton = KeyboardButton(text='Отправить геолокацию',
                                         request_location=True)

regular_btn: KeyboardButton = KeyboardButton(text='Создать опрос',
                                          request_poll=KeyboardButtonPollType(
                                              type='regular'))

quiz_btn: KeyboardButton = KeyboardButton(text='Создать викторину',
                                          request_poll=KeyboardButtonPollType(
                                              type='quiz'))

web_app_keyboard: KeyboardButton = KeyboardButton(text='Start Web App',
                                                  web_app=WebAppInfo(url='https://stepik.org/'))

# Добавляем кнопки в билдер
kb_builder.row(contact_btn, geo_btn, regular_btn, quiz_btn, web_app_keyboard, width=1)

# Создаем объект клавиатуры
keyboard: ReplyKeyboardMarkup = kb_builder.as_markup(resize_keyboard=True,
                                                     one_time_keyboard=True)


# Этот хэндлер будет срабатывать на команду "/start"
# и отправлять в чат клавиатуру
@dp.message(CommandStart())
async def process_start_command(message: Message):
    await message.answer(text='Экспериментируем со специальными кнопками',
                         reply_markup=keyboard)

if __name__ == '__main__':
    dp.run_polling(bot)
