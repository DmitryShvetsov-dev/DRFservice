import telebot
import os

bot = telebot.TeleBot(os.environ.get("TELEGRAM_TOKEN"))

def send_notification(chat_id: int, message: str):
    bot.send_message(chat_id, message)