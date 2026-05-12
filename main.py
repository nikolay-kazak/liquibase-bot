import telebot
import os
from telebot import types

TOKEN = os.getenv("TOKEN")

bot = telebot.TeleBot(TOKEN)

# ✅ Главное меню
def main_menu():
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("👤 Профиль")
    btn2 = types.KeyboardButton("ℹ️ О нас")
    markup.add(btn1, btn2)
    return markup

# ✅ Команда /start
@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(
        message.chat.id,
        "💧 Добро пожаловать в LiquiBase!\n\nВыберите пункт меню:",
        reply_markup=main_menu()
    )

# ✅ Обработка кнопок
@bot.message_handler(func=lambda message: True)
def handle_message(message):

    if message.text == "👤 Профиль":
        user = message.from_user
        bot.send_message(
            message.chat.id,
            f"👤 Ваш профиль:\n\n"
            f"Имя: {user.first_name}\n"
            f"Username: @{user.username}\n"
            f"ID: {user.id}",
            reply_markup=main_menu()
        )

    elif message.text == "ℹ️ О нас":
        bot.send_message(
            message.chat.id,
            "💧 LiquiBase — это современный Telegram сервис.\n\n"
            "Мы развиваем удобные инструменты для пользователей 🚀",
            reply_markup=main_menu()
        )

    else:
        bot.send_message(
            message.chat.id,
            "Выберите кнопку из меню 👇",
            reply_markup=main_menu()
        )

print("LiquiBase бот с меню запущен...")
bot.polling(none_stop=True)
