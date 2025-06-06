import telebot
import config
from sqlalchemy import (
    Column,
    Integer,
    String,
    Boolean,
    ForeignKey,
    create_engine,
    DateTime,
)
from sqlalchemy.orm import declarative_base, sessionmaker
import time

bot = telebot.TeleBot(config.TELEGRAM_TOKEN)

Base = declarative_base()


class CustomUser(Base):
    __tablename__ = "users_customuser"
    id = Column(Integer, primary_key=True)
    username = Column(String)
    phone = Column(String)
    telegram_id = Column(String)


class Orders(Base):
    __tablename__ = "products_orders"
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("users_customuser.id"))
    product = Column(String)
    order_date = Column(DateTime)
    is_notified = Column(Boolean)


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


def check_new_orders():
    while True:
        new_orders = session.query(Orders).filter_by(is_notified=False).all()

        for order in new_orders:
            user = session.query(CustomUser).filter_by(id=order.user_id).first()

            bot.send_message(
                user.telegram_id, f"Вам пришёл новый заказ: {order.product}"
            )
            order.is_notified = True
            session.commit()

        session.close()
        time.sleep(10)  

check_new_orders()
bot.polling(none_stop=True)
