import telebot
import config
from sqlalchemy import (
    Column,
    Integer,
    String,
    create_engine,
)
from sqlalchemy.orm import declarative_base, sessionmaker

bot = telebot.TeleBot(config.TELEGRAM_TOKEN)

Base = declarative_base()


class CustomUser(Base):
    __tablename__ = "users_customuser"
    id = Column(Integer, primary_key=True)
    username = Column(String)
    phone = Column(String)
    telegram_id = Column(String)

engine = create_engine(config.DATABASE_URL)
Session = sessionmaker(bind=engine)
session = Session()


@bot.message_handler(commands=["start"])
def start_command(message):
    markup = telebot.types.ReplyKeyboardMarkup(
        resize_keyboard=True, one_time_keyboard=True
    )
    button = telebot.types.KeyboardButton("Поделиться номером", request_contact=True)
    markup.add(button)
    bot.send_message(
        message.chat.id, "Пожалуйста, поделитесь номером телефона:", reply_markup=markup
    )


@bot.message_handler(content_types=["contact"])
def handle_contact(message):
    if message.contact:
        phone = message.contact.phone_number
        tg_id = str(message.chat.id)

        user = session.query(CustomUser).filter(CustomUser.phone == phone).first()
        if user:
            user.telegram_id = tg_id
            session.commit()
            bot.send_message(message.chat.id, "Вы успешно зарегистрированы в системе")
        else:
            bot.send_message(message.chat.id, "Пользователь с таким номером не найден")
        session.close()

bot.polling(none_stop=True)
